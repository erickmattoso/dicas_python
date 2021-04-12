import gdown
import os
path = "data"
os.makedirs(path, exist_ok=True)
url = 'https://drive.google.com/uc?id=0B9P1L--7Wd2vU3VUVlFnbTgtS2c'
output = path+'/spam.txt'
gdown.download(url, output, quiet=False)

# for title, url in media_files.items():
#    wget.download(url, out = "ml-cards/{}.png".format(title))
