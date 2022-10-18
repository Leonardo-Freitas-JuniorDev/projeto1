from tkinter import font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import COLOR_SCHEME, popup

# Criar janelas e estilos
nome = ''
def janela_conf():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Bem vindo ao D"fome')],
        [sg.Button('Sair',key='sair'),sg.Button('Entrar',key='entrar')]
    ]
    return sg.Window('Confirmação', layout=layout,finalize=True)

def janela_login():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Usuario')],
        [sg.Input(key='nome')],
        [sg.Text('Senha')],
        [sg.Input(key='senha',password_char='*')],
        [sg.Button('Novo usuário (em breve)')],
        [sg.Button('Continuar')],
        [sg.Button('Voltar',key='voltar2')]

    ]
    return sg.Window('Login', layout=layout,finalize=True)
    
def janela_pedido():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('pizza peperone',key='pizza1'),sg.Checkbox('pizza frango',key='pizza2')],
        [sg.Button('Voltar'),sg.Button('Concluir')]
    ]
    return sg.Window('Montar pedido', layout=layout,finalize=True)

def janela_bebidas():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Você deseja alguma bebida?')],
        [sg.Checkbox('Coca-Cola',key='b1')],
        [sg.Checkbox('Sprite',key='b2')],
        [sg.Checkbox('Fanta uva',key='b3'),sg.Checkbox('Fanta laranja',key='b4')],
        [sg.Checkbox('Pepsi',key='b5')],
        [sg.Button('Não quero bebida'),sg.Button('Confirmar pedido',key='confirmar1')]
    ]
    return sg.Window('Bebidas', layout=layout,finalize=True)
# Criar janelas iniciais

janela1,janela2,janela3,janela4 = janela_conf(),None,None,None

#Criar loop de leitura de eventos

while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'sair':
        sg.popup('Adeus')
        break
    if window == janela1 and event == 'entrar':
        janela2 = janela_login()
        janela1.hide()
    if window == janela2 and event == 'Continuar':
        if values['nome'] == 'cliente' and values['senha'] == '12345':
            sg.popup('Olá, cliente')  
            janela3 = janela_pedido()
            janela2.hide()
        else:
            sg.popup('Usuário e/ou senha incorreto. Tente novamente')
    if window == janela2 and event == 'voltar2':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()
        
    if window == janela3 and event == 'Concluir':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Dois pedidos realizados')
            janela3.hide
            janela4 = janela_bebidas()

        elif values['pizza1'] == True:
            sg.popup('Primeiro pedido realizado ')
            janela3.hide
            janela4 = janela_bebidas()

        elif values['pizza2'] == True:
            sg.popup('Segundo pedido realizado ')
            janela3.hide
            janela4 = janela_bebidas()            
    if window ==  janela4 and event == 'Não quero bebida':
        sg.popup('Pedido realizado. Bom apetite!')
        break
    elif window ==  janela4 and event == 'Confirmar pedido':
        sg.popup('Pedido realizado. Bom apetite!')
        break
    
        

        
        

# Logica de o que deve acontecer