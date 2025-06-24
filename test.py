import requests
from bs4 import BeautifulSoup

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

def url_maker():
    url = f'https://nutritionanalysis.dds.uconn.edu/longmenu.aspx?sName=UCONN+Dining+Services&locationNum=16&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate=06%2f24%2f2025&mealName=Breakfast'
    return url

content = get_website_content(url_maker())
print(extract_menu_items(content))