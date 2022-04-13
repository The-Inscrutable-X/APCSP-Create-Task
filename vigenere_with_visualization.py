import PySimpleGUI as sg
from vigenere import generator_cipher as cipher

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Vigenere Cipher')],
            [sg.Text('Input Text'), sg.InputText(key="input")],
            [sg.Text('key'), sg.InputText(key="key")],
            [sg.Text('Encrypt or Decrypt'), sg.InputText(key="option")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
      print(values["option"])
      generator = cipher(values['key'], values['input'], values['option'])
      print(next(generator))

window.close()