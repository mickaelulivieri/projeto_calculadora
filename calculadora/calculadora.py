from tkinter import *

cor_1= "#145ea8"
cor_2= "#2b33ab"
cor_3= "#5c656b"
cor_4= "#fcfcfc"
cor_5= "#b55921"
cor_6= "#0a1529"

# Criar janela e fazer configs básicas
janela = Tk()
janela.title("Calculator")
janela.geometry("235x310")
janela.config(bg=cor_2)

# Dividir em 2 partes: teclado/display
frame_tela = Frame(janela, width=235, height=50, bg=cor_6)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variável para armazenar todos os valores
todos_valores = ''

# Função para inserir valores na tela
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

# Função para calcular o resultado
def calcular_resultado():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except:
        valor_texto.set("Erro")
        todos_valores = ''

# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# Criando label
valor_texto = StringVar()
app_label = Label(frame_tela, text='', textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 17 bold'), bg=cor_6, fg=cor_4)
app_label.place(x=0, y=0)

# Botões da calculadora
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=9, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=8, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=70, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=14, height=2, bg=cor_5, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=135, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=39)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=46, y=39)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=92, y=39)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=78)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=46, y=78)

b_9 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=92, y=78)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=117)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=46, y=117)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=92, y=117)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=18, height=3, bg=cor_3, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=156)

b_14 = Button(frame_corpo, command=calcular_resultado, text="=", width=32, height=3, bg=cor_6, fg=cor_4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=0, y=208)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=13, height=3, bg=cor_5, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=137, y=39)

b_16 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=13, height=3, bg=cor_5, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=137, y=95)

b_17 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=13, height=3, bg=cor_5, fg=cor_4, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=136, y=152)

janela.mainloop()