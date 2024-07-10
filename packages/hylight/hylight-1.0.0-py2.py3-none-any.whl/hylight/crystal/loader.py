"""Read vibrational modes from CRYSTAL log.
"""

# Copyright (c) 2024, Théo Cavignac <theo.cavignac+dev@gmail.com>, The PyDEF team <camille.latouche@cnrs-imn.fr>
# Licensed under the EUPL
import numpy as np

from itertools import groupby

from ..constants import cm1_in_J, eV_in_J
from ..mode import Mode

cm1_in_meV = cm1_in_J / eV_in_J * 1000


def load_phonons(path: str) -> tuple[list[Mode], list[int], list[float]]:
    """Load phonons from a CRYSTAL17 logfile.

    :returns: :code:`(phonons, pops, masses)`

        - *phonons*: list of hylight.mode.Mode instances
        - *pops*: population for each atom species
        - *masses*: list of SI masses
    """

    phonons = []
    masses: list[float] = []
    names: list[str] = []

    with open(path) as log:
        for line in log:
            if "DIRECT LATTICE VECTORS CARTESIAN COMPONENTS (ANGSTROM)" in line:
                break

        #         X                    Y                    Z
        next(log)
        # Collect the three lines and convert to floats
        lattice_ = [next(log).split() for _ in range(3)]
        lattice = np.array(lattice_, dtype=float)

        for line in log:
            if "CARTESIAN COORDINATES - PRIMITIVE CELL" in line:
                break

        # *******************************************************************************
        # *      ATOM          X(ANGSTROM)         Y(ANGSTROM)         Z(ANGSTROM)
        # *******************************************************************************
        next(log)
        next(log)
        next(log)  # noqa: E702

        pos_ = []
        for line in log:
            l = line.strip()  # noqa: E741
            if l:
                pos_.append(l.split()[3:])
            else:
                break

        pos = np.array(pos_, dtype=float)

        for line in log:
            if "ATOMS ISOTOPIC MASS" in line:
                break

        next(log)

        for line in log:
            l = line.strip()  # noqa: E741
            if l:
                fields = l.split()
                masses.extend(map(float, fields[2::3]))
                names.extend(map(normalize, fields[1::3]))
            else:
                break

        _masses_12 = np.sqrt(masses).reshape((-1, 1))

        for line in log:
            if "NORMAL MODES NORMALIZED" in line:
                break

        next(log)

        head = next(log).strip()
        c = 0
        while head.startswith("FREQ"):
            freqs = map(float, head.strip().split()[1:])
            next(log)
            ats = []
            for _ in masses:
                # Drop the 13 first characters that qualify the line
                # Each line contains the infos for some number of modes
                # Note: the str to float conversion is delayed to be done
                # in batch in the next loop by numpy.
                # This is much faster than doing it here
                xs = next(log)[13:].strip().split()
                ys = next(log)[13:].strip().split()
                zs = next(log)[13:].strip().split()
                ats.append(zip(xs, ys, zs))

            # This loop actually has a small number of iteration corresponding
            # to how many columns the data is formatted in. On the other hand
            # `ats` has as many items as there are atoms in the system.
            # I am pretty sure it is fairly inneficient.
            # But, It works(TM).
            for f, disp in zip(freqs, zip(*ats)):
                c += 1  # Crystal does not index its phonons so I use a counter
                eigenvec = _masses_12 * np.array(disp, dtype=float)
                # FIXME The data found in the log file are the
                # eigendisplacement, thus I need to apply the sqrt of the mass
                # matrix to make them orthogonal (Can be verified on a system
                # with large mass differences like CaWO4). However, they are
                # still not orthonormal and I cannot find a proper explication
                # of what the amplitude is supposed to be. There is a vague
                # "classical amplitude in bohr" mention in the CRYSTAL log
                # file, but that is not very helpful in my opinion. In
                # particular it does not specify how the normalization is
                # applied, or what the amplitude depends on.
                eigenvec /= np.linalg.norm(eigenvec)

                # Note: imaginary freqs are logged as negative frequencies
                # Note 2: Mode currently expect the following units:
                # - frequency: meV
                # - positions: A
                # - eigenvec: normalized to 1
                # - masses: atomic masses
                phonons.append(
                    Mode(
                        lattice,
                        names,
                        c,
                        f >= 0,
                        abs(f) * cm1_in_meV,
                        pos,
                        eigenvec,
                        masses,
                    )
                )
            next(log)
            head = next(log).strip()

    pops = [sum(1 for _ in s) for (_, s) in groupby(names)]
    return phonons, pops, masses


def normalize(name):
    "Normalize an atom name (e.g. ZR -> Zr)."
    return name[0].upper() + name[1:].lower()
