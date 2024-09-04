from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = 'https://en.wikipedia.org/wiki/List_of_airlines_of_Nepal'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

def remove_references(text):
    return re.sub(r'\[\d+\]', '', text).strip()

tables = soup.find_all('table', class_ = 'wikitable sortable static-row-numbers static-row-header-text')
all_titles = tables[0].find_all('th')


table_titles = [remove_references(th.text.strip()) for th in all_titles]

print (table_titles)
my_frames = pd.DataFrame(columns=table_titles)
column_data = tables[0].find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [remove_references(data.text.strip()) for data in row_data]
    length = len(my_frames)
    my_frames.loc[length] = individual_row_data

    print(individual_row_data)


print(my_frames)

my_frames+=1
my_frames.to_csv(r'C:\Users\bibhu\OneDrive\Desktop\python\WebScaraping\Airlines.csv',index_label='No.')

