 import PySimpleGUI as sg
from vigenere import generator_cipher as cipher
import time
import turtle
import tkinter as tk
#from PIL import Image, ImageTk

# config recta visualization size
filename = 'recta.png'
size = (500, 500)

# function for moving turtles
def intersection(canvas, block_size, input_position, key_position):
  turtle1 = turtle.RawTurtle(canvas, visible=False)
  turtle1.penup()
  turtle1.speed(5)
  turtle1.goto(3*block_size/2+block_size*input_position-size[0]/2, -block_size+size[1]/2)
  turtle1.st()
  turtle1.color('red')
  turtle1.setheading(-90)
  turtle1.forward(block_size*key_position)
  

  turtle2 = turtle.RawTurtle(canvas, visible=False)
  turtle2.penup()
  turtle2.speed(5)
  turtle2.goto(+block_size-size[1]/2, -3*block_size/2-block_size*key_position+size[0]/2)
  turtle2.st()
  turtle2.color('red')
  turtle2.setheading(0)
  turtle2.forward(block_size*input_position)
  return turtle1, turtle2
  


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Vigenere Cipher')],
            [sg.Canvas(size=size, key='-canvas-')], 
            [sg.Text('Output', key = 'output')],
            [sg.Text('Input Text'), sg.InputText(key="input")],
            [sg.Text('key'), sg.InputText(key="key")],
            [sg.Text('Encrypt or Decrypt'), sg.InputText(key="option")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout, finalize=True)


# create the canvas for visualization
canvas = window['-canvas-'].TKCanvas
screen = turtle.TurtleScreen(canvas)
screen.bgpic('500recta.png')
#recta = tk.PhotoImage(file='500recta.png')

#canvas.create_image(size[0], size[1], image=recta, anchor=tk.SE)
# Event Loop to process "events" and get the "values" of the inputs
count = 0
generator = 'none'
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
      break
      
    if event == 'Ok':
      generator = cipher(values['key'], values['input'], values['option'])

      output = ''
      for i in generator:
        print(i)
        window['output'].update(i)
        t1, t2 = intersection(screen, 18.5, i[1][0], i[1][1])
        #canvas.create_image(size[0], size[1], image=recta, anchor=tk.CENTER)
        time.sleep(.1)
        t1.ht()
        t2.ht()
        window.refresh()
        output += i[0]
        #(output_letter_alphabet, 
           # [alphabet_position, 
           #  shifts_due_to_key, 
           #  final_alphabet_position,
           #  e_or_d])
        
      else:
        window['output'].update('Converted string='+output)
        window.refresh()

window.close()