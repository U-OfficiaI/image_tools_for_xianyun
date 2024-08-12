import json
import base64
import os
import datetime

class restorer:
    '''
    cache --> json --> image
    在各项check_files方法中，依据不同浏览器缓存文件的特点，逐一读取缓存文件，对合适的缓存文件进行 cache --> json 的转换
    随后立即调用json_2_image_output方法完成 json --> image
    '''

    cache_folder_path = ''
    output_folder_path = ''
    
    # TODO
    # 1.根据cache_folder_path，读取路径下的所有文件
    # 2.读取这些文件，从中筛选能够还原为图片的数据
    # 3.还原数据为图片，输出到output_folder_path

    def __init__ (self, json_folder_path, output_folder_path, browser):
        self.browser = browser
        self.cache_folder_path = json_folder_path
        self.output_folder_path = output_folder_path

    def do(self):
        if self.browser == 'firefox':
            self.firefox_check_files()
            return True
        elif self.browser == 'chrome':
            self.chrome_check_files()
            return True

    def firefox_check_files(self):
        '''
        input:
            none
        do:
            逐个检查json_folder_path中的文件，根据内容挑选出其中来自xianyun站的可以转换为图像的文件
            将这些文件的字典内容传递给json_2_image_output()处理
        output:
            True（成功检查完所有文件）
        '''
        # 获取cahce_folder_path目录下的所有缓存文件名称
        for filename in os.listdir(self.cache_folder_path):
            print('读取'+filename)

            with open(os.path.join(self.cache_folder_path, filename), 'rb') as file:
                '''
                firefox浏览器缓存文件的格式特征：缓存内容在前面，后面都会附有其他信息，并且不能被 UTF-8 编码
                所需要的缓存内容可以被UTF-8解码，并且能够以解析 json 字符串的方式解析为字典数据，因此可以利用这个特性获取需要的数据
                '''
                for line in file:
                    try:
                        # 逐行解码为 UTF-8 文本
                        line_decoded = line.decode('utf-8')
                        try:
                            # 解码为 UTF-8 文本后尝试以解析 json 的方式解析
                            json_data = json.loads(line_decoded)
                            # 解析到的内容不是字典类型数据就报错，因为我们需要的 json 一定是字典类型数据
                            if not isinstance(json_data, dict):
                                raise ValueError
                            # 检查字典类型数据是否有需要的内容，决定是否到json_2_image_output()中转换为图片
                            if 'completed_at' in json_data and 'image_base64' in json_data:
                                self.json_2_image_output(json_data)
                        except (json.JSONDecodeError, ValueError):
                            # 不能解析则报错，解析后不为字典类型数据也报错
                            continue
                    except UnicodeDecodeError:
                        # 遇到无法用 UTF-8 解码的行，停止解码
                        break
        return True

    def chrome_check_files(self):
        '''
        firefox浏览器缓存文件的格式特征：整个都是缓存内容
        所需要的缓存内容可以被UTF-8解码，并且能够以解析 json 字符串的方式解析为字典数据，因此可以利用这个特性获取需要的数据
        看起来思路似乎和firefox一样，并且更简单了
        '''
        self.firefox_check_files()
        return True

    def json_2_image_output(self, data):
        '''
        input:
            json的字典内容
        do:
            保存字典内容中储存的图像文件到output_folder_path（以字典内容中储存的时间命名）
        output:
            True（成功转换并保存图像）
        '''
        # 创建保存图片的目录
        save_dir = self.cache_folder_path
        os.makedirs(save_dir, exist_ok=True)

        # 提取 Base64 编码的图片数据与完成时间
        image_base64 = data['image_base64']
        completed_at = data['completed_at'] # 例："Mon, 17 Jun 2024 02:50:58 GMT"

        # 解码 Base64 数据
        image_data = base64.b64decode(image_base64)

        # 根据完成时间生成图片文件名称
        dt = datetime.datetime.strptime(completed_at, "%a, %d %b %Y %H:%M:%S %Z")
        new_name = dt.strftime("%Y-%m-%d %H-%M-%S")

        # 保存图片
        with open(self.output_folder_path+'\\'+new_name+'.png', 'wb') as image_file:
            image_file.write(image_data)

        print(f"Image saved to {self.output_folder_path+'\\'+new_name+'.png'}")
        return True
    
    def count(self):
        count = 0
        for file in os.listdir(self.cache_folder_path):
            file_path = os.path.join(self.cache_folder_path, file)
            if os.path.isfile(file_path):
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # 转换为MB
                if file_size_mb > 1:
                    count = count + 1
        return count