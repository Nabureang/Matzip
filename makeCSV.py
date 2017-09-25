import hashlib
import sqlite3
import os
from main import *
import Item
from file_info import *





def printItemList() :
    for i in main.itemList :
        print(i.showInfo())

def makeCSV() :
    f = open("list.csv", 'w')
    f.write("\"이름\" \"경로\"  \"크기\"  \"MD5\" \"SHA-1\"   \"마지막 수정시간\"   \"마지막 실행시간\"   \"파일 생성시간\"   \"색인\"\n")
    for i in main.itemList :
        f.write("\""+i.name + "\" \"" + i.path + "\" \"" + str(i.size)
                + "\" \"" + str(i.md5) + "\" \"" + str(i.sha1) + "\" \"" + str(i.modify_time)+ "\" \""
                + str(i.access_time)+ "\" \"" + str(i.create_time)+ "\" \"" +str(i.index) + "\"\n")


print("Pleas input path > ")
default_path = input()
directory = os.listdir(default_path)
for items in directory :
    one_item = os.path.join(default_path, items) #디렉토리에있는 파일 및 폴더 읽어온다.

    if os.path.isfile(one_item) : # 파일이면, itemList에 집어넣을 것
        file_inform = file_info
        item = Item.Item(file_inform['name'], file_inform['path'], file_inform['size'], file_inform['md5'], file_inform['sha1']
                    , file_inform['modify_time'], file_inform['access_time'], file_inform['create_time']
                    , file_inform['index']) # 새로운 Item객체 만듬, 정보대입
        main.itemList.append(item) #itemList에 item객체를 넣는다
printItemList()
makeCSV()



#conn = sqlite3.connect("filelist.db")
#cur = conn.cursor()
