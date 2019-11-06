#!/usr/bin/env python3

import operator
import readline
import tkinter as tk

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def foo(bar):
    return


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()
numlist = ''

def main():
    
    
    def addin(num):
        global numlist
        numlist+=num
   
    root = tk.Tk()
    root.title("rpn calculator")
    total1 = tk.StringVar()  
    final= tk.IntVar()
    def update(event):
        total1.set(numlist)
    def calc(event):
        final.set(calculate(numlist))
    
    root.bind_all("<ButtonRelease>", update)
    root.bindtags(('Entry', 'all'))
 
    
    button1 = tk.Button(root, text='1', command=lambda: addin(str(1))) 
    button1.grid(row=3,column=1)
    button2 = tk.Button(root, text='2', command=lambda: addin(str(2)))
    button2.grid(row=3,column=2)
    button3 = tk.Button(root, text='3', command=lambda: addin(str(3)))
    button3.grid(row=3,column=3)
    button4 = tk.Button(root, text='4', command=lambda: addin(str(4)))
    button4.grid(row=2,column=1)
    button5 = tk.Button(root, text='5', command=lambda: addin(str(5)))
    button5.grid(row=2,column=2)
    button6 = tk.Button(root, text='6', command=lambda: addin(str(6)))
    button6.grid(row=2,column=3)
    button7 = tk.Button(root, text='7', command=lambda: addin(str(7)))
    button7.grid(row=1,column=1)
    button8 = tk.Button(root, text='8', command=lambda: addin(str(8)))
    button8.grid(row=1,column=2)
    button9 = tk.Button(root, text='9', command=lambda: addin(str(9)))
    button9.grid(row=1,column=3)
    
    buttonadd = tk.Button(root, text='+', command=lambda: addin('+'))
    buttonadd.grid(row=1,column=4)
    buttonsub = tk.Button(root, text='-', command=lambda: addin('-'))
    buttonsub.grid(row=2,column=4)
    buttonmut = tk.Button(root, text='*', command=lambda: addin('*'))
    buttonmut.grid(row=3,column=4)
    buttondiv = tk.Button(root, text='/', command=lambda: addin('/'))
    buttondiv.grid(row=4,column=4)
    buttonpow = tk.Button(root, text='^', command=lambda: addin('^'))
    buttonpow.grid(row=5,column=4)

    buttonspa = tk.Button(root, text='space', command=lambda: addin(' '))
    buttonspa.grid(row=6,column=4)

    eq = tk.Button(root, text='=')
    eq.grid(row=7,column=3)
    eq.bind("<ButtonRelease>",calc)
    def empty():
        global numlist
        numlist = ""
    clear = tk.Button(root, text='c', command=empty)
    clear.grid(row=7,column=4)



    test = tk.Label(root, textvariable=total1)
    test.grid(row=8)
    total = tk.Label(root, textvariable=final)
    total.grid(row=9)
   
    root.mainloop()
   




if __name__ == '__main__':
    main()
