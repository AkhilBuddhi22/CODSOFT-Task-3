from tkinter import *
import string
import random
import pyperclip
def generator():
    smallalphabets=string.ascii_lowercase
    capitalalphabets=string.ascii_uppercase
    numbers=string.digits
    specialcharacters=string.punctuation

    all=smallalphabets+capitalalphabets+numbers+specialcharacters
    passwordlength=int(lengthBox.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(smallalphabets,passwordlength))
    if choice.get()==2:
        passwordField.insert(0,random.sample(smallalphabets+capitalalphabets,passwordlength))  
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,passwordlength))
    password=random.sample(all,passwordlength)
    passwordField.insert(0,password)


def copy():
    randompassword=passwordField.get()
    pyperclip.copy(randompassword)


root =Tk()
root.config(bg="gray20")
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'))
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font=('times new roman',20,'bold'),bg='gray20',fg='white')
lengthLabel.grid(pady=5)

lengthBox=Spinbox(root,from_=5,to_=18,width=5,font=Font)
lengthBox.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()
