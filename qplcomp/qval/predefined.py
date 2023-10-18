# ------------------------------------------------------------
# predefined.py
# All the predefined operators are provided by this file
# ------------------------------------------------------------

import numpy as np
from typing import Dict

# TODO #3
# So that it can make use of symbolic expressions.

optlib = {
    "c1" : np.array(
        [[1.]]
    ),

    "c0" : np.array(
        [[0.]]
    ),


    # unitary
    "I" : np.array(
        [[1., 0.],
        [0., 1.]]
    ),
    
    "X" : np.array(
        [[0., 1.],
        [1., 0.]]
    ),

    "Y" : np.array(
        [[0., -1.j],
        [1.j, 0.]]
    ),

    "Z" : np.array(
        [[1., 0.],
        [0., -1.]]
    ),

    "H" : np.array(
        [[1., 1.],
        [1., -1.]]
    )/np.sqrt(2),

    "S" : np.array(
        [[1., 0.],
         [0., 1j]]
    ),

    "CX" : np.array(
        [[1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 0., 1.],
        [0., 0., 1., 0.]]
    ).reshape((2,2,2,2)),

    "CZ" : np.array(
        [[1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., -1.]]
    ).reshape((2,2,2,2)),

    "CH" : np.array(
        [[1., 0., 0., 0.],
        [0., 1., 0., 0.,],
        [0., 0., 1./np.sqrt(2), 1./np.sqrt(2)],
        [0., 0., 1./np.sqrt(2), -1./np.sqrt(2)]]
    ).reshape((2,2,2,2)),

    "SWAP" : np.array(
        [[1., 0., 0., 0.],
        [0., 0., 1., 0.],
        [0., 1., 0., 0.],
        [0., 0., 0., 1.]]
    ).reshape((2,2,2,2)),


    "CCX" : np.array(       # it is also called the "Toffolli gate"
        [[1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 1., 0.]]
    ).reshape((2,2,2,2,2,2)),
    
    # hermitian operators
    "Idiv2" : np.array(
        [[1., 0.],
        [0., 1.]]
    )/2.,

    "Zero0" : np.zeros((1,1)),

    "Zero" : np.zeros((2,2)),

    "P0" : np.array(
        [[1., 0.],
        [0., 0.]]
    ),

    "P0div2" : np.array(
        [[1., 0.],
        [0., 0.]]
    )/2,

    "P1" : np.array(
        [[0., 0.],
        [0., 1.]]
    ),

    "P1div2" : np.array(
        [[0., 0.],
        [0., 1.]]
    )/2,

    "Pp" : np.array(
        [[0.5, 0.5],
        [0.5, 0.5]]
    ),

    "Ppdiv2" : np.array(
        [[0.5, 0.5],
        [0.5, 0.5]]
    )/2,

    "Pm" : np.array(
        [[0.5, -0.5],
        [-0.5, 0.5]]
    ),

    "Pmdiv2" : np.array(
        [[0.5, -0.5],
        [-0.5, 0.5]]
    )/2,
    
    "P00" : np.array(
        [[1., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]
    ),

    # 2 qubits equal on the 01 basis
    "Eq01_2" : np.array(
        [[1., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 1.]]
    ).reshape((2,2,2,2)),
    
    # 2 qubits not equal on the 01 basis
    "Neq01_2" : np.array(
        [[0., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., 0.]]
    ).reshape((2,2,2,2)),

    # 3 qubits equal on the 01 basis
    "Eq01_3" : np.array(
        [[1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1.]]
    ).reshape((2,2,2,2,2,2)),

    # Density Operators
    "Omega" : np.array(
        [[0.5, 0., 0., 0.5],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0.5, 0., 0., 0.5]]
    ),

    #####################################################
    # Kraus operator
    "E10" : np.array(
        [[0., 1.],
         [0., 0.]]
    )
}


soptlib = {
    "E'P0" :
    [optlib["P0"]],
    "E'P1" :
    [optlib["P1"]],
    "E'DP" :
    [optlib["P0"], optlib["P1"]],
    "E'Set0" : 
    [optlib["P0"], optlib["E10"]],
}

# some functions

def Rz(theta : float) -> np.ndarray:
    return np.cos(theta/2) * optlib["I"] - 1j*np.sin(theta/2) * optlib["Z"]


# transform to QVal instances

from .val import QVal
from .qopt import QOpt
from .qso import QSOpt

qvallib : Dict[str, QVal]= {}
for key in optlib:
    qvallib[key] = QOpt(optlib[key])

for key in soptlib:
    m_kraus = soptlib[key]
    opt_kraus = [QOpt(E) for E in m_kraus]
    qvallib[key] = QSOpt(opt_kraus)