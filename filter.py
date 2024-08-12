import hashlib
import os
import shutil

class fliter:
    '''
    通过对图片的md5值进行对比来筛选重复的图片
    '''
    gallery_path = ''
    output_path = '' # 约定上一个程序还原的图片输出的位置为output_path
    md5_record_file_name = 'md5 record.txt' # 该文件位于gallery_path内
    duplicate_images_floder_name = 'duplicate images' # 该文件夹位于output_path内

    def __init__(self, output_path, gallery_path):
        self.output_path = output_path
        self.gallery_path = gallery_path

    def do(self):
        # 获取gallery中所有图片的MD5值
        image_md5_dict = self.get_gallery_images_md5()

        # 把上述md5值与图片的对应关系保存到文件
        self.save_md5_to_file(image_md5_dict)

        # 从上述文件加载对应关系
        md5_image_dict = self.read_md5_from_record()

        # 一一计算还原的图片的md5值，与记录的gallery中的md5值比对确定是否重复，移动重复图片
        self.find_and_move_duplicates(md5_image_dict)

    def calculate_md5(self, file_path):
        """计算文件的MD5值"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_gallery_images_md5(self):
        """遍历文件夹及其子文件夹，计算所有图片文件的MD5值"""
        image_md5_dict = {}
        for root, dirs, files in os.walk(self.gallery_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    file_path = os.path.join(root, file)
                    image_md5_dict[file_path] = self.calculate_md5(file_path) # 以路径为键，MD5值为值，构造image_md5_dict
        return image_md5_dict

    def save_md5_to_file(self, image_md5_dict):
        output_file_path = os.path.join(self.gallery_path, self.md5_record_file_name)
        """将路径与MD5值的对应关系保存到文件中"""
        with open(output_file_path, "w") as f:
            for path, md5 in image_md5_dict.items():
                f.write(f"{path}\t{md5}\n")
    
    def read_md5_from_record(self):
        md5_image_dict = {}
        record_file_path = os.path.join(self.gallery_path, self.md5_record_file_name)
        with open(record_file_path, "r") as f:
            for line in f:
                path, md5 = line.strip().split("\t")
                md5_image_dict[md5] = path  # 以MD5值为键，路径为值，读取md5_image_dict
        return md5_image_dict

    def find_and_move_duplicates(self, md5_image_dict):
        duplicate_folder = os.path.join(self.output_path, self.duplicate_images_floder_name)
        """查找并移动重复的图片"""
        if not os.path.exists(duplicate_folder):
            os.makedirs(duplicate_folder)

        for root, dirs, files in os.walk(self.output_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    file_path = os.path.join(root, file)
                    md5_value = self.calculate_md5(file_path)

                    if md5_value in md5_image_dict:
                        print(f"找到重复的图片: {file_path}")
                        shutil.move(file_path, os.path.join(duplicate_folder, file))