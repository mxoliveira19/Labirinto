import numpy as np

from tkinter import *

import time

janela = Tk()

janela.title("Labirinto")
janela.geometry("400x400")

def l1():
    label_0_0['bg'] = "yellow"

def l2():
    label_0_1['bg'] = "yellow"
def l3():
    label_0_2['bg'] = "yellow"
def l4():
    label_1_0['bg'] = "yellow"
def l5():
    label_1_1['bg'] = "yellow"

def l6():
    label_1_2['bg'] = "yellow"
def l7():
    label_2_0['bg'] = "yellow"
def l8():
    label_2_1['bg'] = "yellow"
def l9():
    label_2_2['bg'] = "yellow"

def myClick():
            # if __name__ == '__main__':

    path = ag.act()
    print("P: ", path)
    #ag.color()

    x = 400
    for count in path:
        if (count[0] == [0, 0]).all():
            janela.after(x,l1)
            x += x

        elif (count[0] == [0, 1]).all():
            janela.after(x,l2)
            x += x

        elif (count[0] == [0, 2]).all():
            janela.after(x,l3)
            x += x

        elif (count[0] == [1, 0]).all():
            janela.after(x,l4)
            x += x

        elif (count[0] == [1, 1]).all():
            janela.after(x,l5)
            x += x


        elif (count[0] == [1, 2]).all():
            janela.after(x,l6)
            x += x

        elif (count[0] == [2, 0]).all():
            janela.after(x,l7)
            x += x

        elif (count[0] == [2, 1]).all():
            janela.after(x,l8)
            x += x

        elif (count[0] == [2, 2]).all():
            janela.after(x,l9)
            x += x








label_0_0 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_0_1 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_0_2 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_1_0 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_1_1 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_1_2 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_2_0 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_2_1 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
label_2_2 = Label(janela,text= "", width=6, height=3,bd=1, relief="solid")
btn = Button(janela,text="ok", command=myClick)


label_0_0['bg'] = "green"
label_0_1['bg'] = "green"
label_0_2['bg'] = "red"
label_1_0['bg'] = "red"
label_1_1['bg'] = "green"
label_1_2['bg'] = "red"
label_2_0['bg'] = "red"
label_2_1['bg'] = "green"
label_2_2['bg'] = "green"


label_0_0.grid(row=0,column=0,ipadx=2, ipady=2)
label_0_1.grid(row=0,column=1,ipadx=2, ipady=2)
label_0_2.grid(row=0,column=2,ipadx=2, ipady=2)
label_1_0.grid(row=1,column=0,ipadx=2, ipady=2)
label_1_1.grid(row=1,column=1,ipadx=2, ipady=2)
label_1_2.grid(row=1,column=2,ipadx=2, ipady=2)
label_2_0.grid(row=2,column=0,ipadx=2, ipady=2)
label_2_1.grid(row=2,column=1,ipadx=2, ipady=2)
label_2_2.grid(row=2,column=2,ipadx=2, ipady=2)
btn.grid(row=4,column=2)



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
            #print(pos)
            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis
                #print(available)
                print('xxxxxxxxxxx: ', self.agent_position)
        return{'available_positions': available,       # retorna quais as posições disponíveis
                'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
                 'goal': self.goal}



    def signal(self, action):
        self.agent_position = action['go_to'] # posição do agente

        available = []                             # disponíveis
        for a in self.actions:                          # para cada um dos passos possíveis
            pos = self.agent_position + a                   # posição inicial mais o passo dado
            #print(pos)
            if (0 <= pos[0] < self.map.shape[0])  and (0 <= pos[1] < self.map.shape[1]) and self.map[pos[0]][pos[1]] == 0:  # se o mapa estiver livre nessa posição e não sair dele
                available.append(pos)      # armazena todas as disponíveis
                #print(available)
        return{'available_positions': available,       # retorna quais as posições disponíveis
               'position': self.agent_position,     # retorna a posição do agente(?? como, se o agente não tomu nenhum atitude ainda; só viu as disponíveis)
               'goal': self.goal}



class Agent:

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.env = env
        self.cor = np.array([])
        self.q1  = False
        self.q2  = False
        self.q3  = False
        self.q4  = False
        self.q5  = False
        self.q6  = False
        self.q7  = False
        self.q8  = False
        self.q9  = False
        self.q10 = False
        self.q11 = False
        self.q12 = False
        self.q13 = False
        self.q14 = False
        self.q15 = False
        self.q16 = False

        # print(self.belief_state)

    def color(self):

        x = 0
        if self.q1 == True:
            label_0_0['bg'] = "blue"

        time.sleep(x)
        if self.q2 == True:
            label_0_1['bg'] = "blue"

        time.sleep(x)
        if self.q3 == True:
            label_0_2['bg'] = "blue"

        time.sleep(x)

        if self.q4 == True:
            label_1_0['bg'] = "blue"

        time.sleep(x)
        if self.q5 == True:
            label_1_1['bg'] = "blue"

        time.sleep(x)
        if self.q6 == True:
            label_1_2['bg'] = "blue"

        time.sleep(x)

        if self.q7 == True:
            label_2_0['bg'] = "blue"

        time.sleep(x)
        if self.q8 == True:
            label_2_1['bg'] = "blue"

        time.sleep(x)
        if self.q9 == True:
            label_2_2['bg'] = "blue"

        time.sleep(x)

    def act(self):
        F = [[self.belief_state['position']] ]  # posição inicial do agente

        print('posição inicial:', F)
        i = 0
        while F:
            i += 1
            print(i,' F:     ',F)

            path  = F.pop(0)        # posição do agente - F[0]
            self.cor = path[-1]

            if self.cor[0] == [0] and self.cor[1] == [0]:
                self.q1 = True
            if self.cor[0] == [0] and self.cor[1] == [1]:
                self.q2 = True
            if self.cor[0] == [0] and self.cor[1] == [2]:
                self.q3 = True
            if self.cor[0] == [1] and self.cor[1] == [0]:
                self.q4 = True
            if self.cor[0] == [1] and self.cor[1] == [1]:
                self.q5 = True
            if self.cor[0] == [1] and self.cor[1] == [2]:
                self.q6 = True
            if self.cor[0] == [2] and self.cor[1] == [0]:
                self.q7 = True
            if self.cor[0] == [2] and self.cor[1] == [1]:
                self.q8 = True
            if self.cor[0] == [2] and self.cor[1] == [2]:
                self.q9 = True

            print(i,' path:   ', path)

            self.belief_state = self.env.signal({'go_to':path[-1]}) # sentido da direita pra esquerda


            print(i, 'path-1: ', path[-1])
            print(i, 'belief-state: ', self.belief_state)


            if (path[-1] == self.belief_state['goal']).all():
                return path
            else:
                for p in self.belief_state['available_positions']:
                    F.append(path + [p])  # busca em largura
                    print(i, 'F append: ', F)

        #return []




map = [[0,0,1],
       [1,0,1],
       [1,0,0]]

env = Environment(map,[0,0],[2,2])

ag  = Agent(env)



janela.mainloop()



# depósito
'''
    def color(self):
        time.sleep(0.2)
        x = self.cor
        if x[0] == 0 and x[1] == 0:
            label_0_0['bg'] = "blue"
        if x[0] == 0 and x[1] == 1:
            label_0_1['bg'] = "blue"
        if x[0] == 0 and x[1] == 2:
            label_0_2['bg'] = "blue"

        if x[0] == 1 and x[1] == 0:
            label_1_0['bg'] = "blue"
        if x[0] == 1 and x[1] == 1:
            label_1_1['bg'] = "blue"
        if x[0] == 1 and x[1] == 2:
            label_1_2['bg'] = "blue"

        if x[0] == 2 and x[1] == 0:
            label_2_0['bg'] = "blue"
        if x[0] == 2 and x[1] == 1:
            label_2_1['bg'] = "blue"
        if x[0] == 2 and x[1] == 2:
            label_2_2['bg'] = "blue"




'''