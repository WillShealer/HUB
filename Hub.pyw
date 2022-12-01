import tkinter
import webbrowser
import os

def Youtube():
    webbrowser.open('https://www.youtube.com/')

def MediaCenter():
    webbrowser.open('https://www.ytech.edu/cms/one.aspx?portalId=20326321&pageId=20638810')

def Skyward():
    webbrowser.open('https://skyward.iscorp.com/YorkTechPAStuSTS')

def VSCode():
    os.startfile(r'C:\Program Files\Microsoft VS Code\Code.exe')

window=tkinter.Tk()

btn1=tkinter.Button(command = Youtube, text="Youtube", fg='red').pack()

btn2=tkinter.Button(command = MediaCenter, text="Media Center", fg='green').pack()

btn3=tkinter.Button(command = Skyward, text="Skyward", fg='blue').pack()

btn4=tkinter.Button(command = VSCode, text="VSCode", fg='blue').pack()

window.geometry("300x200")
window.mainloop()






#btn2=tkinter.Button(command = , text=" ", fg=' ').pack()