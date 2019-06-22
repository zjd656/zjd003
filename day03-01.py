import requests
url = 'https://www.baidu.com/'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
        count +=1

if __name__=="__main__":
    wds = ('joker','丑女','美女')
    baidu(wds)