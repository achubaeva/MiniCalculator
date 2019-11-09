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
        self.root.configure(background='black')

        # variables declaration
        self.count = 0
        self.input_1 = ""
        self.input_2 = ""
        
        font_type = "SF Compact"
        bg_color = '#505050'
        font_color = "white"
        
        top_color = "black"
        ops_color = "#FF9500"
        
        # use Frame to set size of window. Frame groups together widgets.
        self.frame = Frame(master = self.root, height = 300, width = 200, background = bg_color)
        self.frame.pack_propagate(0) # don't shrink
        
        self.result_label = Label(master=self.frame, text = "0",
                                  font=(font_type, 30), bg = bg_color, fg = font_color)
        
        self.result_label.pack()
        self.result_label.place(x=12, y=5)
            
        self.operator_funct = ""
        self.operation_used = 0

        
        button_font_size = 20
        
        # AC - clear
        self.button_AC = Button(master = self.frame,text = "AC", font=(font_type, button_font_size), highlightbackground = top_color, fg = font_color,
                                command = self.button_clicked_clear, highlightthickness = 0)
        self.button_AC.pack(side = "top")
        self.button_AC.pack()
        self.button_AC.place(height=50, width=50, y=50)
        
        # Addition and Subtraction
        self.button_PlusMinus = Button(master = self.frame, text = "+/-", font=(font_type, button_font_size), highlightbackground = top_color, fg = font_color,
                             command = self.button_clicked_neg, highlightthickness = 0)
        self.button_PlusMinus.pack(side = "top")
        self.button_PlusMinus.pack()
        self.button_PlusMinus.place(height=50, width=50, y=50, x=50)
        
        # Percent
        self.button_Percent = Button(master = self.frame, text = "%", font=(font_type, button_font_size), highlightbackground = top_color, fg = font_color,
                             command = self.button_clicked_percent, highlightthickness = 0)
        self.button_Percent.pack(side = "top")
        self.button_Percent.pack()
        self.button_Percent.place(height=50, width=50, y=50, x=100)
        
        # Division
        self.button_Div = Button(master = self.frame, text = "÷", font=(font_type, button_font_size), highlightbackground = ops_color, fg = font_color,
                             command = self.button_clicked_div, highlightthickness = 0)
        self.button_Div.pack(side = "top")
        self.button_Div.pack()
        self.button_Div.place(height=50, width=50, y=50, x=150)
        
        # 7
        self.button_7 = Button(master = self.frame, text = "7", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_7, highlightthickness = 0)
        self.button_7.pack(side = "top")
        self.button_7.pack()
        self.button_7.place(height=50, width=50, y=100)
        
        # 8
        self.button_8 = Button(master = self.frame, text = "8", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_8, highlightthickness = 0)
        self.button_8.pack(side = "top")
        self.button_8.pack()
        self.button_8.place(height=50, width=50, y=100, x=50)
        
        # 9
        self.button_9 = Button(master = self.frame, text = "9", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_9, highlightthickness = 0)
        self.button_9.pack(side = "top")
        self.button_9.pack()
        self.button_9.place(height=50, width=50, y=100, x=100)
        
        # Mult
        self.button_Mult = Button(master = self.frame, text = "×", font=(font_type, button_font_size), highlightbackground = ops_color, fg = font_color,
                             command = self.button_clicked_mult, highlightthickness = 0)
        self.button_Mult.pack(side = "top")
        self.button_Mult.pack()
        self.button_Mult.place(height=50, width=50, y=100, x=150)
        
        # 4
        self.button_4 = Button(master = self.frame, text = "4", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_4, highlightthickness = 0)
        self.button_4.pack(side = "top")
        self.button_4.pack()
        self.button_4.place(height=50, width=50, y=150)
        
        # 5
        self.button_5 = Button(master = self.frame, text = "5", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_5, highlightthickness = 0)
        self.button_5.pack(side = "top")
        self.button_5.pack()
        self.button_5.place(height=50, width=50, y=150, x=50)
        
        # 6
        self.button_6 = Button(master = self.frame, text = "6", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_6, highlightthickness = 0)
        self.button_6.pack(side = "top")
        self.button_6.pack()
        self.button_6.place(height=50, width=50, y=150, x=100)
        
        # Minus
        self.button_Minus = Button(master = self.frame, text = "-", font=(font_type, button_font_size), highlightbackground = ops_color, fg = font_color,
                             command = self.button_clicked_minus, highlightthickness = 0)
        self.button_Minus.pack(side = "top")
        self.button_Minus.pack()
        self.button_Minus.place(height=50, width=50, y=150, x=150)
        
        # 1
        self.button_1 = Button(master = self.frame, text = "1", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_1, highlightthickness = 0)
        self.button_1.pack(side = "top")
        self.button_1.pack()
        self.button_1.place(height=50, width=50, y=200)
        
        # 2
        self.button_2 = Button(master = self.frame, text = "2", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_2, highlightthickness = 0)
        self.button_2.pack(side = "top")
        self.button_2.pack()
        self.button_2.place(height=50, width=50, y=200, x=50)
        
        # 3
        self.button_3 = Button(master = self.frame, text = "3", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_3, highlightthickness = 0)
        self.button_3.pack(side = "top")
        self.button_3.pack()
        self.button_3.place(height=50, width=50, y=200, x=100)
        
        # Plus
        self.button_Plus = Button(master = self.frame, text = "+", font=(font_type, button_font_size), highlightbackground = ops_color, fg = font_color,
                             command = self.button_clicked_plus, highlightthickness = 0)
        self.button_Plus.pack(side = "top")
        self.button_Plus.pack()
        self.button_Plus.place(height=50, width=50, y=200, x=150)
        
         # 0
        self.button_0 = Button(master = self.frame, text = "0", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_0, highlightthickness = 0)
        self.button_0.pack(side = "top")
        self.button_0.pack()
        self.button_0.place(height=50, width=100, y=250)
        
        # .
        self.button_Dot = Button(master = self.frame, text = ".", font=(font_type, button_font_size), highlightbackground = bg_color, fg = font_color,
                             command = self.button_clicked_Dot, highlightthickness = 0)
        self.button_Dot.pack(side = "top")
        self.button_Dot.pack()
        self.button_Dot.place(height=50, width=50, y=250, x=100)
        
        # =
        self.button_Equals = Button(master = self.frame, text = "=", font=(font_type, button_font_size), highlightbackground = ops_color, fg = font_color,
                             command = self.button_clicked_equals, highlightthickness = 0)
        self.button_Equals.pack(side = "top")
        self.button_Equals.pack()
        self.button_Equals.place(height=50, width=50, y=250, x=150)

        self.frame.pack()     
    
    def button_clicked_clear(self):
        self.input_1 = ""
        self.input_2 = ""
        self.operation_used = 0
        self.result_label["text"] = "0"
        
    def button_clicked_percent(self):
         if self.operation_used == 0:
            self.input_1 = str(float(self.input_1)/(100))
            self.result_label["text"] = self.input_1
         if self.operation_used == 1:
            self.input_2 = str(float(self.input_2)/(100))
            self.result_label["text"] = self.input_2
        
    def button_clicked_neg(self):
        if self.operation_used == 0:
            self.input_1 = str(float(self.input_1)*(-1))
            self.result_label["text"] = self.input_1
        if self.operation_used == 1:
            self.input_2 = str(float(self.input_2)*(-1))
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
            self.input_1 = self.input_1 + "2"
            self.result_label["text"] = self.input_1
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
            self.result = self.input_1_f + self.input_2_f
        if self.operator_funct == "-":
            self.result = self.input_1_f - self.input_2_f
        if self.operator_funct == "×":
            self.result = (self.input_1_f) * (self.input_2_f)
        if ((self.operator_funct == "÷") and (self.input_2 != "0")):
            self.result = self.input_1_f / self.input_2_f

        
        if ("." in (self.input_1+self.input_2)) or (float(self.result) != int(self.result)):
            self.result_final = str(float(self.result))
        else:
            self.result_final = str(int(self.result))
        
        if ((self.operator_funct == "÷") and (self.input_2 == "0")):
            self.result_label["text"] = "Error"
            self.input_1 = ""
            self.input_2 = ""
            self.operation_used = ""
        
        else:
            self.result_label["text"] = self.result_final 
            self.input_1 = self.result_final
            self.input_2 = ""
            self.operation_used = ""           

    def button_clicked_plus(self):
        self.operator_funct = "+"
        self.operation_used = 1
    
    def button_clicked_minus(self):
        self.operator_funct = "-"
        self.operation_used = 1
    
    def button_clicked_mult(self): 
        self.operator_funct = "×"
        self.operation_used = 1
    
    def button_clicked_div(self):
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



        
