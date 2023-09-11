import stack
from customtkinter import StringVar

class Compute():
    def __init__(self):
        self.displayValue = StringVar(value="0")
        self.operatorStack = stack.Stack()
        self.numberStack = stack.Stack()
        self.newNumFlag = False

    def setNum(self, num: str):
        if self.displayValue.get() == "0" and num == '0':
            return
        elif self.displayValue.get() == "0" or self.displayValue.get() == 'Error' or self.newNumFlag:
            self.newNumFlag = False
            self.displayValue.set(num)
        else:
            self.displayValue.set(self.displayValue.get() + num)

    def setOperator(self, op: str):
        if self.operatorStack.isEmpty():
            self.numberStack.push(float(self.displayValue.get()))
            self.operatorStack.push(op)
            self.newNumFlag = True
        else:
            if not self.numberStack.isEmpty():
                num1 = self.numberStack.pop()
                num2 = float(self.displayValue.get())
                previous_op = self.operatorStack.pop()

                match previous_op:
                    case '+':
                        result = num1 + num2
                        
                    case '-':
                        result = num1 - num2

                    case 'x':
                        result = num1 * num2

                    case '÷':
                        if num2 == 0:
                            self.displayValue.set('Error')
                            return
                        else:
                            result = num1 / num2

                if op == ' ':
                    self.operatorStack.clearAll()
                else:
                    self.operatorStack.push(op)    

                self.numberStack.push(result)
                self.displayValue.set(str(result))
                self.newNumFlag = True

    def buttonPressed(self, id: str):
        match id:
            case '+' | '-' | 'x' | '÷':
                if self.displayValue.get() == 'Error':
                    self.displayValue.set(value='0')
                self.setOperator(id)
        
            case '=':
                if not self.operatorStack.isEmpty():
                    self.setOperator(' ')

            case 'AC':
                self.displayValue.set("0")
                self.operatorStack.clearAll()
                self.numberStack.clearAll()

            case 'C':
                self.displayValue.set("0")

            case '.':
                if self.displayValue.get().find('.') == -1:
                    self.displayValue.set(self.displayValue.get() + '.')

            case '%':
                if self.displayValue.get() != '0' and self.displayValue.get() != 'Error':
                    self.displayValue.set(str(float(self.displayValue.get())/100))
                else:
                    self.displayValue.set(value='0')

            case '𝒳²':
                if self.displayValue.get() != '0' and self.displayValue.get() != 'Error':
                    num = float(self.displayValue.get())
                    self.displayValue.set(str(num * num))
                else:
                    self.displayValue.set(value='0')

            case _ :
                self.setNum(id)