# Matplotlib Pyplot functions

Personal functions for making [Pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html) figures compatible with Latex documents.
These functions are used for several of my personal projects, including [LAMMPS tutorials](https://lammpstutorials.github.io) and 
[NMRforMD](https://nmrformd.readthedocs.io).

## Light mode vs dark mode

To improve the visual of the [website](https://lammpstutorials.github.io) I am creating, 
I systematically generate figures for both light mode and dark mode, with 
transparent background. For a scientific publication, use the light mode
without transparent background.

## Example

See the [examples](examples.ipynb) notebook for the commands behind these figures.

### Single panel

![illustration](examples/example-1-light.png#gh-light-mode-only)

![illustration](examples/example-1-dark.png#gh-dark-mode-only)

### Triple panel with different widths

![illustration](examples/example-2-light.png#gh-light-mode-only)

![illustration](examples/example-2-dark.png#gh-dark-mode-only)

## Open symbols

For open symbol plot, use:

``` python
markeredgewidth=3, 
markeredgecolor=colors["mygray"],
markerfacecolor='none',
```
