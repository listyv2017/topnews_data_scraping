import requests
from bs4 import BeautifulSoup as bs4
import re

#retrieve 10 topnews
def get_data():

    load_url = "https://news.yahoo.co.jp/"

    try:

        res = requests.get(load_url)
        res.raise_for_status()#eroor check
    
    # bs4のオブジェクトをsoupに格納
        soup = bs4(res.content, "html.parser")
        
        # 取得したHTML全体の表示
        #print(soup)
    except requests.exceptions.RequestException as e:
        print(f"error in loading url: {e}")

    #search top news return list
    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    #print(elems)

    for elem in elems:
        print(elem.contents[0])
        #すべての子要素　content 引数でタイトルのみの表示
        print(elem.attrs['href'])


if __name__ == "__main__":

    get_data()
    
    