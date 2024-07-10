# The Hylight Package

## About

Welcome to Hylight's code repository!

Hylight is a post-processing tool written in Python to simulate the
luminescence of solids based on the results of *ab initio* computations.

You may be interested in reading our first paper using it:
[Modeling Luminescence Spectrum of BaZrO3:Ti Including Vibronic Coupling from First Principles Calculations][1].

## Installation

Hylight is published on PyPI. You can install it with `pip`

For a **minimal** installation (maybe you want to use some of the features on a cluster) use `pip install hylight`.
For you own workstation, we recommend that you enable **all optional features**: `pip install hylight[hdf5,plotting,phonopy]`.

## Usage

To learn how to use Hylight, you can read [documentation and tutorial](https://pydef.github.io/hylight) (or the [PDF version](./public/latex/hylight.pdf))

## Attribution

### License

Hylight is written and maintained by the PyDEF team.
The source code for Hylight is distributed under the EUPL_ license.
This is a non viral copyleft license, to be compared to MPL.
However, unlike the MPL, it is available in all official languages of the EU,
including authors own language, french.

See [LICENSE](https://github.com/PyDEF/hylight/blob/main/LICENSE)

### Citing Hylight

If you ever use Hylight for a published scientific work, we ask that you cite the related paper:
[Simulation of luminescence spectra in solids: Hylight, an easy-to-use post-processing software][2].

[1]: https://www.doi.org/10.1021/acs.jctc.2c00949
[2]: coming soon
