'''
从浏览器的缓存文件中还原出图片
'''
from xianyun_json2image import json2image

# 【自行修改】缓存文件所在的路径
input = 'C:\\Users\\28013\\Desktop\\cache' # 【示例】

# 【自行修改】输出图片的位置
output = 'C:\\Users\\28013\\Desktop\\picture' # 【示例】

# 缓存文件属于哪种浏览器（目前仅有firefox和chrome）
browser = 'firefox'

# 运行还原代码
task = json2image(input, output, browser)
task.do()

'''
因为缓存中难免有之前已经保存过的图片，为了避免重复，可以把之前存过的图片作为图库
将还原出的图片与图库中的图片对比，把重复的图片移到output内一个新建文件夹中，方便整理
'''
from md5_check import md5_check

# 【自行修改】图库路径
gallery = 'C:\\Users\\28013\\Desktop\\gallery' # 【示例】

test_class = md5_check(gallery, output)

test_class.do()
# 图库路径下会留下一个txt文件，记录图片和md5的对应关系，不想要的话请记得删除