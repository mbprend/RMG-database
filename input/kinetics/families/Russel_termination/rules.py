#!/usr/bin/env python
# encoding: utf-8

name = "Russel_termination/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "Russel",
    kinetics = ArrheniusEP(
        A = (1e10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (273, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)
