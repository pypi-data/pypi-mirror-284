# coding: utf-8
# Copyright (c) Max-Planck-Institut für Eisenforschung GmbH - Computational Materials Design (CM) Department
# Distributed under the terms of "New BSD License", see the LICENSE file.

from ase.atoms import Atoms
import numpy as np

__author__ = "Osamu Waseda"
__copyright__ = (
    "Copyright 2021, Max-Planck-Institut für Eisenforschung GmbH - "
    "Computational Materials Design (CM) Department"
)
__version__ = "1.0"
__maintainer__ = "Osamu Waseda"
__email__ = "waseda@mpie.de"
__status__ = "development"
__date__ = "Sep 1, 2018"


def get_equivalent_atoms(
    structure: Atoms, symprec: float = 1e-5, angle_tolerance: float = -1.0
):
    """
    Args: (read phonopy.structure.spglib for more details)
        symprec:
            float: Symmetry search tolerance in the unit of length.
        angle_tolerance:
            float: Symmetry search tolerance in the unit of angle deg.
                If the value is negative, an internally optimized routine
                is used to judge symmetry.

    """
    import spglib as spg
    from phonopy.structure.atoms import PhonopyAtoms

    positions = structure.get_scaled_positions()
    cell = structure.cell
    types = structure.get_chemical_symbols()
    types = list(types)
    natom = len(types)
    positions = np.reshape(np.array(positions), (natom, 3))
    cell = np.reshape(np.array(cell), (3, 3))
    unitcell = PhonopyAtoms(symbols=types, cell=cell, scaled_positions=positions)
    ops = spg.get_symmetry(unitcell, symprec=symprec, angle_tolerance=angle_tolerance)
    return ops["equivalent_atoms"]
