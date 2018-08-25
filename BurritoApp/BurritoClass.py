#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat=False,guacamole=False,cheese=False,
                    pico=False,corn=False):
        #First, edit the constructor of your Burrito class.
        #Instead of calling setters to set the values of the
        #attributes self.meat, self.rice, and self.beans, it
        #should instead create new instances of Meat, Rice, and
        #Beans. The arguments to these new instances should be
        #the same as the arguments you were sending to the
        #setters previously (e.g. self.rice = Rice("brown")
        #instead of set_rice("brown")).
        self.meat=Meat(meat)
        self.to_go=Rice(to_go)
        self.rice=Beans(rice)

        self.extra_meat=self.set_extra_meat(extra_meat)
        self.guacamole=self.set_guacamole(guacamole)
        self.cheese =self.set_cheese(cheese)
        self.pico=self.set_pico(pico)
        self.corn=self.set_corn(corn)

        self.baseCost=5.0


    def set_to_go(self,to_go):
        if to_go in [True, False]:
            return to_go
        else:
            return None

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
        if self.meat.get_value() in ["chicken", "pork" or "tofu"]:
            self.baseCost+=1
        elif self.meat.get_value() in 'steak':
            self.baseCost+=1.5
        if self.extra_meat:
            self.baseCost+=1
        if self.guacamole:
            self.baseCost+=0.75
        return float(self.baseCost)

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
