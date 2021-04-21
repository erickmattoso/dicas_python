import gdown
import os
path = "data"
os.makedirs(path, exist_ok=True)
# url = 'https://drive.google.com/uc?id=0B9P1L--7Wd2vU3VUVlFnbTgtS2c'
url ="https://drive.google.com/file/d/18W2IylJ7eNNlGaV_ck7MPacXSGtsYdvK/view?usp=sharing" 
output = path+'/cep.zip'
gdown.download(url, output, quiet=False)

# for title, url in media_files.items():
#    wget.download(url, out = "ml-cards/{}.png".format(title))
