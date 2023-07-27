import requests
import pandas as pd
from bs4 import BeautifulSoup


target = "https://www.spotrac.com/mlb/contracts/sort-value/pitching/all-time/draft-year-"
limit = "/limit-2000/"
period = range(2023,1981,-1)

salary = []  #各球員薪資
player = []  #各球員
rank = []    #排名
d_year = []  #選秀年分
start_relief = [] #先發字串長度為40，後援為38，終結者30
contract_start_year = [] #年份格式統一為20
contract_length = [] #合約長度
signed_age = [] #簽約年紀
Team = [] #所屬球隊

for draft_year in period:
    url = target + str(draft_year) + limit

    r = requests.get(url)

    sp = BeautifulSoup(r.text,"html5lib")##用來搜尋物件

#----------------------------------------爬出薪水-------------------------------------------------
    
    lines = sp.findAll(class_= "cap")
    s  = ""
    

    flag = 0
    for line  in lines: #用line取出 lines[0] lines[1] lines[2] ......
    
        x = line.text.strip().replace("$","").replace(",","")
        x = int(x)
        if flag % 2 ==0:
            salary.append(x)
            flag += 1
        else :
            flag += 1
 
#----------------------------------------爬出球員名字-------------------------------------------------
 
    player_search = sp.findAll(class_= "team-name")
    
    for man in player_search:
        name = man.text.strip()
        player.append(name)
    #標示該球員選秀年分    
        d_year.append(draft_year)
      
#----------------------------------------標示投手類型及合約開始年度-------------------------------------------------

    position = sp.findAll(class_= "rank-position")

    



    for pos in position:
        cha = pos.text.strip()
        if len(cha) == 40 :
             start_relief.append("Starting pitcher")
        elif len(cha) == 38 :
             start_relief.append("Relief Pitcher")
        elif len(cha) == 32 :
             start_relief.append("uncertain")
        elif len(cha) == 30 :
             start_relief.append("Closer")
        elif len(cha) <= 20 and  len(cha) >= 17 :
            contract_start_year.append(eval(cha[0:4]))
#----------------------------------------合約長度 + 簽約年紀-------------------------------------------------       
    cashes = sp.findAll(class_= "center small")
    flag4 = 0
    for qo  in cashes[2:]: 
        if flag4 % 2 == 1:
            x = eval(qo.text.strip())
            contract_length.append(x)
            #print(type(x))
            flag4 += 1
        else:
            x = qo.text.strip()
            signed_age.append(x)
            flag4 += 1


#----------------------------------------選手所屬隊伍-------------------------------------------------
    rank_position = sp.findAll('div',class_= "rank-position")
    for rank_p in rank_position:
        img = rank_p.find('img')
        if img == None:
            continue
        else:
            team = img.get('src')
            team = team.split("/")
            team = team[-1]
            team = team.split(".")
            team = team[0]
            team = team.split("_")
            team = team[-1]
            if team == "2022":
                team = "cle"
            Team.append(team)


#----------------------------------------標示累積人數-------------------------------------------------


total = []
for mm in range(1,len(player)+1):
    total.append(mm)



#----------------------------------------檢查用-------------------------------------------------------------------

print("player:",len((player)))  
print("salary:",len((salary)))
print("total :",len((total)))
print("d_year :",len((d_year)))
print("start_relief :",len((start_relief)))
print("contract_start_year :",len((contract_start_year)))
print("contract_length :",len((contract_length)))
print("signed_age :",len((signed_age)))
print("Team: ", len(Team))
#----------------------------------------匯出檔案-------------------------------------------------------------------

data = pd.DataFrame({"order":total,"player":player,"total value":salary,"draft year":d_year,"contract start year" : contract_start_year,"start or relief" : start_relief,"signed age": signed_age,"contract length" : contract_length , "player team" : Team})
#----------------------------------------平均年薪-----------------------------------------------------------
data["avg"] = round(data["total value"].div(data["contract length"]))



data.to_csv(r'D:\data_analysis_ML\v3.csv', index=False)
