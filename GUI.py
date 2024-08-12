import tkinter as tk
from tkinter import filedialog, messagebox
from restorer import restorer  # 逻辑函数：图片恢复
from filter import fliter # 逻辑函数：图片筛重

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("图片处理工具")

        # 创建 StringVar 实例来设置和获取文本框的默认值
        self.input_path_var = tk.StringVar(value=".\\input")
        self.output_path_var = tk.StringVar(value=".\\output")
        self.gallery_path_var = tk.StringVar(value=".\\gallery")

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

        # 执行图片还原操作
        self.restore_button = tk.Button(root, text="图片恢复", command=self.restore_images)
        self.restore_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # 执行图片筛重操作
        self.duplicate_button = tk.Button(root, text="图片筛重", command=self.filter_images)
        self.duplicate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

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

        if not input_dir or not output_dir:
            messagebox.showerror("错误", "请输入正确的路径！")
            return

        try:
            do = restorer(input_dir, output_dir, 'chrome')
            do.do()
            messagebox.showinfo("完成", "图片恢复完成！")
        except Exception as e:
            messagebox.showerror("错误", f"图片恢复失败: {e}")

    def filter_images(self):
        output_dir = self.output_path.get()
        gallery_dir = self.gallery_path.get()

        if not output_dir or not gallery_dir:
            messagebox.showerror("错误", "请输入正确的路径！")
            return

        try:
            do = fliter(output_dir, gallery_dir)
            do.do()
            messagebox.showinfo("完成", "图片筛重完成！")
        except Exception as e:
            messagebox.showerror("错误", f"图片筛重失败: {e}")