import tkinter as tk
from tkinter import filedialog, messagebox
from restorer import restorer  # 逻辑函数：图片恢复
from filter import fliter # 逻辑函数：图片筛重

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("网站缓存还原小程序")

        # 创建 StringVar 实例来设置和获取文本框的默认值
        self.input_path_var = tk.StringVar(value=".\\input") # 定义默认值
        self.output_path_var = tk.StringVar(value=".\\output") # 定义默认值
        self.gallery_path_var = tk.StringVar(value=".\\gallery") # 定义默认值

        # Input路径选择
        self.input_label = tk.Label(root, text="Input文件夹路径:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_path = tk.Entry(root, width=50)
        self.input_path.grid(row=0, column=1, padx=10, pady=10)
        self.input_button = tk.Button(root, text="浏览...", command=self.browse_input)
        self.input_button.grid(row=0, column=2, padx=10, pady=10)

        # Output路径选择
        self.output_label = tk.Label(root, text="Output文件夹路径:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10)
        self.output_path = tk.Entry(root, width=50)
        self.output_path.grid(row=1, column=1, padx=10, pady=10)
        self.output_button = tk.Button(root, text="浏览...", command=self.browse_output)
        self.output_button.grid(row=1, column=2, padx=10, pady=10)

        # Gallery路径选择
        self.gallery_label = tk.Label(root, text="Gallery文件夹路径:")
        self.gallery_label.grid(row=2, column=0, padx=10, pady=10)
        self.gallery_path = tk.Entry(root, width=50)
        self.gallery_path.grid(row=2, column=1, padx=10, pady=10)
        self.gallery_button = tk.Button(root, text="浏览...", command=self.browse_gallery)
        self.gallery_button.grid(row=2, column=2, padx=10, pady=10)

        # 浏览器选择（单选按钮）
        self.option_label = tk.Label(root, text="选择缓存所属浏览器:")
        self.option_label.grid(row=3, column=0, padx=10, pady=10)
        self.selected_browser = tk.StringVar(value="chrome") # 定义默认值

        # 创建两个单选按钮
        self.browser_frame = tk.Frame(root)
        self.browser_frame.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky="w")
        
        self.radio_chrome = tk.Radiobutton(self.browser_frame, text="chrome", variable=self.selected_browser, value="chrome")
        self.radio_chrome.grid(row=0, column=0, padx=10, pady=5)

        self.radio_firefox = tk.Radiobutton(self.browser_frame, text="firefox", variable=self.selected_browser, value="firefox")
        self.radio_firefox.grid(row=0, column=1, padx=10, pady=5)

        # 执行图片还原操作
        self.restorer_button = tk.Button(root, text="图片恢复", command=self.restore_images)
        self.restorer_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # 执行图片筛重操作
        self.filter_button = tk.Button(root, text="图片筛重", command=self.filter_images)
        self.filter_button.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

        # 帮助区域的Frame
        self.help_frame = tk.Frame(root)
        self.help_frame.grid(row=5, column=0, columnspan=4, sticky='nsew')

        # 帮助内容
        help_text_for_restorer = "【图片恢复】\n图片恢复功能可以从浏览器缓存中恢复xianyun.cool内的图片\n［操作］\n在input中填入缓存文件的路径\n在output中填入想要保存恢复的图片的路径\n并选择缓存所属的浏览器类型\n"
        help_text_for_filter = "【图片筛重】\n考虑到缓存的图片可能有与先前已保存的图片重复的图片，这个功能可以结合先前保存的图片，筛选出output中与之重复的图片\n［操作］\n在output中填入已恢复的图片的路径\n在gallery中填入先前保存的图片所在的路径\n［注意］\n重复的图片会移到output下的duplicate images文件夹"
        self.help_content = tk.Label(self.help_frame, text=help_text_for_restorer+help_text_for_filter,
                                     wraplength=400, justify='left')
        self.help_content.grid(row=1, column=0, padx=10, pady=5, sticky='w')

    def browse_input(self):
        path = filedialog.askdirectory()
        if path:
            self.input_path.insert(0, path)

    def browse_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path.insert(0, path)

    def browse_gallery(self):
        path = filedialog.askdirectory()
        if path:
            self.gallery_path.insert(0, path)

    def restore_images(self):
        input_dir = self.input_path.get()
        output_dir = self.output_path.get()
           
        # 检查路径是否存在（这里可以根据实际需求进行更复杂的验证）
        do_return = False
        if not input_dir:
            self.input_path.configure(bg='#F07C82')
            do_return = True
        if not output_dir:
            self.output_path.configure(bg='#F07C82')
            do_return = True
        
        if do_return:
            return
        else:
            self.input_path.configure(bg='white')
            self.output_path.configure(bg='white')

        try:
            do = restorer(input_dir, output_dir, self.selected_browser.get())
            do.do()
            messagebox.showinfo("完成", "图片恢复完成！")
        except Exception as e:
            messagebox.showerror("错误", f"图片恢复失败: {e}")

    def filter_images(self):
        output_dir = self.output_path.get()
        gallery_dir = self.gallery_path.get()

        # 检查路径是否存在（这里可以根据实际需求进行更复杂的验证）
        do_return = False
        if not output_dir:
            self.output_path.configure(bg='#F07C82')
            do_return = True
        if not gallery_dir:
            self.gallery_path.configure(bg='#F07C82')
            do_return = True
        
        if do_return:
            return
        else:
            self.input_path.configure(bg='white')
            self.output_path.configure(bg='white')


        if not output_dir or not gallery_dir:
            messagebox.showerror("错误", "请输入正确的路径！")
            return

        try:
            do = fliter(output_dir, gallery_dir)
            do.do()
            messagebox.showinfo("完成", "图片筛重完成！")
        except Exception as e:
            messagebox.showerror("错误", f"图片筛重失败: {e}")