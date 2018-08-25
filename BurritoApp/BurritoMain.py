#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""


#
#Second, modify your getters and setters from your
#original code so that they still return the same value
#as before. get_rice(), for example, should still
#return "brown" for brown rice, False for no rice, etc.
#instead of returning the instance of Rice.
#
#Third, make sure that your get_cost function still
#works when you're done changing your code.
#
#Hint: When you're done, creating a new instance of
#Burrito with Burrito("pork", True, "brown", "pinto")
#should still work to create a new Burrito. The only
#thing changing is the internal reasoning of the
#Burrito class.
#
#Hint 2: Notice that the classes Meat, Beans, and Rice
#already contain the code to validate whether input is
#valid. So, your setters in the Burrito class no
#longer need to worry about that -- they can just pass
#their input to the set_value() methods for those
#classes.
#
#Hint 3: This exercise requires very little actual
#coding: you'll only write nine lines of new code, and
#those nine lines all replace existing lines of code
#in the constructor, getters, and setters of Burrito.
#
#You should not need to modify the code below.

"""
from BurritoClass import *
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
def total_cost(burrito_list):
    total_cost=0.0
    for each_burrito in burrito_list:
        total_cost+=each_burrito.get_cost()
    return total_cost

def main():

    #First test:

    #If your function works correctly, this will originally
    #print: 7.75
    #a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
    #print(a_burrito.get_cost())

    #Second test:

    #Below are some lines of code that will test your function.
    #You can change the value of the variable(s) to test your
    #function with different inputs. Note that these lines
    #will ONLY work if you copy/paste your Burrito, Meat,
    #Beans, and Rice classes in.
    #If your function works correctly, this will originally
    #print: 27.0

    burrito_1 = Burrito("tofu", True, "white", "black")
    burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
    burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
    burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
    burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
    print(total_cost(burrito_list))





if __name__=='__main__':
    main()
