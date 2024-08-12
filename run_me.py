import GUI
import tkinter as tk
'''
restorer初始化需要浏览器种类作为参数，目前只支持firefox和chrome且方法没有本质区别，所以在GUI中创建restorer时填入了chrome
'''
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI.GUI(root)
    root.mainloop()

# import os
# '''
# 做什么？
# '''
# restore = True # 还原
# duplicate_check = False # 查重

# '''
# 参数设置
# '''
# # 【自行修改】缓存文件所在的路径
# input = '.\\input' # 【示例】
# # 【自行修改】输出图片的位置
# output = '.\\output' # 【示例】
# if not os.path.exists(output):
#     os.makedirs(output)
# # 【自行修改】图库路径
# gallery = '.\\gallery' # 【示例】

# '''
# 从浏览器的缓存文件中还原出图片
# '''
# if restore:
#     from restorer import restorer

#     # 缓存文件属于哪种浏览器（目前仅有firefox和chrome）
#     browser = 'chrome'

#     # 运行还原代码
#     task = restorer(input, output, browser)
#     task.do()

# '''
# 因为缓存中难免有之前已经保存过的图片，为了避免重复，可以把之前存过的图片作为图库
# 将还原出的图片与图库中的图片对比，把重复的图片移到output内一个新建文件夹中，方便整理
# '''
# if duplicate_check:
#     from filter import md5_check

#     test_class = md5_check(gallery, output)

#     test_class.do()
#     # 图库路径下会留下一个txt文件，记录图片和md5的对应关系，不想要的话请记得删除