#!/usr/bin/env python
# encoding: utf-8

name = "Russel_termination"
shortDesc = u""
longDesc = u"""
The Russel termination mechanism is an important termination step for the autoxidation chain reaction for active
pharmaceutical ingredients.

The termination reaction goes through an unstable tetroxide intermediate. Primary and secondary tetroxides readily 
decomposes to form three non-radical products (alcohol, carbonyl compound, and singlet oxygen O=O)
via a six-membered cyclic transition state. 

This family describes the following reaction:
(R1,R2,H)-C-O-Od + (R3,R4,H)-C-O-Od -> O=O + (R1,R2)-C=O + (R3,R4,H)-C-OH

atom labels:
(R1,R2,H[*2])-C[*1]-O[*3]-Od[*4] + (R3,R4,H)-C-O[*5]-Od[*6] -> O[*4]=O[*6] + (R1,R2)-C[*1]=O[*3] + (R3,R4,H[*2])-C-O[*5]H
"""

template(reactants=["R1R2COO", "R3R4COO"], products=["O=O", "R1R2C=O", "R3R4COH"], ownReverse=False)

reverse = "reverse_Russel"

reversible = False

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['FORM_BOND', '*4', 1, '*6'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['LOSE_RADICAL', '*4', '1'],
    ['LOSE_RADICAL', '*6', '1'],
    ['CHANGE_BOND', '*4', 1, '*6'],
    ['CHANGE_BOND', '*1', 1, '*3'],
])

entry(
    index = 0,
    label = "R1R2COO",
    group =
"""
1  *1 C u0 p0 c0 {2,S} {3,S}
2  *2 H u0 p0 c0 {1,S}
3  *3 O u0 p2 c0 {1,S} {4,S}
4  *4 O u1 p1 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "R3R4COO",
    group =
"""
1     C u0 p0 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3  *5 O u0 p2 c0 {1,S} {4,S}
4  *6 O u1 p1 c0 {3,S}
""",
    kinetics = None,
)

tree(
"""
L1: R1R2COO
L1: R3R4COO
"""
)
