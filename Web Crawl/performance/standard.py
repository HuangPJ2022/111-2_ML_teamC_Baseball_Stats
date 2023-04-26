from bs4 import BeautifulSoup
import requests
import pandas as pd

data =pd.read_csv('url_001_100.csv')
error_list = []

def standard(name, url_, x):

    #載入網站html
    html_text = requests.get(url_)
    soup = BeautifulSoup(html_text.text, 'lxml')
    
    try:    
        #爬取欄位名稱
        standard_piching = soup.find('div', id='mlb_career')
        div = standard_piching.find('div', id='mlbPitching')
        thead = div.find('thead')
        tr = thead.find('tr')
        th = tr.find_all('th')[1:]
        columns_name = []
        for i in th:
            columns_name.append(i.text)

        #爬取data
        tbody = div.find('tbody')
        tr = tbody.find_all('tr', class_="default-table-row")
        standard_data = []
        for i in tr:
            td = i.find_all('td')
            standard_row = []
            for j in td:
                standard_row.append(j.text.strip())
            standard_data.append(standard_row[1:])
        standard_data = standard_data[:-2]

        #創建dataframe
        df = pd.DataFrame(standard_data, columns = columns_name)
        file_name = 'standard data/' + name + '(Standard).csv'
        df.to_csv(file_name, index=False)
        print(x)
    except:
        error_list.append(name)
        print('e'+str(x))

for i in range(100):
    standard(data['name'][i], data['url'][i], i)

print('error_list:')
print(error_list)

