# reza shojaei
import tkinter
import json
#//////////////////////// 

#______________________________
def submit():
     lbl3.configure(text=" ")

     
     user=txt1.get()
     pas=txt2.get()
         
     with open ('d:/app.json') as f:
         dct=json.load(f)
     
     if ((user in dct) and (dct[user]==pas)):
         lbl3.configure(text='username and password unusable',bg='red',fg='white')
         return
     else:
         
         dct[user]=pas
         with open ('d:/app.json' , 'w') as f:
             json.dump(dct,f)
         lbl3.configure(text='username and password created',bg='green',fg='white')
         return
         
#----------- 
def login():
    lbl3.configure(text=" ")
    
    user=txt1.get()
    pas=txt2.get()
       
    with open ('d:/app.json') as f:
        dct=json.load(f)
        
    if ((user in dct) and (dct[user]==pas)):
        lbl3.configure(text='welcome',bg='green',fg='white')
        return
    else:
        lbl3.configure(text='sername and password not exist',bg='red',fg='white')
        return
        
    
#----------- 
def delete():
    lbl3.configure(text=" ") 
    
    user=txt1.get()
    pas=txt2.get()
        
    with open ('d:/app.json') as f:
        dct=json.load(f)
        
    if ((user in dct) and (dct[user]==pas)):
        dct.pop(user)
        with open ('d:/app.json' , 'w') as f:
             json.dump(dct,f)
        
        lbl3.configure(text='username and password deleted',bg='green',fg='white')
        return
    else:
        lbl3.configure(text='username and password not found',bg='red',fg='white')
        return
        
# ..................................................................

win=tkinter.Tk()
win.title('win1')
win.geometry('250x200+500+200')
# -------------
lbl1=tkinter.Label(win,text='username ')
lbl1.grid(column=0,row=0,padx=14,pady=15)
txt1=tkinter.Entry(win,width=30)
txt1.grid(column=1,row=0)
# ------------- 
lbl2=tkinter.Label(win,text='password ')
lbl2.grid(column=0,row=1,padx=14,pady=15)
txt2=tkinter.Entry(win,width=30)
txt2.grid(column=1,row=1)
# -------------
lbl3=tkinter.Label(win,text='welcome dear')
lbl3.grid(column=1,row=2,padx=14,pady=15)
# -------------
btn2=tkinter.Button(win,text='SUBMIT',command=submit)
btn2.grid(column=0,row=3)
# -------------
btn=tkinter.Button(win,text='LOGIN',command=login)
btn.grid(column=1,row=3)
# -------------
btn3=tkinter.Button(win,text='Delete',command=delete)
btn3.grid(column=2,row=3)

win.mainloop()
