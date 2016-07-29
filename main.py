import operator
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty

class CalculatorApp(App):
    def build(self):
        return Calculator(size=Window.size)

class Calculator(Widget):
    display_str=StringProperty('0')
    
    def number_pressed(self, val):
        if self.display_str != '0':
            self.display_str+=str(val)
        else:
            self.display_str=str(val)
            
    def operator_pressed(self,operator):
        ops = ['-','+','*','/']
        if self.display_str[-1] not in ops:
            for i in ops:
                if i in self.display_str:
                    self.evaluate_expression()
                    break
            self.display_str+=operator
        else:
            self.display_str=self.display_str[:-1]
            self.display_str+=val
            
    def evaluate_expression(self):
        ops = {'-':operator.sub,'+':operator.add,'*':operator.mul,'/':operator.truediv}
        for i in ops.keys():
            if i in self.display_str:
                val1, val2 = self.display_str.split(i)
                ans = ops[i](float(val1),float(val2))
                self.display_str=str(ans)
        
    def clear(self):
        self.display_str='0'
    
CalculatorApp().run()
