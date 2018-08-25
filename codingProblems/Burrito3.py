#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""
#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
"""
class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat=False,guacamole=False,cheese=False,
                    pico=False,corn=False):

        self.meat=self.set_meat(meat)
        self.to_go=self.set_to_go(to_go)
        self.rice=self.set_rice(rice)
        self.beans=self.set_beans(beans)
        self.extra_meat=self.set_extra_meat(extra_meat)
        self.guacamole=self.set_guacamole(guacamole)
        self.cheese =self.set_cheese(cheese)
        self.pico=self.set_pico(pico)
        self.corn=self.set_corn(corn)

        self.baseCost=5.0


    def set_meat(self,meat):
        if meat in["chicken", "pork", "steak", "tofu"]:
            return meat
        else:
            meat=False
            return meat

    def set_to_go(self,to_go):
        if to_go in [True, False]:
            return to_go
        else:
            return None

    def set_rice(self,rice):
        if rice in ["brown", "white"]:
            return rice
        else:
            return False

    def set_beans(self,beans):
        if beans in ["black", "pinto"]:
            return beans
        else:
            return False
    def set_extra_meat(self,extra_meat):
        if extra_meat in [True, False]:
            return extra_meat
        else:
            return None
    def set_guacamole(self,guacamole):
        if guacamole in [True, False]:
            return guacamole
        else:
            return None
    def set_cheese(self,cheese):
        if cheese in [True, False]:
            return cheese
        else:
            return None
    def set_pico(self,pico):
        if pico in [True, False]:
            return pico
        else:
            return None

    def set_corn(self,corn):
        if corn in [True, False]:
            return corn
        else:
            return None
    def get_cost(self):
        if self.meat in ["chicken", "pork" or "tofu"]:
            self.baseCost+=1
        elif self.meat in 'steak':
            self.baseCost+=1.5
        if self.extra_meat:
            self.baseCost+=1
        if self.guacamole:
            self.baseCost+=0.75
        return float(self.baseCost)


