
from tkinter import *
from tkinter import ttk

# CORES
cor1 = '#3b3b3b' # preta
cor2 = '#feffff' # branca
cor3 = '#38576b' # Azul
cor4 = '#ECEFF1' # cinza
cor5 = '#FFAB40' # laranjado

janela = Tk()
janela.title('Calculadora')
janela.geometry('233x215')
janela.config(bg=cor1)
janela.resizable(False, False)

# FRAMES PARA DIVIDIR A TELA
"""FRAME 1 VISOR DA CALCULADORA"""
frame_visor = Frame(janela, width=233, height=50, bg=cor3)
frame_visor.grid(row=0, column=0)

"""FRAME 2 BOTÃO DA CALCULADAORA"""
frame_botao = Frame(janela, width=233, height=268)
frame_botao.grid(row=1, column=0)

"""LOGICA USANDO FUNCAO"""
todos_valores = ''
valor_texto = StringVar()
def entrar_valores_visor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # passando o valor para o visor
    valor_texto.set(todos_valores)
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    # imprimir no visor
    valor_texto.set(str(resultado))
def limpa_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# CRIANDO LABEL
visor_label = Label(frame_visor, textvariable=valor_texto, width=16, height=2, padx=4, relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 17 bold', bg=cor3, fg=cor2)
visor_label.place(x=0, y=0)

# CRIANDO OS BOTÕES
"""1º linha"""
botao_clear = Button(frame_botao, command= limpa_tela, text='C', width=11, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_clear.place(x=2, y=0)
botao_porcento = Button(frame_botao, command=lambda: entrar_valores_visor('%'), text='%', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_porcento.place(x=123, y=0)
botao_divisao = Button(frame_botao, command=lambda: entrar_valores_visor('/'), text='/', width=4, height=1, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_divisao.place(x=183, y=0)
"""2º linha"""
botao_7 = Button(frame_botao, command=lambda: entrar_valores_visor('7'), text='7', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_7.place(x=2,y=33)
botao_8 = Button(frame_botao, command=lambda: entrar_valores_visor('8'), text='8', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_8.place(x=62,y=33)
botao_9 = Button(frame_botao, command=lambda: entrar_valores_visor('9'), text='9', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_9.place(x=123,y=33)
botao_multiplicacao = Button(frame_botao, command=lambda: entrar_valores_visor('*'), text='*', width=4, height=1, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_multiplicacao.place(x=183, y=33)
"""3º linha"""
botao_4 = Button(frame_botao, command=lambda: entrar_valores_visor('4'), text='4', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_4.place(x=2,y=66)
botao_5 = Button(frame_botao, command=lambda: entrar_valores_visor('5'), text='5', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_5.place(x=62,y=66)
botao_6 = Button(frame_botao, command=lambda: entrar_valores_visor('6'), text='6', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_6.place(x=123,y=66)
botao_subtracao = Button(frame_botao, command=lambda: entrar_valores_visor('-'), text='-', width=4, height=1, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_subtracao.place(x=183, y=66)
"""4º linha"""
botao_1 = Button(frame_botao, command=lambda: entrar_valores_visor('1'), text='1', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_1.place(x=2,y=99)
botao_2 = Button(frame_botao, command=lambda: entrar_valores_visor('2'), text='2', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_2.place(x=62,y=99)
botao_3 = Button(frame_botao, command=lambda: entrar_valores_visor('3'), text='3', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_3.place(x=123,y=99)
botao_adicao = Button(frame_botao, command=lambda: entrar_valores_visor('+'), text='+', width=4, height=1, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_adicao.place(x=183, y=99)
"""5º linha"""
botao_zero = Button(frame_botao, command=lambda: entrar_valores_visor('0'), text='0', width=11, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_zero.place(x=2, y=132)
botao_ponto = Button(frame_botao, command=lambda: entrar_valores_visor('.'), text='.', width=5, height=1, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_ponto.place(x=123, y=132)
botao_igual = Button(frame_botao, command= calcular, text='=', width=4, height=1, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
botao_igual.place(x=183, y=132)

janela.mainloop()