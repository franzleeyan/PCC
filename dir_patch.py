import os
import shutil


class Shear():

    def __int__(self):
        # 源目录
        self.src = ""
        # 目标目录
        self.dest = ""

    def start_shear(self, a_filepath):
        for a_item in os.listdir(a_filepath):
            a_absolute_path = os.path.join(a_filepath, a_item)
            is_file = os.path.isfile(a_absolute_path)
            is_dir = os.path.isdir(a_absolute_path)
            if is_file:
                if a_item == "数据传输日志.log":
                    pass
                else:
                    print(a_item)
            elif is_dir:
                if a_item == "回盘文件":
                    pass
                elif a_item == "已导入数据库":
                    pass
                else:
                    print("目录为--%s--的有一下文件:" % a_item)
                    shear.start_shear(a_absolute_path)


if __name__ == "__main__":
    shear = Shear()
    shear.start_shear(shear.src)
