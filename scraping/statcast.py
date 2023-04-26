from bs4 import BeautifulSoup
import requests
import pandas as pd

data =pd.read_csv('url_001_100.csv')
error_list = []

def statcast(name, url_, x):

    try:
        #載入網站html
        html_text = requests.get(url_)
        soup = BeautifulSoup(html_text.text, 'lxml')

        #爬取欄位名稱
        statcast_piching = soup.find('div', id='statcastPitching')
        thead = statcast_piching.find('thead')
        tr = thead.find('tr')
        th = tr.find_all('th')
        columns_name = []
        for i in th:
            columns_name.append(i.text)

        #爬取data
        tbody = statcast_piching.find('tbody')
        tr = tbody.find_all('tr', class_="default-table-row")
        statcast_data = []
        for i in tr:
            td = i.find_all('td')
            statcast_row = []
            for j in td:
                statcast_row.append(j.text.strip())
            statcast_data.append(statcast_row)
        statcast_data = statcast_data[:-3]

        #創建dataframe
        df = pd.DataFrame(statcast_data, columns = columns_name)
        file_name = 'statcast data/' + name + '(Statcast).csv'
        df.to_csv(file_name, index=False)
        print(x)
    except:
        error_list.append(name)
        print('e'+str(x))
for i in range(100):
    statcast(data['name'][i], data['url'][i], i)

print('error_list:')
print(error_list)

