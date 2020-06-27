import os
import datetime
import zipfile
import shutil


def mkZip(startdir):
    file_news = startdir + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  #参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        print(dirpath)
        fpath = dirpath.replace(
            startdir,
            startdir.split('/')[-1])  #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  #这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    print('%s  压缩成功' % startdir)
    z.close()


# 原文链接：https://blog.csdn.net/qq_24495287/java/article/details/84799512


def unZip(file_name, upload_path):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(os.path.join(upload_path, file_name))
    file_name_pre = file_name.split('.')[0]
    restore_path = os.path.join(upload_path, file_name_pre)

    if not os.path.exists(restore_path):
        os.makedirs(restore_path)
    for names in zip_file.namelist():
        zip_file.extract(names, restore_path)
    zip_file.close()
    return restore_path


# 原文链接：https://blog.csdn.net/qq_24495287/java/article/details/84799512

if __name__ == "__main__":
    print(os.path.dirname(__file__))
    startdir = "J:/nz/wx/nz_wx_server_v1.1.23_2020"  #要压缩的文件夹路径
    mkZip(startdir)
