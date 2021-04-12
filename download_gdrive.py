import gdown
import os

path = "data"
try:
    os.mkdir(path)
except:
    pass


# os.makedirs('ml-cards', exist_ok=True) # crir um diretório para armazenar as fotos
# for title, url in media_files.items():
#    wget.download(url, out = "ml-cards/{}.png".format(title)) #Pegue as photos!

url = 'https://drive.google.com/uc?id=0B9P1L--7Wd2vU3VUVlFnbTgtS2c'
output = path+'/spam.txt'

gdown.download(url, output, quiet=False)
