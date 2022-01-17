#-*- coding: utf8 -*-
import tkinter
import time
import threading
import ctypes
import pyautogui 

####
# footSW
def footSW():
    ####
    #main
    #Foot Pedalに割り当てられたキーに対応する番号を入力。詳細はreadme.
    #deafultではF24キー、番号：0x87
    aimkey = 0x87
    aimkeyName = "F24"

    try:
        while True:
            #Foot pedalにF24キーを割り当て
            #0x87=F24キー
            if ctypes.windll.user32.GetAsyncKeyState(aimkey) == 0x8000:
                #F24が押されたら以下の処理を実行
                print(aimkeyName)
                #なんでこのsleepが必要かは謎。
                pyautogui.sleep(0.2)
                pyautogui.hotkey("ctrl", "s")
                #モニタ上に保存処理が実施されている事を表示
                time.sleep(1)
                pyautogui.press("return")
                #誤動作防止の為にペダルを3秒間無効化
                time.sleep(3)
            #escキーでプログラム終了
            elif ctypes.windll.user32.GetAsyncKeyState(0x1B) == 0x8000:
                print("Esc")
                break
        pyautogui.alert(text="footSW-annotation has finished normally", timeout=2000)
        print("footSW-annotation has Finished Normally")
        exit()
    except KeyboardInterrupt:
        print("exit1")
        exit()
####
# ボタンクリック後の動作
def outputEsc():
    print("esc")
    pyautogui.press("esc")  

####
# GUI設定
def thread_mainGUI():
    # Windowの設定
    root = tkinter.Tk()
    root.title("footSW-annotation")
    root.geometry("240x135")
    # ラベル表示
    var = tkinter.StringVar()
    var.set("実行中")
    label = tkinter.Label(root, textvariable=var)
    label.pack()
    # ボタン表示と押された際の処理
    button = tkinter.Button(root, text='終了',command=outputEsc)
    button.pack()
    # mainloop
    root.mainloop()
    
####
#Thread開始
thread1 = threading.Thread(target=thread_mainGUI)
thread1.setDaemon(True)
thread1.start()
print("Thread START")

#mainGUI開始
footSW()






