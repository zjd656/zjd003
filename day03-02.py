import requests
def get_imageNet_data(path):
    headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808',headers=headers)
    HTML = response.text
    split_urls = HTML.split('\r\n')
    for url in split_urls:
        try:
            picture = requests.get(url=url,headers=headers)
        except Exception as e:
            picture = requests.get(url=url,headers=headers)
            print(e)
        else:
            picture = requests.get(url=url,headers=headers)
            imageName = url.split('/')[-1]
            with open(path+imageName,'wb') as f:
                 f.write(picture.content)

if __name__ == "__main__":
    path = '‪C:/Users/Administrator/ggg/'
    get_imageNet_data(path=path)