# PyGEP: Gene Expression Programming for Python
# Copyright (C) 2007  Ryan J. O'Neil
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''
Common rounding functions:
    - (floor) floor_op: math.floor(x)
    - (ceil ) ceil_op:  math.ceil(x)
    - (abs  ) abs_op:   abs(x)
'''

from pygep.chromosome import symbol
import math


__all__ = 'ROUNDING_ALL', 'ROUNDING_ARITY_1'


@symbol('floor')
def floor_op(i):
    '''@return: math.floor(i)'''
    return math.floor(i)


@symbol('ceil')
def ceil_op(i):
    '''@return: math.ceil(i)'''
    return math.ceil(i)


@symbol('abs')
def abs_op(i):
    '''@return: abs(i)'''
    return abs(i)


ROUNDING_ARITY_1 = floor_op, ceil_op, abs_op
ROUNDING_ALL = ROUNDING_ARITY_1
