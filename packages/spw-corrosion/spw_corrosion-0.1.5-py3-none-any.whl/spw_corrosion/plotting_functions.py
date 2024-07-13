import numpy as np
from scipy import stats
from typing import Optional, Union, List
from spw_corrosion.corrosion import CorrosionModel
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def plot_posterior(model: CorrosionModel, post_pdf: np.ndarray[("n_C50_grid", "n_pf_times", "n_true_C50s"), float],
                   true_C50s: np.ndarray["n_true_C50s", float]) -> plt.Figure:

    colors = plt.cm.get_cmap('Spectral', true_C50s.size)

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    ax.plot(model.config.C50_grid, model.config.C50_prior_pdf, c='b')
    if true_C50s.size > 1:
        for i, C50 in enumerate(true_C50s):
            for j in range(post_pdf.shape[-2]):
                post = post_pdf[:, j, i]
                ax2.plot(model.config.C50_grid, post, c=colors(i), alpha=0.4)
            ax.axvline(C50, c=colors(i), linestyle='--')
    else:
        for i in range(post_pdf.shape[-1]):
            for j in range(post_pdf.shape[-2]):
                post = post_pdf[:, j, i]
                ax2.plot(model.config.C50_grid, post, c=colors(i))
        ax.axvline(true_C50s, c=colors(0), linestyle='--')
    ax.set_xlabel('${C}_{50}$ [mm]', fontsize=12)
    ax.set_ylabel('A-priori verdeling [-]', fontsize=12)
    ax2.set_ylabel('A-posteriori verdeling [-]', fontsize=12)

    plt.close()

    return fig


def plot_pf_timeline(pf_timelines: np.ndarray[("n_true_C50s", "n_pf_times"), float],
                     times: Union[np.ndarray["n_pf_times", float], np.ndarray["n_pf_times", int]],
                     true_C50s: np.ndarray["n_true_C50s", float]) -> plt.Figure:

    norm = matplotlib.colors.Normalize(vmin=true_C50s.min(), vmax=true_C50s.max())
    cmap = matplotlib.cm.ScalarMappable(norm=norm, cmap=matplotlib.cm.jet)

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    for i, pf in enumerate(pf_timelines):
        ax.plot(times, pf, label=true_C50s[i], c=cmap.to_rgba(i+1))
    ax.set_xlabel('Tijd [jaar]', fontsize=12)
    ax.set_ylabel('${P}_{f}$ [-]', fontsize=12)
    ax.set_yscale('log', base=10)
    cbar = fig.colorbar(cmap)
    tick_list = list(np.linspace(true_C50s.min(), true_C50s.max(), 10))
    cbar.set_ticks(tick_list)
    cbar.set_ticklabels([str(round(tick, 1)) for tick in tick_list])
    cbar.ax.get_yaxis().labelpad = 18
    cbar.ax.set_ylabel('Echte ${C}_{50}$ [mm]', fontsize=12, rotation=270)
    ax.set_title('A-posteriori ${P}_{f}$ per echte ${C}_{50}$\n(Gemiddelde over MC tijdlijnen)')
    plt.close()

    return fig


def plot_beta_timeline(pf_timelines: np.ndarray[("n_true_C50s", "n_pf_times"), float],
                       times: Union[np.ndarray["n_pf_times", float], np.ndarray["n_pf_times", int]],
                       true_C50s: np.ndarray["n_true_C50s", float],
                       beta_req: Optional[float] = None) -> plt.Figure:

    norm = matplotlib.colors.Normalize(vmin=true_C50s.min(), vmax=true_C50s.max())
    cmap = matplotlib.cm.ScalarMappable(norm=norm, cmap=matplotlib.cm.jet)

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    for i, pf in enumerate(pf_timelines):
        beta = -stats.norm.ppf(pf, loc=0, scale=1)
        ax.plot(times, beta, c=cmap.to_rgba(i+1), label=true_C50s[i])
    if beta_req is not None:
        ax.axhline(beta_req, linestyle='--', c='r', label='Betrouwbaarsheidindex\n requirement')
    ax.set_xlabel('Tijd [jaar]', fontsize=12)
    ax.set_ylabel('Betrouwbaarsheidindex [-]', fontsize=12)
    # ax.set_yscale('log', base=10)
    cbar = fig.colorbar(cmap)
    tick_list = list(np.linspace(true_C50s.min(), true_C50s.max(), 10))
    cbar.set_ticks(tick_list)
    cbar.set_ticklabels([str(round(tick, 1)) for tick in tick_list])
    cbar.ax.get_yaxis().labelpad = 18
    cbar.ax.set_ylabel('Echte ${C}_{50}$ [mm]', fontsize=12, rotation=270)
    ax.set_title('A-posteriori betrouwbaarsheid index per echte ${C}_{50}$\n(Gemiddelde over MC tijdlijnen)')
    plt.close()

    return fig


def plot_posterior_per_C50(model: CorrosionModel, post_pdf: np.ndarray[("n_C50_grid", "n_pf_times"), float],
                           true_C50: float) -> plt.Figure:

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    ax.plot(model.config.C50_grid, model.config.C50_prior_pdf, c='b', label='A-priori verdeling')
    for post in post_pdf.T:
        ax2.plot(model.config.C50_grid, post, c='r', alpha=0.4)
    ax2.plot(model.config.C50_grid, post, c='r', alpha=0.4, label='A-posteriori verdelingen')
    ax.axvline(true_C50, c='k', linestyle='--', label='Echte ${C}_{50}$')
    ax.set_xlabel('${C}_{50}$ [mm]', fontsize=12)
    ax.set_ylabel('A-priori verdeling [-]', fontsize=12)
    ax2.set_ylabel('A-posteriori verdeling [-]', fontsize=12)
    ax.set_title('Echte ${C}_{50}$=' + str(round(true_C50, 2)) + '[mm]', fontsize=14)
    plt.close()

    return fig


def plot_pf_timeline_per_C50(pf_timeline: np.ndarray[("n_MC_timelines, n_pf_times"), float],
                             times: Union[np.ndarray["n_pf_times", float], np.ndarray["n_pf_times", int]],
                             true_C50: float,
                             true_pfs: np.ndarray[("n_pf_times"), float],
                             prior_pf: np.ndarray[("n_pf_times"), float],
                             pi_bnds: List[float] = [0.05, 0.95]) -> plt.Figure:

    pi_lvl = max(pi_bnds) - min(pi_bnds)
    pi = np.quantile(pf_timeline, pi_bnds, axis=0)

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(times, pf_timeline.mean(axis=0), c='r', label='A-posteriori ${P}_{f}$\n(Gemiddelde over MC tijdlijnen)')
    ax.fill_between(times, pi[0], pi[1], color='r', alpha=0.3, label=str(round(pi_lvl*100))+'% prediction interval')
    ax.plot(times, true_pfs, c='k', label='Echte ${P}_{f}$')
    ax.plot(times, prior_pf, c='b', label='A-priori ${P}_{f}$')
    ax.set_xlabel('Tijd [jaar]', fontsize=12)
    ax.set_ylabel('${P}_{f}$ [-]', fontsize=12)
    ax.set_yscale('log', base=10)
    ax.legend(fontsize=12)
    ax.set_title('Echte ${C}_{50}$=' + str(round(true_C50, 2)) + '[mm]', fontsize=14)
    plt.close()

    return fig


def plot_beta_timeline_per_C50(pf_timeline: np.ndarray[("n_pf_times"), float],
                               times: Union[np.ndarray["n_pf_times", float], np.ndarray["n_pf_times", int]],
                               true_C50: float,
                               true_pfs: np.ndarray[("n_pf_times"), float],
                               prior_pf: np.ndarray[("n_pf_times"), float],
                               pi_bnds: List[float] = [0.05, 0.95]) -> plt.Figure:

    pi_lvl = max(pi_bnds) - min(pi_bnds)
    beta_timeline = - stats.norm.ppf(pf_timeline, loc=0, scale=1)
    pi = np.quantile(beta_timeline, pi_bnds, axis=0)

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(times, beta_timeline.mean(axis=0), c='r',
            label='A-posteriori betrouwbaarsheidindex\n(Gemiddelde over MC tijdlijnen)')
    ax.fill_between(times, pi[0], pi[1], color='r', alpha=0.3, label=str(round(pi_lvl*100))+'% prediction interval')
    ax.plot(times, -stats.norm.ppf(true_pfs, loc=0, scale=1), c='k', label='Echte $β$')
    ax.plot(times, -stats.norm.ppf(prior_pf, loc=0, scale=1), c='b', label='Prior $β$')
    ax.set_xlabel('Tijd [jaar]', fontsize=12)
    ax.set_ylabel('Betrouwbaarsheidindex [-]', fontsize=12)
    # ax.set_yscale('log', base=10)
    ax.legend(fontsize=12)
    ax.set_title('Echte ${C}_{50}$=' + str(round(true_C50, 2)) + '[mm]', fontsize=14)
    plt.close()

    return fig


def plot_results(
        model: CorrosionModel,
        savefile: str,
        true_C50s: np.ndarray["n_true_C50s", float],
        post_pdf: np.ndarray[("n_C50_grid", "n_pf_times", "n_true_C50s"), float],
        pf: np.ndarray[("n_MC_timelines", "n_true_C50s", "n_pf_times"), float],
        pf_time_grid: Union[np.ndarray["n_pf_times", int], np.ndarray["n_pf_times", float]],
        true_pfs: np.ndarray[("n_true_C50s", "n_pf_times"), float],
        prior_pf: np.ndarray["n_pf_times", float],
        pi_bnds: List[float] = [0.05, 0.95]
) -> None:

    figs = []

    for i, true_C50 in enumerate(true_C50s):

        fig_posterior_per_C50 = plot_posterior_per_C50(model, post_pdf[..., i], true_C50)
        figs.append(fig_posterior_per_C50)

        fig_pf_timeline_per_C50 = plot_pf_timeline_per_C50(pf[:, i, :], pf_time_grid, true_C50, true_pfs[i],
                                                           prior_pf, pi_bnds)
        figs.append(fig_pf_timeline_per_C50)

        """ Removed reliability index plots """
        # fig_beta_timeline_per_C50 = plot_beta_timeline_per_C50(pf[:, i, :], pf_time_grid, true_C50, true_pfs[i],
        #                                                        prior_pf, pi_bnds)
        # figs.append(fig_beta_timeline_per_C50)

    fig_posterior = plot_posterior(model, post_pdf, true_C50s)
    fig_pf_timeline = plot_pf_timeline(pf.mean(axis=0), pf_time_grid, true_C50s)
    # fig_beta_timeline = plot_beta_timeline(pf, pf_time_grid, true_C50s, 3.5)  # Remove reliability index plots

    figs.append(fig_posterior)
    figs.append(fig_pf_timeline)
    # figs.append(fig_beta_timeline)

    pp = PdfPages(savefile)
    [pp.savefig(fig) for fig in figs]
    pp.close()
