#Packages
#--Web scraping packages
from bs4 import BeautifulSoup
import requests
#Pandas/numpy for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

def gtGradingScale (varName, g1, g2, g3, g4, g5, g6, g7, g8, g9):
    x = varName
    if finalRatios[x].item() > g1:
        grades[x] = 10
    elif finalRatios[x].item() >= g2:
        grades[x] = 9
    elif finalRatios[x].item() >= g3:
        grades[x] = 8
    elif finalRatios[x].item() >= g4:
        grades[x] = 7
    elif finalRatios[x].item() >= g5:
        grades[x] = 6
    elif finalRatios[x].item() >= g6:
        grades[x] = 5
    elif finalRatios[x].item() >= g7:
        grades[x] = 4
    elif finalRatios[x].item() >= g8:
        grades[x] = 3
    elif finalRatios[x].item() >= g9:
        grades[x] = 2
    else:
        grades[x] = 1

def ltGradingScale (varName, g1, g2, g3, g4, g5, g6, g7, g8, g9):
    x = varName
    if finalRatios[x].item() < g1:
        grades[x] = 10
    elif finalRatios[x].item() <= g2:
        grades[x] = 9
    elif finalRatios[x].item() <= g3:
        grades[x] = 8
    elif finalRatios[x].item() <= g4:
        grades[x] = 7
    elif finalRatios[x].item() <= g5:
        grades[x] = 6
    elif finalRatios[x].item() <= g6:
        grades[x] = 5
    elif finalRatios[x].item() <= g7:
        grades[x] = 4
    elif finalRatios[x].item() <= g8:
        grades[x] = 3
    elif finalRatios[x].item() <= g9:
        grades[x] = 2
    else:
        grades[x] = 1

url1 = 'https://www.reuters.com/companies/'

# CHANGE COMPANY STRING TO 'COMPANY TICKER.EXCHANGE ACRONYM'
print("Please find your company on https://www.reuters.com to find the appropriate ticker and stock exchange acronym. Inputs are case-insensitive and letters only.")
ticker = input('Please enter company ticker: ')
stockexch = input('Please enter the Reuters stock exchange acronym \nIt comes after the ticker (i.e. MSFT.OQ would be OQ). If there is none leave this blank.): ')

if stockexch == '':
    company = ticker.upper()
else:
    company = ticker.upper() + '.' + stockexch.upper()

#INCOME STATEMENT

is_url = '/financials/income-statement-annual'

incomestatement_url = url1 + company + is_url

IS_BASE_URL = [incomestatement_url]
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

isResults = isResults.replace({'\(':'-'},regex=True).replace({'\)':''},regex=True).replace({',':''},regex=True).replace({'--':'0'},regex=True).apply(pd.to_numeric,1).astype(float)

#BALANCE SHEET

bs_url = '/financials/balance-sheet-annual'

balancesheet_url = url1 + company + bs_url

BS_BASE_URL = [balancesheet_url]
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

bsResults = bsResults.replace({'\(':'-'},regex=True).replace({'\)':''},regex=True).replace({',':''},regex=True).replace({'--':'0'},regex=True).apply(pd.to_numeric,1).astype(float)

#CASH FLOW 

cf_url = '/financials/cash-flow-annual'

cashflow_url = url1 + company + cf_url

CF_BASE_URL = [cashflow_url]
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

cfResults = cfResults.replace({'\(':'-'},regex=True).replace({'\)':''},regex=True).replace({',':''},regex=True).replace({'--':'0'},regex=True).apply(pd.to_numeric,1).astype(float)
print(cfResults)

# FINAL RESULTS

finalResults = []
finalResults = pd.DataFrame(finalResults)
finalRatios = [0]
finalRatios = pd.DataFrame(finalRatios)
grades = pd.DataFrame(finalRatios)

try:
    finalResults['Gross_Profit_Margin'] = isResults['Gross Profit'] / isResults['Total Revenue']
    finalResults['Depreciation_Expense_Ratio'] = cfResults['Depreciation/Depletion'] / isResults['Total Revenue']
    finalResults['Interest_Payout_to_Income'] = isResults['Interest Inc.(Exp.),Net-Non-Op., Total'] / isResults['Operating Income']
    finalResults['Net_Earnings_Trend'] = ((isResults['Net Income'] - isResults['Net Income'].shift(periods=-1)) / isResults['Net Income'].shift(periods=-1)) +1
    finalResults['Total_Revenues_Earnings'] = isResults['Net Income'] / isResults['Total Revenue']
    finalResults['EPS_Trend'] = ((isResults['Diluted Normalized EPS'] - isResults['Diluted Normalized EPS'].shift(periods=-1)) / isResults['Diluted Normalized EPS'].shift(periods=-1)) +1
    finalResults['Cash_Trend'] = ((bsResults['Cash & Equivalents'] - bsResults['Cash & Equivalents'].shift(periods=-1)) / bsResults['Cash & Equivalents'].shift(periods=-1)) +1
    finalResults['Inventory_Trend'] = ((bsResults['Total Inventory'] - bsResults['Total Inventory'].shift(periods=-1)) / bsResults['Total Inventory'].shift(periods=-1)) +1
    finalResults['Current_Ratio'] = bsResults['Total Current Assets'] / bsResults['Total Current Liabilities']
    finalResults['Short_Term_Debt'] = bsResults['Notes Payable/Short Term Debt'] / bsResults['Total Common Shares Outstanding']
    finalResults['Long_Term_Debt'] = ((bsResults['Total Long Term Debt'] - bsResults['Total Long Term Debt'].shift(periods=-1)) / bsResults['Total Long Term Debt'].shift(periods=-1)) +1
    finalResults['Debt_to_SH_Equity'] = bsResults['Total Liabilities'] / bsResults['Total Liabilities & Shareholders\' Equity']
    finalResults['Retained_Earnings_Growth'] =((bsResults['Retained Earnings (Accumulated Deficit)'] - bsResults['Retained Earnings (Accumulated Deficit)'].shift(periods=-1)) / bsResults['Retained Earnings (Accumulated Deficit)'].shift(periods=-1)) +1
    finalResults['Return_on_SHE'] = isResults['Net Income'] / bsResults['Total Liabilities & Shareholders\' Equity']
    finalResults['CapEx_Ratio'] = cfResults['Capital Expenditures'] / isResults['Net Income']



    print(finalResults)

    finalRatios['Gross_Profit_Margin'] = round(finalResults.Gross_Profit_Margin.mean(), 2)
    finalRatios['Depreciation_Expense_Ratio'] = round(finalResults.Depreciation_Expense_Ratio.mean(), 2)
    finalRatios['Interest_Payout_to_Income'] = round(finalResults.Interest_Payout_to_Income.mean(), 2)
    finalRatios['Net_Earnings_Trend'] = round(finalResults.Net_Earnings_Trend.mean(), 2)
    finalRatios['Total_Revenues_Earnings'] = round(finalResults.Total_Revenues_Earnings.mean(), 2)
    finalRatios['EPS_Trend'] = round(finalResults.EPS_Trend.mean(), 2)
    finalRatios['Cash_Trend'] = round(finalResults.Cash_Trend.mean(), 2)
    finalRatios['Inventory_Trend'] = round(finalResults.Inventory_Trend.mean(), 2)
    finalRatios['Current_Ratio'] = round(finalResults.Current_Ratio.mean(), 2)
    finalRatios['Short_Term_Debt'] = round(finalResults.Short_Term_Debt.mean(), 2)
    finalRatios['Long_Term_Debt'] = round(finalResults.Long_Term_Debt.mean(), 2)
    finalRatios['Debt_to_SH_Equity'] = round(finalResults.Debt_to_SH_Equity.mean(), 2)
    finalRatios['Retained_Earnings_Growth'] = round(finalResults.Retained_Earnings_Growth.mean(), 2)
    finalRatios['Return_on_SHE'] = round(finalResults.Return_on_SHE.mean(), 2)
    finalRatios['CapEx_Ratio'] = round(finalResults.CapEx_Ratio.mean(), 2)

    finalRatios = finalRatios.drop(finalRatios.columns[0],1)
    print(finalRatios)

    gtGradingScale(varName='Gross_Profit_Margin', g1=.55, g2=.5, g3=.45, g4=.4, g5=.35, g6=.3, g7=.25, g8=.2, g9=.15)
    ltGradingScale(varName='Depreciation_Expense_Ratio', g1=0, g2=.05, g3=.1, g4=.15, g5=.2, g6=.25, g7=.3, g8=.35, g9=.4)
    ltGradingScale(varName='Interest_Payout_to_Income', g1=.05, g2=.1, g3=.15, g4=.2, g5=.25, g6=.3, g7=.35, g8=.4, g9=.45)
    gtGradingScale(varName='Net_Earnings_Trend', g1=1.5, g2=1.4, g3=1.3, g4=1.2, g5=1.1, g6=1, g7=.9, g8=.8, g9=.7)
    gtGradingScale(varName='Total_Revenues_Earnings', g1=.3, g2=.25, g3=.2, g4=.17, g5=.14, g6=.11, g7=.08, g8=.05, g9=0)
    gtGradingScale(varName='EPS_Trend', g1=1.5, g2=1.4, g3=1.3, g4=1.2, g5=1.1, g6=1, g7=.9, g8=.8, g9=.7)
    gtGradingScale(varName='Cash_Trend', g1=1.5, g2=1.4, g3=1.3, g4=1.2, g5=1.1, g6=1, g7=.9, g8=.8, g9=.7)
    gtGradingScale(varName='Inventory_Trend', g1=1.5, g2=1.4, g3=1.3, g4=1.2, g5=1.1, g6=1, g7=.9, g8=.8, g9=.7)
    gtGradingScale(varName='Current_Ratio', g1=1.2, g2=1.1, g3=1, g4=.85, g5=.6, g6=.45, g7=.3, g8=.15, g9=0)
    ltGradingScale(varName='Short_Term_Debt', g1=.5, g2=.55, g3=.6, g4=.65, g5=.7, g6=.75, g7=.8, g8=.85, g9=.9)
    gtGradingScale(varName='Long_Term_Debt', g1=1.5, g2=1.4, g3=1.3, g4=1.2, g5=1.1, g6=1, g7=.9, g8=.8, g9=.7)
    ltGradingScale(varName='Debt_to_SH_Equity', g1=.7, g2=.75, g3=.8, g4=.85, g5=.9, g6=.95, g7=1, g8=1.05, g9=1.1)
    gtGradingScale(varName='Retained_Earnings_Growth', g1=1.25, g2=1.2, g3=1.15, g4=1.1, g5=1.05, g6=1, g7=.95, g8=.9, g9=.85)
    gtGradingScale(varName='Return_on_SHE', g1=.35, g2=.3, g3=.24, g4=.2, g5=.16, g6=.12, g7=.08, g8=.04, g9=0)
    ltGradingScale(varName='CapEx_Ratio', g1=.15, g2=.2, g3=.25, g4=.3, g5=.35, g6=.4, g7=.45, g8=.5, g9=.55)
except(KeyError):
    print('\nSorry, this company does not provide the financials needed to complete calculations.')
    print('Please try a different company.')

grades = grades.drop(grades.columns[0],1)

finalGrade = grades.mean(axis=1)
if finalGrade.item() >= 7.5:
    decision = 'Buy'
elif finalGrade.item() >= 5:
    decision = 'Hold'
elif finalGrade.item() >=.01:
    decision = 'Sell'
else:
    print("No information available.")

try:
    print("\nThe rating for this stock is: " + decision)
    print(finalGrade)

    grades.plot(kind='bar')
    plt.show()
except(TypeError, NameError):
    print('Sorry.')
