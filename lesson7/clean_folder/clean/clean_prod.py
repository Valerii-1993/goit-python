import pathlib
import string
import sys
import os
import re
import shutil


New_PATH = ''

folders = ['images', 'videos', 'documents', 'music', 'else_format']
imgs = ['.jpg', '.png', '.jpeg']
docs= ['.pdf', '.docx', '.txt', '.xlsx']
music = ['.mp3', '.ogg', '.wav', '.amr']
videos = ['.mkv', '.flv', '.avi']

def normalize(your_put):
    map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ж'): 'j',\
    ord('з'): 'z', ord('и'): 'i', ord('й'): 'j', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',\
    ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'):'ts', ord('ч'):'ch',\
    ord('ш'):'sh',ord('щ'):'shch',ord('ъ'):'y',ord('ы'):'y',ord('ь'):"'",ord('э'):'e',ord('ю'):'yu',ord('я'):'ya',\
    ord('А'):'A',ord('Б'):'B',ord('В'):'V',ord('Г'):'G',ord('Д'):'D',ord('Е'):'E',ord('Ё'):'Yo',ord('Ж'):'Zh',\
    ord('З'):'Z',ord('И'):'I',ord('Й'):'J',ord('К'):'K',ord('Л'):'L',ord('М'):'M',ord('Н'):'N',ord('О'):'O',\
    ord('П'):'P',ord('Р'):'R',ord('С'):'S',ord('Т'):'T',ord('У'):'U',ord('Ф'):'F',ord('Х'):'H',ord('Ц'):'Ts',\
    ord('Ч'):'Ch',ord('Ш'):'Sh',ord('Щ'):'Shch',ord('Ъ'):'Y',ord('Ы'):'Y',ord('Ь'):"'",ord('Э'):'E',\
    ord('Ю'):'Yu',ord('Я'):'Ya',}
    
    translate_name = your_put.translate(map)
    str_translate_name = ''
    
    for name in translate_name:
        
        if name.isalpha() or name.isnumeric() or name == "'":
            str_translate_name = str_translate_name + name
        else:
            name = '_'
            str_translate_name = str_translate_name+name
        global final_results_string    
        final_results_string = str_translate_name
        
    return final_results_string


def create_folder():

    for name in folders:
        directory = os.path.join(New_PATH, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


def transfer_file(files_info):

    create_folder()
    info = files_info.split(";")
    src = os.path.join(info[1], info[2]+info[3])
    dest = os.path.join(New_PATH, info[0], normalize(info[2])+info[3])

    if info[0] == 'archives':
        shutil.unpack_archive(shutil.move(src, dest),
                              os.path.join(New_PATH, info[0]))
        os.remove(dest)
    else:
        shutil.move(src, dest)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


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


def distribute_file(collection, path, nesting):

    for files in collection:
        file_name, file_extension = os.path.splitext(files)
        if file_extension in imgs:
            transfer_file(f'images;{path};{file_name};{file_extension}')
        elif file_extension in docs:
            transfer_file(f'documents;{path};{file_name};{file_extension}')
        elif file_extension in music:
            transfer_file(f'music;{path};{file_name};{file_extension}')
        elif file_extension in videos:
            transfer_file(f'videos;{path};{file_name};{file_extension}')
        else: 
            transfer_file(f'else_format;{path};{file_name};{file_extension}')

def catch_path(path, nesting=0):

    collection = []

    for files in os.listdir(path):
        if os.path.isdir(os.path.join(path, files)):
            catch_path(os.path.join(path, files), nesting + 1)
        else:
            collection.append(files)

    distribute_file(collection, path, nesting)

def main():
    New_PATH = r'C:\Users\PC\Documents\Activision'

    catch_path(r'C:\Users\PC\Documents\Activision')
    
if __name__ == "__main__":
       main()

