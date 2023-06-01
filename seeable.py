import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
import tkinter.messagebox as msg
import time
import sys 
import stats
import image
import search
#模块1:登录系统
#第一部分 画布
with open("uap.log",mode="r",encoding="utf-8") as s:
    n=s.readlines()
    if len(n)!=2 and len(n)!=4:
        print("注册表被篡改,无法打开程序.")
        time.sleep(3)
        sys.exit()

root=tk.Tk()
root.geometry("800x600+0+0") 
root.title("登录")
x=150
label0=ttk.Label(root,text="用户名:");label0.place(x=x,y=20)
entry0=ttk.Entry(root);entry0.place(x=x+50,y=20)
label_1=ttk.Label(root,text="密码:");label_1.place(x=x+220,y=20)
entry_1=ttk.Entry(root,show="*");entry_1.place(x=x+270,y=20)  
IF=False
#第二部分 登录
def g():
    global entry0,entry_1,IF,label0,label_1,q  
    username=entry0.get()
    password=entry_1.get()
    with open("uap.log",mode="r",encoding="utf-8") as uap:
        an=uap.readlines()
        anu=an[0].replace("\n","")
        anp=an[1].replace("\n","")
        try:bnu=an[2].replace("\n","");bnp=an[3].replace("\n","")
        except:bnu=anu;bnp=""
        if (username==anu and password==anp) or (username==bnu and password==bnp): 
            IF=True
            root.destroy()  
        else:
            q.config(width=25)
            q.place(x=200,y=50)
            q["text"]="用户名或密码不正确!(点击重试)" 

#第三部分 注册 
def zc():
    global entry0,entry_1,IF,label0,label_1,q  
    username=entry0.get()
    password=entry_1.get()
    with open("uap.log",mode="r",encoding="utf-8") as uap:
        an=uap.readlines()
        anu=an[0].replace("\n","")
        anp=an[1].replace("\n","")
        try:bnu=an[2].replace("\n","");bnp=an[3].replace("\n","")
        except:bnu="";bnp=""
        if username==anu or username==bnu or password==anp or password==bnp: 
            z.config(width=40)
            z.place(x=220,y=80)
            z["text"]="该用户已经存在或有输入为空.请重新注册.(再次点击)"
        else:
            if len(an)==2:
                with open("uap.log",mode="a",encoding="utf-8") as u1:
                    u1.write("\n"+username)
                    u1.write("\n"+password)
                z.config(width=25)
                z.place(x=230,y=80)
                z["text"]="注册成功!请重新登录账号."
                time.sleep(3)
                IF=True
                root.destroy() 
            else:
                z["text"]="已有两个账号.请前往uap.log删除."    

q = ttk.Button(root, text="确定并进入", command=g);q.place(x=250,y=50)
z = ttk.Button(root, text="注册新账号",command=zc);z.place(x=320,y=80)
out = ttk.Button(root,text="退出",command=sys.exit);out.place(x=400,y=50) 
root.mainloop() 
del root

try:
    if IF: 
        local1=local2=input1=input2=""
        QD=False
        def make ():
            global entry2,local1,local2,butto1,QD,input1,input2 
            if (local1):
                input1=local1.name
                try:input2=local2.name  
                except:input2=entry2.get()
                butto1["text"]="已确定"   
                QD=True 
                
        def iget1(): 
            global local1
            local1=fd.askopenfile(title="打开...",filetypes=[("数据存储文件",["*.txt","*.csv","*.log","*.img","*.png","*.jpg","*.jpeg","*.html","*.m3u8"])]) 

        def iget2(): 
            global local2
            local2=fd.askopenfile(title="打开...",filetypes=[("数据存储文件",["*.txt","*.csv","*.log"])])     

        def do1():
            if QD:
                global input1,input2,butto1
                print(input1) 
                try:
                    r1,r2=stats.st(input1,float(input2))
                    msg.showinfo("结果","%s\n返回值:%s"%(r1,r2))
                except Exception as e:
                    msg.showerror("错误","%s"%e)
                butto1["text"]="确定"   
            else:
                msg.showwarning("警告","您未点击\"确定\".")  


        def do2():
            if QD:
                global input1
                i=input1[-1:-4]
                if i!=".png" and i!=".img" and i!=".jpg" and i!=".jpeg" and i!=".html" and i!=".m3u8":
                    msg.showerror("错误","给定的文件不合法.")
                try:
                    reslut=image.get(input1)
                    msg.showinfo("结果","返回值:%s"%reslut)
                except Exception as e:
                    msg.showerror("错误","%s"%e)
            else:
                msg.showwarning("警告","您未点击\"确定\".")  

        def do3():
            pass                

        root=tk.Tk()
        root.geometry("800x600+0+0")
        root.title("Python人工智能项目")
        menubar=tk.Menu(root)
        filemenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="项目...",menu=filemenu)
        filemenu.add_command(label="单向数据分析",command=do1),filemenu.add_command(label="图像识别",command=do2),filemenu.add_command(label="简易搜索引擎",command=do3)
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
        label1=ttk.Label(pw1,text="数据一路径:(必填.直接定位文件绝对路径)")
        butto_1=ttk.Button(pw1,text="打开...",command=iget1)
        butto_2=ttk.Button(pw1,text="打开...",command=iget2)
        label2=ttk.Label(pw1,text="数据二路径:(选填.也可定位文件绝对路径)")  
        value1=tk.StringVar()
        value2=tk.StringVar()  
        entry2=ttk.Entry(pw1)
        label3=ttk.Label(pw1,text="数据分析复杂度:默认为0(最高),范围0-10(10最低)")
        scale1=tk.Scale(pw1,from_=0,to=10,orient="horizontal")
        scale1.config(length=200)
        butto1=ttk.Button(pw1,text="确定",command=make)  
        butto2=ttk.Button(pw1,text="退出",command=sys.exit)  
        label1.place(x=120,y=20),butto_1.place(x=350,y=20),label2.place(x=120,y=50),entry2.place(x=350,y=50),butto_2.place(x=500,y=50),label3.place(x=250,y=80),scale1.place(x=300,y=110),butto1.place(x=300,y=160),butto2.place(x=300,y=190)

        help_=ttk.Label(pw2,text="或许你只是没有把上面的横线往下拉!")
        root.mainloop()
    else:
        sys.exit()    
except NameError:
    sys.exit()       
