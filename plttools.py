import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.ticker import AutoMinorLocator

sys.path.append("colors/")
from colorseries import colorserie1

fontsize = 34
font = {'family': 'sans', 'color':  'black', 'weight': 'normal', 'size': fontsize}

class PltTools():
    """
    fig_size must be chosen as a tuple, e.g. (18,6)
    If dark_mode, then a dark background is set.
    """
    def __init__(self,
                 fig_size = None,
                 dark_mode = False,
                 transparency = False,
                 use_serif = True,
                 tex_font = True,
                 x = None,
                 y = None,
                 marker = None,
                 type = "plot",
                 markersize = 12,
                 linewidth = 4,
                 data_color = None,
                 axis_color = 'black',
                 data_label = None,
                 panel_label = None,
                 shift_label_panel = 0.2,
                 sshift_label_panel = None,
                 type_label_panel = "a",
                 open_symbols = False,
                 markeredgewidth = 0,
                 n_colone = 1,
                 n_line = 1,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self.fig_size = fig_size
        self.dark_mode = dark_mode
        self.transparency = transparency
        self.use_serif = use_serif
        self.tex_font = tex_font
        self.x = x
        self.y = y
        self.type = type
        self.marker = marker
        self.markersize = markersize
        self.linewidth = linewidth
        self.data_color = data_color
        self.axis_color = axis_color
        self.data_label = data_label
        self.panel_label = panel_label
        self.open_symbols = open_symbols
        self.markeredgewidth = markeredgewidth
        self.shift_label_panel = shift_label_panel
        self.sshift_label_panel = sshift_label_panel
        self.type_label_panel = type_label_panel
        self.n_colone = n_colone
        self.n_line = n_line

    def update_parameters(self, **args):    
        for arg, value in args.items():
            if hasattr(self, arg) and value is not None:
                setattr(self, arg, value)

    def prepare_figure(self, **args):

        self.update_parameters(**args)

        # set the right background
        if self.transparency is False:
            if self.dark_mode:
                plt.style.use('dark_background')
            else:
                plt.style.use('default')
        # set the figure size
        fig = plt.figure(figsize=self.fig_size)
        # choose the font
        if self.tex_font:
            if self.use_serif:
                # Serif latex font
                plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "serif",
                    "font.serif": ["Palatino"],
                }) 
            else:
                # Non-serif latex font
                plt.rcParams.update({
                    "text.usetex": True,
                    "font.family": "sans-serif",
                    "font.serif": ["Open Sans"],
                    "text.latex.preamble" : r"\usepackage{cmbright}"
                })
        
        self.fig = fig

        if self.open_symbols:
            self.markerfacecolor = 'none'
        else:
            self.markerfacecolor = self.data_color

    def add_panel(self, **args):

        self.update_parameters(**args)

        try:
            self.id_panel += 1
            self.ax.append(plt.subplot(self.n_line, self.n_colone, self.id_panel))
        except:
            self.ax = []
            self.id_panel = 1
            self.ax.append(plt.subplot(self.n_line, self.n_colone, self.id_panel))
        self.cpt_colors = 0

    def add_plot(self, **args):

        self.update_parameters(**args)

        if self.data_color is None:
            data_color = colorserie1[self.cpt_colors]
        else:
            data_color = self.data_color
            
        #assert self.x is not None
        self.ax[-1].plot(self.x,
                    self.y,
                    self.marker,
                    color = data_color,
                    markersize = self.markersize,
                    linewidth = self.linewidth,
                    label = self.data_label,
                    markeredgewidth = self.markeredgewidth,
                    markeredgecolor = data_color,
                    markerfacecolor = self.markerfacecolor)
        self.cpt_colors += 1
        
        if (self.type == 'semilogy') | (self.type == 'loglog'):
            self.ax[-1].set_yscale('log')
        if (self.type == 'semilogx') | (self.type == 'loglog'):
            self.ax[-1].set_xscale('log')

    def add_subplotlabels(self, **args):

        """Add a labels to each axis of a figure."""

        self.update_parameters(**args)

        if self.type_label_panel == "a":
            labels = []
            for i, value in zip(range(len(self.ax)), list(map(chr, range(97, 123)))):
                if self.tex_font:
                    labels.append(r"$\textrm{a}$")
                else:
                    labels.append(value)

        for i, subplotlabel in enumerate(labels):
            if self.sshift_label_panel is None:
                trans = mtransforms.ScaledTranslation(
                    self.shift_label_panel, -0.2, self.fig.dpi_scale_trans)
            else:
                trans = mtransforms.ScaledTranslation(
                    self.sshift_label_panel[i], 0, self.fig.dpi_scale_trans) 
            self.ax[i].text(
                0.0,
                1.0,
                subplotlabel,
                transform=self.ax[i].transAxes + trans,
                va="top",
                #bbox=dict(facecolor="none", alpha=0.5, edgecolor="none", pad=3.0),
                fontdict = font,
                color=self.axis_color
            )     


def complete_panel(ax, xlabel, ylabel, cancel_x=False, cancel_y=False,
                font=font, fontsize=fontsize, linewidth=2.5, tickwidth1=2.5,
                tickwidth2=2, legend=True, ncol=1, locator_x = 2, locator_y = 2,
                title=None, axis_color=None, xpad = None, ypad = None):
    
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontdict=font)
        if cancel_x:
            ax.set_xticklabels([])
    else:
        ax.set_xticklabels([])

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontdict=font)
        if cancel_y:
            ax.set_yticklabels([])  
    else:
        ax.set_yticklabels([])

    if title is not None:
        ax.set_title(title, fontdict=font)

    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    ax.yaxis.offsetText.set_fontsize(20)
    ax.minorticks_on()

    ax.tick_params('both', length=10, width=tickwidth1, which='major', direction='in')
    ax.tick_params('both', length=6, width=tickwidth2, which='minor', direction='in')
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # border of graph
    ax.spines["top"].set_linewidth(linewidth)
    ax.spines["bottom"].set_linewidth(linewidth)
    ax.spines["left"].set_linewidth(linewidth)
    ax.spines["right"].set_linewidth(linewidth)

    if locator_x is not None:
        minor_locator_x = AutoMinorLocator(locator_x)
        ax.xaxis.set_minor_locator(minor_locator_x)
    if locator_y is not None:
        minor_locator_y = AutoMinorLocator(locator_y)
        ax.yaxis.set_minor_locator(minor_locator_y)

    if legend:
        ax.legend(frameon=False, fontsize=fontsize, labelcolor=axis_color,
                loc='best', handletextpad=0.5, ncol=ncol,
                handlelength = 0.86, borderpad = 0.3, 
                labelspacing=0.3)
                
    if axis_color is not None:
        ax.xaxis.label.set_color(axis_color)
        ax.yaxis.label.set_color(axis_color)
        ax.tick_params(axis='x', colors=axis_color)
        ax.tick_params(axis='y', colors=axis_color)
        ax.spines['left'].set_color(axis_color)
        ax.spines['top'].set_color(axis_color)
        ax.spines['bottom'].set_color(axis_color)
        ax.spines['right'].set_color(axis_color)
        ax.tick_params(axis='y', which='both', colors=axis_color)
        ax.tick_params(axis='x', which='both', colors=axis_color)

    if xpad is not None:
        ax.tick_params(axis='x', colors=axis_color, pad = xpad)

    if ypad is not None:
        ax.tick_params(axis='y', colors=axis_color, pad = ypad)

def save_figure(plt, fig, mode, git_root, path_figures, filename, show=False, transparency=True):
    assert os.path.exists(git_root + path_figures)
    fig.tight_layout()
    if mode == 'light':
        if transparency is False:
            plt.style.use('default')
        plt.savefig(git_root + path_figures + filename + "-light.png",
                    bbox_inches = 'tight', pad_inches = 0.062,
                    transparent=transparency, dpi=200)
    else:
        if transparency is False:
            plt.style.use('default')
        plt.savefig(git_root + path_figures + filename + "-dark.png",
                    bbox_inches = 'tight', pad_inches = 0.062,
                    transparent=transparency, dpi=200)
    if show:
        plt.show()

def set_boundaries(plt, x_boundaries=None, x_ticks=None, y_boundaries=None, y_ticks=None):
    if x_boundaries is not None:
        plt.xlim(x_boundaries)
    if x_ticks is not None:
        plt.xticks(x_ticks)
    if y_boundaries is not None:
        plt.ylim(y_boundaries)
    if y_ticks is not None:
        plt.yticks(y_ticks)  

def import_ave_time(filename, folder=None):
    assert filename[:6] == "output"
    if folder is None:
        if os.path.exists(filename):
            data = np.loadtxt(filename)
            try:
                time, data = data.T
            except:
                time, data, _ = data.T
            if os.path.exists("data_plot/") is False:
                os.mkdir("data_plot/")
            np.savetxt("data_plot/"+filename[7:], np.vstack([time, data]).T)
        else:
            time, data = np.loadtxt("data_plot/"+filename[7:]).T
    else:
        if os.path.exists(folder+filename):
            data = np.loadtxt(folder+filename)
            try:
                time, data = data.T
            except:
                time, data, _ = data.T
            if os.path.exists("data_plot/") is False:
                os.mkdir("data_plot/")
            np.savetxt("data_plot/"+filename[7:], np.vstack([time, data]).T)
    return time, data