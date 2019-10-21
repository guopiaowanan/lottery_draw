import time
import threading
import tkinter as tk  
import random    

root = tk.Tk()      #初始化Tk() 建立一个窗口
root.title('快来抽奖吧！') # 设置标题
root.minsize(1000, 700)

label0 = tk.Label(root, bg='black')
label0.place(x=0, y=0, width=620, height=620)


label1 = tk.Label(root, text='自行车*1', bg='yellow', font=('Arial', 20))
label1.place(x=5, y=5, width=200, height=200)

label2 = tk.Label(root, text='谢谢惠顾', bg='yellow', font=('Arial', 20))
label2.place(x=210, y=5, width=200, height=200)

label3 = tk.Label(root, text='牛奶*1', bg='yellow', font=('Arial', 20))
label3.place(x=415, y=5, width=200, height=200)

label4 = tk.Label(root, text='再来一次', bg='yellow', font=('Arial', 20))
label4.place(x=415, y=210, width=200, height=200)

label5 = tk.Label(root, text='谢谢惠顾', bg='yellow', font=('Arial', 20))
label5.place(x=415, y=415, width=200, height=200)

label6 = tk.Label(root, text='IPhone X *1', bg='yellow', font=('Arial', 20))
label6.place(x=210, y=415, width=200, height=200)

label7 = tk.Label(root, text='谢谢惠顾', bg='yellow', font=('Arial', 20))
label7.place(x=5, y=415, width=200, height=200)

label8 = tk.Label(root, text='美的空调*1', bg='yellow', font=('Arial', 20))
label8.place(x=5, y=210, width=200, height=200)

# 将所有抽奖选项添加到列表
things = [label1, label2, label3, label4, label5, label6, label7, label8]
cont =  (len(things) - 1)

starts = random.randint(0, cont)
# 是否停止标志
notround = False

# 定义滚动函数
def round():
    t = threading.Thread(target=startup) #启动start
    t.start()

# 定义开始函数
def startup():
    global starts
    global notround
    while True:
        # 检测停止按钮是否被按下
        if notround == True:
            notround = False
            return starts

        # 程序延时(跳动时间间隔)
        time.sleep(0.01)

        # 在所有抽奖选项中循环滚动
        for i in things:
            i['bg'] = 'lightSkyBlue' #开始时 底色变成天蓝
        things[starts]['bg'] = 'red' #滚动框为 红色
        starts += 1
        if starts > cont:
            starts = 0
            
# 定义停止函数
def stops():
    global notround # notround 为全局变量
    global starts

    notround = True  #停止标志位

    # 设置用户不能中奖，哈哈哈哈哈哈
    # if starts in [0,2,5,7]:
    #     tmp = [1,3,4,6]
    #     starts = random.choice(tmp)

    # 设置用户一定中奖 略略略
    # tmp = [0,2,5,7]
    # starts = random.choice(tmp) 

    # 设置用户一定某个奖项
    starts = 5




# 设置启动按键 
btn1 = tk.Button(root, text='开始', bg='lightSkyBlue', font=('Arial', 50), command=round)
btn1.place(x=130, y=640, width=180, height=60)

# 设置停止按键 
btn2 = tk.Button(root, text='结束', bg='red', font=('Arial', 50), command=stops)
btn2.place(x=330, y=640, width=180, height=60)

root.mainloop()
