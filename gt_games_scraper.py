from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time

urla = 'https://www.sports-reference.com/cfb/play-index/pgl_finder.cgi?request=1&match=game&year_min=&year_max=&conf_id=&school_id=georgia-tech&opp_id=&game_type=&game_num_min=&game_num_max=&game_location=&game_result=&class=&c1stat=pass_cmp&c1comp=gt&c1val=&c2stat=rush_att&c2comp=gt&c2val=&c3stat=rec&c3comp=gt&c3val=&c4stat=td&c4comp=gt&c4val=&order_by=player&order_by_asc=Y&offset='

my_dfa = []

for n in range(0,100):
    print(n)
    new_url = urla + str(n) + '00'
    site = requests.get(new_url)
    soup = bs(site.content,'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table),header=1)
    df = df[0]
    my_dfa.append(df)
    time.sleep(1)

my_dfa = pd.concat(my_dfa)
my_dfa = my_dfa[my_dfa['Player'] != 'Player']
my_dfa['Key'] = my_dfa['Player'] + my_dfa['Date']

urlb = 'https://www.sports-reference.com/cfb/play-index/pgl_finder.cgi?request=1&match=game&year_min=&year_max=&conf_id=&school_id=georgia-tech&opp_id=&game_type=&game_num_min=&game_num_max=&game_location=&game_result=&class=&c1stat=points&c1comp=gt&c1val=&c2stat=xpm&c2comp=gt&c2val=&c3stat=kick_ret&c3comp=gt&c3val=&c4stat=punt_ret&c4comp=gt&c4val=&order_by=player&order_by_asc=Y&offset='

my_dfb = []
for n in range(0,100):
    print(n)
    new_url = urlb + str(n) + '00'
    site = requests.get(new_url)
    soup = bs(site.content,'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table),header=1)
    df = df[0]
    my_dfb.append(df)
    time.sleep(1)

my_dfb = pd.concat(my_dfb)
my_dfb = my_dfb[my_dfb['Player'] != 'Player']
my_dfb['Key'] = my_dfb['Player'] + my_dfb['Date']

urlc = 'https://www.sports-reference.com/cfb/play-index/pgl_finder.cgi?request=1&match=game&year_min=&year_max=&conf_id=&school_id=georgia-tech&opp_id=&game_type=&game_num_min=&game_num_max=&game_location=&game_result=&class=&c1stat=tackles_solo&c1comp=gt&c1val=&c2stat=def_int&c2comp=gt&c2val=&c3stat=fumbles_rec&c3comp=gt&c3val=&c4stat=punt&c4comp=gt&c4val=&order_by=player&order_by_asc=Y&offset='

my_dfc = []
for n in range(0,100):
    print(n)
    new_url = urlc + str(n) + '00'
    site = requests.get(new_url)
    soup = bs(site.content,'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table),header=1)
    df = df[0]
    my_dfc.append(df)
    time.sleep(1)

my_dfc = pd.concat(my_dfc)
my_dfc = my_dfc[my_dfc['Player'] != 'Player']
my_dfc['Key'] = my_dfc['Player'] + my_dfc['Date']

result = my_dfa.merge(my_dfb, on='Key', how='outer')
result = result.merge(my_dfc, on='Key', how='outer')

result.to_csv('gt_player_games.csv',sep=',')
