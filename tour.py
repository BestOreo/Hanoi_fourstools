"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time
from toah_model import TOAHModel

global step
step = 0
K=[]


def Hanoi_Three(model, n, a,b,c,delay_between_moves,animate):
    """
    Recursive algorithm for Hanoi problems with 3 stools
    :param model: ToahModel
    :param n: number of cheese
    :param a: stool 0
    :param b: stool 1
    :param c: stool 2
    :param delay_between_moves: 
    :param animate: whether visiable
    :return: None
    """
    if(n<0):
        return
    global step
    step += 1

    if( n == 1 ):
        model.move(a,c)
        if (animate == True):
            print(model)
            time.sleep(delay_between_moves)

        return

    else:
        Hanoi_Three(model,n-1,a,c,b,delay_between_moves,animate)
        model.move(a,c)
        if(animate == True):
            print(model)
            time.sleep(delay_between_moves)

        Hanoi_Three(model,n-1,b,a,c,delay_between_moves,animate)

def Hanoi_Four(model,n,a,b,c,d,delay_between_moves,animate):
    """
    Recursive algorithm for Hanoi problems with 4 stools
    :param model: ToahModel
    :param n: number of cheese
    :param a: stool 0
    :param b: stool 1
    :param c: stool 2
    :param d: stool 3
    :param delay_between_moves: delay time
    :param animate: whether visiable
    :return: None
    """
    if(n<0):
        return

    if(n==1):
        global step
        step += 1
        model.move(a,d)
        if (animate == True):
            print(model)
            time.sleep(delay_between_moves)
        return
    else:
        kn = K[n]
        Hanoi_Four(model,n-kn,a, c, d, b, delay_between_moves, animate)
        Hanoi_Three(model,kn,a,c,d, delay_between_moves, animate)
        Hanoi_Four(model,n-kn,b, a, c, d, delay_between_moves, animate)


def Init_K(model):
    """
    find the best k According to Frame–Stewart Algorithm
    :param model: ToahModel
    :return: None
    """
    max = model.number_of_cheeses
    m = [0 for i in range(max+1)]
    for i in range(1,max+1):
        m[i] = 1000000
        for k in range(1,i+1):
            temp = 2*m[i-k] + 2**k - 1
            if(temp < m[i]):
                m[i] = temp
                K[i] = k



def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    #pass
    for i in range(model.number_of_cheeses+1):
        K.append(0)
    Init_K(model)
    Hanoi_Four(model, model.number_of_cheeses, 0,1,2,3,delay_between_moves,animate)


if __name__ == '__main__':
    num_cheeses = 4
    delay_between_moves = 0.5
    console_animate = True

    print("Cheese Number: " + str(num_cheeses))

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
