import bson
import json
import filesearch as fs
# tkinter 是UI套件
import tkinter as tk
import os

pathHere = os.getcwd()
print(pathHere)

def B2J(txtFile):
    
    # F= filedialog.askopenfilename()
    # if F  == None:
    #     return
    # file_path = filedialog.askdirectory()
    # if file_path  == None:
    #     return 
    # with open("D:/arkinght/autoupdata/activity_table.txt", "r") as f:
    # print(file_path)
    # return 
    
    for f in txtFile:
        if "display_meta_table.txt" in f:
            continue
        if "data_version.txt" in f:
            continue
        input_file = open(f, 'br')
        try:
            reading = (input_file.read())
            datas = bson.BSON.decode(reading)
            output_file = open(str(f).replace("txt","json"), 'w',encoding='utf-8')
            json.dump(datas, output_file,ensure_ascii=False)
            input_file.close()
            output_file.close()
        except:
            print(f)
    txt = open(pathHere+'\\txt.txt','w',encoding='utf-8') 
    for f in range(len(txtFile)):
        print(f'{txtFile[f]}',file=txt)
    txt.close()
    print("完成")
    lable_str.set('OK!')
    return

    
    # f = open("D:/arkinght/autoupdata/activity_table.txt", "r")


def FileOpen():
    lable_str.set('wait')
    F=fs.Opendir()
    txtfile = fs.FileSearch(F,filetypes=["*.txt"])
    B2J(txtFile=txtfile)
        

# 設定一個win視窗物件
win = tk.Tk()
# title
win.title("BSON轉JSON")
# 大小
win.geometry('800x400')
#可調整大小
win.resizable(True, True)

fm = tk.Frame(win)

# I = tk.Entry(fm)
# I.pack(padx=20,pady=10)
btnstr = tk.StringVar() # 初始化tk的字串變數
lable_str = tk.StringVar() # 初始化tk的字串變數
lable_str.set('')
btnstr.set('選擇資料夾')
btn = tk.Button(fm,textvariable=btnstr, font=('微軟正黑體', 20), command=FileOpen)
lab = tk.Label(fm,textvariable=lable_str, font=('微軟正黑體', 35))

btn.pack()
lab.pack()
fm.pack(expand=True)




# 啟動語 城市要寫在上面
win.mainloop()

