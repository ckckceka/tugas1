import tkinter as tk
theme = 0
calculate = ""
def calculation(symbol):
    global calculate
    calculate += str(symbol)
    text.delete(1.0,"end")
    text.insert(1.0,calculate)
def clear():
    global calculate
    calculate = ""
    text.delete(1.0,"end")
def evaluate():
    global calculate
    try:
        calculate = str(eval(calculate))
        text.delete(1.0,"end")
        text.insert(1.0,calculate)
    except:
        clear()
        text.insert(1.0,"error")
def apply_theme():
    global theme
    light_mode = {
        'bg':'white',
        'fg' : 'black' , 
        'entry_bg' : '#eee',
        'entry_fg' : 'black',
        'btn_bg' : '#ddd' ,
        'btn_fg' : 'black'
    }
    dark_mode ={
        'bg':'#333',
        'fg' : 'white' , 
        'entry_bg' : '#555',
        'entry_fg' : 'white',
        'btn_bg' : '#444' ,
        'btn_fg' : 'white'
    }
    if theme == 0:
        theme +=1
        root.config(bg = dark_mode['bg'])
        btn_1.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_2.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_3.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_4.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_5.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_6.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_7.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_8.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_9.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_0.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_plus.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_min.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_divide.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_multiply.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_open.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_close.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_ans.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_clear.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        btn_switch.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
        text.config(bg=dark_mode['entry_bg'],fg = dark_mode['entry_fg'])
    elif theme == 1:
        theme -= 1
        root.config(bg = light_mode['bg'])
        btn_1.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_2.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_3.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_4.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_5.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_6.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_7.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_8.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_9.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_0.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_plus.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_min.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_divide.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_multiply.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_open.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_close.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_ans.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_clear.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        btn_switch.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])
        text.config(bg=light_mode['entry_bg'],fg = light_mode['entry_fg'])

root  = tk.Tk()
root.geometry("300x320")

text = tk.Text(root,height=2,width=16,font=("arial",24))
text.grid(columnspan=5)

btn_1 = tk.Button(root,text="1",command=lambda:calculation(1),width = 5,font=("Arial",14))
btn_2 = tk.Button(root,text="2",command=lambda:calculation(2),width = 5,font=("Arial",14))
btn_3 = tk.Button(root,text="3",command=lambda:calculation(3),width = 5,font=("Arial",14))
btn_4 = tk.Button(root,text="4",command=lambda:calculation(4),width = 5,font=("Arial",14))
btn_5 = tk.Button(root,text="5",command=lambda:calculation(5),width = 5,font=("Arial",14))
btn_6 = tk.Button(root,text="6",command=lambda:calculation(6),width = 5,font=("Arial",14))
btn_7 = tk.Button(root,text="7",command=lambda:calculation(7),width = 5,font=("Arial",14))
btn_8 = tk.Button(root,text="8",command=lambda:calculation(8),width = 5,font=("Arial",14))
btn_9 = tk.Button(root,text="9",command=lambda:calculation(9),width = 5,font=("Arial",14))
btn_0 = tk.Button(root,text="0",command=lambda:calculation(0),width = 5,font=("Arial",14))
btn_plus = tk.Button(root,text="+",command=lambda:calculation("+"),width = 5,font=("Arial",14))
btn_min = tk.Button(root,text="-",command=lambda:calculation("-"),width = 5,font=("Arial",14))
btn_divide = tk.Button(root,text=":",command=lambda:calculation("/"),width = 5,font=("Arial",14))
btn_multiply = tk.Button(root,text="x",command=lambda:calculation("*"),width = 5,font=("Arial",14))
btn_open = tk.Button(root,text="(",command=lambda:calculation(")"),width = 5,font=("Arial",14))
btn_close = tk.Button(root,text=")",command=lambda:calculation(")"),width = 5,font=("Arial",14))
btn_ans = tk.Button(root,text="=",command=lambda:evaluate(),width = 11,font=("Arial",14))
btn_clear = tk.Button(root,text="CLEAR",command=lambda:clear(),width = 11,font=("Arial",14))
btn_switch = tk.Button(root,text="🔀",command=lambda:apply_theme(),width = 24,font=("Arial",14))

btn_1.grid(row=2,column=1)
btn_2.grid(row=2,column=2)
btn_3.grid(row=2,column=3)
btn_4.grid(row=3,column=1)
btn_5.grid(row=3,column=2)
btn_6.grid(row=3,column=3)
btn_7.grid(row=4,column=1)
btn_8.grid(row=4,column=2)
btn_9.grid(row=4,column=3)
btn_0.grid(row=5,column=1)
btn_plus.grid(row=2,column=4)
btn_min.grid(row=3,column=4)
btn_divide.grid(row=4,column=4)
btn_multiply.grid(row=5,column=4)
btn_open.grid(row=5,column=2)
btn_close.grid(row=5,column=3)
btn_ans.grid(row=6,column=1,columnspan=2)
btn_clear.grid(row=6,column=3,columnspan=2)
btn_switch.grid(row=7,column=1,columnspan=4)

root.mainloop()