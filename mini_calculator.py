from tkinter import *
window = Tk()
window.title("MINI CALCULATOR")
window.geometry('350x200')

lbl= Label(window,text="---")
lbl.grid(column=0,row=0)

btn = Label(window,text="first number")
btn.grid(column=0,row=1)

txt = Entry(window)
txt.grid(column=1 ,row=1)

btn2 = Label(window,text="second number")
btn2.grid(column=0,row=2)
       
txt2 = Entry(window)
txt2.grid(column=1 ,row=2)

def addition():
   if txt.get() and txt2 .get() != "":
      num1 = float(txt.get())
      num2 = float(txt2 .get())
      answer = num1 + num2
      lbl.configure(text=answer)
   else:
      answer_l.configure(text="fill in all the required field")
def subtraction():
   if txt.get() and txt2 .get() != "":
      num1 = float(txt.get())
      num2 = float(txt2 .get())
      answer = num1 - num2
      lbl.configure(text=answer)
   else:
      answer_l.configure(text="fill in all the required field")

def multiplication():
   if txt.get() and txt2 .get() != "":
      num1 = float(txt.get())
      num2 = float(txt2 .get())
      answer = num1 * num2
      lbl.configure(text=answer)
   else:
      answer_l.configure(text="fill in all the required field")

def divide():
   if txt.get() and txt2 .get() != "":
      num1 = float(txt.get())
      num2 = float(txt2 .get())
      answer = num1 / num2
      lbl.configure(text=answer)
   else:
      answer_l.configure(text="fill in all the required field")
cal_btn = Button(window,text="Add",command=addition)
cal_btn.grid(column= 3 , row=0)

cal_btn = Button(window,text="Subtract",command=subtraction)
cal_btn.grid(column= 4 , row=0)

cal_btn = Button(window,text="Multiply",command=multiplication)
cal_btn.grid(column= 3 , row=1)

cal_btn = Button(window,text="divide",command=divide)
cal_btn.grid(column= 4 , row=1)
window.mainloop()

   

   
