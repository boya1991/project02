import os,sys
sys.path.append(os.getcwd())
import yaml


class ReadYaml():
    def __init__(self,filename):
        self.path= os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yaml(self):
        with open(self.path,"r",encoding="utf-8")as f:
            return yaml.load(f)
    def read_yaml1(self):
        with open("../Data/login1.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)
if __name__ == '__main__':
    datas=ReadYaml("login1.yaml").read_yaml1().values()

    attr=[]
    for data in datas:
        attr.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    print(attr)