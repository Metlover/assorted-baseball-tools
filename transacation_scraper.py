import pandas
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import requests
import json
#from flatten_json import flatten

print("WARNING: Scraping extremely long time periods (1+ years or longer) may result in error.")
start_date = input("Enter start date for transacation scraping (YYYY/MM/DD): ")
end_date = input("Enter end date for transacation scraping (YYYY/MM/DD): ")

start_date = start_date.replace('/', '')
end_date = end_date.replace('/','')

url = "http://lookup-service-prod.mlb.com/json/named.transaction_all.bam?start_date=" + start_date + "&end_date=" + end_date + "&sport_code=%27mlb%27"
lookup = requests.get(url)
data = lookup.text
parsed = json.loads(data)
parsed = parsed['transaction_all']
parsed = parsed['queryResults']
transactions = [transaction for transaction in parsed['row']]
#flat = flatten(parsed)
df = pandas.DataFrame(data=transactions)
df.to_csv('transactions.csv',sep=',')
