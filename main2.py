import re
import os,time
import shutil
import hashlib
import pathlib
import datetime

#1)
print("№1")
file = open("C:\\text.txt")
textFile = file.readlines()
for i in range(len(textFile)):
    textFile[i] = re.sub("[\W\d]","",textFile[i])   
for i in range(len(textFile)):
    n = float(len(textFile[0]))
    result = {}
    resultStatistic = {} 
    for x in textFile[i]:
        result[x] = textFile[0].count(x)
        resultStatistic[x] =(result[x])/n
    for x in result:
        print(result[x], x ,resultStatistic[x])

#2)
print("№2")
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
path = "C:\package"
arrayHashs = []
arrayFiles = []
packages = os.listdir(path)
for i in range(len(packages)):
    path+="\\"+packages[i]
    files = (os.listdir(path))
    for x in range(len(files)):    
        arrayHashs.append(md5(path+"\\"+files[x]))
        arrayFiles.append(files[x])
    path = "C:\package"
for i in range(len(arrayHashs)):
    for v in range(len(arrayHashs)):
        if i == v : continue
        if arrayHashs[i] == arrayHashs[v]:
            print(arrayFiles[i]) 

#3)
print("№3")
directory = "C:\music"
file = open("C:\music\listMusic.txt")
textFile = file.readlines()
textFile = [line.rstrip() for line in textFile]
i=0
for file in os.listdir(directory):
    format = pathlib.Path(directory+"\\"+file).suffix
    if format == ".mp3":
       newName = textFile[i]
       print(file)
       os.rename(directory+"\\"+file,directory+"\\"+newName)
       i+=1

#4)
print("№4")
print("Вариант 1")
def find_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for num_line, line in enumerate(f):
            required = re.findall(r'\d{2}-\d{2}-\d{4}', line)
            for _ in required:
            	print(f"Строка {num_line + 1}, позиция {line.find(required[0])} : найдено '{required[0]}'")

if __name__ == "__main__":
    find_data('test.txt')

#5)
print("№5")
text = input("Введите текст : ").split(" ")
for i in range(len(text)):
    result = re.search("[A-Z][a-z]+\d{2,4}",text[i])
    if result != None:
       print(result.group())

#6)
print("№6")
days = int(input("Введите количество дней : "))
size = int(input("Введите количество Байтов : "))
directory = "C:\source"
files = os.listdir(directory)
Ar,Si = True,True
today = datetime.datetime.today().strftime("%d")
for i in range(len(files)):
    dateCreateFile = time.ctime(os.path.getmtime(directory+"\\"+files[i]))
    timeCreate = time.strftime("%d",time.strptime(dateCreateFile))
    differenceDay = int(today) - int(timeCreate)
    sizeFile = int(os.path.getsize(directory+"\\"+files[i]))
    if differenceDay>days :
        if Ar == True : 
            os.mkdir(directory+"\\"+"Archive")
        shutil.copy(directory+"\\"+files[i],directory+"\\"+"Archive")
        Ar = False
    if size>sizeFile :
        if Si == True : 
            os.mkdir(directory+"\\"+"Size")
        shutil.copy(directory+"\\"+files[i],directory+"\\"+"Size")
        Si = False         