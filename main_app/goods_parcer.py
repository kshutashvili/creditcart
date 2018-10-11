from urllib.parse import urlparse
import bs4, requests, re

class Good:
    name = ''
    description = ''
    attributes = []
    shop = ''
    price = 0
    photo = ''#[]
    photos = []

    def __init__(self, name, description, attributes, shop, price, photo, photos = []):
            self.name = name
            self.description = description
            self.attributes = attributes
            self.shop = shop
            self.price = price
            self.photo = photo
            self.photos = photos

def PromUaGood(url):
    s=requests.get(url)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    price = re.sub("\D\,", "", b.find("span", itemprop="price").text)
    name = b.find("h1", itemprop="name").text
    description = getattr(b.find("div", itemprop="description"), 'text', 'Описание отсутствует...')
    attributes = []
    attributes_tr = b.find_all("tr", attrs = {'data-qaid':'attribute_line'})
    for td in attributes_tr:
        attr_name = re.sub(' +',' ', getattr(td.find_all('td')[0], 'text', ''))
        attr_val = re.sub(' +',' ', getattr(td.find_all('td')[1], 'text', ''))
        attributes.append(attr_name + ':' + attr_val)
    shop = 'prom.ua'
    image = b.find("img", itemprop = 'image').attrs.get('src')
    images = []
    li = b.find_all("li", attrs = {'data-big-image-src' : True})
    for l in li:
        images.append(l.attrs.get('data-big-image-src'))
    return Good(name, description, attributes, shop, price, image, images)
    

def getGoodFromSite(good_url):
    parced_url = urlparse(good_url)
    if parced_url.netloc == 'prom.ua':
        return PromUaGood(good_url)
