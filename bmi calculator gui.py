from tkinter import *
import tkinter as tk
from tkinter import Frame, Tk, Button, Label, Entry
from tkinter import ttk

window = tk.Tk()
window.title("Window, Brandpointone")
window.config(bg = "maroon", padx=5, pady=5)

def BMICalculator():
   if Weight.get() == "" or Height.get() == "":
       response = "You have missing information"
       Convert.insert(0, response)

   try: 
      heightSquared = float(Height.get())**2
   except:
      ValueError

   try:
      BMI = float(Weight.get()) / float(heightSquared)
      BMI = round(BMI, 2)
      response = "Your BMI is: "+str(BMI)
      Convert.insert(0, response)
      
   except:
      UnboundLocalError

'''     
  
   try:
      BMI = float(BMI)
      if BMI < 20:
          response = "Your BMI is: "+str(BMI) + "This means you are underweight"
          Convert.insert(0, response)
      elif round(BMI) == 20 or round(BMI) == 21 or round(BMI) == 22 or round(BMI) == 23 or round(BMI)== 24 or BMI == 25:
          response = "Your BMI is: "+str(BMI) + "This means you are in the Ideal Weight range"
          Convert.insert(0, response)
      else:
          response = "This means you are Overweight"
          Convert.insert(0, response)
   except:
      ValueError

#height = float(input("Please enter height: "))
#weight = float(input("Please enter weight: "))

BMICalculator()


def show_answer():
    try:
        Ans = float(Weight.get())/ (float(Height.get()) * float(Height.get()))
        Convert.insert(0, Ans)
    except:
        invalid =  "Invalid Input"
        Convert.insert(0, invalid)
        
'''       

framemcolour = "rebeccapurple"
padding = 7
framem = tk.Frame(window)
framem.config(bg = framemcolour, padx=10, pady=10)
framem.grid(column = 0, row = 0, padx=20, pady=10)

 
Heading1 = Label (framem, text = "Calculate your BMI")
Heading1.grid(column = 0, row = 0, columnspan = 4, pady = padding)
Heading1.config(width = 24, height = 2, bg = "wheat", \
               font = ("Calibri bold", 24),\
               fg = "black",)


Weight_Label = Label (framem, text = "Enter your weight in kg \n to the right:")
Weight_Label.grid(column = 0, row = 2, columnspan = 2, pady = padding)
Weight_Label.config(width = 26, height = 2, bg ="wheat", \
               fg = "black", \
               font = ("Calibri bold", 14), justify = "center")


Weight = Entry (framem)
Weight.grid(column = 3, row = 2, sticky="e")
Weight.config(width = 4, bg = "white", fg = "black", \
            relief = "ridge", justify = "center", \
            font = ("Calibri", 26))


Height_Label = Label (framem, text = "  Enter your height in meters \n to the right:")
Height_Label.grid(column = 0, row = 4, columnspan = 2, pady = padding)
Height_Label.config(width = 26, height = 2, bg ="wheat"  , \
               fg = "black", \
               font = ("Calibri bold", 14), justify = "center")


Height = Entry (framem)
Height.grid(column = 3, row = 4, sticky = "e")
Height.config(width = 4, bg = "white", fg = "black", \
            justify = "center", \
            font = ("Calibri", 26))


Gender_Label = Label (framem, text = "  Enter your height in meters \n to the right:")
Gender_Label.grid(column = 0, row = 6, columnspan = 2, pady = padding)
Gender_Label.config(width = 26, height = 2, bg ="wheat"  , \
               fg = "black", \
               font = ("Calibri bold", 14), justify = "center")

v = IntVar()
Gender_Male = Radiobutton(framem, text="Male", variable=v, value=1)
Gender_Female = Radiobutton(framem, text="Female", variable=v, value=2)

Gender_Male.grid(column = 2, row = 6)
Gender_Male.config(width = 5, bg="White", fg = "black", \
            justify = "center", \
            font = ("Calibri", 12))

Gender_Female.grid(column = 3, row = 6)
Gender_Female.config(width = 5, bg="White", fg = "black", \
            justify = "center", \
            font = ("Calibri", 12))
v.set(1)


PressMe = Button(framem, text = "Press to find \n your BMI",command=BMICalculator)
PressMe.grid(row = 8, column = 1, columnspan = 2, pady = padding, sticky = "w")
PressMe.config(width = 19, height = 2, bg = "darkslategray", fg = "white",\
               bd = 3, relief = "ridge",
               font = ("Calibri bold", 14, "bold"))



Heading = Label(framem, text = "Your BMI is:")
Heading.grid(column = 0, row = 10, columnspan = 4, pady = padding, sticky = "w")
Heading.config(width = 41, height = 2, bg = "white", fg = "black",\
               font = ("Calibri bold", 14))



Convert = Entry(framem)
Convert.grid(column = 0, row = 12, columnspan = 4, pady = padding, sticky = "nsew")
Convert.config(width = 0, height = 2, bg = "white", fg = "black", font = ("Calibri bold", 14, "bold"))


window.mainloop()
