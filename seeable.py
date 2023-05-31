import tkinter as tk
import tkinter.ttk as ttk
import time
import sys
"""
root=tk.Tk()
root.geometry("800x600+0+0") 
label=ttk.Label(root,text="正在加载数据...")
label.pack()
time.sleep(2)
quit = ttk.Button(root, text="确定并进入", command=root.destroy) 
out = ttk.Button(root,text="退出",command=sys.exit)
out.pack()
quit.pack()
root.mainloop() 
del root,label
"""
def make():
    global value1,value2
    print(value1)
    print(value2)
def make1():
    global value1
    print(value1)
root=tk.Tk()
root.geometry("800x600+0+0")

menubar=tk.Menu(root)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="项目...",menu=filemenu)
filemenu.add_command(label="单向数据分析"),filemenu.add_command(label="图像识别"),filemenu.add_command(label="简易搜索引擎")
root.config(menu=menubar) 
pw=tk.PanedWindow(root,orient="vertical",sashrelief="sunken")
pw.pack(fill="both",expand=1) 

separator = ttk.Separator(root).pack(padx=2, fill='x')
status_frame = ttk.Frame(root, relief='raised').pack(fill='x')
label_status = ttk.Label(status_frame, text='工作状态').pack(side='left', fill='x')
sizegrip = ttk.Sizegrip(status_frame).pack(anchor='ne') 

pw1=tk.PanedWindow(root,orient="vertical",sashrelief="flat")
pw2=tk.PanedWindow(root,orient="vertical",sashrelief="flat")
pw.add(pw1),pw.add(pw2)
label1=ttk.Label(pw1,text="数据一路径:(必填)")
label2=ttk.Label(pw1,text="数据二路径:(选填)")
value1=tk.StringVar()
value2=tk.StringVar()
entry1=ttk.Entry(pw1,textvariable=value1) 
entry1.bind("<KeyPress-\n>",make1)
entry2=ttk.Entry(pw1,textvariable=value2)
label3=ttk.Label(pw1,text="数据分析复杂度:默认为0(最高),范围0-10(10最低)")
scale1=tk.Scale(pw1,from_=0,to=10,orient="horizontal")
butto1=ttk.Button(pw1,text="确定",command=make)
butto2=ttk.Button(pw1,text="退出",command=sys.exit)  
label1.pack(),entry1.pack(),label2.pack(),entry2.pack(),label3.pack(),scale1.pack(),butto1.pack(),butto2.pack()

root.mainloop()