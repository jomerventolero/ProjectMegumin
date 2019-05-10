import pandas as pd
import werkzeug as werk
import os


top_dir = 'D:\\AmadeusSystem\\ProgramsProjects\\Pygame\\KivyProjects'

def search_file(self, ext_name, root_dir=top_dir):
    allfiles = []
    for dirs, _, files in os.walk(root_dir):
        print(dirs)
        print(files)
        for f in files:
            if f.endswith(ext_name):
                print(f)
                fullname = os.path.join(dirs, f)
                allfiles.append(fullname)
    allfiles.sort()
    return allfiles


def create_hash(msg, salt_length=8):
    data_hash = werk.generate_password_hash(msg)
    return data_hash

def open_csv(name):
    data = pd.read_csv(os.getcwd() + "\\KivyProjects\\AmadeusSystem\\users.csv")
    return data


d = open_csv("users.csv")

print(d['username'])
user = 'jomer287'
passw = 'junefour1999'

pwd = werk.generate_password_hash(passw)
print(pwd)

for i in d['username']:
    if i.startswith(user):
        for pwd in d['password']:
            if pwd == 'pbkdf2:sha256:150000$CumA8jmn$65f1a266e90c4dc638a400b304ada62c0e5b6fd10a93766adb293dd63df61642':
                if werk.check_password_hash(passw, pwd):
                    print("Successful!")
            else:
                print("Error!")

