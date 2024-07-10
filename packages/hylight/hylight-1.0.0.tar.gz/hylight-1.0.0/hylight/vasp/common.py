"""Common utilities to read and write VASP files.
"""

# Copyright (c) 2024, Théo Cavignac <theo.cavignac+dev@gmail.com>, The PyDEF team <camille.latouche@cnrs-imn.fr>
# Licensed under the EUPL
import numpy as np

from ..utils import InputError
from ..struct import Struct


class Poscar(Struct):
    """A crystal cell from a VASP POSCAR file."""

    @classmethod
    def from_file(cls, filename):
        """Load a POSCAR file

        :param filename: path to the file to read
        :returns: a Poscar object.
        """
        with open(filename) as f:
            next(f)  # system name
            fac = float(next(f))
            params = fac * np.array(
                [
                    np.array(l.strip().split(), dtype="float")
                    for _, l in zip(range(3), f)
                ]
            )

            labels = next(f).strip().split()
            atoms_pop = list(map(int, next(f).strip().split()))
            if len(labels) != len(atoms_pop):
                raise InputError(f"{filename} is not a coherent POSCAR file.")

            mode = next(f).strip()[0].lower()

            species = {}

            if mode == "s":
                # selective dynamics, skip the line
                mode = next(f).strip()[0].lower()

            if mode == "d":
                for spec, n in zip(labels, atoms_pop):
                    pos = []
                    for _, line in zip(range(n), f):
                        ls = line.strip()
                        if not ls:
                            raise InputError(
                                f"{filename} is not a coherent POSCAR file."
                            )
                        x, y, z, *_ = ls.split()
                        pos.append(np.array([x, y, z], dtype="float").dot(params))
                    species[spec] = np.array(pos)
            else:
                for spec, n in zip(labels, atoms_pop):
                    pos = []
                    for _, line in zip(range(n), f):
                        ls = line.strip()
                        if not ls:
                            raise InputError(
                                f"{filename} is not a coherent POSCAR file."
                            )
                        x, y, z, *_ = ls.split()
                        pos.append(np.array([x, y, z], dtype="float"))
                    species[spec] = np.array(pos)

            return Poscar(params, species, species_names=labels)

    def to_stream(self, out, cartesian=True):
        """Write a POSCAR content to a stream.

        The property system_name may be set to change the comment at the top of
        the file.

        :param path: path to the file to write
        :param cartesian:

            - if True, write the file in cartesian representation,
            - if False, write in fractional representation
        """
        species = [(n, self.species[n]) for n in self._species_names]

        out.write(f"{self.system_name}\n")
        out.write("1.0\n")
        np.savetxt(out, self.lattice, "%15.12f", delimiter="\t", newline="\n")

        out.write(" ".join(f"{name:6}" for name, _lst in species))
        out.write("\n")
        out.write(" ".join(f"{len(lst):6}" for _name, lst in species))
        out.write("\n")

        if cartesian:
            out.write("Cartesian\n")
            for _name, lst in species:
                for pos in lst:
                    out.write("  ".join(f"{x:.8f}" for x in pos))
                    out.write("\n")
        else:
            out.write("Direct\n")
            inv_params = np.linalg.inv(self.lattice)
            for _name, lst in species:
                for pos in lst:
                    d_pos = pos.dot(inv_params)
                    out.write("  ".join(f"{x:.8f}" for x in d_pos))
                    out.write("\n")

    def to_file(self, path="POSCAR", cartesian=True):
        """Write to a POSCAR file.

        The property system_name may be set to change the comment at the top of
        the file.

        :param path: path to the file to write
        :param cartesian:

            - if True, write the file in cartesian representation,
            - if False, write in fractional representation
        """
        with open(path, "w+") as out:
            self.to_stream(out, cartesian=cartesian)
