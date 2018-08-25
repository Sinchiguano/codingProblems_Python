#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
from Burrito3 import *

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())


def main():
    #Feel free to add code below to test out the class
    newBurrito = Burrito("steak", True, True, True)
    print(newBurrito.meat)
    print(newBurrito.to_go)
    print(newBurrito.guacamole)
    print(newBurrito.extra_meat)
    print(newBurrito.cheese)

if __name__=='__main__':
    main()
