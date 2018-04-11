#TP4
#Ariq Naufal Satria
#1706027414

from tkinter import *
import math
from idlelib.tooltip import *

class kalkulator :
    def __init__(self) :
        #init window, init frame
        win = Tk()
        win.title("Boi SuperCalc by Ariq Naufal ")
        frame = Frame(win)
        frame.pack()

        #Making Attributes for the operation later on
        self.memory = ''
        self.expr = ''
        self.startOfNextOperand = True
        self.afterOperator = False

        #Making the Entry box
        self.entry = Entry(frame,relief = RIDGE, borderwidth = 3,bg = 'Black',fg = '#FFFF4E',
                           width = 36, font = 'None 18',justify = RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 5,)

        #Making list for buttons and tooltips
        buttons = [['Clr',  'MC',   'M+',   'M-',   'MR'],
                   ['d',    'e',    'f',    '+',    '-'],
                   ['a',    'b',    'c',    '/',    '*'],
                   ['7',    '8',    '9',    '**',   '\u221A'],
                   ['4',    '5',    '6',    'sin',  'cos'],
                   ['1',    '2',    '3',    'tan',  'ln'],
                   ['0',    '.',    '+-',   '~',    '2C'],
                   ['x',    'o',    '^',    '|',    '&'],
                   ['\u03C0',    'int',  'rad',  '//',   'exp'],
                   ['bin',  'hex',  'oct',  '%',    '=']]

        ToolTips = [['Clear', 'Memory Clear', 'Memory Add', 'Memory Subtract', 'Memory Recall'	     ],
		    ['Letter d', 'Letter e/Euler Number', 'Letter f', 'Add', 'Subtract'		     ],
		    ['Letter a', 'Letter b', 'Letter c', 'Float Divide', 'Multiply'		     ],
		    ['Seven', 'Eight', 'Nine', 'Power by n', 'Square Root'			    ],
		    ['Four', 'Five', 'Six', 'sine(deg)', 'cos(deg)'				    ],
		    ['One', 'Two', 'Three', 'tan(deg)', 'natural log'				 ],
		    ['Zero', 'Decimal point', 'Toggle +- sign', 'Bitwise complement', "32bit 2's Complement"],
		    ['Letter x', 'Letter o', 'Bitwise XOR', 'Bitwise OR', 'Bitwise AND' ],
		    ['Pi', 'Change to Integer', 'Change to radians', 'Integer divide', 'Power of E' ],
		    ['Change to binary', 'Change to hexadecimal', 'Change to octal', 'Modulo', 'Compute to decimal']]

        for i in range(10) :
            for j in range(5) :

                def cmd (x = buttons[i][j]) :
                    self.click(x)
                
                if buttons[i][j] in '1234567890' :
                    b = Button(frame, text = buttons[i][j], width = 6,relie = GROOVE,
                         bg = '#FA9C19', fg = 'white', font = 'None 18', command = cmd)
                    b.grid (row = i+1, column = j)
                
                elif buttons[i][j] in 'Clr' :
                    b = Button(frame, text = buttons[i][j], width = 6,relie = GROOVE,
                         bg = '#AE001F', fg = 'white', font = 'None 18', command = cmd)
                    b.grid (row = i+1, column = j)

                else :
                    b = Button(frame, text = buttons[i][j], width = 6,relie = GROOVE,
                         bg = '#FAC019', fg = 'white', font = 'None 18', command = cmd)
                    b.grid (row = i+1, column = j)

                ToolTip(b,ToolTips[i][j])

        win.mainloop()

    def click(self, key):
        e = math.e

        #Function to display Error text 
        def Error ():
            self.entry.delete(0,END)
            self.entry.insert(END, 'ERROR')
            self.startOfNextOperand = True

        #A Function to display the res/result to the entry box
        #oh and also as a sign of a new operand
        def Input(res) :
            self.entry.delete(0,END)
            self.entry.insert(END, res)
            self.expr = ''
            self.startOfNextOperand = True
            
        #Display the result in box with help of eval
        if key == '=' :
            try :
                result = eval(self.expr + self.entry.get())
                Input(result)
            except :
                Error()

        #Append the number to expr attributes along with the operator inputted
        elif key in '+**-//%&^|' :
            #this part is tricky, when the last one in self.expr is operator,
            #and you press another operator, the last one will be overwrite with the new operator
            #sel.afterOperator is a boolean that tell you whether the last one is operator or not
            if not self.afterOperator :
                self.expr += self.entry.get()
                self.expr += key
                self.afterOperator = True
            else :
                if self.expr[-1:-3:-1] == "**" :
                    self.expr = self.expr.replace(self.expr[-1:-3:-1],key)
                else :
                    self.expr = self.expr.replace(self.expr[-1],key)

            self.startOfNextOperand = True
    
        #Change the number to - or +
        elif key == '+-' :
            try :
                if self.entry.get()[0] == '-' :
                    self.entry.delete(0)
                elif self.entry.get()[0] == '0' : #handling so -0 didnt appear he he he
                    pass
                else :
                    self.entry.insert(0,'-')

            except :
                pass

        #Clear entry box 
        elif key == 'Clr' :
            self.expr = ''
            self.entry.delete(0,END)

        #Sqrt operation
        elif key == '\u221A' : #Sqrt
            try :
                result = math.sqrt(eval(self.expr + self.entry.get()))
                Input(result)
            except :
                Error()

        #Display pi value, treat it like number
        elif key == '\u03C0' : #Pi
            try :
                self.entry.delete(0,END)
                self.entry.insert(END, math.pi)
                self.startOfNextOperand = True
                
            except :
                Error()

        #operation with sine,cos,tangen in degree
        elif key == 'sin' or key == 'cos' or key =='tan'  :
            try :
                result = str(math.radians(eval(self.expr + self.entry.get())))
                result = eval('math.{}'.format(key)+'('+result+')')

                Input(result)
            except :
                Error()

        #operation with natural log
        elif key == 'ln' :
            try :
                result = math.log(eval(self.entry.get()))
                Input(result)
            except :
                Error()

        #Bitwise complement
        elif key == '~' :
            try :
                result = eval('~{}'.format(self.entry.get()))
                Input(result)
            except :
                Error()
            self.startOfNextOperand = True

        #two's Complement but in 32digit binary
        elif key == '2C' :
            try :
                number = self.entry.get()
                if number[0] == '-' :
                    number = number[1:] #Deleting negative sign
                    result = format(2**32 - (eval(number)), '#032b')
                    Input(result)
                else :
                    result = format(eval(number),'#032b')
                    Input(result)
            except :
                Error() 

        #Make the number integer
        elif key == 'int' :
            try :
                result = eval(self.expr+self.entry.get())
                Input(result)
            except :
                Error()

        #Change to radians
        elif key == 'rad' :
            try :
                result = math.radians(eval(self.expr+self.entry.get()))
                Input(result)
            except :
                Error()

        
        elif key == 'exp' : #Power of E (euler number)
            try :
                result = math.exp(eval(self.expr+self.entry.get()))
            except :
                Error()
        
        #Change the number to binary, hexadecimal, or octadecimal
        elif key == 'bin' or key == 'hex' or key =='oct' :
            try :
                if key == 'bin' :
                    result = bin(eval(self.expr + self.entry.get()))
                if key == 'hex' :
                    result = hex(eval(self.expr + self.entry.get()))
                if key == 'oct' :
                    result = oct(eval(self.expr + self.entry.get()))

                Input(result)
            except :
                Error()

        #Input '.' dot if there is no '.' before
        elif key == '.' :
                if '.' not in self.entry.get() :
                    self.entry.insert(END,'.')

        #Memory Clear, Memory append (+/-) and Memory Recall
        elif key == 'MC' or key == 'M+' or key == "M-" or key =='MR' :
            try :
                if key == 'MC' :
                    self.memory = ''
                elif key == 'M+' or key == 'M-' :
                    self.memory += key[1]
                    self.memory += self.entry.get()

                elif key == 'MR' :
                    self.entry.delete(0,END)
                    self.entry.insert(END,eval(self.memory))
            except :
                Error()

            self.startOfNextOperand = True
                                 

        else  :
            # Insert digits or alphabet at the end of entry
            # or insert in first entry if starting next Operand
            # This part also tells you that the last one inputted wasnt operator but Operand
                if self.startOfNextOperand :
                    self.entry.delete(0,END)
                    self.startOfNextOperand = False

                self.entry.insert(END, key)
                self.afterOperator = False


#start the program 
if __name__ == '__main__' :
    kalkulator()