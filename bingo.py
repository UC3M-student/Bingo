import random as rd
import numpy as np


bingo_numbers = list(np.arange(1,91,1))
people = np.arange(1,5001,1)
numbers_carton1 = rd.sample(bingo_numbers,15)

def carton_bingo():
    lista_carton = [2,2,2,2,2,2,1,1,1]
    rd.shuffle(lista_carton)
    lst_0 = np.arange(1,10,1)
    lst_1 = np.arange(10,20,1)
    lst_2 = np.arange(20,30,1)
    lst_3 = np.arange(30,40,1)
    lst_4 = np.arange(40,50,1)
    lst_5 = np.arange(50,60,1)
    lst_6 = np.arange(60,70,1)
    lst_7 = np.arange(70,80,1)
    lst_8 = np.arange(80,91,1)
    list_ = [lst_0,lst_1,lst_2,lst_3,lst_4,lst_5,lst_6,lst_7,lst_8]

    a = 0
    carton = []
    for i in lista_carton:
        list__ = list_[a].tolist()
        if i == 1:
            numbers = rd.sample(list__,1)
        else:
            numbers = rd.sample(list__,2)
        a = a + 1
        carton.append(numbers)
    return carton
