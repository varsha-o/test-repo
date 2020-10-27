'''
import os
import os.path, time
from tomark import Tomark

def read_md_file(md_file_path):
    f = open(md_file_path, 'r')
    file_string = f.read()
    dummy_list = []
    file_string_list = file_string.split("\n")[2:-1]
    for i in file_string_list:
        list = i.split(" | ")
        dummy_dict = {"filename": list[0].strip('| '), "created": list[1], "modified": list[2].strip(' |')}
        dummy_list.append(dummy_dict)
    #print(dummy_list)
    return dummy_list

def detect_file_change(md_file_content):
    dummy_file_list=[]
    for i in md_file_content:
        dummy_file_list.append(i["filename"])
    directory_path = "C:\\Users\\Dell\\Desktop\\detect_file_change\\test"
    files_list = os.listdir(directory_path)
    file_dict = []
    for file in files_list:
        created_date = time.ctime(os.path.getctime(directory_path + "\\" + file))
        modified_date = time.ctime(os.path.getmtime(directory_path + "\\" + file))
        #for first run
        if md_file_content == []:
            file_dict.append({"filename": file, "created": created_date, "modified": "-"})
        else:
            #new file created
            if (file not in dummy_file_list) :
                file_dict.append({"filename": file, "created": created_date, "modified": "-"})
            #check for modified files
            for i in md_file_content:
                if (i["filename"] == file) and (i["created"] != modified_date):
                    file_dict.append({"filename": file, "created": created_date, "modified": modified_date})
    print(file_dict)
    f = open(md_file_path, "w")
    f.write(Tomark.table(file_dict))
    f.close()
    #markdown = Tomark.table(file_dict)
    #print(markdown)

md_file_path = 'C:\\Users\\Dell\\Desktop\\detect_file_change\\test.md'
if os.path.isfile(md_file_path):
    md_file_content = read_md_file(md_file_path)
    detect_file_change(md_file_content)
else:
    detect_file_change(md_file_path)

'''
from git import *
from pydriller import RepositoryMining

import re
import os

dummy_markdown_list={}
result='null'
Repo_DIR = os.getcwd()
repo = Repo.init(Repo_DIR)
print(repo.tags['v1.0'])
print(repo.commit('v1.0'))
for commit in RepositoryMining(Repo_DIR, from_tag='v1.0').traverse_commits():
    print(commit.msg)








