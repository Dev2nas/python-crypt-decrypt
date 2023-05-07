import os 
def cryto(d):
    if os.path.isdir(d):
        for f in os.listdir(d):
            if os.path.isfile(f):
                fc=os.system("base64 %s"%f)
                print(fc)
# cryto("C:/Users/Lepro/Desktop/UIN/Python/bash")
cryto("/home/devnas/Bureau/Cryptographie/crypt")