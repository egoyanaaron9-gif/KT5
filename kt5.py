from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("500x450")
root.configure(background="black")

label1 = ttk.Label(text="Мои текущие задачи", background="black", foreground="yellow", font=("Arial", 24))
label1.pack(anchor=CENTER,)

frame = Frame(root, background="black")
frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

f = open('tasks.txt', 'r', encoding="utf-8")

for line in f:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
      
    if "Прямо щаз происходит" in line:
        color = "orange" 
        text = line.replace("-", "").strip()
    elif "Осталось" in line:
        color = "white"   
        text = line.replace("-", "").strip()
    elif "Прошло" in line:
        color = "red"     
        text = line.replace("-", "").strip()
    else:
        color = "white"
        text = line.replace("-", "").strip()
    
    label = ttk.Label(frame, text=text, background="black", foreground=color)
    label.pack(anchor=CENTER)

f.close()
root.mainloop()

