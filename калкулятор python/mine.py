from tkinter import *
from math import *
import math 

root = Tk()
root.geometry("310x400")
root.title("Calculator")
root.config(background="lightgray")

expression = ""

result = StringVar()
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=3, ipadx=70)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.set("error")
        expression = ""

def converter():
    actual_coin = list_of_coins.get(list_of_coins.curselection())
    umn = 1
    if actual_coin == "Rub to Dollar":
        umn = 0.017
    elif actual_coin == "Dollar to Rub":
        umn = 60.58
    elif actual_coin == "Rub to Euro":
        umn = 0.016
    else:
        umn = 62.56
    global expression
    total = str(eval(expression) * umn)
    result.set(total)
    expression = total

def sqrt_exp():
        global expression
        total = str(math.sqrt(eval(expression)))
        result.set(total)
        expression = total
def sqr_exp():
        global expression
        total = str(eval(expression) * eval(expression))
        result.set(total)
        expression = total
def sin_exp():
        global expression
        total = str(math.sin(math.radians(eval(expression))))
        result.set(total)
        expression = total
def cos_exp():
        global expression
        total = str(math.cos(math.radians(eval(expression))))
        result.set(total)
        expression = total
def asin_exp():
        global expression
        total = str(math.degrees(math.asin(eval(expression))))
        result.set(total)
        expression = total
def acos_exp():
        global expression
        total = str(math.degrees(math.acos(eval(expression))))
        result.set(total)
        expression = total

def reset():
    global expression
    total = ""
    result.set(total)
    expression = total

button1 = Button(text=1,height=1,width=8, command=lambda: press_num(1))
button1.grid(row=2,column=0)

button2 = Button(text=2,height=1,width=8, command=lambda: press_num(2))
button2.grid(row=2,column=1)

button3 = Button(text=3,height=1,width=8, command=lambda: press_num(3))
button3.grid(row=2,column=2)

button4 = Button(text=4,height=1,width=8, command=lambda: press_num(4))
button4.grid(row=3,column=0)

button5 = Button(text=5,height=1,width=8, command=lambda: press_num(5))
button5.grid(row=3,column=1)

button6 = Button(text=6,height=1,width=8, command=lambda: press_num(6))
button6.grid(row=3,column=2)

button7 = Button(text=7,height=1,width=8, command=lambda: press_num(7))
button7.grid(row=4,column=0)

button8 = Button(text=8,height=1,width=8, command=lambda: press_num(8))
button8.grid(row=4,column=1)

button9 = Button(text=9,height=1,width=8, command=lambda: press_num(9))
button9.grid(row=4,column=2)

plus = Button(text="+",height=1,width=8, command=lambda: press_num("+"))
plus.grid(row=5,column=0)

button0 = Button(text=0,height=1,width=8, command=lambda: press_num(0))
button0.grid(row=5,column=1)

minus = Button(text="-",height=1,width=8, command=lambda: press_num("-"))
minus.grid(row=5,column=2)

equal = Button(text="=",height=1,width=8, command=equalpress)
equal.grid(row=7,column=1)

mult = Button(text="*",height=1,width=8, command=lambda: press_num("*"))
mult.grid(row=6,column=0)

divi = Button(text="/",height=1,width=8, command=lambda: press_num("/"))
divi.grid(row=6,column=2)

coins = ["Rub to Dollar", "Dollar to Rub", "Rub to Euro", "Euro to Rub"]
list_of_coins = Listbox(width=10, height=5)
list_of_coins.grid(row=8,column=0)

for coin in coins:
    list_of_coins.insert(0, coin)

convert = Button(text="convert",height=1,width=8, command=converter)
convert.grid(row=8,column=1)

sqrt = Button(text="√",height=1,width=8, command=sqrt_exp)
sqrt.grid(row=7,column=0)

sqr = Button(text="х²",height=1,width=8, command=sqr_exp)
sqr.grid(row=7,column=2)

reset = Button(text="RESET",height=1,width=8, command=reset)
reset.grid(row=8,column=2)

point = Button(text=".",height=1,width=8, command=lambda: press_num("."))
point.grid(row=6,column=1)

sin = Button(text="sin",height=1,width=8, command=sin_exp)
sin.grid(row=9,column=1)

cos = Button(text="cos",height=1,width=8, command=cos_exp)
cos.grid(row=9,column=0)

asin = Button(text="arcsin",height=1,width=8, command=asin_exp)
asin.grid(row=10,column=1)

acos = Button(text="arccos",height=1,width=8, command=acos_exp)
acos.grid(row=10,column=0)

root.mainloop()