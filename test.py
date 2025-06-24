import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_website_content(url):
    ''' gets raw html content '''
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the website: {e}"
    
def extract_menu_items(content):
    ''' gets the menu items from the raw html content '''
    soup = BeautifulSoup(content, 'html.parser')
    menu_items = [item.get_text(strip=True) for item in soup.select('div.longmenucoldispname a')]
    return menu_items

def url_maker(location, meal):
    ''' makes url; takes date, location, and meal '''

    options = {'Connecticut': '03', 'North': '07', 'Putnam': '06',
               'Towers': '42', 'Northwest': '15', 'Whitney': '01',
               'McMahon': '05', 'South': '16'}
    locNum = options[location] # picks location

    date = datetime.today().strftime(f'%m %d %Y').split()

    return f'https://nutritionanalysis.dds.uconn.edu/longmenu.aspx?sName=UCONN+Dining+Services&locationNum={locNum}&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate={date[0]}%2f{date[1]}%2f{date[2]}&mealName={meal}'

def get_all_meals(hall):
    ''' returns breakfast, lunch, and dinner in a set '''
    content = get_website_content(url_maker(hall, 'Breakfast'))
    breakfast = extract_menu_items(content)
    content = get_website_content(url_maker(hall, 'Lunch'))
    lunch = extract_menu_items(content)
    content = get_website_content(url_maker(hall, 'Dinner'))
    dinner = extract_menu_items(content)
    return breakfast, lunch, dinner

hall = input('select dining hall: ')
all_meals = get_all_meals(hall)
print('Breakfast\n', all_meals[0], '\n')
print('Lunch\n', all_meals[1], '\n')
print('Dinner\n', all_meals[2], '\n')