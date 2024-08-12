import GUI
import tkinter as tk
'''
restorer初始化需要浏览器种类作为参数，目前只支持firefox和chrome且方法没有本质区别，所以在GUI中创建restorer时填入了chrome
'''
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI.GUI(root)
    root.mainloop()