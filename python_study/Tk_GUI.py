#!/usr/bin/python
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *
import pymysql
from builtins import int


def connDB():  # 连接数据库
    conn = pymysql.connections.Connection(host="localhost", user="root", passwd="111", db="GradeManager")
    cur = conn.cursor()
    return (conn, cur)


def exeDelete(conn, cur, IDs):  # 删除操作
    sta = 0
    for eachID in IDs.split(' '):
        sta += cur.execute("delete from Student where Sno=%d" % (int(eachID)))
    conn.commit()
    return (sta)

def exeDelete2(conn, cur, IDs):  # 删除操作
    sta = 0
    for eachID in IDs.split(' '):
        sta += cur.execute("delete from Grade where Sno=%d" % (int(eachID)))
    conn.commit()
    return (sta)

def exeDelete3(conn, cur, IDs):  # 删除操作
    sta = 0
    for eachID in IDs.split(' '):
        sta += cur.execute("delete from Course where Cno=%d" % (int(eachID)))
    conn.commit()
    return (sta)

def exeDelete4(conn, cur, IDs):  # 删除操作
    sta = 0
    for eachID in IDs.split(' '):
        sta += cur.execute("delete from Class where Clno=%d" % (int(eachID)))
    conn.commit()
    return (sta)

def exeQuery(cur, sql):  # 查找操作
    cur.execute(sql)
    return (cur)

def exeUpdate(conn, cur, sql):  # 更新或插入操作
    sta = cur.execute(sql)
    conn.commit()
    return (sta)


conn, cur = connDB()


LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):
    '''
    多页面测试程序
        界面与逻辑分离
    '''

    def __init__(self):
        super().__init__()

        # self.iconbitmap(default="kankan_01.ico")
        self.wm_title("信息管理系统")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Student, Grade, Course, Class):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


class StartPage(tk.Frame):
    '''主页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="Mamanger", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="学生管理", command=lambda: root.show_frame(Student)).pack()
        button2 = Button(self, text="成绩管理", command=lambda: root.show_frame(Grade)).pack()
        button3 = Button(self, text="课程管理", command=lambda: root.show_frame(Course)).pack()
        button4 = Button(self, text="班级管理", command=lambda: root.show_frame(Class)).pack()

### 学生表管理 ###
class Student(tk.Frame):
    '''第一页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = Label(self, text="Student", font=LARGE_FONT)
        label.grid(row=0, column=3)

        # ### 删除 ###

        label1 = Label(self, text="删除")
        self.msgd = StringVar()
        entry1 = Entry(self, textvariable=self.msgd)
        btChangeText1 = Button(self, text="确认删除", command=self.processButton_D)
        self.lb1 = Label(self, text="返回结果")
        self.lb1.grid(row=1, column=3)
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        btChangeText1.grid(row=1, column=2)


        ### 查询操作 ###

        label2 = Label(self, text="查询")
        self.msgq = StringVar()
        entry2 = Entry(self, textvariable=self.msgq)
        btChangeText2 = Button(self, text="确认查询", command=self.processButton_Q)
        self.lb2 = Label(self, text="返回结果")
        self.lb2.grid(row=3, column=3)
        label2.grid(row=3, column=0)
        entry2.grid(row=3, column=1)
        btChangeText2.grid(row=3, column=2)


        ### 添加操作 ###
        label3 = Label(self, text="添加")
        #self.label3.pack()
        self.msg1 = StringVar()
        self.msg2 = StringVar()
        self.msg3 = StringVar()
        self.msg4 = StringVar()
        self.msg5 = StringVar()
        entry11 = Entry(self, textvariable=self.msg1)
        entry22 = Entry(self, textvariable=self.msg2)
        entry33 = Entry(self, textvariable=self.msg3)
        entry44 = Entry(self, textvariable=self.msg4)
        entry55 = Entry(self, textvariable=self.msg5)
        btChangeText3 = Button(self, text="确认添加", command=self.processButton_U)
        self.lb3 = Label(self, text="返回结果")
        self.lb3.grid(row=5, column=7)

        label3.grid(row=5, column=0)
        entry11.grid(row=5, column=1)
        entry22.grid(row=5, column=2)
        entry33.grid(row=5, column=3)
        entry44.grid(row=5, column=4)
        entry55.grid(row=5, column=5)
        btChangeText3.grid(row=5, column=6)

        button1 = Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=7, column=3)
        # button2 = Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

    def processButton_D(self):
        Sno = self.msgd.get()
        try:
            exeDelete(conn, cur, Sno)
            self.lb1["text"] = "删除成功"
        except Exception:
            self.lb1["text"] = "删除失败"
            raise
            # self.lb1["text"] = self.msg.get()

    def processButton_Q(self):
        Sno = self.msgq.get()
        sql = "select * from Student where Student.Sno=%d" % (int(Sno))
        try:
            cu = exeQuery(cur, sql)
            for item in cu:
                self.lb2["text"] = ("num=" + str(item[0]) + " name=" + item[1])
        except Exception:
            self.lb2["text"] = "查询失败"
            raise

    def processButton_U(self):
        Sno = self.msg1.get()
        Sname = self.msg2.get()
        Ssex = self.msg3.get()
        Sage = self.msg4.get()
        Clno = self.msg5.get()
        sql = "insert into Student(Sno,Sname,Ssex,Sage,Clno) values('%d','%s','%s','%d','%d')" % (
        int(Sno), Sname, Ssex, int(Sage), int(Clno))
        try:
            exeUpdate(conn, cur, sql)
            self.lb3["text"] = "添加成功"
        except Exception:
            self.lb3["text"] = "添加失败"
            raise




### 成绩表管理 ###
class Grade(tk.Frame):
    '''第二页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = Label(self, text="Grade", font=LARGE_FONT)
        label.grid(row=0, column=3)

        # ### 删除 ###
        label1 = Label(self, text="删除")
        self.msgd = StringVar()
        entry1 = Entry(self, textvariable=self.msgd)
        btChangeText1 = Button(self, text="确认删除", command=self.processButton_D)
        self.lb1 = Label(self, text="返回结果")
        self.lb1.grid(row=1, column=3)
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        btChangeText1.grid(row=1, column=2)


        ### 查询操作 ###

        label2 = Label(self, text="查询")
        self.msgq = StringVar()
        entry2 = Entry(self, textvariable=self.msgq)
        btChangeText2 = Button(self, text="确认查询", command=self.processButton_Q)
        self.lb2 = Label(self, text="返回结果")
        self.lb2.grid(row=3, column=3)
        label2.grid(row=3, column=0)
        entry2.grid(row=3, column=1)
        btChangeText2.grid(row=3, column=2)


        ### 添加操作 ###
        label3 = Label(self, text="添加")
        #self.label3.pack()
        self.msg1 = StringVar()
        self.msg2 = StringVar()
        self.msg3 = StringVar()
        entry11 = Entry(self, textvariable=self.msg1)
        entry22 = Entry(self, textvariable=self.msg2)
        entry33 = Entry(self, textvariable=self.msg3)
        btChangeText3 = Button(self, text="确认添加", command=self.processButton_U)
        self.lb3 = Label(self, text="返回结果")
        self.lb3.grid(row=5, column=5)

        label3.grid(row=5, column=0)
        entry11.grid(row=5, column=1)
        entry22.grid(row=5, column=2)
        entry33.grid(row=5, column=3)
        btChangeText3.grid(row=5, column=4)

        button1 = Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=7, column=3)
        # button2 = Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

    def processButton_D(self):
        Sno = self.msgd.get()
        try:
            exeDelete2(conn, cur, Sno)
            self.lb1["text"] = "删除成功"
        except Exception:
            self.lb1["text"] = "删除失败"
            raise
            # self.lb1["text"] = self.msg.get()

    def processButton_Q(self):
        Sno = self.msgq.get()
        sql = "select * from Grade where Grade.Sno=%d" % (int(Sno))
        try:
            cu = exeQuery(cur, sql)
            for item in cu:
                self.lb2["text"] = ("num=" + str(item[0]) + " name=" + item[1])
        except Exception:
            self.lb2["text"] = "查询失败"
            raise

    def processButton_U(self):
        Sno = self.msg1.get()
        Cno = self.msg2.get()
        Gmark = self.msg3.get()

        sql = "insert into Grade(Sno,Cno,Gmark) values('%d','%d','%d')" % (int(Sno),int(Cno), int(Gmark))
        try:
            exeUpdate(conn, cur, sql)
            self.lb3["text"] = "添加成功"
        except Exception:
            self.lb3["text"] = "添加失败"
            raise


### 课程表管理 ###
class Course(tk.Frame):
    '''第三页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = Label(self, text="Course", font=LARGE_FONT)
        label.grid(row=0, column=3)

        # ### 删除 ###
        label1 = Label(self, text="删除")
        self.msgd = StringVar()
        entry1 = Entry(self, textvariable=self.msgd)
        btChangeText1 = Button(self, text="确认删除", command=self.processButton_D)
        self.lb1 = Label(self, text="返回结果")
        self.lb1.grid(row=1, column=3)
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        btChangeText1.grid(row=1, column=2)


        ### 查询操作 ###

        label2 = Label(self, text="查询")
        self.msgq = StringVar()
        entry2 = Entry(self, textvariable=self.msgq)
        btChangeText2 = Button(self, text="确认查询", command=self.processButton_Q)
        self.lb2 = Label(self, text="返回结果")
        self.lb2.grid(row=3, column=3)
        label2.grid(row=3, column=0)
        entry2.grid(row=3, column=1)
        btChangeText2.grid(row=3, column=2)


        ### 添加操作 ###
        label3 = Label(self, text="添加")
        #self.label3.pack()
        self.msg1 = StringVar()
        self.msg2 = StringVar()
        self.msg3 = StringVar()
        entry11 = Entry(self, textvariable=self.msg1)
        entry22 = Entry(self, textvariable=self.msg2)
        entry33 = Entry(self, textvariable=self.msg3)
        btChangeText3 = Button(self, text="确认添加", command=self.processButton_U)
        self.lb3 = Label(self, text="返回结果")
        self.lb3.grid(row=5, column=5)

        label3.grid(row=5, column=0)
        entry11.grid(row=5, column=1)
        entry22.grid(row=5, column=2)
        entry33.grid(row=5, column=3)
        btChangeText3.grid(row=5, column=4)

        button1 = Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=7, column=3)
        # button2 = Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

    def processButton_D(self):
        Cno = self.msgd.get()
        try:
            exeDelete3(conn, cur, Cno)
            self.lb1["text"] = "删除成功"
        except Exception:
            self.lb1["text"] = "删除失败"
            raise
            # self.lb1["text"] = self.msg.get()

    def processButton_Q(self):
        Cno = self.msgq.get()
        sql = "select * from Course where Course.Cno=%d" % (int(Cno))
        try:
            cu = exeQuery(cur, sql)
            for item in cu:
                self.lb2["text"] = ("num=" + str(item[0]) + " name=" + item[1])
        except Exception:
            self.lb2["text"] = "查询失败"
            raise

    def processButton_U(self):
        Cno = self.msg1.get()
        Cname = self.msg2.get()
        Credit = self.msg3.get()

        sql = "insert into Course(Cno,Cname,Credit) values('%d','%s','%d')" % (int(Cno), Cname, int(Credit))
        try:
            exeUpdate(conn, cur, sql)
            self.lb3["text"] = "添加成功"
        except Exception:
            self.lb3["text"] = "添加失败"
            raise


### 班级表管理 ###
class Class(tk.Frame):
    '''第四页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = Label(self, text="Class", font=LARGE_FONT)
        label.grid(row=0, column=3)

        # ### 删除 ###
        label1 = Label(self, text="删除")
        self.msgd = StringVar()
        entry1 = Entry(self, textvariable=self.msgd)
        btChangeText1 = Button(self, text="确认删除", command=self.processButton_D)
        self.lb1 = Label(self, text="返回结果")
        self.lb1.grid(row=1, column=3)
        label1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)
        btChangeText1.grid(row=1, column=2)


        ### 查询操作 ###

        label2 = Label(self, text="查询")
        self.msgq = StringVar()
        entry2 = Entry(self, textvariable=self.msgq)
        btChangeText2 = Button(self, text="确认查询", command=self.processButton_Q)
        self.lb2 = Label(self, text="返回结果")
        self.lb2.grid(row=3, column=3)
        label2.grid(row=3, column=0)
        entry2.grid(row=3, column=1)
        btChangeText2.grid(row=3, column=2)


        ### 添加操作 ###
        label3 = Label(self, text="添加")
        #self.label3.pack()
        self.msg1 = StringVar()
        self.msg2 = StringVar()
        self.msg3 = StringVar()
        self.msg4 = StringVar()
        self.msg5 = StringVar()
        entry11 = Entry(self, textvariable=self.msg1)
        entry22 = Entry(self, textvariable=self.msg2)
        entry33 = Entry(self, textvariable=self.msg3)
        entry44 = Entry(self, textvariable=self.msg4)
        entry55 = Entry(self, textvariable=self.msg5)
        btChangeText3 = Button(self, text="确认添加", command=self.processButton_U)
        self.lb3 = Label(self, text="返回结果")
        self.lb3.grid(row=5, column=7)

        label3.grid(row=5, column=0)
        entry11.grid(row=5, column=1)
        entry22.grid(row=5, column=2)
        entry33.grid(row=5, column=3)
        entry44.grid(row=5, column=4)
        entry55.grid(row=5, column=5)
        btChangeText3.grid(row=5, column=6)

        button1 = Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=7, column=3)
        # button2 = Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

    def processButton_D(self):
        Clno = self.msgd.get()
        try:
            exeDelete4(conn, cur, Clno)
            self.lb1["text"] = "删除成功"
        except Exception:
            self.lb1["text"] = "删除失败"
            raise
            # self.lb1["text"] = self.msg.get()

    def processButton_Q(self):
        Cno = self.msgq.get()
        sql = "select * from Class where Class.Clno=%d" % (int(Cno))
        try:
            cu = exeQuery(cur, sql)
            for item in cu:
                self.lb2["text"] = ("num=" + str(item[0]) + " name=" + item[1])
        except Exception:
            self.lb2["text"] = "查询失败"
            raise

    def processButton_U(self):
        Clno = self.msg1.get()
        Speciality = self.msg2.get()
        Inyear = self.msg3.get()
        Number = self.msg4.get()
        Moniter = self.msg5.get()

        sql = "insert into Class(Clno,Speciality,Inyear,Number,Moniter) values('%d','%s','%d','%d','%d')" % (int(Clno), Speciality, int(Inyear), int(Number), int(Moniter))
        try:
            exeUpdate(conn, cur, sql)
            self.lb3["text"] = "添加成功"
        except Exception:
            self.lb3["text"] = "添加失败"
            raise


if __name__ == '__main__':
    # 实例化Application
    app = Application()

    # 主消息循环:
    app.mainloop()