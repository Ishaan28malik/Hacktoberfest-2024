from __future__ import division
 from tkinter import *

 
 
  buttons = [{'btn7':{'row':1,'col':0,'text':'7','value':'7'},'btn8':{'row':1,'col':1,'text':'8','value':'8'},
             'btn9':{'row':1,'col':2,'text':'9','value':'9'},'btnAdd':{'row':1,'col':3,'text':'+','value':'+'},
             #Second row
             'btn4':{'row':2,'col':0,'text':'4','value':'4'},'btn5':{'row':2,'col':1,'text':'5','value':'5'},
             'btn6':{'row':2,'col':2,'text':'6','value':'6'},'btnSub':{'row':2,'col':3,'text':'- ','value':'-'},
             #Third row
             'btn1':{'row':3,'col':0,'text':'1','value':'1'},'btn2':{'row':3,'col':1,'text':'2','value':'2'},
             'btn3':{'row':3,'col':2,'text':'3','value':'3'},'btnMult':{'row':3,'col':3,'text':'* ','value':'*'},
             #Fourth row
             'btn0':{'row':4,'col':0,'text':'0','value':'0'},
             'btnDiv':{'row':4,'col':2,'text':'/ ','value':'/'}
           }]

 
  class Calculator(object):

      def __init__(self,equation):
             self.equation = equation
             self.tot = self.Calc()

      def __add__(self, other):
         return Calculator(str(self.tot)+'+'+other.equation)

      def __sub__(self, other):
         return Calculator(str(self.tot)+'-'+other.equation)

      def __mul__(self,other):
         return Calculator(str(self.tot)+'*'+other.equation)

      def __div__(self,other):
         return Calculator(str(self.tot)+'/'+other.equation)

 
      def Calc(self):
         return eval(self.equation)

 
  def InputText(text):
     global operator
     global clicks

      if clicks == 0:
         operator = ""

      clicks += 1
     operator = operator + str(text)
     text_input.set(operator)

  def Clear():
     global operator
     global prevCalc
     global currentCalc
     global clicks

      prevCalc = None
     currentCalc = Calculator('0')
     clicks = 0
     operator = "0"
     text_input.set(operator)

  def Equal():
     global clicks
     global operator
     global currentCalc
     global prevCalc

      if operator[-1:] in ['+','-','*','/']:
         operator = operator[:-1]

      clicks = 0
     prevCalc = currentCalc

      if operator[:1] in ['+','-','*','/']:
         if operator[:1] == '+':
             currentCalc = prevCalc + Calculator(operator[1:])
         elif operator[:1] == '-':
             currentCalc = prevCalc - Calculator(operator[1:])
         elif operator[:1] == '*':
             currentCalc = prevCalc * Calculator(operator[1:])
         elif operator[:1] == '/':
             currentCalc = prevCalc / Calculator(operator[1:])
     else:
         currentCalc = Calculator(operator)

      operator = str(currentCalc.tot)
     text_input.set(operator)

 
 
 
  #Start GUI object
 calc = Tk()

  calc.title('Calculator Project')

  text_input = StringVar()
 operator = "0"
 text_input.set(operator)
 prevCalc = None
 clicks = 0

  currentCalc = Calculator('0')
 #Top display of calculator

  Entry(calc,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,
     bg='powder blue', justify='right').grid(columnspan=4)

  for btn, value in buttons[0].items():
     Button(calc,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text=value['text'],
         bg='powder blue', command=lambda val=value['value']:InputText(val)).grid(row=value['row'],column=value['col'])

  Button(calc,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
             text='=',bg='powder blue',command=lambda:Equal()).grid(row=4,column=3)

  Button(calc,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
             text='C',bg='powder blue',command=lambda:Clear()).grid(row=4,column=1)

 
  calc.mainloop()
