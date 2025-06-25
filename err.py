import tkinter as tk
def err():
    root = tk.Tk()
    root.geometry("300x200")

    # 创建一个标签控件
    label = tk.Label(root, text="steamAPI或者AppID输入错误", font=("Arial", 14))
    label.pack(pady=10)

    # # 点击按钮刷新文字
    # def update_text():
    #     label.config(text="这是新的内容")

    # btn = tk.Button(root, text="刷新文字", command=update_text)
    # btn.pack()

    root.mainloop()
