
import time
import  concurrent.futures
import requests

start=time.perf_counter()

img_urls=['https://images.unsplash.com/photo-1519389950473-47ba0277781c',
          'https://images.unsplash.com/photo-1474377207190-a7d8b3334068',
          'https://images.unsplash.com/photo-1646673940197-dbf528eea559',
          'https://images.unsplash.com/photo-1646538230367-ad94dbb809a1']

'''


for img_url in img_urls:
    img_bytes=requests.get(img_url).content
    img_name=img_url.split('/')[3]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as imgs:
        imgs.write(img_bytes)
        print(f'{img_name} downloaded...')

'''
def download_imges(urls):
    imgs_bytes=requests.get(urls).content
    img_name=urls.split('/')[3]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as imgs:
        imgs.write(imgs_bytes)
        return '{} is downloaded..'.format(img_name)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=executor.map(download_imges,img_urls)
    for result in results:
        print(result)




end=time.perf_counter()

print('Time takes to complete :{}'.format(round(end-start,2)))
