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
                 xlabel = None,
                 ylabel = None,
                 cancel_x = False,
                 cancel_y = False,
                 font = font,
                 fontsize = fontsize,
                 tickwidth1 = 2.5,
                 tickwidth2 = 2,
                 legend = True,
                 ncol = 1,
                 locator_x = 2,
                 locator_y = 2,
                 title = None,
                 xpad = None,
                 ypad = None,
                 x_boundaries=None,
                 x_ticks=None,
                 y_boundaries=None,
                 y_ticks=None,
                 git_root = None,
                 path_figures = None,
                 filename = None,
                 show = True,
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
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.cancel_x = cancel_x
        self.cancel_y = cancel_y
        font = font
        self.fontsize = fontsize
        self.tickwidth1 = tickwidth1
        self.tickwidth2 = tickwidth2
        self.legend = legend
        self.ncol = ncol
        self.locator_x = locator_x
        self.locator_y = locator_y
        self.title = title
        self.axis_color = axis_color
        self.xpad = xpad
        self.ypad = ypad
        self.x_boundaries=x_boundaries
        self.x_ticks=x_ticks
        self.y_boundaries=y_boundaries
        self.y_ticks=y_ticks
        self.git_root = git_root
        self.path_figures = path_figures
        self.filename = filename
        self.show = show
        # differenciate linewidth figure and data 

    def update_parameters(self, **args):    
        for arg, value in args.items():
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


    def complete_panel(self, **args):
        
        self.update_parameters(**args)

        if self.xlabel is not None:
            self.ax[-1].set_xlabel(self.xlabel, fontdict=font)
            if self.cancel_x:
                self.ax[-1].set_xticklabels([])
        else:
            self.ax[-1].set_xticklabels([])

        if self.ylabel is not None:
            self.ax[-1].set_ylabel(self.ylabel, fontdict=font)
            if self.cancel_y:
                self.ax[-1].set_yticklabels([])  
        else:
            self.ax[-1].set_yticklabels([])

        if self.title is not None:
            self.ax[-1].set_title(self.title, fontdict=font)

        plt.xticks(fontsize=self.fontsize)
        plt.yticks(fontsize=self.fontsize)
        self.ax[-1].yaxis.offsetText.set_fontsize(20)
        self.ax[-1].minorticks_on()

        self.ax[-1].tick_params('both', length=10, width=self.tickwidth1, which='major', direction='in')
        self.ax[-1].tick_params('both', length=6, width=self.tickwidth2, which='minor', direction='in')
        self.ax[-1].xaxis.set_ticks_position('both')
        self.ax[-1].yaxis.set_ticks_position('both')

        # border of graph
        self.ax[-1].spines["top"].set_linewidth(self.linewidth)
        self.ax[-1].spines["bottom"].set_linewidth(self.linewidth)
        self.ax[-1].spines["left"].set_linewidth(self.linewidth)
        self.ax[-1].spines["right"].set_linewidth(self.linewidth)

        if self.locator_x is not None:
            minor_locator_x = AutoMinorLocator(self.locator_x)
            self.ax[-1].xaxis.set_minor_locator(minor_locator_x)
        if self.locator_y is not None:
            minor_locator_y = AutoMinorLocator(self.locator_y)
            self.ax[-1].yaxis.set_minor_locator(minor_locator_y)

        if self.legend:
            self.ax[-1].legend(frameon=False, fontsize=fontsize, labelcolor=self.axis_color,
                    loc='best', handletextpad=0.5, ncol=self.ncol,
                    handlelength = 0.86, borderpad = 0.3, 
                    labelspacing=0.3)
                    
        if self.axis_color is not None:
            self.ax[-1].xaxis.label.set_color(self.axis_color)
            self.ax[-1].yaxis.label.set_color(self.axis_color)
            self.ax[-1].tick_params(axis='x', colors=self.axis_color)
            self.ax[-1].tick_params(axis='y', colors=self.axis_color)
            self.ax[-1].spines['left'].set_color(self.axis_color)
            self.ax[-1].spines['top'].set_color(self.axis_color)
            self.ax[-1].spines['bottom'].set_color(self.axis_color)
            self.ax[-1].spines['right'].set_color(self.axis_color)
            self.ax[-1].tick_params(axis='y', which='both', colors=self.axis_color)
            self.ax[-1].tick_params(axis='x', which='both', colors=self.axis_color)

        if self.xpad is not None:
            self.ax[-1].tick_params(axis='x', colors=self.axis_color, pad = self.xpad)

        if self.ypad is not None:
            self.ax[-1].tick_params(axis='y', colors=self.axis_color, pad = self.ypad)

    def set_boundaries(self, **args):
        self.update_parameters(**args)
        if self.x_boundaries is not None:
            plt.xlim(self.x_boundaries)
        if self.x_ticks is not None:
            plt.xticks(self.x_ticks)
        if self.y_boundaries is not None:
            plt.ylim(self.y_boundaries)
        if self.y_ticks is not None:
            plt.yticks(self.y_ticks)  

    def save_figure(self, **args):
        self.update_parameters(**args)

        assert os.path.exists(self.git_root + self.path_figures)

        self.fig.tight_layout()
        if self.dark_mode:
            if self.transparency is False:
                plt.style.use('default')
            plt.savefig(self.git_root + self.path_figures + self.filename + "-dm.png",
                        bbox_inches = 'tight', pad_inches = 0.062,
                        transparent=self.transparency, dpi=200)
            
        else:
            if self.transparency is False:
                plt.style.use('default')
            plt.savefig(self.git_root + self.path_figures + self.filename + ".png",
                        bbox_inches = 'tight', pad_inches = 0.062,
                        transparent=self.transparency, dpi=200)
        if self.show:
            plt.show()

