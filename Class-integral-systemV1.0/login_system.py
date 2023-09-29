# login of system
import tkinter as tk
import re
'''
this code writing by Green DZ
YEAR 2020 MONTH 5 DAY 2
Write the code for Class-integral-system v1.0
This is the login system
It's very small.It smaller than Linux 0.11
'''


def exit():
    exit(0)


def threads():

    import sys
    sys.path.append('Class-integral-systemV1.0/main_system')
    import main_system
    if main_system.close():
        main_system.main()
    else:
        Textlabel['text'] = '程序运行异常[ERROR_R1]'
        exit(1)


top = tk.Tk()
top.geometry('400x170+350+150')
top.wm_title('班级积分管理系统登录入口')
top.iconbitmap('')


def validata():
    val = entry_username.get()
    if re.findall('^[0-9a-zA-Z_]{1,}$', str(val)):
        return True
    else:
        Textlabel['text'] = '用户名只能包含字母、数字、下划线'
        return False


def ann_button():
    if str.upper(entry_username.get()) == 'ADAIR' and entry_password.get() == '5200':
        Textlabel['text'] = '登录成功'
        threads()
    else:
        Textlabel['text'] = '用户名或密码输入错误，请重新输入！'


label_username = tk.Label(top, text='用户名:', font=('宋体', '18'))
label_username.grid(row=0, column=0)
label_password = tk.Label(top, text='密码:', font=('宋体', '18'))
label_password.grid(row=1, column=0)
entry_v = tk.StringVar()
entry_username = tk.Entry(top, font=('楷体', '18'), textvariable=entry_v, \
                          validate='focusout', validatecommand=validata)
entry_username.grid(row=0, column=1)
entry_username.focus_force()  # 强制获得焦点
entry_password = tk.Entry(top, font=('楷体', '18'), show='*')
entry_password.grid(row=1, column=1)
button_loginTrue = tk.Button(top, text='登录', font=('宋体', '18'), command=ann_button)
button_loginTrue.grid(row=2, column=0, padx=50, pady=10)
button_end = tk.Button(top, text='退出', font=('宋体', '18'), command=exit)
button_end.grid(row=2, column=1, padx=80, pady=10)
Textlabel = tk.Label(top, text="", font=('华文新魏', '16'), relief='ridge', width=35)
Textlabel.grid(row=3, column=0, padx=10, pady=10, columnspan=5, sticky='sw')
'''
构建输入框，将其与StringVar函数绑定以监视输入的类型，并且绑定验证函数，以验证其输入字符合法性
'''
tk.mainloop()