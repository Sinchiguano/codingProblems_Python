#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute.
#Each setter should accept a value as an argument. If the
#value is a valid value, it should set the corresponding
#attribute to the given value. Otherwise, it should set the
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format:
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!

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




#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.
newBurrito = Burrito("steak", True, True, True)
print(newBurrito.meat)
print(newBurrito.to_go)
print(newBurrito.guacamole)
print(newBurrito.extra_meat)
print(newBurrito.cheese)
