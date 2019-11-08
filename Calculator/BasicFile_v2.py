#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:48:41 2019

@author: Anna
"""
from tkinter import *
from tkinter import Tk, Label, Button



class GuiApp(object):
   
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("My Calculator")
        
        # use Frame to set size of window. Frame groups together widgets.
        self.frame = Frame(master = self.root, height = 600, width = 400)
        self.frame.pack_propagate(0) # don't shrink
        
        self.count = 0
        self.input_1 = ""
        self.input_2 = ""
        
        self.result_label = Label(master=self.frame, text = "",
                                  font=("Times", 70))
        
       
        self.result_label.pack()
        self.result_label.place(x=0, y=10)
        
        
        self.operator_funct = ""
        self.operation_used = 0
        #self.label.pack(side = "top") # add the label into the root window
        
        # Entry widget
        
        #self.entry = Entry(master = self.frame)
        #self.entry.place(height=50, width=400, x=0, y=0)
        
        
        # where the buttons go
        
        # AC - clear
        self.button_AC = Button(master = self.frame, text = "AC", 
                             command = self.button_clicked_clear)
        self.button_AC.pack(side = "top")
        self.button_AC.pack()
        self.button_AC.place(height=100, width=100, y=100)
        
        # Addition and Subtraction
        self.button_PlusMinus = Button(master = self.frame, text = "+/-", 
                             command = self.button_clicked_neg)
        self.button_PlusMinus.pack(side = "top")
        self.button_PlusMinus.pack()
        self.button_PlusMinus.place(height=100, width=100, y=100, x=100)
        
        # Percent
        self.button_Percent = Button(master = self.frame, text = "%", 
                             command = self.button_clicked)
        self.button_Percent.pack(side = "top")
        self.button_Percent.pack()
        self.button_Percent.place(height=100, width=100, y=100, x=200)
        
        # Division
        self.button_Div = Button(master = self.frame, text = "/", 
                             command = self.button_clicked_div)
        self.button_Div.pack(side = "top")
        self.button_Div.pack()
        self.button_Div.place(height=100, width=100, y=100, x=300)
        
        # 7
        self.button_7 = Button(master = self.frame, text = "7", 
                             command = self.button_clicked_7)
        self.button_7.pack(side = "top")
        self.button_7.pack()
        self.button_7.place(height=100, width=100, y=200)
        
        # 8
        self.button_8 = Button(master = self.frame, text = "8", 
                             command = self.button_clicked_8)
        self.button_8.pack(side = "top")
        self.button_8.pack()
        self.button_8.place(height=100, width=100, y=200, x=100)
        
        # 9
        self.button_9 = Button(master = self.frame, text = "9", 
                             command = self.button_clicked_9)
        self.button_9.pack(side = "top")
        self.button_9.pack()
        self.button_9.place(height=100, width=100, y=200, x=200)
        
        # Mult
        self.button_Mult = Button(master = self.frame, text = "×", 
                             command = self.button_clicked_mult)
        self.button_Mult.pack(side = "top")
        self.button_Mult.pack()
        self.button_Mult.place(height=100, width=100, y=200, x=300)
        
        # 4
        self.button_4 = Button(master = self.frame, text = "4", 
                             command = self.button_clicked_4)
        self.button_4.pack(side = "top")
        self.button_4.pack()
        self.button_4.place(height=100, width=100, y=300)
        
        # 5
        self.button_5 = Button(master = self.frame, text = "5", 
                             command = self.button_clicked_5)
        self.button_5.pack(side = "top")
        self.button_5.pack()
        self.button_5.place(height=100, width=100, y=300, x=100)
        
        # 6
        self.button_6 = Button(master = self.frame, text = "6", 
                             command = self.button_clicked_6)
        self.button_6.pack(side = "top")
        self.button_6.pack()
        self.button_6.place(height=100, width=100, y=300, x=200)
        
        # Minus
        self.button_Minus = Button(master = self.frame, text = "-", 
                             command = self.button_clicked_minus)
        self.button_Minus.pack(side = "top")
        self.button_Minus.pack()
        self.button_Minus.place(height=100, width=100, y=300, x=300)
        
        # 1
        self.button_1 = Button(master = self.frame, text = "1", 
                             command = self.button_clicked_1)
        self.button_1.pack(side = "top")
        self.button_1.pack()
        self.button_1.place(height=100, width=100, y=400)
        
        # 2
        self.button_2 = Button(master = self.frame, text = "2", 
                             command = self.button_clicked_2)
        self.button_2.pack(side = "top")
        self.button_2.pack()
        self.button_2.place(height=100, width=100, y=400, x=100)
        
        # 3
        self.button_3 = Button(master = self.frame, text = "3", 
                             command = self.button_clicked_3)
        self.button_3.pack(side = "top")
        self.button_3.pack()
        self.button_3.place(height=100, width=100, y=400, x=200)
        
        # Plus
        self.button_Plus = Button(master = self.frame, text = "+", 
                             command = self.button_clicked_plus)
        self.button_Plus.pack(side = "top")
        self.button_Plus.pack()
        self.button_Plus.place(height=100, width=100, y=400, x=300)
        
         # 0
        self.button_0 = Button(master = self.frame, text = "0", 
                             command = self.button_clicked_0)
        self.button_0.pack(side = "top")
        self.button_0.pack()
        self.button_0.place(height=100, width=200, y=500)
        
        # .
        self.button_Dot = Button(master = self.frame, text = ".", 
                             command = self.button_clicked_Dot)
        self.button_Dot.pack(side = "top")
        self.button_Dot.pack()
        self.button_Dot.place(height=100, width=100, y=500, x=200)
        
        # =
        self.button_Equals = Button(master = self.frame, text = "=", 
                             command = self.button_clicked_equals)
        self.button_Equals.pack(side = "top")
        self.button_Equals.pack()
        self.button_Equals.place(height=100, width=100, y=500, x=300)
        
                 
    
        self.frame.pack()
        
        self.result = ""
             
    # functions at the bottom/lastr
    #def button_clicked_equals(self):
        #self.result_label["text"] = "calculation tbd"
        #self.result_label.configure(text = str(self.entry.get()))
    
    def button_clicked_clear(self):
        self.input_1 = ""
        self.input_2 = ""
        self.operation_used = 0
        self.result_label["text"] = ""
        
    
    
    def button_clicked_neg(self):
        if self.operation_used == 0:
            self.input_1 = str(float(self.input_1)*(-1))
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 = str(float(self.input_2)*(-1))
            self.result_label["text"] = self.input_2
            
    
    def button_clicked_Dot(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "."
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "."
            self.result_label["text"] = self.input_2
    
    def button_clicked_1(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "1"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "1"
            self.result_label["text"] = self.input_2
        
    def button_clicked_2(self):
        if self.operation_used == 0:
            self.input_2 = self.input_2 + "2"
            self.result_label["text"] = self.input_2
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "2"
            self.result_label["text"] = self.input_2
            
    def button_clicked_3(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "3"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "3"
            self.result_label["text"] = self.input_2
    
    def button_clicked_4(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "4"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "4"
            self.result_label["text"] = self.input_2
            
    def button_clicked_5(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "5"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "5"
            self.result_label["text"] = self.input_2
            
    def button_clicked_6(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "6"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "6"
            self.result_label["text"] = self.input_2
            
    def button_clicked_7(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "7"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "7"
            self.result_label["text"] = self.input_2
            
    def button_clicked_8(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "8"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "8"
            self.result_label["text"] = self.input_2
            
    def button_clicked_9(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "9"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "9"
            self.result_label["text"] = self.input_2
            
    def button_clicked_0(self):
        if self.operation_used == 0:
            self.input_1 = self.input_1 + "0"
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = self.input_2 + "0"
            self.result_label["text"] = self.input_2
        
        
    def button_clicked_equals(self):
       
        self.input_1_f = float(self.input_1)
        self.input_2_f = float(self.input_2)

        
        if self.operator_funct == "+":
            self.result = str(self.input_1_f + self.input_2_f)
        if self.operator_funct == "-":
            self.result = str(self.input_1_f - self.input_2_f)
        if self.operator_funct == "×":
            self.result = str((self.input_1_f) * (self.input_2_f))
        if self.operator_funct == "÷":
            self.result = str(self.input_1_f / self.input_2_f)  
        self.result_label["text"] = self.result
        
        
        self.input_1 = self.result
        self.input_2 = ""
        self.operation_used = 0
        
    
    def button_clicked_plus(self):
        self.result_label["text"] = "+"  
        self.operator_funct = "+"
        self.operation_used = 1
    
    def button_clicked_minus(self):
        self.result_label["text"] = "-"  
        self.operator_funct = "-"
        self.operation_used = 1
    
    def button_clicked_mult(self):
        self.result_label["text"] = "×"  
        self.operator_funct = "×"
        self.operation_used = 1
    
    def button_clicked_div(self):
        self.result_label["text"] = "÷"  
        self.operator_funct = "÷"
        self.operation_used = 1
    
    
    
    def show_entry_fields(self):
        print(self.entry.get())

    def run(self):
        self.root.mainloop()


    def button_clicked(self):
        self.count += 1
        self.result_label["text"] = str(self.count)
            
myApp = GuiApp()
myApp.run()



        
