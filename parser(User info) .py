import requests    
from bs4 import BeautifulSoup
import csv


HOST='https://www.olx.ua/'
URL='https://www.olx.ua/uk/transport/'



HEADERS = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

def get_html(url,params=''):
    response=requests.get(url,headers=HEADERS,params=params)
    return response
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='css-1sw7q4x')
    users_data = []
    # count = 0 

    for item in items:
        link_elem = item.find_next('a', class_='css-rc5s2u')
        link = link_elem.get('href') if link_elem else None
        user_data = {}

        if link:
            # count += 1 

            link = HOST + link
            user_data['link'] = link

            
            user_page_html = get_html(link).text
            user_soup = BeautifulSoup(user_page_html, 'html.parser')

            
            name_elem = user_soup.find('h4', class_='css-1lcz6o7 er34gjf0')
            name = name_elem.text.strip() if name_elem else 'name'
            user_data['name'] = name
            
            car_elem = user_soup.find('h4', class_='css-1juynto')
            car = car_elem.text.strip() if car_elem else 'name'
            user_data['car'] = car

            info_cars=item.find_next('span',class_='css-t4djs0')
            info= info_cars.get_text() if info_cars else None
            user_data['info'] = info

            price_item=item.find_next('p',class_='css-10b0gli er34gjf0')
            price= price_item.get_text() if price_item else None
            user_data['price'] = price

            gread_item=item.find_next('span',class_='css-efx9z5')
            gread= gread_item.get_text() if price_item else None
            user_data['gread'] = gread
            

            users_data.append(user_data)

    

    for user in users_data:
        print(f"Name: {user['name']}")
        print(f"Car: {user['car']}")
        print(f"Link: {user['link']}")
        print(f"Info:{user['info']}")
        print(f"Price:{user['price']}")
        print(f"Gread:{user['gread']}")
        print()
    # print(f"Processed {count} advertisements.")
get_content(get_html(URL).text)
