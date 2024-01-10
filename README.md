# Matplotlib Pyplot functions

Personal functions for making [Pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html) figures compatible with Latex documents. These functions are also
in use on [LAMMPS tutorials](https://lammpstutorials.github.io) and 
[NMRforMD](https://nmrformd.readthedocs.io).

## Example

The best of the two images depends on dark-mode / light mode you are using.
See the [examples](examples.ipynb) notebook for illustration of the use the functions.

![illustration](examples/example-1-light.png)

![illustration](examples/example-1-dark.png)

![illustration](examples/example-2-light.png)

![illustration](examples/example-2-dark.png)

## Open symbols

For open symbol plot, use:

``` python
markeredgewidth=3, 
markeredgecolor=colors["mygray"],
markerfacecolor='none',
```
