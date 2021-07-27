#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition_Aromatic/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""


entry(
    index = 0,
    label = "C14H10 + C2H2 <=> C16H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (43.24, 'cm^3/(mol*s)'),
        n = 2.58,
        Ea = (41.945, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 8,
    longDesc = 
"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations; 
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: P + C2H2 <=> P1
XXXXREMOVEXXXX WAS INDEX = 22.
""",
)

entry(
    index = 1,
    label = "C6H6 + C2H2 <=> C8H8",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (261.981, 'cm^3/(mol*s)'),
        n = 2.6786,
        Ea = (147.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
XXXXREMOVEXXXX WAS INDEX = 23.
""",
)

entry(
    index = 2,
    label = "C10H8 + C2H2 <=> C12H10-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (286.399, 'cm^3/(mol*s)'),
        n = 2.61957,
        Ea = (115.627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
XXXXREMOVEXXXX WAS INDEX = 24.
""",
)

entry(
    index = 3,
    label = "C10H8-2 + C2H2 <=> C12H10-4",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (133.129, 'cm^3/(mol*s)'),
        n = 2.69336,
        Ea = (173.905, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
XXXXREMOVEXXXX WAS INDEX = 25.
""",
)

# entry(
#     index = 4,
#     label = "C12H10-2 <=> C2H2 + C10H8",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(7.458e+14, 's^-1'), n=0.0956, Ea=(54.82, 'kcal/mol'), T0=(1, 'K')),
#     reference = Article(
#         authors = ['Comandini, A.', 'Brezinsky, K.'],
#         title = 'Theoretical Study of the Formation of Naphthalene from the Radical/pi-Bond Addition between Single-Ring Aromatic Hydrocarbons',
#         journal = 'The Journal of Physical Chemistry A',
#         volume = '115',
#         pages = '5547-5559',
#         year = '2011',
#     ),
#     referenceType = "theory",
#     rank = 6,
#     longDesc =
# """
# uCCSD(T) with Dunning's correclation-consistent polarized double basis set (cc-pVDZ), TST.
# XXXXREMOVEXXXX WAS INDEX = 20.
# """,
# )
