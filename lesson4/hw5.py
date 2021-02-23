import pathlib
import string
import sys
import os


изображения = []
видео_файлы = []
документы = []
музыка = []
прочее = []
формат = []    

def search(path):
    dir_path = []
    files = os.listdir(path)
    for file_or_dir in files:
        if os.path.isdir(path + os.path.sep + file_or_dir):
            dir_path.append(path + os.path.sep + file_or_dir)
        else:
            sort_by_type(file_or_dir)  
    while(dir_path):
        search(dir_path.pop())          

def sort_by_type(file_name):
    global изображения,видео_файлы,документы,музыка,прочее

    if file_name.endswith(('jpg', 'jpeg', 'png')):
        изображения.append(file_name)
    elif file_name.endswith(('avi', 'mp4', 'mov', 'flv', 'mkv')): 
        видео_файлы.append(file_name)
    elif file_name.endswith(('doc', 'docx', 'txt', 'pdf')):
        документы.append(file_name)
    elif file_name.endswith(('mp3', 'ogg', 'wav', 'amr')):
        музыка.append(file_name)
    else:
        прочее.append(file_name)

def main():
    path = 'E:\\Learning\\Всякое'

    search(path)
    print(f' Music :{музыка}')
    print(f' Document :{документы}')
    print(f' Pictures :{изображения}')
    print(f' Video :{видео_файлы}')
    print(f' Unknown :{прочее}')

if __name__ == "__main__":
       main()