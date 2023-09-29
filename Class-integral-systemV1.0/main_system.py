import tkinter as tk

from tkinter import ttk


def default_text(*args):
    Text_area['text'] = '信息提示区'


def prt_q(*args):
    Text_area['text'] = '查询个人积分记录(包括个人积分增减、学分兑换)'


def prt_a(*args):
    Text_area['text'] = '对个人积分进行操作(违规处理、学分兑换、奖励加分)'


def prt_s(*args):
    Text_area['text'] = '在指定时间内的小组积分统计数据输出'


def prt_as(*args):
    Text_area['text'] = '查看关于本系统作者的基本信息'


def jongs(nmpeople):                            # 积分查询检索函数
            import os
            da = []
            for root, dirs, files in os.walk(r"D:\班级积分管理系统v1.0/Class-integral-systemV1.0/data/group"):
                for file in files:
                    f = os.path.join(file)
                    da.append(f)
                    fi = 'D:/班级积分管理系统v1.0/Class-integral-systemV1.0/data/group/group_1' \
                         + '/' + nmpeople + '.csv'
                    for i in range(len(da)):
                        if (nmpeople + '.csv') == da[i]:
                            f = open(file=fi)
                            data_new = []
                            for line in f:
                                line = line.strip('\n')
                                row = line.split(',')
                                line = ' '.join(row)
                                row = line.split()
                                row = row[0:]
                                data_new.append(row)
                            data_new = data_new[0:]
                            f.close()
                            pro_f_name = '姓名：'+data_new[0][0]
                            people_forma_n = tk.Label(inteq, text=pro_f_name, font=('楷体', '16'))
                            people_forma_n.place(x=200, y=5)
                            pro_f_schoolnums = '学号：'+data_new[0][1]
                            people_f_s = tk.Label(inteq, text=pro_f_schoolnums, font=('楷体', '16'))
                            people_f_s.place(x=200, y=40)
                            pro_f_group_name = '组别：'+data_new[0][2]
                            people_f_gn = tk.Label(inteq, text=pro_f_group_name, font=('楷体', '16'))
                            people_f_gn.place(x=400, y=5)
                            pro_f_zc = '职位：'+data_new[0][3]
                            people_f_zc = tk.Label(inteq, text=pro_f_zc, font=('楷体', '16'))
                            people_f_zc.place(x=400, y=40)
                            dataTreeview = tk.ttk.Treeview(inteq, show='headings',
                                                    column=('year', 'month',
                                                            'day', 'item', 'add', 'nums', 'name'))
                            dataTreeview.column('year', width=150, anchor="center")
                            dataTreeview.column('month', width=150, anchor="center")
                            dataTreeview.column('day', width=150, anchor="center")
                            dataTreeview.column('item', width=150, anchor="center")
                            dataTreeview.column('add', width=150, anchor='center')
                            dataTreeview.column('nums', width=150, anchor="center")
                            dataTreeview.column('name', width=150, anchor="center")

                            dataTreeview.heading('year', text='年份')
                            dataTreeview.heading('month', text='月份')
                            dataTreeview.heading('day', text='日份')
                            dataTreeview.heading('item', text='说明')
                            dataTreeview.heading('add', text='加/减分')
                            dataTreeview.heading('nums', text='分值')
                            dataTreeview.heading('name', text='审批人')
                            dataTreeview.place(x=30, y=145, width=1300, height=450)
                            for item in data_new[1:]:
                                dataTreeview.insert("", 1, text="line1", values=item)
                        else:
                            Label_text['text'] = '检索失败'
                    Label_text['text'] = '检索成功'


def prt_text():                             # 积分查询检索入口
        Entry_people.select_clear()
        name = Entry_people.get()
        jongs(name)


def integral_query(*args):                  # 积分查询系统
    root.destroy()
    global inteq
    inteq = tk.Toplevel()
    h = inteq.winfo_screenheight()
    w = inteq.winfo_screenwidth()
    inteq.geometry('%dx%d' % (w, h))
    inteq.iconbitmap('picture/Green DZ.ico')
    inteq.wm_title('班级积分管理系统    积分查询')
    y = tk.StringVar()
    people_text = tk.Label(inteq, text='姓名:')
    people_text.place(x=5, y=8)
    global Entry_people
    Entry_people = tk.Entry(inteq, textvariable=y, validate='focusout', \
                            width=20, validatecommand=prt_text)
    Entry_people.place(x=67, y=10)
    Entry_people.focus_force()
    global Label_text
    Label_text = tk.Label(inteq, text='信息提示区', relief='ridge', width=15, height=5)
    Label_text.place(x=5, y=40)
    Button_again = tk.Button(inteq, text='检索', font=('宋体', '12'), command=prt_text, relief='groove')
    Button_again.place(x=600, y=5)
    inteq.mainloop()


def integral_add():
    root.destroy()


def close():
    f = open('班级积分管理系统V1.0/Class-integral-systemV1.0/data/some/state.txt', 'r+')
    state = f.readlines()
    for i in str(state):
        if i == 'True':
            close_p = 'true'
        else:
            close_p = 'false'
        if close_p == 'true':
            return True
    return False


root = tk.Toplevel()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry('%dx%d' % (w, h))
root.iconbitmap('picture/Green DZ.ico')
root.wm_title('班级积分管理系统_v1.0')
main_tip = tk.PhotoImage(file='picture/main_title.gif')
main_photo = tk.Label(root, image=main_tip, width=900, height=530, relief='ridge')
main_photo.pack(anchor='w')
# 设置各个按钮
integral_query = tk.Button(root, text='积分查询', font=('宋体', '12'), width=18, \
                           height=3, command=integral_query)
integral_query.place(x=920, y=534)
integral_query.bind('<Enter>', prt_q)
integral_query.bind('<Leave>', default_text)

integral_add = tk.Button(root, text='积分增减', font=('宋体', '12'), width=18, height=3)
integral_add.place(x=1120, y=534)
integral_add.bind('<Enter>', prt_a)
integral_add.bind('<Leave>', default_text)

integral_statistics = tk.Button(root, text='积分统计', font=('宋体', '12'), width=18, height=3)
integral_statistics.place(x=920, y=610)
integral_statistics.bind('<Enter>', prt_s)
integral_statistics.bind('<Leave>', default_text)

about_us = tk.Button(root, text='关于作者', font=('宋体', '12'), width=18, height=3)
about_us.place(x=1120, y=610)
about_us.bind('<Enter>', prt_as)
about_us.bind('<Leave>', default_text)

# 用信息提示去来提示用户按钮的作用
Text_area = tk.Label(root, text='信息提示区', width=128,
                     font=('宋体', '10'), height=6, relief='ridge')
Text_area.place(x=5, y=550)

# 用标签介绍本系统
my = '本系统是用于管理班级\n积分,属于中型系\n统,代码全开放,但作\n者仍享有软件的著作\n权,由于时间匆促,预\n计' \
         '会在4.0版本时\n' \
         '完全更换为Java语\n言编写全新版本,本版\n本有诸多不足,若有有\n意者请根据“关于作者”\n里的信息与作者取得联\n系.'
Text_AREA = tk.Label(root, text=my, font=('楷体', '12'), width=60, height=30, relief='ridge')
Text_AREA.place(x=905, y=0)
me_centre = tk.Button(root, text='个人中心', width=7, height=5)
me_centre.place(x=1300, y=550)
root.mainloop()
