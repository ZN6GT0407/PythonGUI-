import tkinter as tk
from tkinter import ttk, StringVar, Entry, OptionMenu, Label, Button, messagebox
import datetime,io,os,sys,threading,base64,webbrowser
from PIL import Image, ImageTk
from GMS2_GET import SetHeartBeat,carbox1,carbox2,TestRlyVCP,RlyVCPApp_Main

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("登入介面範例")  # 設定窗口標題
        self.root.geometry('300x300')  # 設定窗口大小
        self.root.resizable(False, False)  # 禁止調整窗口大小
        # 判斷是否為打包後的執行檔，獲取相應的目錄
        if getattr(sys, 'frozen', False):
            script_dir = sys._MEIPASS
        else:
            script_dir = os.path.dirname(__file__)
        # 設定圖標、狗狗圖片的路徑
        icon_path = os.path.join(script_dir, '.ico')
        dog_path = os.path.join(script_dir, '.png')
        # 讀取圖標並設定
        with open(icon_path, 'rb') as icon_file:
            icon_data = base64.b64encode(icon_file.read()).decode('utf-8')
        self.root.iconbitmap(icon_path)
        # 讀取狗狗圖片
        with open(dog_path, 'rb') as dog_file:
            dog_data = base64.b64encode(dog_file.read()).decode('utf-8')
        decoded_dog = base64.b64decode(dog_data)
        dog = Image.open(io.BytesIO(decoded_dog))
        self.tk_dog = ImageTk.PhotoImage(dog)
        # 設定狗狗圖片 Label
        self.dog_img = Label(self.root, image=self.tk_dog, width=350, height=350)
        self.dog_img.place(x=150, y=150, anchor=tk.CENTER)
        # 設定用戶名標籤、輸入框
        self.username_label = tk.Label(root, text='Username:')
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        # 設定密碼標籤、輸入框（顯示為*）
        self.password_label = tk.Label(root, text='Password:')
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()
        # 設定登入按鈕，點擊時執行 check_login 函數
        self.login_button = tk.Button(root, text='Login', command=self.check_login)
        self.login_button.pack()
    def check_login(self):
        # 在這裡實現你的登入驗證邏輯
        # 這裡使用的僅是示範帳號和密碼，請根據實際需求修改
        username = "admin"
        password = "admin" 
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        if entered_username == username and entered_password == password:
            # 登入成功，顯示主應用程式視窗
            self.root.destroy()  # 關閉登入視窗
            new_root = tk.Tk()
            app = ex(new_root)  # 建立新的應用程式視窗
            new_root.mainloop()  # 啟動應用程式視窗
        else:
            messagebox.showerror("Login failed", "登入失敗，請檢查帳號和密碼！")
            self.password_entry.delete(0, 'end')  # 清除密碼欄
class ex:
    def __init__(self, root):
        self.root = root
        self.root.title("範例主程式")  # 設定窗口標題
        self.root.geometry('340x660')  # 設定窗口大小
        self.root.resizable(False, False)  # 禁止調整窗口大小
        # 判斷是否為打包後的執行檔，獲取相應的目錄
        if getattr(sys, 'frozen', False):
            script_dir = sys._MEIPASS
        else:
            script_dir = os.path.dirname(__file__)
        # 設定圖標、圖片、Logo、動畫的路徑
        icon_path = os.path.join(script_dir, 'ico')
        image_path = os.path.join(script_dir, 'png')
        logo_path = os.path.join(script_dir, "png")
        fight_path = os.path.join(script_dir, "gif")
        # 讀取圖標並設定
        with open(icon_path, 'rb') as icon_file:
            icon_data = base64.b64encode(icon_file.read()).decode('utf-8')
        self.root.iconbitmap(icon_path)
        # 讀取主要圖片
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        decoded_image = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(decoded_image))
        # 讀取Logo
        with open(logo_path, 'rb') as logo_file:
            logo_data = base64.b64encode(logo_file.read()).decode('utf-8')
        decoded_logo = base64.b64decode(logo_data)
        logo = Image.open(io.BytesIO(decoded_logo))
        # 讀取動畫
        with open(fight_path, 'rb') as fight_file:
            fight_data = base64.b64encode(fight_file.read()).decode('utf-8')
        decoded_fight = base64.b64decode(fight_data)
        fight = Image.open(io.BytesIO(decoded_fight))
        # 設定時區、時間變數、並顯示當前時間
        self.GMT = datetime.timezone(datetime.timedelta(hours=8))
        self.clock = StringVar()
        Label(self.root, text='現在時間(GMT+8)', fg='brown3', font=('Arial', 20)).pack()
        Label(self.root, textvariable=self.clock, fg='brown3', font=('Arial', 20)).pack()
        self.showTime()
        # 創建 notebook 並添加分頁
        self.create_notebook()
        # 設定 圖片
        self.tk_P = ImageTk.PhotoImage(image)
        self.P_img = Label(self.root, image=self.tk_P, width=210, height=30)
        self.P_img.place(x=170, y=400, anchor=tk.CENTER)
        self.P_img.bind("<Button-1>", self.open_link)
        # 設定 Logo 圖片
        self.tk_Logo = ImageTk.PhotoImage(logo)
        self.Logo_img = Label(self.root, image=self.tk_Logo, width=80, height=20)
        self.Logo_img.place(x=300, y=435, anchor=tk.CENTER)
        # 設定動畫 Label、frames、並啟動動畫更新
        self.tk_fight = ImageTk.PhotoImage(fight)
        self.fight_gif = Label(self.root, image=self.tk_fight, width=250, height=200)
        self.fight_gif.place(x=170, y=550, anchor=tk.CENTER)
        self.fight_frames = []
        self.load_frames(fight)
        self.current_frame = 0
        self.update_label()
    def open_link(self, event):
        # 在此設定你要開啟的超連結
        url = "https://www.ex.com.tw/"
        webbrowser.open(url)
    def load_frames(self, gif):
        try:
            # 不斷讀取 GIF 的每一幀，並將其轉換為 PhotoImage 對象，然後將其添加到 frames 列表中
            while True:
                gif.seek(len(self.fight_frames))
                frame = ImageTk.PhotoImage(gif.copy())
                self.fight_frames.append(frame)
        except EOFError:
            # 當 GIF 達到結尾時，捕獲 EOFError
            pass

    def update_label(self):
        # 更新 Label 上顯示的圖片，實現動畫效果
        self.fight_gif.configure(image=self.fight_frames[self.current_frame])
        self.current_frame += 1
        self.current_frame %= len(self.fight_frames)  # 循環顯示 frames 中的圖片
        self.root.after(30, self.update_label)  # 遞迴調用自身，實現動畫的更新頻率30
    def create_notebook(self):
        # 創建一個 ttk.Notebook，用於建立選項卡式的介面
        self.notebook = ttk.Notebook(self.root)
        # 創建第一個選項卡的 Frame，用於後端更新相關設定
        self.setup_frame = ttk.Frame(self.notebook)
        self.setup_frame.pack()
        # 創建第二個選項卡的 Frame，用於Carbox.dat下載相關設定
        self.setup_frame1 = ttk.Frame(self.notebook)
        self.setup_frame1.pack()
        # 創建第三個選項卡的 Frame，用於VCP_Device 相關設定
        self.setup_frame2 = ttk.Frame(self.notebook)
        self.setup_frame2.pack()  
        # 在 ttk.Notebook 中新增第一個選項卡，標題為 "後端更新"
        self.notebook.add(self.setup_frame, text="範例介面1")
        self.create_setup_page()  # 創建 "後端更新" 選項卡的內容頁面
        # 在 ttk.Notebook 中新增第二個選項卡，標題為 "Carbox.dat下載"
        self.notebook.add(self.setup_frame1, text="範例介面2")
        self.create_setup_page1()  # 創建 "Carbox.dat下載" 選項卡的內容頁面
        # 在 ttk.Notebook 中新增第三個選項卡，標題為 "VCP_Device"
        self.notebook.add(self.setup_frame2, text="範例介面3")
        self.create_setup_page2()  # 創建 "VCP_Device" 選項卡的內容頁面
        # 設定 ttk.Notebook 在主視窗中的擴展與填充方式
        self.notebook.pack(expand=1, fill='both')
    def create_setup_page(self):
        # 在 self.setup_frame 中添加所有 "後端更新" 页面的控件
        self.IP_label = Label(self.setup_frame, text='IP:')
        self.IP_label.place(x=97, y=20, anchor=tk.CENTER)
        self.SetUpIPvar = StringVar(self.setup_frame)
        self.SetUpIPvar.set("範例:http://192.168.1.1/")
        self.SetUpIPentry = Entry(self.setup_frame, textvariable=self.SetUpIPvar, fg="gray")
        self.SetUpIPentry.place(x=180, y=20, anchor=tk.CENTER)
        self.SetUpIPentry.bind("<FocusIn>", self.on_entry_focus_in_out)
        self.SetUpIPentry.bind("<FocusOut>", self.on_entry_focus_in_out)

        self.NAME_label = Label(self.setup_frame, text='帳號:')
        self.NAME_label.place(x=90, y=60, anchor=tk.CENTER)
        self.SetUpNAMEvar = StringVar(self.setup_frame)
        self.SetUpNAMEentry = Entry(self.setup_frame, textvariable=self.SetUpNAMEvar)
        self.SetUpNAMEentry.place(x=180, y=60, anchor=tk.CENTER)

        self.PWD_label = Label(self.setup_frame, text='密碼:')
        self.PWD_label.place(x=90, y=100, anchor=tk.CENTER)
        self.SetUpPWDvar = StringVar(self.setup_frame)
        self.SetUpPWDentry = Entry(self.setup_frame, textvariable=self.SetUpPWDvar)
        self.SetUpPWDentry.place(x=180, y=100, anchor=tk.CENTER)

        self.TYPE_label = Label(self.setup_frame, text='XXX:')
        self.TYPE_label.place(x=80, y=140, anchor=tk.CENTER)
        self.SetUpTYPEvar = StringVar(self.setup_frame)
        self.SetUpTYPEvar.set("--XXX--")
        self.TYPE_menu = OptionMenu(self.setup_frame, self.SetUpTYPEvar, "A", "B", "C", command=self.update_set_menu)
        self.TYPE_menu.config(width=12, fg='#0000CD', bg='cornsilk1', font="Arial 12")
        self.TYPE_menu.place(x=180, y=140, anchor=tk.CENTER)

        self.SET_label = Label(self.setup_frame, text='設定XXX:')
        self.SET_label.place(x=77, y=180, anchor=tk.CENTER)
        self.SET_menu_var = StringVar(self.setup_frame)
        self.SET_menu_var.set("--XXX--")
        self.SET_menu = OptionMenu(self.setup_frame, self.SET_menu_var, "1", "2", "3", "4", "5", "6", "7", "8")
        self.SET_menu.config(width=12, fg='#458B00', bg='cornsilk1', font="Arial 12")
        self.SET_menu.place(x=180, y=180, anchor=tk.CENTER)

        self.NUM_label = Label(self.setup_frame, text='OOO:')
        self.NUM_label.place(x=90, y=220, anchor=tk.CENTER)
        self.SetUpNUMvar = StringVar(self.setup_frame)
        self.SetUpNUMentry = Entry(self.setup_frame, textvariable=self.SetUpNUMvar)
        self.SetUpNUMentry.place(x=180, y=220, anchor=tk.CENTER)

        self.SetUpOKbutton = Button(self.setup_frame, text='確定', command=self.SUPOKbutton_event)
        self.SetUpOKbutton.place(x=167, y=260, anchor=tk.CENTER)

    def create_setup_page1(self):
        # 在 self.setup_frame1 中添加所有 "Carbox.dat下載" 页面的控件
        self.CBIPvar = StringVar()
        self.CBIPvar.set("範例:http://192.168.1.1/")
        self.CBNAMEvar = StringVar()
        self.CBPWDvar = StringVar()
        self.CBDevice_IDvar = StringVar()

        self.CBIP_label = Label(self.setup_frame1, text='ZZZ:')
        self.CBIP_label.place(x=97, y=20, anchor=tk.CENTER)
        self.CBIP_entry = Entry(self.setup_frame1, textvariable=self.CBIPvar, fg="gray")
        self.CBIP_entry.place(x=180, y=20, anchor=tk.CENTER)
        # 绑定获得焦点和失去焦点的事件
        self.CBIP_entry.bind("<FocusIn>", self.on_entry_focus_in_out)
        self.CBIP_entry.bind("<FocusOut>", self.on_entry_focus_in_out)
        
        self.NAME_label = Label(self.setup_frame1, text='帳號:')
        self.NAME_label.place(x=90, y=80, anchor=tk.CENTER)
        self.NAME_entry = Entry(self.setup_frame1, textvariable=self.CBNAMEvar)
        self.NAME_entry.place(x=180, y=80, anchor=tk.CENTER)

        self.PWD_label = Label(self.setup_frame1, text='密碼:')
        self.PWD_label.place(x=90, y=140, anchor=tk.CENTER)
        self.PWD_entry = Entry(self.setup_frame1, textvariable=self.CBPWDvar)
        self.PWD_entry.place(x=180, y=140, anchor=tk.CENTER)

        self.Device_ID_label = Label(self.setup_frame1, text='QQQ:')
        self.Device_ID_label.place(x=85, y=200, anchor=tk.CENTER)
        self.Device_ID_entry = Entry(self.setup_frame1, textvariable=self.CBDevice_IDvar)
        self.Device_ID_entry.place(x=180, y=200, anchor=tk.CENTER)

        self.GMSOK_button = Button(self.setup_frame1, text='B1', command=self.GMSCBOKbutton_event)
        self.GMSOK_button.place(x=140, y=240, anchor=tk.CENTER)
        self.GMS2OK_button = Button(self.setup_frame1, text="B2", command=self.GMS2CBOKbutton_event)
        self.GMS2OK_button.place(x=210, y=240, anchor=tk.CENTER)
    
    def create_setup_page2(self):
        self.VCPIDvar = StringVar()
        self.VCPIDvar.set("EXEX")
        self.VCPNAMEvar = StringVar()
        self.VCPPWDvar = StringVar()
        
        self.VCPDevice_ID_label = Label(self.setup_frame2, text='ZZZ:')
        self.VCPDevice_ID_label.place(x=95, y=80, anchor=tk.CENTER)
        self.VCPDevice_ID_entry = Entry(self.setup_frame2, textvariable=self.VCPIDvar, fg="gray")
        self.VCPDevice_ID_entry.place(x=180, y=80, anchor=tk.CENTER)
        self.VCPDevice_ID_entry.bind("<FocusIn>", self.on_entry_focus_in_out1)
        self.VCPDevice_ID_entry.bind("<FocusOut>", self.on_entry_focus_in_out1)
        
        self.VCPNAME_label = Label(self.setup_frame2, text='帳號:')
        self.VCPNAME_label.place(x=90, y=140, anchor=tk.CENTER)
        self.VCPNAME_entry = Entry(self.setup_frame2, textvariable=self.VCPNAMEvar)
        self.VCPNAME_entry.place(x=180, y=140, anchor=tk.CENTER)

        self.VCPPWD_label = Label(self.setup_frame2, text='密碼:')
        self.VCPPWD_label.place(x=90, y=200, anchor=tk.CENTER)
        self.VCPPWD_entry = Entry(self.setup_frame2, textvariable=self.VCPPWDvar)
        self.VCPPWD_entry.place(x=180, y=200, anchor=tk.CENTER)


        self.VCPOK_button = Button(self.setup_frame2, text='B3', command=self.VCPOKbutton_event)
        self.VCPOK_button.place(x=130, y=260, anchor=tk.CENTER)
        self.VCPSET_button = Button(self.setup_frame2, text='B4', command=self.VCPSETbutton_event)
        self.VCPSET_button.place(x=210, y=260, anchor=tk.CENTER)
    def on_entry_focus_in_out(self, event):
        # 定義範例文字
        example_text = "範例:http://192.168.1.1/"
        # 當輸入框內容等於範例文字時
        if event.widget.get() == example_text:
            # 清空輸入框內容
            event.widget.delete(0, 'end')
            # 設定文字顏色為黑色
            event.widget.config(fg="black")  
        # 當輸入框內容為空時
        elif not event.widget.get():
            # 插入範例文字到輸入框
            event.widget.insert(0, example_text)
            # 設定文字顏色為灰色
            event.widget.config(fg="gray")
    def on_entry_focus_in_out1(self, event):
        example_text = "EXEX"
        if event.widget.get() == example_text:
            event.widget.delete(0, 'end')
            event.widget.config(fg="black")
        elif not event.widget.get():
            event.widget.insert(0, example_text)
            event.widget.config(fg="gray")

    def update_set_menu(self, *args):#*args可以傳遞0個或多個函數，且不一定要使用
        # 更新設定選單的內容
        selected_type = self.SetUpTYPEvar.get()
        # 獲取用戶選擇的設定類型
        if selected_type == "A":
            # 如果選擇的是網絡設定
            options = ["1", "2"]
        elif selected_type == "B":
            # 如果選擇的是編碼設定
            options = ["3", "4", "5", "6"]
        elif selected_type == "C":
            # 如果選擇的是系統設定
            options = ["7", "8"]
        else:
            # 如果選擇的設定類型未知或為空
            options = []    
        # 清空原有的選單項目0是第0位址到end最後
        self.SET_menu['menu'].delete(0, 'end')
        # 將新的選項添加到選單中
        for option in options:
            self.SET_menu['menu'].add_command(label=option, command=tk._setit(self.SET_menu_var, option))
    def SUPOKbutton_event(self):
        if self.SetUpIPvar.get() == '':
            tk.messagebox.showerror('message', '未輸入AAA')
        elif self.SetUpIPvar.get() != "":
            print(self.SetUpIPvar.get())
        else:
            tk.messagebox.showerror('message', 'AAA錯誤')
        if self.SetUpNAMEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入帳號')
        elif self.SetUpNAMEvar.get() != "":
            print(self.SetUpNAMEvar.get())
        else:
            tk.messagebox.showerror('message', '帳號錯誤')
        if self.SetUpPWDvar.get() == '':
            tk.messagebox.showerror('message', '未輸入密碼')
        elif self.SetUpPWDvar.get() != "":
            print(self.SetUpPWDvar.get())
        else:
            tk.messagebox.showerror('message', '密碼錯誤')
        if self.SetUpTYPEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入OOO')
        elif self.SetUpTYPEvar.get() != "":
            print(self.SetUpTYPEvar.get())
        else:
            tk.messagebox.showerror('message', 'OOO參數錯誤')
        if self.SET_menu_var.get() == '':
            tk.messagebox.showerror('message', '未輸入OOO參數')
        elif self.SET_menu_var.get() != "":
            print(self.SET_menu_var.get())
        else:
            tk.messagebox.showerror('message', '設定OOO錯誤')
        if self.SetUpNUMvar.get() == '':
            tk.messagebox.showerror('message', '未輸入OOO')
        elif self.SetUpNUMvar.get() != "":
            print(self.SetUpNUMvar.get())
        else:
            tk.messagebox.showerror('message', '輸入OOO錯誤')
        
        # 创建一个线程来处理 SetHeartBeat 函数
        thread = threading.Thread(target=self.call_OIUOU)
        thread.start()


    def OKbutton_event(self):
        if self.CBIPvar.get() == "":
            tk.messagebox.showerror('message', '未輸入YTR')
        elif self.CBIPvar.get() != "":
            print("您輸入的QQQQ為:" + self.CBIPvar.get())
        else:
            tk.messagebox.showerror('message', 'YYYY錯誤')

        if self.CBNAMEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入帳號')
        elif self.CBNAMEvar.get() != "":
            print("您輸入的帳號為:" + self.CBNAMEvar.get())
        else:
            tk.messagebox.showerror('message', '帳號錯誤')

        if self.CBPWDvar.get() == '':
            tk.messagebox.showerror('message', '未輸入密碼')
        elif self.CBPWDvar.get() != "":
            print("您輸入的密碼為:" + self.CBPWDvar.get())
        else:
            tk.messagebox.showerror('message', '密碼錯誤')

        if self.CBDevice_IDvar.get() == '':
            tk.messagebox.showerror('message', '未輸入YYYY')
        elif self.CBDevice_IDvar.get() != "":
            print("您輸入的RYRY為:" + self.CBDevice_IDvar.get())
        else:
            tk.messagebox.showerror('message', 'YYYY錯誤')
        thread = threading.Thread(target=self.call_EYEYE)
        thread.start()
        
    def OKbutton_event1(self):
        if self.CBIPvar.get() == "":
            tk.messagebox.showerror('message', '未輸入QQQQQ')
        elif self.CBIPvar.get() != "":
            print("您輸入的QQQQQ為:" + self.CBIPvar.get())
        else:
            tk.messagebox.showerror('message', 'QQQQ錯誤')

        if self.CBNAMEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入帳號')
        elif self.CBNAMEvar.get() != "":
            print("您輸入的帳號為:" + self.CBNAMEvar.get())
        else:
            tk.messagebox.showerror('message', '帳號錯誤')

        if self.CBPWDvar.get() == '':
            tk.messagebox.showerror('message', '未輸入密碼')
        elif self.CBPWDvar.get() != "":
            print("您輸入的密碼為:" + self.CBPWDvar.get())
        else:
            tk.messagebox.showerror('message', '密碼錯誤')

        if self.CBDevice_IDvar.get() == '':
            tk.messagebox.showerror('message', '未輸入WWWWW')
        elif self.CBDevice_IDvar.get() != "":
            print("您輸入的WWWWW為:" + self.CBDevice_IDvar.get())
        else:
            tk.messagebox.showerror('message', 'WWWWW錯誤')
        thread = threading.Thread(target=self.call_LLILI)
        thread.start()
        
    def VCPOKbutton_event(self):
        if self.VCPIDvar.get() == "":
            tk.messagebox.showerror('message', '未輸入IIII')
        elif self.VCPIDvar.get() != "":
            print("您輸入的IIIII為:" + self.VCPIDvar.get())
        else:
            tk.messagebox.showerror('message', 'IIIII錯誤')

        if self.VCPNAMEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入帳號')
        elif self.VCPNAMEvar.get() != "":
            print("您輸入的帳號為:" + self.VCPNAMEvar.get())
        else:
            tk.messagebox.showerror('message', '帳號錯誤')

        thread = threading.Thread(target=self.call_OIOIP)
        thread.start()
    def VCPSETbutton_event(self):
        if self.VCPIDvar.get() == "":
            tk.messagebox.showerror('message', '未輸入OOOOO')
        elif self.VCPIDvar.get() != "":
            print("您輸入的OOOO為:" + self.VCPIDvar.get())
        else:
            tk.messagebox.showerror('message', 'OOOO錯誤')

        if self.VCPNAMEvar.get() == '':
            tk.messagebox.showerror('message', '未輸入帳號')
        elif self.VCPNAMEvar.get() != "":
            print("您輸入的帳號為:" + self.VCPNAMEvar.get())
        else:
            tk.messagebox.showerror('message', '帳號錯誤')
        
        thread = threading.Thread(target=self.call_TUTTTU)
        thread.start()
        
    def call_call_OIUOU(self):
        carbox1(self.CBIPvar.get(), self.CBNAMEvar.get(), self.CBPWDvar.get(), self.CBDevice_IDvar.get())

    def call_EYEYE(self):
        carbox2(self.CBIPvar.get(), self.CBNAMEvar.get(), self.CBPWDvar.get(), self.CBDevice_IDvar.get())

    def call_LLILI(self):
        SetHeartBeat(self.SetUpIPvar.get(), self.SetUpNAMEvar.get(), self.SetUpPWDvar.get(),
                      self.SetUpTYPEvar.get(), self.SET_menu_var.get(), self.SetUpNUMvar.get())
    def call_OIOIP(self):
        TestRlyVCP(self.VCPIDvar.get(), self.VCPPWDvar.get(), self.VCPNAMEvar.get())
    def call_TUTTTU(self):
        #使用after方法設定一個事件，使得RlyVCPApp_Main函數在主視窗更新之後0是0秒執行的意思
        #lambda: 是一個匿名函數的關鍵字。該函數不接受任何參數，並執行後面的表達式。
        self.root.after(0, lambda: RlyVCPApp_Main(self.VCPIDvar.get(), self.VCPPWDvar.get(), self.VCPNAMEvar.get()))
    def showTime(self):
        now = datetime.datetime.now(tz=self.GMT).strftime('%H:%M:%S')
        self.clock.set(now)
        self.root.after(1000, self.showTime)


if __name__ == "__main__":
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()