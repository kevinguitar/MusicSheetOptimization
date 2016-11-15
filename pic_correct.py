__author__ = 'Kevin_Chiu'

from tkinter import *
from tkinter import filedialog
import cv2

root = Tk()
root.wm_title("樂譜清晰化程式")
root.geometry('300x300')
root.resizable(width=False, height=False)

def open_File():
    file_path = filedialog.askopenfilenames()
    for i in file_path:
        txt_File.insert(END, i + '\n')

def convert_File():
    folder = filedialog.askdirectory(title='選擇儲存圖片的資料夾')
    files = txt_File.get("1.0", END).replace('/', '//')
    folder = folder.replace('/', '//')
    index = 1
    for i in files.split('\n'):
        if(i != ''):
            image = cv2.imread(i)
            th, thres = cv2.threshold(image, 145, 255, cv2.THRESH_BINARY)
            smooth = cv2.medianBlur(thres, 3, 3)
            cv2.imwrite(folder + '//' + str(index) + '.jpg', smooth)
            index = index + 1
    txt_File.insert(END, '轉換完成！\n若要繼續轉換圖片, 請重新啟動程式')
    btn_Open.config(state=DISABLED)
    btn_Convert.config(state=DISABLED)

btn_Open = Button(root, text='開啟圖片', command=open_File)
btn_Open.pack(padx=20, pady=10, side=TOP)
txt_File = Text(root, height=15)
txt_File.pack(padx=20, pady=0, side=TOP)
btn_Convert = Button(root, text='轉換圖片', command=convert_File)
btn_Convert.pack(padx=20, pady=10, side=TOP)

root.mainloop()
