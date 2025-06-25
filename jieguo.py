import tkinter as tk
from tkinter import scrolledtext
def jieguo():
    root = tk.Tk()
    root.title("滚动文本演示")
    root.geometry("500x300")          # 窗口固定大小

    # 创建带自动滚动条的多行文本框
    outbox = scrolledtext.ScrolledText(root,
                                    wrap="word",     # 自动按单词换行
                                    font=("Arial", 11))
    outbox.pack(fill="both", expand=True)

    # 插入长文本
    with open("fanyi.txt", "r", encoding="utf-8") as f:
        long_text = "\n".join([line.strip() for line in f])
        outbox.insert("end", long_text)

    # 如果只读，最后锁定
    outbox.config(state="disabled")

    root.mainloop()
