from tkinter import *
import parser

class Calculator:

    def __init__(self,window):

        window.title("Calculator")

        self.display = Entry(window)
        self.display.grid(row= 0, columnspan= 6, sticky= W+E)
        self.dispCounter = 0
        self.initButtons(window)

    def initButtons(self,window):

        Button(window, text="1", command= lambda: self.showDisplayNum("1")).grid(row=1, column=0)
        Button(window, text="2", command= lambda: self.showDisplayNum("2")).grid(row=1, column=1)
        Button(window, text="3", command= lambda: self.showDisplayNum("3")).grid(row=1, column=2)
        Button(window, text="+", command= lambda: self.showDisplayOp("+")).grid(row=1, column=3)
        Button(window, text="-", command= lambda: self.showDisplayOp("-")).grid(row=1, column=4)

        Button(window, text="4", command= lambda: self.showDisplayNum("4")).grid(row=2, column=0)
        Button(window, text="5", command= lambda: self.showDisplayNum("5")).grid(row=2, column=1)
        Button(window, text="6", command= lambda: self.showDisplayNum("6")).grid(row=2, column=2)
        Button(window, text="*", command= lambda: self.showDisplayOp("*")).grid(row=2, column=3)
        Button(window, text="/", command= lambda: self.showDisplayOp("//")).grid(row=2, column=4)

        Button(window, text="7", command= lambda: self.showDisplayNum("7")).grid(row=3, column=0)
        Button(window, text="8", command= lambda: self.showDisplayNum("8")).grid(row=3, column=1)
        Button(window, text="9", command= lambda: self.showDisplayNum("9")).grid(row=3, column=2)
        Button(window, text="%", command= lambda: self.showDisplayOp("%")).grid(row=3, column=3)
        Button(window, text="^", command= lambda: self.showDisplayOp("**")).grid(row=3, column=4)

        Button(window, text="AC", command= lambda: self.allClearDisplay()).grid(row=4, column=0)
        Button(window, text="0", command= lambda: self.showDisplayNum("0")).grid(row=4, column=1)
        Button(window, text="C", command= lambda: self.undoDisplay()).grid(row=4, column=2)
        Button(window, text="=", command= lambda: self.calculate()).grid(row=4, column=3, columnspan=2)


    def showDisplayNum(self, num):
        self.display.insert(self.dispCounter, num)
        self.dispCounter+= 1

    def showDisplayOp(self, op):
        opLength= len(op)
        self.display.insert(self.dispCounter, op)
        self.dispCounter+= opLength

    def allClearDisplay(self):
        self.display.delete(0,END)

    def undoDisplay(self):
        displayString = self.display.get()

        if len(displayString) > 0:
            newDisplayString = displayString[:-1]
            self.allClearDisplay()
            self.display.insert(0, newDisplayString)
        else:
            self.allClearDisplay()

    def calculate(self):
        displayString = self.display.get()

        try:
            exp = parser.expr(displayString).compile()
            resultString = eval(exp)
            self.allClearDisplay()
            self.display.insert(0,resultString)
        except Exception:
            self.allClearDisplay()
            self.display.insert(0, "Error")

root = Tk()

calc = Calculator(root)

root.mainloop()