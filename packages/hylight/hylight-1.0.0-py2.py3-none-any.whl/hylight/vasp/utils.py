"""Pervasive utilities for hylight.vasp submodule.
"""

# Copyright (c) 2024, Théo Cavignac <theo.cavignac+dev@gmail.com>, The PyDEF team <camille.latouche@cnrs-imn.fr>
# Licensed under the EUPL
from copy import deepcopy as copy

import numpy as np

from ..constants import atomic_mass
from ..multi_modes import compute_delta_R
from ..mode import get_energies, Mask

from ..loader import load_phonons
from .common import Poscar


def make_finite_diff_poscar(
    outcar,
    poscar_gs,
    poscar_es,
    A=0.01,
    *,
    load_phonons=load_phonons,
    bias=0,
    mask=None,
):
    """Compute positions for evaluation of the curvature of the ES PES.

    :param outcar: the name of the file where the phonons will be read.
    :param poscar_gs: the path to the ground state POSCAR
    :param poscar_es: the path to the excited state POSCAR, it will be used as
        a base for the generated Poscars
    :param A: (optional, 0.01) the amplitude of the displacement in A.
    :param load_phonons: (optional, vasp.loader.load_phonons) the procedure use
        to read outcar
    :param bias: an energy under which modes are ignored, 0 by default
    :param mask: a :class:`..mode.Mask` to select the modes to consider, override the bias.
    :return: :code:`(mu, pes_left, pes_right)`

        - mu: the effective mass in kg
        - pes_left: a Poscar instance representing the left displacement
        - pes_right: a Poscar instance representing the right displacement
    """

    if mask is None:
        mask = Mask.from_bias(bias)

    delta_R = compute_delta_R(poscar_gs, poscar_es)

    phonons, _, masses = load_phonons(outcar)
    phonons = [p for p in phonons if p.real and mask.accept(p.energy)]

    m = np.array(masses).reshape((-1, 1))
    delta_Q = np.sqrt(m) * delta_R

    k = get_energies(phonons, mask=mask) ** 2
    d = np.array(
        [np.sum(p.eigenvector * delta_Q) for p in phonons if mask.accept(p.energy)]
    )

    kd = k * d

    grad = m ** (-0.5) * np.sum(
        (np.array([p.eigenvector for p in phonons]) * kd.reshape((-1, 1, 1))), axis=0
    )

    g_dir = -grad / np.linalg.norm(grad)

    delta = A * g_dir

    pes = Poscar.from_file(poscar_es)
    pes_left = copy(pes)
    pes_right = copy(pes)

    pes_left.raw -= delta
    pes_right.raw += delta

    mu = (np.linalg.norm(g_dir, axis=-1) ** 2).dot(masses) * atomic_mass
    return mu, pes_left, pes_right
