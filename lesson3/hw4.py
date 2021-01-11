import os
import sys
path = 'E:\Учёба\Всякое'
files = os.listdir(path)
изображения = []
видео_файлы = []
документы = []
музыка = []
прочее = []
формат = []
for i in files:
    if i.endswith(('jpg', 'jpeg', 'png')):
        изображения.append(i)
    elif i.endswith(('avi', 'mp4', 'mov', 'flv', 'mkv')):
        видео_файлы.append(i)
    elif i.endswith(('doc', 'docx', 'txt', 'pdf')):
        документы.append(i)
    elif i.endswith(('mp3', 'ogg', 'wav', 'amr')):
        музыка.append(i)
    else:
        прочее.append(i)
for l in files:
        l = l.rsplit('.')[1]
        формат.append(l)

my_list = ['ИЗОБРАЖЕНИЯ:'+ str(изображения), 'ВИДЕО:'+ str(видео_файлы),'ДОКУМЕНТЫ:' + str(документы), 'МУЗЫКА:' + str(музыка),'ПРОЧЕЕ:'+ str(прочее), 'ОБЩИЙ СПИСОК ФОРМАТОВ:'+ str(формат)]
print(my_list)