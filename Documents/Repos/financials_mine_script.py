#Packages
#--Web scraping packages
from bs4 import BeautifulSoup
import requests
#Pandas/numpy for data manipulation
import pandas as pd
import numpy as np

#INCOME STATEMENT

IS_BASE_URL = ['https://www.reuters.com/companies/MSFT.OQ/financials/income-statement-annual']
for data in IS_BASE_URL:
    html = requests.get(data).text
    soup = BeautifulSoup(html, "html.parser")

    vars = []
    isData = []

for tr in soup.find_all('tr'):
    values1 = [th.text.strip() for th in tr.find_all('th')]
    vars.append(values1)

is_vars_df = pd.DataFrame(vars)
is_vars_df = is_vars_df.drop(is_vars_df.columns[6],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.columns[5],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.columns[4],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.columns[3],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.columns[2],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.columns[1],axis=1)
is_vars_df = is_vars_df.drop(is_vars_df.index[0])

for tr in soup.find_all('tr'):
    values = [td.text.strip() for td in tr.find_all('td')]
    isData.append(values)

isData = pd.DataFrame(isData)
isData = isData.drop(isData.columns[5],1)
isData = isData.drop(isData.index[0])

isResults = pd.concat([is_vars_df, isData], ignore_index=True, axis=1)
isResults = isResults.transpose()
isResults = isResults.rename(columns=isResults.iloc[0])
isResults = isResults.drop(isResults.index[0])

print(isResults)

# #BALANCE SHEET

BS_BASE_URL = ['https://www.reuters.com/companies/MSFT.OQ/financials/balance-sheet-annual']
for data in BS_BASE_URL:
    html = requests.get(data).text
    soup = BeautifulSoup(html, "html.parser")

    bs_vars = []
    bsData = []

for tr in soup.find_all('tr'):
    bs_values = [th.text.strip() for th in tr.find_all('th')]
    bs_vars.append(bs_values)

bs_vars_df = pd.DataFrame(bs_vars)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[6],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[5],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[4],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[3],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[2],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.columns[1],axis=1)
bs_vars_df = bs_vars_df.drop(bs_vars_df.index[0])

for tr in soup.find_all('tr'):
    bs_values = [td.text.strip() for td in tr.find_all('td')]
    bsData.append(bs_values)

bsData = pd.DataFrame(bsData)
bsData = bsData.drop(bsData.columns[5],1)
bsData = bsData.drop(bsData.index[0])

bsResults = pd.concat([bs_vars_df, bsData], ignore_index=True, axis=1)
bsResults = bsResults.transpose()
bsResults = bsResults.rename(columns=bsResults.iloc[0])
bsResults = bsResults.drop(bsResults.index[0])

print(bsResults)

#CASH FLOW 

CF_BASE_URL = ['https://www.reuters.com/companies/MSFT.OQ/financials/cash-flow-annual']
for data in CF_BASE_URL:
    html = requests.get(data).text
    soup = BeautifulSoup(html, "html.parser")

    cf_vars = []
    cfData = []

for tr in soup.find_all('tr'):
    cf_values = [th.text.strip() for th in tr.find_all('th')]
    cf_vars.append(cf_values)

cf_vars_df = pd.DataFrame(cf_vars)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[6],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[5],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[4],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[3],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[2],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.columns[1],axis=1)
cf_vars_df = cf_vars_df.drop(cf_vars_df.index[0])

for tr in soup.find_all('tr'):
    cf_values = [td.text.strip() for td in tr.find_all('td')]
    cfData.append(cf_values)

cfData = pd.DataFrame(cfData)
cfData = cfData.drop(cfData.columns[5],1)
cfData = cfData.drop(cfData.index[0])

cfResults = pd.concat([cf_vars_df, cfData], ignore_index=True, axis=1)
cfResults = cfResults.transpose()
cfResults = cfResults.rename(columns=cfResults.iloc[0])
cfResults = cfResults.drop(cfResults.index[0])

print(cfResults)