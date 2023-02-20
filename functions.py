import json


def load_files(path):
    file = json.load(open(path, encoding='utf-8'))
    return file


def upload_files(path, picture, content):
    file = json.load(open(path, encoding='utf-8'))
    file.append({"pic": picture, "content": content})
    newfile = open(path, 'w')
    json.dump(file, newfile)


