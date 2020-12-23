#!python3
# Simulador de dado - Valor 1 a 6.

import random

import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo valor para o dado?'
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('nao')]
        ]

    def Iniciar(self):

        # criar janela
        self.janela = sg.Window('Simulador de Dado', layout = self.layout)
        #ler valores
        self.eventos,self.valores=self.janela.Read()
        #fazer algo com os valores

       

        try:
            
            if self.eventos=='sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos=='nao' or self.eventos == 'n':
                print('Agradecemos a sua participação')

            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro')

    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
