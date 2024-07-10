"""Write Jmol files."""

# Copyright (c) 2024, Théo Cavignac <theo.cavignac+dev@gmail.com>, The PyDEF team <camille.latouche@cnrs-imn.fr>
# Licensed under the EUPL
from zipfile import ZIP_DEFLATED, ZipFile
import io

import numpy as np

from .. import __version__
from ..constants import atomic_mass


def write_xyz(f, atoms, ref, delta):
    """Write the coordinates and displacements of in the JMol xyz format.

    :param f: a file-like object to write to.
    :param atoms: the list of atom names
    :param ref: an array of atomic positions
    :param delta: an array of displacements
    """
    arr = np.hstack([ref, delta])
    for sp, row in zip(atoms, arr):
        print(f"{sp:2}", *(f"  {x:-12.05e}" for x in row), file=f)


def write_jmol_options(f, opts):
    """Write options in the form of a JMol script.

    :param f: a file like object.
    :param opts: a dictionary of options

        - *unitcell*: lattice vectors as a 3x3 matrix where vectors are in rows.
        - *bonds*: a list of :code:`(sp_a, sp_b, min_dist, max_dist)` where species
            names are strings of names of species and `*_dist` are interatomic distances
            in Angstrom.
        - *atom_colors*: a list of (sp, color) where sp is the name of a
            species and color is the name of a color or an HTML hex code (example
            :code:`"#FF0000"` for pure red).
        - *origin*: the origin of the unitcell box (in fractional coordinates)
    """
    if "unitcell" in opts:
        print(
            "unitcell [ {0 0 0}",
            format_v(opts["unitcell"][0]),
            format_v(opts["unitcell"][1]),
            format_v(opts["unitcell"][2]),
            "]",
            file=f,
        )
        origin = opts.get("origin", [0.5, 0.5, 0.5])
        print("unitcell CENTER", format_v(origin), file=f)

    if "bonds" in opts:
        for sp1, sp2, dmin, dmax in opts["bonds"]:
            print(
                f"connect {float(dmin):0.02} {float(dmax):0.02} (_{sp1}) (_{sp2})",
                file=f,
            )

    if "atom_colors" in opts:
        for sp, color in opts["atom_colors"]:
            if color.startswith("#"):
                c = f"x{color[1:7]:>06}"
                print(f"color (_{sp}) [{c}]", file=f)
            else:
                print(f"color (_{sp}) {color}", file=f)


def format_v(v):
    "Format a vector in Jmol syntax."
    x, y, z = v
    return f"{{ {x:0.5f} {y:0.5f} {z:0.5f} }}"


def export(
    dest,
    mode,
    *,
    displacement=True,
    scale=1.0,
    compression=ZIP_DEFLATED,
    offset=None,
    recenter=True,
    **opts,
):
    """Export a mode to JMol zip format.

    :param dest: path to the JMol zip file.
    :param mode: the mode to export.
    :param displacement: (kw only, default True) choose between eigendisplacements and eigenvectors
    :param scale: (kw only, default 1.0) a scale factor for the displacements/eigenvectors
    :param compression: (kw only) zipfile compression algorithm.
    :param offset: (kw only, `np.array([0, 0, 0])`) offset vector (in fractional coordinates) to shift the atoms in the unit cell to have different atoms at the center
    :param recenter: (kw only, `True`) wether atoms should be moved according to periodic conditions to fit in the unit cell
    :param \\**opts: see :func:`write_jmol_options`
    """

    if opts.get("unitcell", True) is True:
        opts["unitcell"] = mode.lattice

    ref = mode.ref.copy()

    if offset is not None:
        ref += (offset @ mode.lattice)[np.newaxis, :]

    if recenter:
        pfrac = np.remainder(ref @ np.linalg.inv(mode.lattice), 1.0)
        ref = pfrac @ mode.lattice

    with ZipFile(dest, mode="w", compression=compression) as ar:
        ar.writestr("JmolManifest.txt", manifest.encode("utf8"))
        ar.writestr("state.spt", state.encode("utf8"))

        with io.StringIO() as f:
            print(len(mode.atoms), file=f)
            print(f"Mode {mode.n}", file=f)

            if displacement:
                write_xyz(f, mode.atoms, ref, scale * mode.delta * np.sqrt(atomic_mass))
            else:
                write_xyz(f, ref, ref, scale * mode.eigenvector)

            ar.writestr("system.xyz", f.getvalue().encode("utf8"))

        with io.StringIO() as f:
            print("// System configuration", file=f)
            print(f"// Generated with Hylight {__version__}", file=f)
            write_jmol_options(f, opts)
            ar.writestr("system.spt", f.getvalue().encode("utf8"))


def export_disp(dest, struct, disp, *, compression=ZIP_DEFLATED, **opts):
    """Export a difference between two positions to JMol zip format.

    :param dest: path to the JMol zip file.
    :param struct: the reference position (a :py:class:`hylight.struct.Struct` instance).
    :param disp: an array of displacements.
    :param compression: (optional) zipfile compression algorithm.
    :param \\**opts: see :func:`write_jmol_options`
    """
    with ZipFile(dest, mode="w", compression=compression) as ar:
        ar.writestr("JmolManifest.txt", manifest.encode("utf8"))
        ar.writestr("state.spt", state.encode("utf8"))

        with io.StringIO() as f:
            print(len(struct.atoms), file=f)
            print(struct.system_name, file=f)
            write_xyz(f, struct.atoms, struct.raw, disp)
            ar.writestr("system.xyz", f.getvalue().encode("utf8"))

        with io.StringIO() as f:
            print("// System configuration", file=f)
            print(f"// Generated with Hylight {__version__}", file=f)
            write_jmol_options(f, opts)
            ar.writestr("system.spt", f.getvalue().encode("utf8"))


manifest = f"""\
# Jmol Manifest Zip Format 1.1
# Created with Hylight {__version__}
state.spt
"""

state = """\
function setupDisplay() {
  set antialiasDisplay;

  color background white;
}

function setupVectors() {
  vector on;
  color vector yellow;
  vector scale 2;
  vector 0.08;
}

function setupBonds() {
    wireframe 0.1;
}

function loadSystem() {
  load "xyz::$SCRIPT_PATH$system.xyz";
  connect delete;
  script "$SCRIPT_PATH$system.spt";
}

function _setup() {
  initialize;
  set refreshing false;
  setupDisplay;
  loadSystem;
  setupVectors;
  setupBonds;
  set refreshing true;
}

_setup;
"""
