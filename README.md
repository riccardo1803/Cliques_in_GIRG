# Counting triangles in Geometric Inhomogeneous random graph
In this repository is contained the Python code used for sampling the Geometric Inhomogeneous random graph and counting the number of triangles contained.

- girgs.py

The main python file. The package "girg_sampling" is used to sample efficiently the GIRG. (https://pypi.org/project/girg-sampling/)
.

- gamma-1.5 | gamma-2.0 | gamma-5.0

In these folders are collected the results of the simulation for different values of gamma and different values of the power law exponent tau. The txt files collect the number of triangles from multiple simulations of the GIRG under the same parameters. In each line is also encoded the corrispondent seed (weight seed + position seed + edge probability seed) used to generate the GIRG.
.

- PICTURES

In the png files is possible to observe the asmptotic behaviour for the number of triangles under the specific set of parameters indicated in the nale of the files. There are in total four pictures, two for the normal plot in the case tau=2.1 and tau=2.7, two for the log-log plot in the case tau=2.1 and tau=2.7. In each picture different values of gamma are shown with different colors.
