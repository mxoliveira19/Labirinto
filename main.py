# 1.LARGURA
# 2.PROFUNDIDADE
# 3. GULOSO 

import numpy as np

from tkinter import *

import time

fase = 0
janela = Tk()

janela.title("LABIRINTO LARGURA")
janela.geometry("432x500")

a = 0
b = 0

def change_button(x,y):
    global fase
    global a
    global b

    if fase == 5:
        fase = 3

    if fase == 1:

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "red"
            map[0][0] = 1

        if x == 0 and y == 1:
            btn_0_1['bg'] = "red"
            map[0][1] = 1

        if x == 0 and y == 2:
            btn_0_2['bg'] = "red"
            map[0][2] = 1

        if x == 0 and y == 3:
            btn_0_3['bg'] = "red"
            map[0][3] = 1

        if x == 0 and y == 4:
            btn_0_4['bg'] = "red"
            map[0][4] = 1

        if x == 0 and y == 5:
            btn_0_5['bg'] = "red"
            map[0][5] = 1

        if x == 0 and y == 6:
            btn_0_6['bg'] = "red"
            map[0][6] = 1

        if x == 0 and y == 7:
            btn_0_7['bg'] = "red"
            map[0][7] = 1

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "red"
            map[1][0] = 1

        if x == 1 and y == 1:
            btn_1_1['bg'] = "red"
            map[1][1] = 1

        if x == 1 and y == 2:
            btn_1_2['bg'] = "red"
            map[1][2] = 1

        if x == 1 and y == 3:
            btn_1_3['bg'] = "red"
            map[1][3] = 1

        if x == 1 and y == 4:
            btn_1_4['bg'] = "red"
            map[1][4] = 1

        if x == 1 and y == 5:
            btn_1_5['bg'] = "red"
            map[1][5] = 1

        if x == 1 and y == 6:
            btn_1_6['bg'] = "red"
            map[1][6] = 1

        if x == 1 and y == 7:
            btn_1_7['bg'] = "red"
            map[1][7] = 1

        if x == 2 and y == 0:
            btn_2_0['bg'] = "red"
            map[2][0] = 1

        if x == 2 and y == 1:
            btn_2_1['bg'] = "red"
            map[2][1] = 1

        if x == 2 and y == 2:
            btn_2_2['bg'] = "red"
            map[2][2] = 1

        if x == 2 and y == 3:
            btn_2_3['bg'] = "red"
            map[2][3] = 1

        if x == 2 and y == 4:
            btn_2_4['bg'] = "red"
            map[2][4] = 1

        if x == 2 and y == 5:
            btn_2_5['bg'] = "red"
            map[2][5] = 1

        if x == 2 and y == 6:
            btn_2_6['bg'] = "red"
            map[2][6] = 1

        if x == 2 and y == 7:
            btn_2_7['bg'] = "red"
            map[2][7] = 1

        if x == 3 and y == 0:
            btn_3_0['bg'] = "red"
            map[3][0] = 1

        if x == 3 and y == 1:
            btn_3_1['bg'] = "red"
            map[3][1] = 1

        if x == 3 and y == 2:
            btn_3_2['bg'] = "red"
            map[3][2] = 1

        if x == 3 and y == 3:
            btn_3_3['bg'] = "red"
            map[3][3] = 1

        if x == 3 and y == 4:
            btn_3_4['bg'] = "red"
            map[3][4] = 1

        if x == 3 and y == 5:
            btn_3_5['bg'] = "red"
            map[3][5] = 1

        if x == 3 and y == 6:
            btn_3_6['bg'] = "red"
            map[3][6] = 1

        if x == 3 and y == 7:
            btn_3_7['bg'] = "red"
            map[3][7] = 1

        if x == 4 and y == 0:
            btn_4_0['bg'] = "red"
            map[4][0] = 1

        if x == 4 and y == 1:
            btn_4_1['bg'] = "red"
            map[4][1] = 1

        if x == 4 and y == 2:
            btn_4_2['bg'] = "red"
            map[4][2] = 1

        if x == 4 and y == 3:
            btn_4_3['bg'] = "red"
            map[4][3] = 1

        if x == 4 and y == 4:
            btn_4_4['bg'] = "red"
            map[4][4] = 1

        if x == 4 and y == 5:
            btn_4_5['bg'] = "red"
            map[4][5] = 1

        if x == 4 and y == 6:
            btn_4_6['bg'] = "red"
            map[4][6] = 1

        if x == 4 and y == 7:
            btn_4_7['bg'] = "red"
            map[4][7] = 1

        if x == 5 and y == 0:
            btn_5_0['bg'] = "red"
            map[5][0] = 1

        if x == 5 and y == 1:
            btn_5_1['bg'] = "red"
            map[5][1] = 1

        if x == 5 and y == 2:
            btn_5_2['bg'] = "red"
            map[5][2] = 1

        if x == 5 and y == 3:
            btn_5_3['bg'] = "red"
            map[5][3] = 1

        if x == 5 and y == 4:
            btn_5_4['bg'] = "red"
            map[5][4] = 1

        if x == 5 and y == 5:
            btn_5_5['bg'] = "red"
            map[5][5] = 1

        if x == 5 and y == 6:
            btn_5_6['bg'] = "red"
            map[5][6] = 1

        if x == 5 and y == 7:
            btn_5_7['bg'] = "red"
            map[5][7] = 1

        if x == 6 and y == 0:
            btn_6_0['bg'] = "red"
            map[6][0] = 1

        if x == 6 and y == 1:
            btn_6_1['bg'] = "red"
            map[6][1] = 1

        if x == 6 and y == 2:
            btn_6_2['bg'] = "red"
            map[6][2] = 1

        if x == 6 and y == 3:
            btn_6_3['bg'] = "red"
            map[6][3] = 1

        if x == 6 and y == 4:
            btn_6_4['bg'] = "red"
            map[6][4] = 1

        if x == 6 and y == 5:
            btn_6_5['bg'] = "red"
            map[6][5] = 1

        if x == 6 and y == 6:
            btn_6_6['bg'] = "red"
            map[6][6] = 1

        if x == 6 and y == 7:
            btn_6_7['bg'] = "red"
            map[6][7] = 1

        if x == 7 and y == 0:
            btn_7_0['bg'] = "red"
            map[7][0] = 1

        if x == 7 and y == 1:
            btn_7_1['bg'] = "red"
            map[7][1] = 1

        if x == 7 and y == 2:
            btn_7_2['bg'] = "red"
            map[7][2] = 1

        if x == 7 and y == 3:
            btn_7_3['bg'] = "red"
            map[7][3] = 1

        if x == 7 and y == 4:
            btn_7_4['bg'] = "red"
            map[7][4] = 1

        if x == 7 and y == 5:
            btn_7_5['bg'] = "red"
            map[7][5] = 1

        if x == 7 and y == 6:
            btn_7_6['bg'] = "red"
            map[7][6] = 1

        if x == 7 and y == 7:
            btn_7_7['bg'] = "red"
            map[7][7] = 1



    if fase == 2:

        # início
        a = x
        b = y

        fase = 5


        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"


    if fase == 3:
        # fim
        global env
        global ag
        env = Environment(map, [a, b], [x, y])
        ag = Agent(env)

        fase = 4

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"



def b00():
    btn_0_0['bg'] = "yellow"


def b01():
    btn_0_1['bg'] = "yellow"


def b02():
    btn_0_2['bg'] = "yellow"


def b03():
    btn_0_3['bg'] = "yellow"


def b04():
    btn_0_4['bg'] = "yellow"


def b05():
    btn_0_5['bg'] = "yellow"


def b06():
    btn_0_6['bg'] = "yellow"


def b07():
    btn_0_7['bg'] = "yellow"


def b10():
    btn_1_0['bg'] = "yellow"


def b11():
    btn_1_1['bg'] = "yellow"


def b12():
    btn_1_2['bg'] = "yellow"


def b13():
    btn_1_3['bg'] = "yellow"


def b14():
    btn_1_4['bg'] = "yellow"


def b15():
    btn_1_5['bg'] = "yellow"


def b16():
    btn_1_6['bg'] = "yellow"


def b17():
    btn_1_7['bg'] = "yellow"


def b20():
    btn_2_0['bg'] = "yellow"


def b21():
    btn_2_1['bg'] = "yellow"


def b22():
    btn_2_2['bg'] = "yellow"


def b23():
    btn_2_3['bg'] = "yellow"


def b24():
    btn_2_4['bg'] = "yellow"


def b25():
    btn_2_5['bg'] = "yellow"


def b26():
    btn_2_6['bg'] = "yellow"


def b27():
    btn_2_7['bg'] = "yellow"


def b30():
    btn_3_0['bg'] = "yellow"


def b31():
    btn_3_1['bg'] = "yellow"


def b32():
    btn_3_2['bg'] = "yellow"


def b33():
    btn_3_3['bg'] = "yellow"


def b34():
    btn_3_4['bg'] = "yellow"


def b35():
    btn_3_5['bg'] = "yellow"


def b36():
    btn_3_6['bg'] = "yellow"


def b37():
    btn_3_7['bg'] = "yellow"


def b40():
    btn_4_0['bg'] = "yellow"


def b41():
    btn_4_1['bg'] = "yellow"


def b42():
    btn_4_2['bg'] = "yellow"


def b43():
    btn_4_3['bg'] = "yellow"


def b44():
    btn_4_4['bg'] = "yellow"


def b45():
    btn_4_5['bg'] = "yellow"


def b46():
    btn_4_6['bg'] = "yellow"


def b47():
    btn_4_7['bg'] = "yellow"


def b50():
    btn_5_0['bg'] = "yellow"


def b51():
    btn_5_1['bg'] = "yellow"


def b52():
    btn_5_2['bg'] = "yellow"


def b53():
    btn_5_3['bg'] = "yellow"


def b54():
    btn_5_4['bg'] = "yellow"


def b55():
    btn_5_5['bg'] = "yellow"


def b56():
    btn_5_6['bg'] = "yellow"


def b57():
    btn_5_7['bg'] = "yellow"


def b60():
    btn_6_0['bg'] = "yellow"


def b61():
    btn_6_1['bg'] = "yellow"


def b62():
    btn_6_2['bg'] = "yellow"


def b63():
    btn_6_3['bg'] = "yellow"


def b64():
    btn_6_4['bg'] = "yellow"


def b65():
    btn_6_5['bg'] = "yellow"


def b66():
    btn_6_6['bg'] = "yellow"


def b67():
    btn_6_7['bg'] = "yellow"


def b70():
    btn_7_0['bg'] = "yellow"


def b71():
    btn_7_1['bg'] = "yellow"


def b72():
    btn_7_2['bg'] = "yellow"


def b73():
    btn_7_3['bg'] = "yellow"


def b74():
    btn_7_4['bg'] = "yellow"


def b75():
    btn_7_5['bg'] = "yellow"


def b76():
    btn_7_6['bg'] = "yellow"


def b77():
    btn_7_7['bg'] = "yellow"




def Reset():
    global fase
    fase = 0

    global map

    map = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

    btn_0_0['bg'] = "green"
    btn_0_1['bg'] = "green"
    btn_0_2['bg'] = "green"
    btn_0_3['bg'] = "green"
    btn_0_4['bg'] = "green"
    btn_0_5['bg'] = "green"
    btn_0_6['bg'] = "green"
    btn_0_7['bg'] = "green"
    btn_1_0['bg'] = "green"
    btn_1_1['bg'] = "green"
    btn_1_2['bg'] = "green"
    btn_1_3['bg'] = "green"
    btn_1_4['bg'] = "green"
    btn_1_5['bg'] = "green"
    btn_1_6['bg'] = "green"
    btn_1_7['bg'] = "green"
    btn_2_0['bg'] = "green"
    btn_2_1['bg'] = "green"
    btn_2_2['bg'] = "green"
    btn_2_3['bg'] = "green"
    btn_2_4['bg'] = "green"
    btn_2_5['bg'] = "green"
    btn_2_6['bg'] = "green"
    btn_2_7['bg'] = "green"
    btn_3_0['bg'] = "green"
    btn_3_1['bg'] = "green"
    btn_3_2['bg'] = "green"
    btn_3_3['bg'] = "green"
    btn_3_4['bg'] = "green"
    btn_3_5['bg'] = "green"
    btn_3_6['bg'] = "green"
    btn_3_7['bg'] = "green"
    btn_4_0['bg'] = "green"
    btn_4_1['bg'] = "green"
    btn_4_2['bg'] = "green"
    btn_4_3['bg'] = "green"
    btn_4_4['bg'] = "green"
    btn_4_5['bg'] = "green"
    btn_4_6['bg'] = "green"
    btn_4_7['bg'] = "green"
    btn_5_0['bg'] = "green"
    btn_5_1['bg'] = "green"
    btn_5_2['bg'] = "green"
    btn_5_3['bg'] = "green"
    btn_5_4['bg'] = "green"
    btn_5_5['bg'] = "green"
    btn_5_6['bg'] = "green"
    btn_5_7['bg'] = "green"
    btn_6_0['bg'] = "green"
    btn_6_1['bg'] = "green"
    btn_6_2['bg'] = "green"
    btn_6_3['bg'] = "green"
    btn_6_4['bg'] = "green"
    btn_6_5['bg'] = "green"
    btn_6_6['bg'] = "green"
    btn_6_7['bg'] = "green"
    btn_7_0['bg'] = "green"
    btn_7_1['bg'] = "green"
    btn_7_2['bg'] = "green"
    btn_7_3['bg'] = "green"
    btn_7_4['bg'] = "green"
    btn_7_5['bg'] = "green"
    btn_7_6['bg'] = "green"
    btn_7_7['bg'] = "green"

def Obstaculos():
    global fase
    fase = 1


def Inifim():
    global fase
    fase = 2


def Run():
            # if __name__ == '__main__':

    path = ag.act()


    x = 400
    y = 400
    for count in path:


        if (count == [0, 0]).all():
            janela.after(x,b00)
            x += y

        elif (count == [0, 1]).all():
            janela.after(x,b01)
            x += y

        elif (count == [0, 2]).all():
            janela.after(x,b02)
            x += y

        elif (count == [0, 3]).all():
            janela.after(x,b03)
            x += y

        elif (count == [0, 4]).all():
            janela.after(x,b04)
            x += y


        elif (count == [0, 5]).all():
            janela.after(x,b05)
            x += y

        elif (count == [0, 6]).all():
            janela.after(x,b06)
            x += y

        elif (count == [0, 7]).all():
            janela.after(x,b07)
            x += y



        if (count == [1, 0]).all():
            janela.after(x,b10)
            x += y

        elif (count == [1, 1]).all():
            janela.after(x,b11)
            x += y

        elif (count == [1, 2]).all():
            janela.after(x,b12)
            x += y

        elif (count == [1, 3]).all():
            janela.after(x,b13)
            x += y

        elif (count == [1, 4]).all():
            janela.after(x,b14)
            x += y


        elif (count == [1, 5]).all():
            janela.after(x,b15)
            x += y

        elif (count == [1, 6]).all():
            janela.after(x,b16)
            x += y

        elif (count == [1, 7]).all():
            janela.after(x,b17)
            x += y



        elif (count == [2, 0]).all():
            janela.after(x,b20)
            x += y

        elif (count == [2, 1]).all():
            janela.after(x,b21)
            x += y

        elif (count == [2, 2]).all():
            janela.after(x,b22)
            x += y

        elif (count == [2, 3]).all():
            janela.after(x,b23)
            x += y

        elif (count == [2, 4]).all():
            janela.after(x,b24)
            x += y


        elif (count == [2, 5]).all():
            janela.after(x,b25)
            x += y

        elif (count == [2, 6]).all():
            janela.after(x,b26)
            x += y

        elif (count == [2, 7]).all():
            janela.after(x,b27)
            x += y



        elif (count == [3, 0]).all():
            janela.after(x,b30)
            x += y

        elif (count == [3, 1]).all():
            janela.after(x,b31)
            x += y

        elif (count == [3, 2]).all():
            janela.after(x,b32)
            x += y

        elif (count == [3, 3]).all():
            janela.after(x,b33)
            x += y

        elif (count == [3, 4]).all():
            janela.after(x,b34)
            x += y


        elif (count == [3, 5]).all():
            janela.after(x,b35)
            x += y

        elif (count == [3, 6]).all():
            janela.after(x,b36)
            x += y

        elif (count == [3, 7]).all():
            janela.after(x,b37)
            x += y



        elif (count == [4, 0]).all():
            janela.after(x,b40)
            x += y

        elif (count == [4, 1]).all():
            janela.after(x,b41)
            x += y

        elif (count == [4, 2]).all():
            janela.after(x,b42)
            x += y

        elif (count == [4, 3]).all():
            janela.after(x,b43)
            x += y

        elif (count == [4, 4]).all():
            janela.after(x,b44)
            x += y


        elif (count == [4, 5]).all():
            janela.after(x,b45)
            x += y

        elif (count == [4, 6]).all():
            janela.after(x,b46)
            x += y

        elif (count == [4, 7]).all():
            janela.after(x,b47)
            x += y



        elif (count == [5, 0]).all():
            janela.after(x,b50)
            x += y

        elif (count == [5, 1]).all():
            janela.after(x,b51)
            x += y

        elif (count == [5, 2]).all():
            janela.after(x,b52)
            x += y

        elif (count == [5, 3]).all():
            janela.after(x,b53)
            x += y

        elif (count == [5, 4]).all():
            janela.after(x,b54)
            x += y


        elif (count == [5, 5]).all():
            janela.after(x,b55)
            x += y

        elif (count == [5, 6]).all():
            janela.after(x,b56)
            x += y

        elif (count == [5, 7]).all():
            janela.after(x,b57)
            x += y



        elif (count == [6, 0]).all():
            janela.after(x,b60)
            x += y

        elif (count == [6, 1]).all():
            janela.after(x,b61)
            x += y

        elif (count == [6, 2]).all():
            janela.after(x,b62)
            x += y

        elif (count == [6, 3]).all():
            janela.after(x,b63)
            x += y

        elif (count == [6, 4]).all():
            janela.after(x,b64)
            x += y


        elif (count == [6, 5]).all():
            janela.after(x,b65)
            x += y

        elif (count == [6, 6]).all():
            janela.after(x,b66)
            x += y

        elif (count == [6, 7]).all():
            janela.after(x,b67)
            x += y



        elif (count == [7, 0]).all():
            janela.after(x,b70)
            x += y

        elif (count == [7, 1]).all():
            janela.after(x,b71)
            x += y

        elif (count == [7, 2]).all():
            janela.after(x,b72)
            x += y

        elif (count == [7, 3]).all():
            janela.after(x,b73)
            x += y

        elif (count == [7, 4]).all():
            janela.after(x,b74)
            x += y


        elif (count == [7, 5]).all():
            janela.after(x,b75)
            x += y

        elif (count == [7, 6]).all():
            janela.after(x,b76)
            x += y

        elif (count == [7, 7]).all():
            janela.after(x,b77)
            x += y







btn_0_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,0))
btn_0_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,1) )
btn_0_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,2) )
btn_0_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,3) )
btn_0_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,4) )
btn_0_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,5) )
btn_0_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,6) )
btn_0_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,7) )
btn_1_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,0) )
btn_1_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,1) )
btn_1_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,2) )
btn_1_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,3) )
btn_1_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,4) )
btn_1_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,5) )
btn_1_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,6) )
btn_1_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,7) )
btn_2_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,0) )
btn_2_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,1) )
btn_2_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,2) )
btn_2_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,3) )
btn_2_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,4) )
btn_2_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,5) )
btn_2_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,6) )
btn_2_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,7) )
btn_3_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,0) )
btn_3_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,1) )
btn_3_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,2) )
btn_3_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,3) )
btn_3_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,4) )
btn_3_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,5) )
btn_3_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,6) )
btn_3_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,7) )
btn_4_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,0) )
btn_4_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,1) )
btn_4_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,2) )
btn_4_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,3) )
btn_4_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,4) )
btn_4_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,5) )
btn_4_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,6) )
btn_4_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,7) )
btn_5_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,0) )
btn_5_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,1) )
btn_5_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,2) )
btn_5_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,3) )
btn_5_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,4) )
btn_5_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,5) )
btn_5_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,6) )
btn_5_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,7) )
btn_6_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,0) )
btn_6_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,1) )
btn_6_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,2) )
btn_6_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,3) )
btn_6_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,4) )
btn_6_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,5) )
btn_6_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,6) )
btn_6_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,7) )
btn_7_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,0) )
btn_7_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,1) )
btn_7_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,2) )
btn_7_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,3) )
btn_7_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,4) )
btn_7_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,5) )
btn_7_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,6) )
btn_7_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,7) )


btn_reset       = Button(janela,text="reset",   command=Reset )
btn_obstaculos  = Button(janela,text="obstác",  command=Obstaculos)
btn_ini_fim     = Button(janela,text="ini_fim", command=Inifim)
btn_run         = Button(janela,text="run",     command=Run   )



btn_0_0.grid(row=0,column=0,ipadx=2, ipady=2)
btn_0_1.grid(row=0,column=1,ipadx=2, ipady=2)
btn_0_2.grid(row=0,column=2,ipadx=2, ipady=2)
btn_0_3.grid(row=0,column=3,ipadx=2, ipady=2)
btn_0_4.grid(row=0,column=4,ipadx=2, ipady=2)
btn_0_5.grid(row=0,column=5,ipadx=2, ipady=2)
btn_0_6.grid(row=0,column=6,ipadx=2, ipady=2)
btn_0_7.grid(row=0,column=7,ipadx=2, ipady=2)
btn_1_0.grid(row=1,column=0,ipadx=2, ipady=2)
btn_1_1.grid(row=1,column=1,ipadx=2, ipady=2)
btn_1_2.grid(row=1,column=2,ipadx=2, ipady=2)
btn_1_3.grid(row=1,column=3,ipadx=2, ipady=2)
btn_1_4.grid(row=1,column=4,ipadx=2, ipady=2)
btn_1_5.grid(row=1,column=5,ipadx=2, ipady=2)
btn_1_6.grid(row=1,column=6,ipadx=2, ipady=2)
btn_1_7.grid(row=1,column=7,ipadx=2, ipady=2)
btn_2_0.grid(row=2,column=0,ipadx=2, ipady=2)
btn_2_1.grid(row=2,column=1,ipadx=2, ipady=2)
btn_2_2.grid(row=2,column=2,ipadx=2, ipady=2)
btn_2_3.grid(row=2,column=3,ipadx=2, ipady=2)
btn_2_4.grid(row=2,column=4,ipadx=2, ipady=2)
btn_2_5.grid(row=2,column=5,ipadx=2, ipady=2)
btn_2_6.grid(row=2,column=6,ipadx=2, ipady=2)
btn_2_7.grid(row=2,column=7,ipadx=2, ipady=2)
btn_3_0.grid(row=3,column=0,ipadx=2, ipady=2)
btn_3_1.grid(row=3,column=1,ipadx=2, ipady=2)
btn_3_2.grid(row=3,column=2,ipadx=2, ipady=2)
btn_3_3.grid(row=3,column=3,ipadx=2, ipady=2)
btn_3_4.grid(row=3,column=4,ipadx=2, ipady=2)
btn_3_5.grid(row=3,column=5,ipadx=2, ipady=2)
btn_3_6.grid(row=3,column=6,ipadx=2, ipady=2)
btn_3_7.grid(row=3,column=7,ipadx=2, ipady=2)
btn_4_0.grid(row=4,column=0,ipadx=2, ipady=2)
btn_4_1.grid(row=4,column=1,ipadx=2, ipady=2)
btn_4_2.grid(row=4,column=2,ipadx=2, ipady=2)
btn_4_3.grid(row=4,column=3,ipadx=2, ipady=2)
btn_4_4.grid(row=4,column=4,ipadx=2, ipady=2)
btn_4_5.grid(row=4,column=5,ipadx=2, ipady=2)
btn_4_6.grid(row=4,column=6,ipadx=2, ipady=2)
btn_4_7.grid(row=4,column=7,ipadx=2, ipady=2)
btn_5_0.grid(row=5,column=0,ipadx=2, ipady=2)
btn_5_1.grid(row=5,column=1,ipadx=2, ipady=2)
btn_5_2.grid(row=5,column=2,ipadx=2, ipady=2)
btn_5_3.grid(row=5,column=3,ipadx=2, ipady=2)
btn_5_4.grid(row=5,column=4,ipadx=2, ipady=2)
btn_5_5.grid(row=5,column=5,ipadx=2, ipady=2)
btn_5_6.grid(row=5,column=6,ipadx=2, ipady=2)
btn_5_7.grid(row=5,column=7,ipadx=2, ipady=2)
btn_6_0.grid(row=6,column=0,ipadx=2, ipady=2)
btn_6_1.grid(row=6,column=1,ipadx=2, ipady=2)
btn_6_2.grid(row=6,column=2,ipadx=2, ipady=2)
btn_6_3.grid(row=6,column=3,ipadx=2, ipady=2)
btn_6_4.grid(row=6,column=4,ipadx=2, ipady=2)
btn_6_5.grid(row=6,column=5,ipadx=2, ipady=2)
btn_6_6.grid(row=6,column=6,ipadx=2, ipady=2)
btn_6_7.grid(row=6,column=7,ipadx=2, ipady=2)
btn_7_0.grid(row=7,column=0,ipadx=2, ipady=2)
btn_7_1.grid(row=7,column=1,ipadx=2, ipady=2)
btn_7_2.grid(row=7,column=2,ipadx=2, ipady=2)
btn_7_3.grid(row=7,column=3,ipadx=2, ipady=2)
btn_7_4.grid(row=7,column=4,ipadx=2, ipady=2)
btn_7_5.grid(row=7,column=5,ipadx=2, ipady=2)
btn_7_6.grid(row=7,column=6,ipadx=2, ipady=2)
btn_7_7.grid(row=7,column=7,ipadx=2, ipady=2)



btn_reset.grid   (row=9,column=1)
btn_obstaculos.grid  (row=9,column=3)
btn_ini_fim.grid (row=9,column=5)
btn_run.grid     (row=9,column=7)

def colorir_inicial():
    if map[0][0] == 0:
        btn_0_0['bg'] = "green"
    else:
        btn_0_0['bg'] = "red"

    if map[0][1] == 0:
        btn_0_1['bg'] = "green"
    else:
        btn_0_1['bg'] = "red"

    if map[0][2] == 0:
        btn_0_2['bg'] = "green"
    else:
        btn_0_2['bg'] = "red"

    if map[1][0] == 0:
        btn_1_0['bg'] = "green"
    else:
        btn_1_0['bg'] = "red"

    if map[1][1] == 0:
        btn_1_1['bg'] = "green"
    else:
        btn_1_1['bg'] = "red"

    if map[1][2] == 0:
        btn_1_2['bg'] = "green"
    else:
        btn_1_2['bg'] = "red"

    if map[2][0] == 0:
        btn_2_0['bg'] = "green"
    else:
        btn_2_0['bg'] = "red"

    if map[2][1] == 0:
        btn_2_1['bg'] = "green"
    else:
        btn_2_1['bg'] = "red"

    if map[2][2] == 0:
        btn_2_2['bg'] = "green"
    else:
        btn_2_2['bg'] = "red"

class Environment:

    def __init__(self, map, start, goal):
        self.map = np.array(map)              # mapa
        self.start = np.array(start)          # posição inicial
        self.goal = np.array(goal)            # objetivo
        self.agent_position = np.array(start) # posição do agente; começa na start
        self.actions = np.array([[1,0], [-1,0], [0,1], [0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]) # passo que se pode dar



    def initial_percepts(self):

        available = []                             # disponíveis

        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.start + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis


        return{'available_positions': available,       # retorna quais as posições disponíveis
                'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
                 'goal': self.goal}



    def signal(self, action):
        self.agent_position = action['go_to'] # posição do agente

        available = []                             # disponíveis
        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.agent_position + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis

        return{'available_positions': available,       # retorna quais as posições disponíveis
               'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
               'goal': self.goal}


class Agent:

    def __init__(self, env):

        self.belief_state = env.initial_percepts()
        self.env = env

    def act(self):

        F = [[self.belief_state['position']]]
        i = 0

        while F:
            path = F.pop(0)
            i += 1
            print(i)

            self.belief_state = self.env.signal({'go_to': path[-1]})

            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:
                    F.append(path + [p])

        return []


'''class Agent:

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.env = env
        self.cor = np.array([])





    def act(self):
        F = [[self.belief_state['position']] ]  # posição inicial do agente


        i = 0
        while F:
            i += 1


            path  = F.pop(0)        # posição do agente - F[0]



            self.belief_state = self.env.signal({'go_to':path[-1]}) # sentido da direita pra esquerda



            a = 0
            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:
                    F.append(path + [p])  # busca em largura
                    a += 1
                    print(a)


        #return []
'''







Reset() # colorir todos de verde e mapa tudo 0




janela.mainloop()



# -----------------------------------------------------------------------------
# profundidade

import numpy as np

from tkinter import *

import time

fase = 0
janela = Tk()

janela.title("LABIRINTO PROFUNDIDADE")
janela.geometry("432x500")

a = 0
b = 0

def change_button(x,y):
    global fase
    global a
    global b

    if fase == 5:
        fase = 3

    if fase == 1:

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "red"
            map[0][0] = 1

        if x == 0 and y == 1:
            btn_0_1['bg'] = "red"
            map[0][1] = 1

        if x == 0 and y == 2:
            btn_0_2['bg'] = "red"
            map[0][2] = 1

        if x == 0 and y == 3:
            btn_0_3['bg'] = "red"
            map[0][3] = 1

        if x == 0 and y == 4:
            btn_0_4['bg'] = "red"
            map[0][4] = 1

        if x == 0 and y == 5:
            btn_0_5['bg'] = "red"
            map[0][5] = 1

        if x == 0 and y == 6:
            btn_0_6['bg'] = "red"
            map[0][6] = 1

        if x == 0 and y == 7:
            btn_0_7['bg'] = "red"
            map[0][7] = 1

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "red"
            map[1][0] = 1

        if x == 1 and y == 1:
            btn_1_1['bg'] = "red"
            map[1][1] = 1

        if x == 1 and y == 2:
            btn_1_2['bg'] = "red"
            map[1][2] = 1

        if x == 1 and y == 3:
            btn_1_3['bg'] = "red"
            map[1][3] = 1

        if x == 1 and y == 4:
            btn_1_4['bg'] = "red"
            map[1][4] = 1

        if x == 1 and y == 5:
            btn_1_5['bg'] = "red"
            map[1][5] = 1

        if x == 1 and y == 6:
            btn_1_6['bg'] = "red"
            map[1][6] = 1

        if x == 1 and y == 7:
            btn_1_7['bg'] = "red"
            map[1][7] = 1

        if x == 2 and y == 0:
            btn_2_0['bg'] = "red"
            map[2][0] = 1

        if x == 2 and y == 1:
            btn_2_1['bg'] = "red"
            map[2][1] = 1

        if x == 2 and y == 2:
            btn_2_2['bg'] = "red"
            map[2][2] = 1

        if x == 2 and y == 3:
            btn_2_3['bg'] = "red"
            map[2][3] = 1

        if x == 2 and y == 4:
            btn_2_4['bg'] = "red"
            map[2][4] = 1

        if x == 2 and y == 5:
            btn_2_5['bg'] = "red"
            map[2][5] = 1

        if x == 2 and y == 6:
            btn_2_6['bg'] = "red"
            map[2][6] = 1

        if x == 2 and y == 7:
            btn_2_7['bg'] = "red"
            map[2][7] = 1

        if x == 3 and y == 0:
            btn_3_0['bg'] = "red"
            map[3][0] = 1

        if x == 3 and y == 1:
            btn_3_1['bg'] = "red"
            map[3][1] = 1

        if x == 3 and y == 2:
            btn_3_2['bg'] = "red"
            map[3][2] = 1

        if x == 3 and y == 3:
            btn_3_3['bg'] = "red"
            map[3][3] = 1

        if x == 3 and y == 4:
            btn_3_4['bg'] = "red"
            map[3][4] = 1

        if x == 3 and y == 5:
            btn_3_5['bg'] = "red"
            map[3][5] = 1

        if x == 3 and y == 6:
            btn_3_6['bg'] = "red"
            map[3][6] = 1

        if x == 3 and y == 7:
            btn_3_7['bg'] = "red"
            map[3][7] = 1

        if x == 4 and y == 0:
            btn_4_0['bg'] = "red"
            map[4][0] = 1

        if x == 4 and y == 1:
            btn_4_1['bg'] = "red"
            map[4][1] = 1

        if x == 4 and y == 2:
            btn_4_2['bg'] = "red"
            map[4][2] = 1

        if x == 4 and y == 3:
            btn_4_3['bg'] = "red"
            map[4][3] = 1

        if x == 4 and y == 4:
            btn_4_4['bg'] = "red"
            map[4][4] = 1

        if x == 4 and y == 5:
            btn_4_5['bg'] = "red"
            map[4][5] = 1

        if x == 4 and y == 6:
            btn_4_6['bg'] = "red"
            map[4][6] = 1

        if x == 4 and y == 7:
            btn_4_7['bg'] = "red"
            map[4][7] = 1

        if x == 5 and y == 0:
            btn_5_0['bg'] = "red"
            map[5][0] = 1

        if x == 5 and y == 1:
            btn_5_1['bg'] = "red"
            map[5][1] = 1

        if x == 5 and y == 2:
            btn_5_2['bg'] = "red"
            map[5][2] = 1

        if x == 5 and y == 3:
            btn_5_3['bg'] = "red"
            map[5][3] = 1

        if x == 5 and y == 4:
            btn_5_4['bg'] = "red"
            map[5][4] = 1

        if x == 5 and y == 5:
            btn_5_5['bg'] = "red"
            map[5][5] = 1

        if x == 5 and y == 6:
            btn_5_6['bg'] = "red"
            map[5][6] = 1

        if x == 5 and y == 7:
            btn_5_7['bg'] = "red"
            map[5][7] = 1

        if x == 6 and y == 0:
            btn_6_0['bg'] = "red"
            map[6][0] = 1

        if x == 6 and y == 1:
            btn_6_1['bg'] = "red"
            map[6][1] = 1

        if x == 6 and y == 2:
            btn_6_2['bg'] = "red"
            map[6][2] = 1

        if x == 6 and y == 3:
            btn_6_3['bg'] = "red"
            map[6][3] = 1

        if x == 6 and y == 4:
            btn_6_4['bg'] = "red"
            map[6][4] = 1

        if x == 6 and y == 5:
            btn_6_5['bg'] = "red"
            map[6][5] = 1

        if x == 6 and y == 6:
            btn_6_6['bg'] = "red"
            map[6][6] = 1

        if x == 6 and y == 7:
            btn_6_7['bg'] = "red"
            map[6][7] = 1

        if x == 7 and y == 0:
            btn_7_0['bg'] = "red"
            map[7][0] = 1

        if x == 7 and y == 1:
            btn_7_1['bg'] = "red"
            map[7][1] = 1

        if x == 7 and y == 2:
            btn_7_2['bg'] = "red"
            map[7][2] = 1

        if x == 7 and y == 3:
            btn_7_3['bg'] = "red"
            map[7][3] = 1

        if x == 7 and y == 4:
            btn_7_4['bg'] = "red"
            map[7][4] = 1

        if x == 7 and y == 5:
            btn_7_5['bg'] = "red"
            map[7][5] = 1

        if x == 7 and y == 6:
            btn_7_6['bg'] = "red"
            map[7][6] = 1

        if x == 7 and y == 7:
            btn_7_7['bg'] = "red"
            map[7][7] = 1



    if fase == 2:

        # início
        a = x
        b = y

        fase = 5


        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"


    if fase == 3:
        # fim
        global env
        global ag
        env = Environment(map, [a, b], [x, y])
        ag = Agent(env)

        fase = 4

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"



def b00():
    btn_0_0['bg'] = "yellow"


def b01():
    btn_0_1['bg'] = "yellow"


def b02():
    btn_0_2['bg'] = "yellow"


def b03():
    btn_0_3['bg'] = "yellow"


def b04():
    btn_0_4['bg'] = "yellow"


def b05():
    btn_0_5['bg'] = "yellow"


def b06():
    btn_0_6['bg'] = "yellow"


def b07():
    btn_0_7['bg'] = "yellow"


def b10():
    btn_1_0['bg'] = "yellow"


def b11():
    btn_1_1['bg'] = "yellow"


def b12():
    btn_1_2['bg'] = "yellow"


def b13():
    btn_1_3['bg'] = "yellow"


def b14():
    btn_1_4['bg'] = "yellow"


def b15():
    btn_1_5['bg'] = "yellow"


def b16():
    btn_1_6['bg'] = "yellow"


def b17():
    btn_1_7['bg'] = "yellow"


def b20():
    btn_2_0['bg'] = "yellow"


def b21():
    btn_2_1['bg'] = "yellow"


def b22():
    btn_2_2['bg'] = "yellow"


def b23():
    btn_2_3['bg'] = "yellow"


def b24():
    btn_2_4['bg'] = "yellow"


def b25():
    btn_2_5['bg'] = "yellow"


def b26():
    btn_2_6['bg'] = "yellow"


def b27():
    btn_2_7['bg'] = "yellow"


def b30():
    btn_3_0['bg'] = "yellow"


def b31():
    btn_3_1['bg'] = "yellow"


def b32():
    btn_3_2['bg'] = "yellow"


def b33():
    btn_3_3['bg'] = "yellow"


def b34():
    btn_3_4['bg'] = "yellow"


def b35():
    btn_3_5['bg'] = "yellow"


def b36():
    btn_3_6['bg'] = "yellow"


def b37():
    btn_3_7['bg'] = "yellow"


def b40():
    btn_4_0['bg'] = "yellow"


def b41():
    btn_4_1['bg'] = "yellow"


def b42():
    btn_4_2['bg'] = "yellow"


def b43():
    btn_4_3['bg'] = "yellow"


def b44():
    btn_4_4['bg'] = "yellow"


def b45():
    btn_4_5['bg'] = "yellow"


def b46():
    btn_4_6['bg'] = "yellow"


def b47():
    btn_4_7['bg'] = "yellow"


def b50():
    btn_5_0['bg'] = "yellow"


def b51():
    btn_5_1['bg'] = "yellow"


def b52():
    btn_5_2['bg'] = "yellow"


def b53():
    btn_5_3['bg'] = "yellow"


def b54():
    btn_5_4['bg'] = "yellow"


def b55():
    btn_5_5['bg'] = "yellow"


def b56():
    btn_5_6['bg'] = "yellow"


def b57():
    btn_5_7['bg'] = "yellow"


def b60():
    btn_6_0['bg'] = "yellow"


def b61():
    btn_6_1['bg'] = "yellow"


def b62():
    btn_6_2['bg'] = "yellow"


def b63():
    btn_6_3['bg'] = "yellow"


def b64():
    btn_6_4['bg'] = "yellow"


def b65():
    btn_6_5['bg'] = "yellow"


def b66():
    btn_6_6['bg'] = "yellow"


def b67():
    btn_6_7['bg'] = "yellow"


def b70():
    btn_7_0['bg'] = "yellow"


def b71():
    btn_7_1['bg'] = "yellow"


def b72():
    btn_7_2['bg'] = "yellow"


def b73():
    btn_7_3['bg'] = "yellow"


def b74():
    btn_7_4['bg'] = "yellow"


def b75():
    btn_7_5['bg'] = "yellow"


def b76():
    btn_7_6['bg'] = "yellow"


def b77():
    btn_7_7['bg'] = "yellow"




def Reset():
    global fase
    fase = 0

    global map

    map = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

    btn_0_0['bg'] = "green"
    btn_0_1['bg'] = "green"
    btn_0_2['bg'] = "green"
    btn_0_3['bg'] = "green"
    btn_0_4['bg'] = "green"
    btn_0_5['bg'] = "green"
    btn_0_6['bg'] = "green"
    btn_0_7['bg'] = "green"
    btn_1_0['bg'] = "green"
    btn_1_1['bg'] = "green"
    btn_1_2['bg'] = "green"
    btn_1_3['bg'] = "green"
    btn_1_4['bg'] = "green"
    btn_1_5['bg'] = "green"
    btn_1_6['bg'] = "green"
    btn_1_7['bg'] = "green"
    btn_2_0['bg'] = "green"
    btn_2_1['bg'] = "green"
    btn_2_2['bg'] = "green"
    btn_2_3['bg'] = "green"
    btn_2_4['bg'] = "green"
    btn_2_5['bg'] = "green"
    btn_2_6['bg'] = "green"
    btn_2_7['bg'] = "green"
    btn_3_0['bg'] = "green"
    btn_3_1['bg'] = "green"
    btn_3_2['bg'] = "green"
    btn_3_3['bg'] = "green"
    btn_3_4['bg'] = "green"
    btn_3_5['bg'] = "green"
    btn_3_6['bg'] = "green"
    btn_3_7['bg'] = "green"
    btn_4_0['bg'] = "green"
    btn_4_1['bg'] = "green"
    btn_4_2['bg'] = "green"
    btn_4_3['bg'] = "green"
    btn_4_4['bg'] = "green"
    btn_4_5['bg'] = "green"
    btn_4_6['bg'] = "green"
    btn_4_7['bg'] = "green"
    btn_5_0['bg'] = "green"
    btn_5_1['bg'] = "green"
    btn_5_2['bg'] = "green"
    btn_5_3['bg'] = "green"
    btn_5_4['bg'] = "green"
    btn_5_5['bg'] = "green"
    btn_5_6['bg'] = "green"
    btn_5_7['bg'] = "green"
    btn_6_0['bg'] = "green"
    btn_6_1['bg'] = "green"
    btn_6_2['bg'] = "green"
    btn_6_3['bg'] = "green"
    btn_6_4['bg'] = "green"
    btn_6_5['bg'] = "green"
    btn_6_6['bg'] = "green"
    btn_6_7['bg'] = "green"
    btn_7_0['bg'] = "green"
    btn_7_1['bg'] = "green"
    btn_7_2['bg'] = "green"
    btn_7_3['bg'] = "green"
    btn_7_4['bg'] = "green"
    btn_7_5['bg'] = "green"
    btn_7_6['bg'] = "green"
    btn_7_7['bg'] = "green"

def Obstaculos():
    global fase
    fase = 1


def Inifim():
    global fase
    fase = 2


def Run():
            # if __name__ == '__main__':

    path = ag.act()


    x = 400
    y = 400
    for count in path:


        if (count == [0, 0]).all():
            janela.after(x,b00)
            x += y

        elif (count == [0, 1]).all():
            janela.after(x,b01)
            x += y

        elif (count == [0, 2]).all():
            janela.after(x,b02)
            x += y

        elif (count == [0, 3]).all():
            janela.after(x,b03)
            x += y

        elif (count == [0, 4]).all():
            janela.after(x,b04)
            x += y


        elif (count == [0, 5]).all():
            janela.after(x,b05)
            x += y

        elif (count == [0, 6]).all():
            janela.after(x,b06)
            x += y

        elif (count == [0, 7]).all():
            janela.after(x,b07)
            x += y



        if (count == [1, 0]).all():
            janela.after(x,b10)
            x += y

        elif (count == [1, 1]).all():
            janela.after(x,b11)
            x += y

        elif (count == [1, 2]).all():
            janela.after(x,b12)
            x += y

        elif (count == [1, 3]).all():
            janela.after(x,b13)
            x += y

        elif (count == [1, 4]).all():
            janela.after(x,b14)
            x += y


        elif (count == [1, 5]).all():
            janela.after(x,b15)
            x += y

        elif (count == [1, 6]).all():
            janela.after(x,b16)
            x += y

        elif (count == [1, 7]).all():
            janela.after(x,b17)
            x += y



        elif (count == [2, 0]).all():
            janela.after(x,b20)
            x += y

        elif (count == [2, 1]).all():
            janela.after(x,b21)
            x += y

        elif (count == [2, 2]).all():
            janela.after(x,b22)
            x += y

        elif (count == [2, 3]).all():
            janela.after(x,b23)
            x += y

        elif (count == [2, 4]).all():
            janela.after(x,b24)
            x += y


        elif (count == [2, 5]).all():
            janela.after(x,b25)
            x += y

        elif (count == [2, 6]).all():
            janela.after(x,b26)
            x += y

        elif (count == [2, 7]).all():
            janela.after(x,b27)
            x += y



        elif (count == [3, 0]).all():
            janela.after(x,b30)
            x += y

        elif (count == [3, 1]).all():
            janela.after(x,b31)
            x += y

        elif (count == [3, 2]).all():
            janela.after(x,b32)
            x += y

        elif (count == [3, 3]).all():
            janela.after(x,b33)
            x += y

        elif (count == [3, 4]).all():
            janela.after(x,b34)
            x += y


        elif (count == [3, 5]).all():
            janela.after(x,b35)
            x += y

        elif (count == [3, 6]).all():
            janela.after(x,b36)
            x += y

        elif (count == [3, 7]).all():
            janela.after(x,b37)
            x += y



        elif (count == [4, 0]).all():
            janela.after(x,b40)
            x += y

        elif (count == [4, 1]).all():
            janela.after(x,b41)
            x += y

        elif (count == [4, 2]).all():
            janela.after(x,b42)
            x += y

        elif (count == [4, 3]).all():
            janela.after(x,b43)
            x += y

        elif (count == [4, 4]).all():
            janela.after(x,b44)
            x += y


        elif (count == [4, 5]).all():
            janela.after(x,b45)
            x += y

        elif (count == [4, 6]).all():
            janela.after(x,b46)
            x += y

        elif (count == [4, 7]).all():
            janela.after(x,b47)
            x += y



        elif (count == [5, 0]).all():
            janela.after(x,b50)
            x += y

        elif (count == [5, 1]).all():
            janela.after(x,b51)
            x += y

        elif (count == [5, 2]).all():
            janela.after(x,b52)
            x += y

        elif (count == [5, 3]).all():
            janela.after(x,b53)
            x += y

        elif (count == [5, 4]).all():
            janela.after(x,b54)
            x += y


        elif (count == [5, 5]).all():
            janela.after(x,b55)
            x += y

        elif (count == [5, 6]).all():
            janela.after(x,b56)
            x += y

        elif (count == [5, 7]).all():
            janela.after(x,b57)
            x += y



        elif (count == [6, 0]).all():
            janela.after(x,b60)
            x += y

        elif (count == [6, 1]).all():
            janela.after(x,b61)
            x += y

        elif (count == [6, 2]).all():
            janela.after(x,b62)
            x += y

        elif (count == [6, 3]).all():
            janela.after(x,b63)
            x += y

        elif (count == [6, 4]).all():
            janela.after(x,b64)
            x += y


        elif (count == [6, 5]).all():
            janela.after(x,b65)
            x += y

        elif (count == [6, 6]).all():
            janela.after(x,b66)
            x += y

        elif (count == [6, 7]).all():
            janela.after(x,b67)
            x += y



        elif (count == [7, 0]).all():
            janela.after(x,b70)
            x += y

        elif (count == [7, 1]).all():
            janela.after(x,b71)
            x += y

        elif (count == [7, 2]).all():
            janela.after(x,b72)
            x += y

        elif (count == [7, 3]).all():
            janela.after(x,b73)
            x += y

        elif (count == [7, 4]).all():
            janela.after(x,b74)
            x += y


        elif (count == [7, 5]).all():
            janela.after(x,b75)
            x += y

        elif (count == [7, 6]).all():
            janela.after(x,b76)
            x += y

        elif (count == [7, 7]).all():
            janela.after(x,b77)
            x += y







btn_0_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,0))
btn_0_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,1) )
btn_0_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,2) )
btn_0_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,3) )
btn_0_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,4) )
btn_0_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,5) )
btn_0_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,6) )
btn_0_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,7) )
btn_1_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,0) )
btn_1_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,1) )
btn_1_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,2) )
btn_1_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,3) )
btn_1_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,4) )
btn_1_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,5) )
btn_1_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,6) )
btn_1_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,7) )
btn_2_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,0) )
btn_2_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,1) )
btn_2_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,2) )
btn_2_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,3) )
btn_2_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,4) )
btn_2_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,5) )
btn_2_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,6) )
btn_2_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,7) )
btn_3_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,0) )
btn_3_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,1) )
btn_3_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,2) )
btn_3_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,3) )
btn_3_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,4) )
btn_3_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,5) )
btn_3_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,6) )
btn_3_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,7) )
btn_4_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,0) )
btn_4_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,1) )
btn_4_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,2) )
btn_4_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,3) )
btn_4_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,4) )
btn_4_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,5) )
btn_4_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,6) )
btn_4_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,7) )
btn_5_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,0) )
btn_5_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,1) )
btn_5_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,2) )
btn_5_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,3) )
btn_5_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,4) )
btn_5_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,5) )
btn_5_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,6) )
btn_5_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,7) )
btn_6_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,0) )
btn_6_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,1) )
btn_6_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,2) )
btn_6_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,3) )
btn_6_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,4) )
btn_6_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,5) )
btn_6_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,6) )
btn_6_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,7) )
btn_7_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,0) )
btn_7_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,1) )
btn_7_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,2) )
btn_7_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,3) )
btn_7_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,4) )
btn_7_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,5) )
btn_7_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,6) )
btn_7_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,7) )


btn_reset       = Button(janela,text="reset",   command=Reset )
btn_obstaculos  = Button(janela,text="obstác",  command=Obstaculos)
btn_ini_fim     = Button(janela,text="ini_fim", command=Inifim)
btn_run         = Button(janela,text="run",     command=Run   )



btn_0_0.grid(row=0,column=0,ipadx=2, ipady=2)
btn_0_1.grid(row=0,column=1,ipadx=2, ipady=2)
btn_0_2.grid(row=0,column=2,ipadx=2, ipady=2)
btn_0_3.grid(row=0,column=3,ipadx=2, ipady=2)
btn_0_4.grid(row=0,column=4,ipadx=2, ipady=2)
btn_0_5.grid(row=0,column=5,ipadx=2, ipady=2)
btn_0_6.grid(row=0,column=6,ipadx=2, ipady=2)
btn_0_7.grid(row=0,column=7,ipadx=2, ipady=2)
btn_1_0.grid(row=1,column=0,ipadx=2, ipady=2)
btn_1_1.grid(row=1,column=1,ipadx=2, ipady=2)
btn_1_2.grid(row=1,column=2,ipadx=2, ipady=2)
btn_1_3.grid(row=1,column=3,ipadx=2, ipady=2)
btn_1_4.grid(row=1,column=4,ipadx=2, ipady=2)
btn_1_5.grid(row=1,column=5,ipadx=2, ipady=2)
btn_1_6.grid(row=1,column=6,ipadx=2, ipady=2)
btn_1_7.grid(row=1,column=7,ipadx=2, ipady=2)
btn_2_0.grid(row=2,column=0,ipadx=2, ipady=2)
btn_2_1.grid(row=2,column=1,ipadx=2, ipady=2)
btn_2_2.grid(row=2,column=2,ipadx=2, ipady=2)
btn_2_3.grid(row=2,column=3,ipadx=2, ipady=2)
btn_2_4.grid(row=2,column=4,ipadx=2, ipady=2)
btn_2_5.grid(row=2,column=5,ipadx=2, ipady=2)
btn_2_6.grid(row=2,column=6,ipadx=2, ipady=2)
btn_2_7.grid(row=2,column=7,ipadx=2, ipady=2)
btn_3_0.grid(row=3,column=0,ipadx=2, ipady=2)
btn_3_1.grid(row=3,column=1,ipadx=2, ipady=2)
btn_3_2.grid(row=3,column=2,ipadx=2, ipady=2)
btn_3_3.grid(row=3,column=3,ipadx=2, ipady=2)
btn_3_4.grid(row=3,column=4,ipadx=2, ipady=2)
btn_3_5.grid(row=3,column=5,ipadx=2, ipady=2)
btn_3_6.grid(row=3,column=6,ipadx=2, ipady=2)
btn_3_7.grid(row=3,column=7,ipadx=2, ipady=2)
btn_4_0.grid(row=4,column=0,ipadx=2, ipady=2)
btn_4_1.grid(row=4,column=1,ipadx=2, ipady=2)
btn_4_2.grid(row=4,column=2,ipadx=2, ipady=2)
btn_4_3.grid(row=4,column=3,ipadx=2, ipady=2)
btn_4_4.grid(row=4,column=4,ipadx=2, ipady=2)
btn_4_5.grid(row=4,column=5,ipadx=2, ipady=2)
btn_4_6.grid(row=4,column=6,ipadx=2, ipady=2)
btn_4_7.grid(row=4,column=7,ipadx=2, ipady=2)
btn_5_0.grid(row=5,column=0,ipadx=2, ipady=2)
btn_5_1.grid(row=5,column=1,ipadx=2, ipady=2)
btn_5_2.grid(row=5,column=2,ipadx=2, ipady=2)
btn_5_3.grid(row=5,column=3,ipadx=2, ipady=2)
btn_5_4.grid(row=5,column=4,ipadx=2, ipady=2)
btn_5_5.grid(row=5,column=5,ipadx=2, ipady=2)
btn_5_6.grid(row=5,column=6,ipadx=2, ipady=2)
btn_5_7.grid(row=5,column=7,ipadx=2, ipady=2)
btn_6_0.grid(row=6,column=0,ipadx=2, ipady=2)
btn_6_1.grid(row=6,column=1,ipadx=2, ipady=2)
btn_6_2.grid(row=6,column=2,ipadx=2, ipady=2)
btn_6_3.grid(row=6,column=3,ipadx=2, ipady=2)
btn_6_4.grid(row=6,column=4,ipadx=2, ipady=2)
btn_6_5.grid(row=6,column=5,ipadx=2, ipady=2)
btn_6_6.grid(row=6,column=6,ipadx=2, ipady=2)
btn_6_7.grid(row=6,column=7,ipadx=2, ipady=2)
btn_7_0.grid(row=7,column=0,ipadx=2, ipady=2)
btn_7_1.grid(row=7,column=1,ipadx=2, ipady=2)
btn_7_2.grid(row=7,column=2,ipadx=2, ipady=2)
btn_7_3.grid(row=7,column=3,ipadx=2, ipady=2)
btn_7_4.grid(row=7,column=4,ipadx=2, ipady=2)
btn_7_5.grid(row=7,column=5,ipadx=2, ipady=2)
btn_7_6.grid(row=7,column=6,ipadx=2, ipady=2)
btn_7_7.grid(row=7,column=7,ipadx=2, ipady=2)



btn_reset.grid   (row=9,column=1)
btn_obstaculos.grid  (row=9,column=3)
btn_ini_fim.grid (row=9,column=5)
btn_run.grid     (row=9,column=7)

def colorir_inicial():
    if map[0][0] == 0:
        btn_0_0['bg'] = "green"
    else:
        btn_0_0['bg'] = "red"

    if map[0][1] == 0:
        btn_0_1['bg'] = "green"
    else:
        btn_0_1['bg'] = "red"

    if map[0][2] == 0:
        btn_0_2['bg'] = "green"
    else:
        btn_0_2['bg'] = "red"

    if map[1][0] == 0:
        btn_1_0['bg'] = "green"
    else:
        btn_1_0['bg'] = "red"

    if map[1][1] == 0:
        btn_1_1['bg'] = "green"
    else:
        btn_1_1['bg'] = "red"

    if map[1][2] == 0:
        btn_1_2['bg'] = "green"
    else:
        btn_1_2['bg'] = "red"

    if map[2][0] == 0:
        btn_2_0['bg'] = "green"
    else:
        btn_2_0['bg'] = "red"

    if map[2][1] == 0:
        btn_2_1['bg'] = "green"
    else:
        btn_2_1['bg'] = "red"

    if map[2][2] == 0:
        btn_2_2['bg'] = "green"
    else:
        btn_2_2['bg'] = "red"

class Environment:

    def __init__(self, map, start, goal):
        self.map = np.array(map)              # mapa
        self.start = np.array(start)          # posição inicial
        self.goal = np.array(goal)            # objetivo
        self.agent_position = np.array(start) # posição do agente; começa na start
        self.actions = np.array([[1,0], [-1,0], [0,1], [0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]) # passo que se pode dar



    def initial_percepts(self):

        available = []                             # disponíveis

        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.start + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis


        return{'available_positions': available,       # retorna quais as posições disponíveis
                'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
                 'goal': self.goal}



    def signal(self, action):
        self.agent_position = action['go_to'] # posição do agente

        available = []                             # disponíveis
        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.agent_position + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis

        return{'available_positions': available,       # retorna quais as posições disponíveis
               'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
               'goal': self.goal}




class Agent:

    def __init__(self, env):

        self.belief_state = env.initial_percepts()
        self.env = env

    def act(self):

        F = [[self.belief_state['position']]]
        global i
        i = 0

        while F:
            path = F.pop(0)
            i += 1
            print(i)

            self.belief_state = self.env.signal({'go_to': path[-1]})

            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:

                    # Checks whether a cycle will be made
                    makes_cycle = False
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = True
                            break

                    if not makes_cycle:
                        F = [path + [p]] + F



        return []



'''class Agent:

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.env = env
        self.cor = np.array([])





    def act(self):
        F = [[self.belief_state['position']] ]  # posição inicial do agente


        i = 0
        while F:
            i += 1


            path  = F.pop(0)        # posição do agente - F[0]



            self.belief_state = self.env.signal({'go_to':path[-1]}) # sentido da direita pra esquerda



            a = 0
            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:

                    # Cheks whter a cycle will be made
                    makes_cycle = False
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = False
                            break


                    if not makes_cycle:
                        F = [path + [p]] + F  # busca em largura
                        a += 1
                        print(a)

'''
        #return []








Reset() # colorir todos de verde e mapa tudo 0




janela.mainloop()


#----------------------------------------------------------------------------------------
# GULOSO

import numpy as np

from tkinter import *

import time

fase = 0
janela = Tk()

janela.title("LABIRINTO PROFUNDIDADE")
janela.geometry("432x500")

a = 0
b = 0

def change_button(x,y):
    global fase
    global a
    global b

    if fase == 5:
        fase = 3

    if fase == 1:

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "red"
            map[0][0] = 1

        if x == 0 and y == 1:
            btn_0_1['bg'] = "red"
            map[0][1] = 1

        if x == 0 and y == 2:
            btn_0_2['bg'] = "red"
            map[0][2] = 1

        if x == 0 and y == 3:
            btn_0_3['bg'] = "red"
            map[0][3] = 1

        if x == 0 and y == 4:
            btn_0_4['bg'] = "red"
            map[0][4] = 1

        if x == 0 and y == 5:
            btn_0_5['bg'] = "red"
            map[0][5] = 1

        if x == 0 and y == 6:
            btn_0_6['bg'] = "red"
            map[0][6] = 1

        if x == 0 and y == 7:
            btn_0_7['bg'] = "red"
            map[0][7] = 1

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "red"
            map[1][0] = 1

        if x == 1 and y == 1:
            btn_1_1['bg'] = "red"
            map[1][1] = 1

        if x == 1 and y == 2:
            btn_1_2['bg'] = "red"
            map[1][2] = 1

        if x == 1 and y == 3:
            btn_1_3['bg'] = "red"
            map[1][3] = 1

        if x == 1 and y == 4:
            btn_1_4['bg'] = "red"
            map[1][4] = 1

        if x == 1 and y == 5:
            btn_1_5['bg'] = "red"
            map[1][5] = 1

        if x == 1 and y == 6:
            btn_1_6['bg'] = "red"
            map[1][6] = 1

        if x == 1 and y == 7:
            btn_1_7['bg'] = "red"
            map[1][7] = 1

        if x == 2 and y == 0:
            btn_2_0['bg'] = "red"
            map[2][0] = 1

        if x == 2 and y == 1:
            btn_2_1['bg'] = "red"
            map[2][1] = 1

        if x == 2 and y == 2:
            btn_2_2['bg'] = "red"
            map[2][2] = 1

        if x == 2 and y == 3:
            btn_2_3['bg'] = "red"
            map[2][3] = 1

        if x == 2 and y == 4:
            btn_2_4['bg'] = "red"
            map[2][4] = 1

        if x == 2 and y == 5:
            btn_2_5['bg'] = "red"
            map[2][5] = 1

        if x == 2 and y == 6:
            btn_2_6['bg'] = "red"
            map[2][6] = 1

        if x == 2 and y == 7:
            btn_2_7['bg'] = "red"
            map[2][7] = 1

        if x == 3 and y == 0:
            btn_3_0['bg'] = "red"
            map[3][0] = 1

        if x == 3 and y == 1:
            btn_3_1['bg'] = "red"
            map[3][1] = 1

        if x == 3 and y == 2:
            btn_3_2['bg'] = "red"
            map[3][2] = 1

        if x == 3 and y == 3:
            btn_3_3['bg'] = "red"
            map[3][3] = 1

        if x == 3 and y == 4:
            btn_3_4['bg'] = "red"
            map[3][4] = 1

        if x == 3 and y == 5:
            btn_3_5['bg'] = "red"
            map[3][5] = 1

        if x == 3 and y == 6:
            btn_3_6['bg'] = "red"
            map[3][6] = 1

        if x == 3 and y == 7:
            btn_3_7['bg'] = "red"
            map[3][7] = 1

        if x == 4 and y == 0:
            btn_4_0['bg'] = "red"
            map[4][0] = 1

        if x == 4 and y == 1:
            btn_4_1['bg'] = "red"
            map[4][1] = 1

        if x == 4 and y == 2:
            btn_4_2['bg'] = "red"
            map[4][2] = 1

        if x == 4 and y == 3:
            btn_4_3['bg'] = "red"
            map[4][3] = 1

        if x == 4 and y == 4:
            btn_4_4['bg'] = "red"
            map[4][4] = 1

        if x == 4 and y == 5:
            btn_4_5['bg'] = "red"
            map[4][5] = 1

        if x == 4 and y == 6:
            btn_4_6['bg'] = "red"
            map[4][6] = 1

        if x == 4 and y == 7:
            btn_4_7['bg'] = "red"
            map[4][7] = 1

        if x == 5 and y == 0:
            btn_5_0['bg'] = "red"
            map[5][0] = 1

        if x == 5 and y == 1:
            btn_5_1['bg'] = "red"
            map[5][1] = 1

        if x == 5 and y == 2:
            btn_5_2['bg'] = "red"
            map[5][2] = 1

        if x == 5 and y == 3:
            btn_5_3['bg'] = "red"
            map[5][3] = 1

        if x == 5 and y == 4:
            btn_5_4['bg'] = "red"
            map[5][4] = 1

        if x == 5 and y == 5:
            btn_5_5['bg'] = "red"
            map[5][5] = 1

        if x == 5 and y == 6:
            btn_5_6['bg'] = "red"
            map[5][6] = 1

        if x == 5 and y == 7:
            btn_5_7['bg'] = "red"
            map[5][7] = 1

        if x == 6 and y == 0:
            btn_6_0['bg'] = "red"
            map[6][0] = 1

        if x == 6 and y == 1:
            btn_6_1['bg'] = "red"
            map[6][1] = 1

        if x == 6 and y == 2:
            btn_6_2['bg'] = "red"
            map[6][2] = 1

        if x == 6 and y == 3:
            btn_6_3['bg'] = "red"
            map[6][3] = 1

        if x == 6 and y == 4:
            btn_6_4['bg'] = "red"
            map[6][4] = 1

        if x == 6 and y == 5:
            btn_6_5['bg'] = "red"
            map[6][5] = 1

        if x == 6 and y == 6:
            btn_6_6['bg'] = "red"
            map[6][6] = 1

        if x == 6 and y == 7:
            btn_6_7['bg'] = "red"
            map[6][7] = 1

        if x == 7 and y == 0:
            btn_7_0['bg'] = "red"
            map[7][0] = 1

        if x == 7 and y == 1:
            btn_7_1['bg'] = "red"
            map[7][1] = 1

        if x == 7 and y == 2:
            btn_7_2['bg'] = "red"
            map[7][2] = 1

        if x == 7 and y == 3:
            btn_7_3['bg'] = "red"
            map[7][3] = 1

        if x == 7 and y == 4:
            btn_7_4['bg'] = "red"
            map[7][4] = 1

        if x == 7 and y == 5:
            btn_7_5['bg'] = "red"
            map[7][5] = 1

        if x == 7 and y == 6:
            btn_7_6['bg'] = "red"
            map[7][6] = 1

        if x == 7 and y == 7:
            btn_7_7['bg'] = "red"
            map[7][7] = 1



    if fase == 2:

        # início
        a = x
        b = y

        fase = 5


        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"


    if fase == 3:
        # fim
        global env
        global ag
        env = Environment(map, [a, b], [x, y], valor)
        ag = Agent(env)

        fase = 4

        if x==0 and y==0:  # se botão 00
            btn_0_0['bg'] = "blue"

        if x == 0 and y == 1:
            btn_0_1['bg'] = "blue"

        if x == 0 and y == 2:
            btn_0_2['bg'] = "blue"

        if x == 0 and y == 3:
            btn_0_3['bg'] = "blue"

        if x == 0 and y == 4:
            btn_0_4['bg'] = "blue"

        if x == 0 and y == 5:
            btn_0_5['bg'] = "blue"

        if x == 0 and y == 6:
            btn_0_6['bg'] = "blue"

        if x == 0 and y == 7:
            btn_0_7['bg'] = "blue"

        if x == 1 and y == 0:  # se botão 00
            btn_1_0['bg'] = "blue"

        if x == 1 and y == 1:
            btn_1_1['bg'] = "blue"

        if x == 1 and y == 2:
            btn_1_2['bg'] = "blue"

        if x == 1 and y == 3:
            btn_1_3['bg'] = "blue"

        if x == 1 and y == 4:
            btn_1_4['bg'] = "blue"

        if x == 1 and y == 5:
            btn_1_5['bg'] = "blue"

        if x == 1 and y == 6:
            btn_1_6['bg'] = "blue"

        if x == 1 and y == 7:
            btn_1_7['bg'] = "blue"

        if x == 2 and y == 0:
            btn_2_0['bg'] = "blue"

        if x == 2 and y == 1:
            btn_2_1['bg'] = "blue"

        if x == 2 and y == 2:
            btn_2_2['bg'] = "blue"

        if x == 2 and y == 3:
            btn_2_3['bg'] = "blue"

        if x == 2 and y == 4:
            btn_2_4['bg'] = "blue"

        if x == 2 and y == 5:
            btn_2_5['bg'] = "blue"

        if x == 2 and y == 6:
            btn_2_6['bg'] = "blue"

        if x == 2 and y == 7:
            btn_2_7['bg'] = "blue"

        if x == 3 and y == 0:
            btn_3_0['bg'] = "blue"

        if x == 3 and y == 1:
            btn_3_1['bg'] = "blue"

        if x == 3 and y == 2:
            btn_3_2['bg'] = "blue"

        if x == 3 and y == 3:
            btn_3_3['bg'] = "blue"

        if x == 3 and y == 4:
            btn_3_4['bg'] = "blue"

        if x == 3 and y == 5:
            btn_3_5['bg'] = "blue"

        if x == 3 and y == 6:
            btn_3_6['bg'] = "blue"

        if x == 3 and y == 7:
            btn_3_7['bg'] = "blue"

        if x == 4 and y == 0:
            btn_4_0['bg'] = "blue"

        if x == 4 and y == 1:
            btn_4_1['bg'] = "blue"

        if x == 4 and y == 2:
            btn_4_2['bg'] = "blue"

        if x == 4 and y == 3:
            btn_4_3['bg'] = "blue"

        if x == 4 and y == 4:
            btn_4_4['bg'] = "blue"

        if x == 4 and y == 5:
            btn_4_5['bg'] = "blue"

        if x == 4 and y == 6:
            btn_4_6['bg'] = "blue"

        if x == 4 and y == 7:
            btn_4_7['bg'] = "blue"

        if x == 5 and y == 0:
            btn_5_0['bg'] = "blue"

        if x == 5 and y == 1:
            btn_5_1['bg'] = "blue"

        if x == 5 and y == 2:
            btn_5_2['bg'] = "blue"

        if x == 5 and y == 3:
            btn_5_3['bg'] = "blue"

        if x == 5 and y == 4:
            btn_5_4['bg'] = "blue"

        if x == 5 and y == 5:
            btn_5_5['bg'] = "blue"

        if x == 5 and y == 6:
            btn_5_6['bg'] = "blue"

        if x == 5 and y == 7:
            btn_5_7['bg'] = "blue"

        if x == 6 and y == 0:
            btn_6_0['bg'] = "blue"

        if x == 6 and y == 1:
            btn_6_1['bg'] = "blue"

        if x == 6 and y == 2:
            btn_6_2['bg'] = "blue"

        if x == 6 and y == 3:
            btn_6_3['bg'] = "blue"

        if x == 6 and y == 4:
            btn_6_4['bg'] = "blue"

        if x == 6 and y == 5:
            btn_6_5['bg'] = "blue"

        if x == 6 and y == 6:
            btn_6_6['bg'] = "blue"

        if x == 6 and y == 7:
            btn_6_7['bg'] = "blue"

        if x == 7 and y == 0:
            btn_7_0['bg'] = "blue"

        if x == 7 and y == 1:
            btn_7_1['bg'] = "blue"

        if x == 7 and y == 2:
            btn_7_2['bg'] = "blue"

        if x == 7 and y == 3:
            btn_7_3['bg'] = "blue"

        if x == 7 and y == 4:
            btn_7_4['bg'] = "blue"

        if x == 7 and y == 5:
            btn_7_5['bg'] = "blue"

        if x == 7 and y == 6:
            btn_7_6['bg'] = "blue"

        if x == 7 and y == 7:
            btn_7_7['bg'] = "blue"



def b00():
    btn_0_0['bg'] = "yellow"


def b01():
    btn_0_1['bg'] = "yellow"


def b02():
    btn_0_2['bg'] = "yellow"


def b03():
    btn_0_3['bg'] = "yellow"


def b04():
    btn_0_4['bg'] = "yellow"


def b05():
    btn_0_5['bg'] = "yellow"


def b06():
    btn_0_6['bg'] = "yellow"


def b07():
    btn_0_7['bg'] = "yellow"


def b10():
    btn_1_0['bg'] = "yellow"


def b11():
    btn_1_1['bg'] = "yellow"


def b12():
    btn_1_2['bg'] = "yellow"


def b13():
    btn_1_3['bg'] = "yellow"


def b14():
    btn_1_4['bg'] = "yellow"


def b15():
    btn_1_5['bg'] = "yellow"


def b16():
    btn_1_6['bg'] = "yellow"


def b17():
    btn_1_7['bg'] = "yellow"


def b20():
    btn_2_0['bg'] = "yellow"


def b21():
    btn_2_1['bg'] = "yellow"


def b22():
    btn_2_2['bg'] = "yellow"


def b23():
    btn_2_3['bg'] = "yellow"


def b24():
    btn_2_4['bg'] = "yellow"


def b25():
    btn_2_5['bg'] = "yellow"


def b26():
    btn_2_6['bg'] = "yellow"


def b27():
    btn_2_7['bg'] = "yellow"


def b30():
    btn_3_0['bg'] = "yellow"


def b31():
    btn_3_1['bg'] = "yellow"


def b32():
    btn_3_2['bg'] = "yellow"


def b33():
    btn_3_3['bg'] = "yellow"


def b34():
    btn_3_4['bg'] = "yellow"


def b35():
    btn_3_5['bg'] = "yellow"


def b36():
    btn_3_6['bg'] = "yellow"


def b37():
    btn_3_7['bg'] = "yellow"


def b40():
    btn_4_0['bg'] = "yellow"


def b41():
    btn_4_1['bg'] = "yellow"


def b42():
    btn_4_2['bg'] = "yellow"


def b43():
    btn_4_3['bg'] = "yellow"


def b44():
    btn_4_4['bg'] = "yellow"


def b45():
    btn_4_5['bg'] = "yellow"


def b46():
    btn_4_6['bg'] = "yellow"


def b47():
    btn_4_7['bg'] = "yellow"


def b50():
    btn_5_0['bg'] = "yellow"


def b51():
    btn_5_1['bg'] = "yellow"


def b52():
    btn_5_2['bg'] = "yellow"


def b53():
    btn_5_3['bg'] = "yellow"


def b54():
    btn_5_4['bg'] = "yellow"


def b55():
    btn_5_5['bg'] = "yellow"


def b56():
    btn_5_6['bg'] = "yellow"


def b57():
    btn_5_7['bg'] = "yellow"


def b60():
    btn_6_0['bg'] = "yellow"


def b61():
    btn_6_1['bg'] = "yellow"


def b62():
    btn_6_2['bg'] = "yellow"


def b63():
    btn_6_3['bg'] = "yellow"


def b64():
    btn_6_4['bg'] = "yellow"


def b65():
    btn_6_5['bg'] = "yellow"


def b66():
    btn_6_6['bg'] = "yellow"


def b67():
    btn_6_7['bg'] = "yellow"


def b70():
    btn_7_0['bg'] = "yellow"


def b71():
    btn_7_1['bg'] = "yellow"


def b72():
    btn_7_2['bg'] = "yellow"


def b73():
    btn_7_3['bg'] = "yellow"


def b74():
    btn_7_4['bg'] = "yellow"


def b75():
    btn_7_5['bg'] = "yellow"


def b76():
    btn_7_6['bg'] = "yellow"


def b77():
    btn_7_7['bg'] = "yellow"




def Reset():
    global fase
    fase = 0

    global map
    global valor

    map = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

    valor =  [[1, 2, 0, 0, 0, 0, 0, 0],
              [1, 2, 0, 0, 0, 0, 0, 0],
              [1, 2, 0, 0, 0, 0, 0, 0],
              [1, 2, 0, 0, 0, 0, 0, 0],
              [1, 2, 3, 0, 0, 0, 0, 0],
              [1, 2, 3, 0, 0, 0, 0, 0],
              [1, 2, 3, 0, 0, 0, 0, 0],
              [1, 2, 3, 0, 0, 0, 0, 0]]

    btn_0_0['bg'] = "green"
    btn_0_1['bg'] = "green"
    btn_0_2['bg'] = "green"
    btn_0_3['bg'] = "green"
    btn_0_4['bg'] = "green"
    btn_0_5['bg'] = "green"
    btn_0_6['bg'] = "green"
    btn_0_7['bg'] = "green"
    btn_1_0['bg'] = "green"
    btn_1_1['bg'] = "green"
    btn_1_2['bg'] = "green"
    btn_1_3['bg'] = "green"
    btn_1_4['bg'] = "green"
    btn_1_5['bg'] = "green"
    btn_1_6['bg'] = "green"
    btn_1_7['bg'] = "green"
    btn_2_0['bg'] = "green"
    btn_2_1['bg'] = "green"
    btn_2_2['bg'] = "green"
    btn_2_3['bg'] = "green"
    btn_2_4['bg'] = "green"
    btn_2_5['bg'] = "green"
    btn_2_6['bg'] = "green"
    btn_2_7['bg'] = "green"
    btn_3_0['bg'] = "green"
    btn_3_1['bg'] = "green"
    btn_3_2['bg'] = "green"
    btn_3_3['bg'] = "green"
    btn_3_4['bg'] = "green"
    btn_3_5['bg'] = "green"
    btn_3_6['bg'] = "green"
    btn_3_7['bg'] = "green"
    btn_4_0['bg'] = "green"
    btn_4_1['bg'] = "green"
    btn_4_2['bg'] = "green"
    btn_4_3['bg'] = "green"
    btn_4_4['bg'] = "green"
    btn_4_5['bg'] = "green"
    btn_4_6['bg'] = "green"
    btn_4_7['bg'] = "green"
    btn_5_0['bg'] = "green"
    btn_5_1['bg'] = "green"
    btn_5_2['bg'] = "green"
    btn_5_3['bg'] = "green"
    btn_5_4['bg'] = "green"
    btn_5_5['bg'] = "green"
    btn_5_6['bg'] = "green"
    btn_5_7['bg'] = "green"
    btn_6_0['bg'] = "green"
    btn_6_1['bg'] = "green"
    btn_6_2['bg'] = "green"
    btn_6_3['bg'] = "green"
    btn_6_4['bg'] = "green"
    btn_6_5['bg'] = "green"
    btn_6_6['bg'] = "green"
    btn_6_7['bg'] = "green"
    btn_7_0['bg'] = "green"
    btn_7_1['bg'] = "green"
    btn_7_2['bg'] = "green"
    btn_7_3['bg'] = "green"
    btn_7_4['bg'] = "green"
    btn_7_5['bg'] = "green"
    btn_7_6['bg'] = "green"
    btn_7_7['bg'] = "green"

def Obstaculos():
    global fase
    fase = 1


def Inifim():
    global fase
    fase = 2


def Run():
            # if __name__ == '__main__':

    path = ag.act()


    x = 400
    y = 400
    for count in path:


        if (count == [0, 0]).all():
            janela.after(x,b00)
            x += y

        elif (count == [0, 1]).all():
            janela.after(x,b01)
            x += y

        elif (count == [0, 2]).all():
            janela.after(x,b02)
            x += y

        elif (count == [0, 3]).all():
            janela.after(x,b03)
            x += y

        elif (count == [0, 4]).all():
            janela.after(x,b04)
            x += y


        elif (count == [0, 5]).all():
            janela.after(x,b05)
            x += y

        elif (count == [0, 6]).all():
            janela.after(x,b06)
            x += y

        elif (count == [0, 7]).all():
            janela.after(x,b07)
            x += y



        if (count == [1, 0]).all():
            janela.after(x,b10)
            x += y

        elif (count == [1, 1]).all():
            janela.after(x,b11)
            x += y

        elif (count == [1, 2]).all():
            janela.after(x,b12)
            x += y

        elif (count == [1, 3]).all():
            janela.after(x,b13)
            x += y

        elif (count == [1, 4]).all():
            janela.after(x,b14)
            x += y


        elif (count == [1, 5]).all():
            janela.after(x,b15)
            x += y

        elif (count == [1, 6]).all():
            janela.after(x,b16)
            x += y

        elif (count == [1, 7]).all():
            janela.after(x,b17)
            x += y



        elif (count == [2, 0]).all():
            janela.after(x,b20)
            x += y

        elif (count == [2, 1]).all():
            janela.after(x,b21)
            x += y

        elif (count == [2, 2]).all():
            janela.after(x,b22)
            x += y

        elif (count == [2, 3]).all():
            janela.after(x,b23)
            x += y

        elif (count == [2, 4]).all():
            janela.after(x,b24)
            x += y


        elif (count == [2, 5]).all():
            janela.after(x,b25)
            x += y

        elif (count == [2, 6]).all():
            janela.after(x,b26)
            x += y

        elif (count == [2, 7]).all():
            janela.after(x,b27)
            x += y



        elif (count == [3, 0]).all():
            janela.after(x,b30)
            x += y

        elif (count == [3, 1]).all():
            janela.after(x,b31)
            x += y

        elif (count == [3, 2]).all():
            janela.after(x,b32)
            x += y

        elif (count == [3, 3]).all():
            janela.after(x,b33)
            x += y

        elif (count == [3, 4]).all():
            janela.after(x,b34)
            x += y


        elif (count == [3, 5]).all():
            janela.after(x,b35)
            x += y

        elif (count == [3, 6]).all():
            janela.after(x,b36)
            x += y

        elif (count == [3, 7]).all():
            janela.after(x,b37)
            x += y



        elif (count == [4, 0]).all():
            janela.after(x,b40)
            x += y

        elif (count == [4, 1]).all():
            janela.after(x,b41)
            x += y

        elif (count == [4, 2]).all():
            janela.after(x,b42)
            x += y

        elif (count == [4, 3]).all():
            janela.after(x,b43)
            x += y

        elif (count == [4, 4]).all():
            janela.after(x,b44)
            x += y


        elif (count == [4, 5]).all():
            janela.after(x,b45)
            x += y

        elif (count == [4, 6]).all():
            janela.after(x,b46)
            x += y

        elif (count == [4, 7]).all():
            janela.after(x,b47)
            x += y



        elif (count == [5, 0]).all():
            janela.after(x,b50)
            x += y

        elif (count == [5, 1]).all():
            janela.after(x,b51)
            x += y

        elif (count == [5, 2]).all():
            janela.after(x,b52)
            x += y

        elif (count == [5, 3]).all():
            janela.after(x,b53)
            x += y

        elif (count == [5, 4]).all():
            janela.after(x,b54)
            x += y


        elif (count == [5, 5]).all():
            janela.after(x,b55)
            x += y

        elif (count == [5, 6]).all():
            janela.after(x,b56)
            x += y

        elif (count == [5, 7]).all():
            janela.after(x,b57)
            x += y



        elif (count == [6, 0]).all():
            janela.after(x,b60)
            x += y

        elif (count == [6, 1]).all():
            janela.after(x,b61)
            x += y

        elif (count == [6, 2]).all():
            janela.after(x,b62)
            x += y

        elif (count == [6, 3]).all():
            janela.after(x,b63)
            x += y

        elif (count == [6, 4]).all():
            janela.after(x,b64)
            x += y


        elif (count == [6, 5]).all():
            janela.after(x,b65)
            x += y

        elif (count == [6, 6]).all():
            janela.after(x,b66)
            x += y

        elif (count == [6, 7]).all():
            janela.after(x,b67)
            x += y



        elif (count == [7, 0]).all():
            janela.after(x,b70)
            x += y

        elif (count == [7, 1]).all():
            janela.after(x,b71)
            x += y

        elif (count == [7, 2]).all():
            janela.after(x,b72)
            x += y

        elif (count == [7, 3]).all():
            janela.after(x,b73)
            x += y

        elif (count == [7, 4]).all():
            janela.after(x,b74)
            x += y


        elif (count == [7, 5]).all():
            janela.after(x,b75)
            x += y

        elif (count == [7, 6]).all():
            janela.after(x,b76)
            x += y

        elif (count == [7, 7]).all():
            janela.after(x,b77)
            x += y







btn_0_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,0))
btn_0_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,1) )
btn_0_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,2) )
btn_0_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,3) )
btn_0_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,4) )
btn_0_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,5) )
btn_0_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,6) )
btn_0_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(0,7) )
btn_1_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,0) )
btn_1_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,1) )
btn_1_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,2) )
btn_1_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,3) )
btn_1_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,4) )
btn_1_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,5) )
btn_1_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,6) )
btn_1_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(1,7) )
btn_2_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,0) )
btn_2_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,1) )
btn_2_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,2) )
btn_2_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,3) )
btn_2_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,4) )
btn_2_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,5) )
btn_2_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,6) )
btn_2_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(2,7) )
btn_3_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,0) )
btn_3_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,1) )
btn_3_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,2) )
btn_3_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,3) )
btn_3_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,4) )
btn_3_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,5) )
btn_3_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,6) )
btn_3_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(3,7) )
btn_4_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,0) )
btn_4_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,1) )
btn_4_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,2) )
btn_4_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,3) )
btn_4_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,4) )
btn_4_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,5) )
btn_4_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,6) )
btn_4_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(4,7) )
btn_5_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,0) )
btn_5_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,1) )
btn_5_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,2) )
btn_5_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,3) )
btn_5_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,4) )
btn_5_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,5) )
btn_5_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,6) )
btn_5_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(5,7) )
btn_6_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,0) )
btn_6_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,1) )
btn_6_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,2) )
btn_6_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,3) )
btn_6_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,4) )
btn_6_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,5) )
btn_6_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,6) )
btn_6_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(6,7) )
btn_7_0 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,0) )
btn_7_1 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,1) )
btn_7_2 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,2) )
btn_7_3 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,3) )
btn_7_4 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,4) )
btn_7_5 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,5) )
btn_7_6 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,6) )
btn_7_7 = Button(janela,text= "", width=6, height=3,bd=1, relief="solid", command = lambda: change_button(7,7) )


btn_reset       = Button(janela,text="reset",   command=Reset )
btn_obstaculos  = Button(janela,text="obstác",  command=Obstaculos)
btn_ini_fim     = Button(janela,text="ini_fim", command=Inifim)
btn_run         = Button(janela,text="run",     command=Run   )



btn_0_0.grid(row=0,column=0,ipadx=2, ipady=2)
btn_0_1.grid(row=0,column=1,ipadx=2, ipady=2)
btn_0_2.grid(row=0,column=2,ipadx=2, ipady=2)
btn_0_3.grid(row=0,column=3,ipadx=2, ipady=2)
btn_0_4.grid(row=0,column=4,ipadx=2, ipady=2)
btn_0_5.grid(row=0,column=5,ipadx=2, ipady=2)
btn_0_6.grid(row=0,column=6,ipadx=2, ipady=2)
btn_0_7.grid(row=0,column=7,ipadx=2, ipady=2)
btn_1_0.grid(row=1,column=0,ipadx=2, ipady=2)
btn_1_1.grid(row=1,column=1,ipadx=2, ipady=2)
btn_1_2.grid(row=1,column=2,ipadx=2, ipady=2)
btn_1_3.grid(row=1,column=3,ipadx=2, ipady=2)
btn_1_4.grid(row=1,column=4,ipadx=2, ipady=2)
btn_1_5.grid(row=1,column=5,ipadx=2, ipady=2)
btn_1_6.grid(row=1,column=6,ipadx=2, ipady=2)
btn_1_7.grid(row=1,column=7,ipadx=2, ipady=2)
btn_2_0.grid(row=2,column=0,ipadx=2, ipady=2)
btn_2_1.grid(row=2,column=1,ipadx=2, ipady=2)
btn_2_2.grid(row=2,column=2,ipadx=2, ipady=2)
btn_2_3.grid(row=2,column=3,ipadx=2, ipady=2)
btn_2_4.grid(row=2,column=4,ipadx=2, ipady=2)
btn_2_5.grid(row=2,column=5,ipadx=2, ipady=2)
btn_2_6.grid(row=2,column=6,ipadx=2, ipady=2)
btn_2_7.grid(row=2,column=7,ipadx=2, ipady=2)
btn_3_0.grid(row=3,column=0,ipadx=2, ipady=2)
btn_3_1.grid(row=3,column=1,ipadx=2, ipady=2)
btn_3_2.grid(row=3,column=2,ipadx=2, ipady=2)
btn_3_3.grid(row=3,column=3,ipadx=2, ipady=2)
btn_3_4.grid(row=3,column=4,ipadx=2, ipady=2)
btn_3_5.grid(row=3,column=5,ipadx=2, ipady=2)
btn_3_6.grid(row=3,column=6,ipadx=2, ipady=2)
btn_3_7.grid(row=3,column=7,ipadx=2, ipady=2)
btn_4_0.grid(row=4,column=0,ipadx=2, ipady=2)
btn_4_1.grid(row=4,column=1,ipadx=2, ipady=2)
btn_4_2.grid(row=4,column=2,ipadx=2, ipady=2)
btn_4_3.grid(row=4,column=3,ipadx=2, ipady=2)
btn_4_4.grid(row=4,column=4,ipadx=2, ipady=2)
btn_4_5.grid(row=4,column=5,ipadx=2, ipady=2)
btn_4_6.grid(row=4,column=6,ipadx=2, ipady=2)
btn_4_7.grid(row=4,column=7,ipadx=2, ipady=2)
btn_5_0.grid(row=5,column=0,ipadx=2, ipady=2)
btn_5_1.grid(row=5,column=1,ipadx=2, ipady=2)
btn_5_2.grid(row=5,column=2,ipadx=2, ipady=2)
btn_5_3.grid(row=5,column=3,ipadx=2, ipady=2)
btn_5_4.grid(row=5,column=4,ipadx=2, ipady=2)
btn_5_5.grid(row=5,column=5,ipadx=2, ipady=2)
btn_5_6.grid(row=5,column=6,ipadx=2, ipady=2)
btn_5_7.grid(row=5,column=7,ipadx=2, ipady=2)
btn_6_0.grid(row=6,column=0,ipadx=2, ipady=2)
btn_6_1.grid(row=6,column=1,ipadx=2, ipady=2)
btn_6_2.grid(row=6,column=2,ipadx=2, ipady=2)
btn_6_3.grid(row=6,column=3,ipadx=2, ipady=2)
btn_6_4.grid(row=6,column=4,ipadx=2, ipady=2)
btn_6_5.grid(row=6,column=5,ipadx=2, ipady=2)
btn_6_6.grid(row=6,column=6,ipadx=2, ipady=2)
btn_6_7.grid(row=6,column=7,ipadx=2, ipady=2)
btn_7_0.grid(row=7,column=0,ipadx=2, ipady=2)
btn_7_1.grid(row=7,column=1,ipadx=2, ipady=2)
btn_7_2.grid(row=7,column=2,ipadx=2, ipady=2)
btn_7_3.grid(row=7,column=3,ipadx=2, ipady=2)
btn_7_4.grid(row=7,column=4,ipadx=2, ipady=2)
btn_7_5.grid(row=7,column=5,ipadx=2, ipady=2)
btn_7_6.grid(row=7,column=6,ipadx=2, ipady=2)
btn_7_7.grid(row=7,column=7,ipadx=2, ipady=2)



btn_reset.grid   (row=9,column=1)
btn_obstaculos.grid  (row=9,column=3)
btn_ini_fim.grid (row=9,column=5)
btn_run.grid     (row=9,column=7)

def colorir_inicial():
    if map[0][0] == 0:
        btn_0_0['bg'] = "green"
    else:
        btn_0_0['bg'] = "red"

    if map[0][1] == 0:
        btn_0_1['bg'] = "green"
    else:
        btn_0_1['bg'] = "red"

    if map[0][2] == 0:
        btn_0_2['bg'] = "green"
    else:
        btn_0_2['bg'] = "red"

    if map[1][0] == 0:
        btn_1_0['bg'] = "green"
    else:
        btn_1_0['bg'] = "red"

    if map[1][1] == 0:
        btn_1_1['bg'] = "green"
    else:
        btn_1_1['bg'] = "red"

    if map[1][2] == 0:
        btn_1_2['bg'] = "green"
    else:
        btn_1_2['bg'] = "red"

    if map[2][0] == 0:
        btn_2_0['bg'] = "green"
    else:
        btn_2_0['bg'] = "red"

    if map[2][1] == 0:
        btn_2_1['bg'] = "green"
    else:
        btn_2_1['bg'] = "red"

    if map[2][2] == 0:
        btn_2_2['bg'] = "green"
    else:
        btn_2_2['bg'] = "red"

class Environment:

    def __init__(self, map, start, goal, valor):
        self.map = np.array(map)              # mapa
        self.start = np.array(start)          # posição inicial
        self.goal = np.array(goal)            # objetivo
        self.agent_position = np.array(start) # posição do agente; começa na start
        self.actions = np.array([[1,0], [-1,0], [0,1], [0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]) # passo que se pode dar
        self.valor = np.array(valor)
        self.x = -1



    def initial_percepts(self):

        available = []                             # disponíveis

        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.start + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                if self.x == -1 or self.valor[pos] < self.x:
                    available.insert(0,pos)      # armazena todas as disponíveis


        return{'available_positions': available,       # retorna quais as posições disponíveis
                'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
                 'goal': self.goal}



    def signal(self, action):
        self.agent_position = action['go_to'] # posição do agente

        available = []                             # disponíveis
        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.agent_position + a                   # posição inicial mais o passo dado

            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                if self.x == -1 or self.valor[pos] < self.x:
                    available.insert(0,pos)      # armazena todas as disponíveis

        return{'available_positions': available,       # retorna quais as posições disponíveis
               'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
               'goal': self.goal}




class Agent:

    def __init__(self, env):

        self.belief_state = env.initial_percepts()
        self.env = env

    def act(self):

        F = [[self.belief_state['position']]]
        global i
        i = 0

        while F:
            path = F.pop(0)
            i += 1
            print(i)

            self.belief_state = self.env.signal({'go_to': path[-1]})

            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:

                    # Checks whether a cycle will be made
                    makes_cycle = False
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = True
                            break

                    if not makes_cycle:
                        F = [path + [p]] + F



        return []



'''class Agent:

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.env = env
        self.cor = np.array([])





    def act(self):
        F = [[self.belief_state['position']] ]  # posição inicial do agente


        i = 0
        while F:
            i += 1


            path  = F.pop(0)        # posição do agente - F[0]



            self.belief_state = self.env.signal({'go_to':path[-1]}) # sentido da direita pra esquerda



            a = 0
            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:

                    # Cheks whter a cycle will be made
                    makes_cycle = False
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = False
                            break


                    if not makes_cycle:
                        F = [path + [p]] + F  # busca em largura
                        a += 1
                        print(a)

'''
        #return []








Reset() # colorir todos de verde e mapa tudo 0




janela.mainloop()




