



import tkinter as tk
from tkinter import ttk, messagebox
from chengJiu import get_chengjiu
from jieguo import jieguo
from err import err

class SteamHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam Info Input")
        self.root.geometry("600x350")  # 跟之前差不多大小

        # 左上角按钮框架
        btn_frame = ttk.Frame(root)
        btn_frame.pack(anchor="nw", padx=10, pady=10)

        self.api_btn = ttk.Button(btn_frame, text="Steam API 获取", width=12, command=self.open_api_info)
        self.api_btn.pack(side="left", padx=(0, 8))

        self.id_btn = ttk.Button(btn_frame, text="Steam ID 获取", width=12, command=self.open_id_info)
        self.id_btn.pack(side="left")

        # 主体内容框架
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Steam API Key 输入
        ttk.Label(main_frame, text="请输入 Steam API Key:", font=("Arial", 12)).pack(anchor="w", pady=(0, 6))
        self.api_key_var = tk.StringVar()
        self.api_entry = ttk.Entry(main_frame, textvariable=self.api_key_var, font=("Arial", 11))
        self.api_entry.pack(fill="x", pady=(0, 20))

        # Steam AppID 输入
        ttk.Label(main_frame, text="请输入 Steam AppID:", font=("Arial", 12)).pack(anchor="w", pady=(0, 6))
        self.appid_var = tk.StringVar()
        self.appid_entry = ttk.Entry(main_frame, textvariable=self.appid_var, font=("Arial", 11))
        self.appid_entry.pack(fill="x", pady=(0, 20))

        # 你可以加个按钮开始后续操作
        self.start_btn = ttk.Button(main_frame, text="开始", command=self.start_action)
        self.start_btn.pack(pady=10)

    def open_api_info(self):
        self.open_info_window("Steam API Key 获取说明",
            "1. 登录 https://steamcommunity.com/dev/apikey\n"
            "2. 注册你的域名并获取 API Key\n"
            "3. 把 API Key 填入上方输入框")

    def open_id_info(self):
        self.open_info_window("Steam ID 获取说明",
            "1. 访问 https://steamid.io/\n"
            "2. 输入你的个人主页链接，获取 SteamID\n"
            "3. 把 SteamID 填入对应输入框（如果需要）")

    def open_info_window(self, title, content):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("400x250")
        win.resizable(False, False)
        label = ttk.Label(win, text=content, font=("Arial", 11), justify="left")
        label.pack(padx=15, pady=15, fill="both", expand=True)
        ttk.Button(win, text="关闭", command=win.destroy).pack(pady=10)

    def start_action(self):
        API_KEY = self.api_key_var.get().strip()
        APP_ID = self.appid_var.get().strip()

        if not API_KEY:
            messagebox.showwarning("输入错误", "Steam API Key 不能为空")
            return
        if not APP_ID:
            messagebox.showwarning("输入错误", "Steam AppID 不能为空")
            return
        
        # 这里你填你的后续逻辑，比如保存，调用API等
        messagebox.showinfo("提示", f"API Key: {API_KEY}\nAppID: {APP_ID}\n\n开始执行后续操作...\n点击“确认”后请等待一会~")
        try:
            get_chengjiu(API_KEY, APP_ID)
            jieguo()
        except:
            err()

if __name__ == "__main__":
    root = tk.Tk()
    app = SteamHelperApp(root)
    root.mainloop()
