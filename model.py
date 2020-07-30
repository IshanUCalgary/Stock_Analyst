from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import view 
import sys
import string

if(len(sys.argv) != 2):
    print('Enter a stock ticker. Eg. analyzeStock.py BRK-B')
    exit()
stock_ticker = str(sys.argv[1])

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

print('Writing File...')
print()

def driverQuit():
    driver.quit()

def yahooFinance():
    driver.get('https://finance.yahoo.com/quote/' + stock_ticker + '/')

    companyName = driver.find_element_by_css_selector("#quote-header-info > div > div > div > h1[data-reactid='7']")
    companyName = companyName.text

    marketName = driver.find_element_by_css_selector("#quote-header-info > div > div > div > span[data-reactid='9']")
    marketName = marketName.text
    if('NYSE' in marketName):
        marketName = 'NYSE'
    if('Nasdaq' in marketName):
        marketName = 'Nasdaq'
    
    currentPrice = driver.find_element_by_css_selector("#quote-header-info > div > div > div > span[data-reactid='32']")
    currentPrice = float(currentPrice.text.replace(',',''))
    view.intialTitle(companyName, currentPrice, marketName)

    values_element = driver.find_elements_by_xpath("//td[@class='Ta(end) Fw(600) Lh(14px)']")
    values = [x.text for x in values_element]
    pe = values[-6]
    view.viewPE(pe)

    week52 = values[5].split(' - ')
    view.view52Week(week52, currentPrice)

    statDetails(currentPrice, marketName)
    guruFocus(stock_ticker, currentPrice)
    profileDesc()

def profileDesc():
    driver.get("https://finance.yahoo.com/quote/" + stock_ticker +"/profile?p=" + stock_ticker)
    genre_element = driver.find_elements_by_xpath("//span[@class='Fw(600)']")
    genre = [y.text for y in genre_element]
    sector = genre[0]
    industry = genre[1]
    desc = driver.find_element_by_xpath("//p[@class='Mt(15px) Lh(1.6)']")
    desc = desc.text
    view.viewProfile(sector, industry, desc)
    
def statDetails(currentPrice, marketName):
    driver.get("https://finance.yahoo.com/quote/" + stock_ticker + "/key-statistics?p="+stock_ticker)
    balanceSheet = driver.find_elements_by_xpath("//td[@class='Fw(500) Ta(end) Pstart(10px) Miw(60px)']")
    values = [x.text for x in balanceSheet]
    beta = values[0]
    currentRatio = values[-4]
    bookValue = values[-3]
    view.viewBeta(beta)
    view.viewCurrentRatio(currentRatio)
    view.viewBookValue(bookValue, currentPrice)
    CAPM(marketName, beta)
    
def guruFocus(stock_ticker, currentPrice):
    stock_ticker = stock_ticker.replace('-','.')
    driver.get("https://www.gurufocus.com/term/iv_dcEarning/" + stock_ticker + "/Intrinsic-Value:-DCF-(Earnings-Based)/")
    
    inValueE = driver.find_element_by_css_selector("#def_body_detail_height > font")
    try:
        inValueE = float(inValueE.text.replace(': $','').replace(' (As of Today)','').replace(',',''))
    except:
        inValueE = float(inValueE.text.replace(': USD ','').replace(' (As of Today)','').replace(',',''))

    driver.get("https://www.gurufocus.com/term/iv_dcf/" + stock_ticker + "/Intrinsic-Value:-DCF-(FCF-Based)/")

    inValueDCF = driver.find_element_by_css_selector("#def_body_detail_height > font")
    try:
        inValueDCF = float(inValueDCF.text.replace(': $','').replace(' (As of Today)','').replace(',',''))
    except:
        inValueDCF = float(inValueDCF.text.replace(': USD ','').replace(' (As of Today)','').replace(',',''))

    driver.get("https://www.gurufocus.com/term/iv_dcf_share/" + stock_ticker + "/Intrinsic-Value:-Projected-FCF/")

    inValuePro = driver.find_element_by_css_selector("#def_body_detail_height > font")
    try:
        inValuePro = float(inValuePro.text.replace(': $','').replace(' (As of Today)','').replace(',',''))
    except:
        inValuePro = float(inValuePro.text.replace(': USD ','').replace(' (As of Today)','').replace(',',''))

    view.viewIV(inValueE, inValueDCF, inValuePro, currentPrice)

def CAPM(marketName, beta):
    if(beta == 'N/A'):
        view.viewCAPM(1, 1, beta, 1)
    else:
        if marketName == 'Nasdaq':
            driver.get("https://money.cnn.com/data/markets/nasdaq/")
        elif marketName == 'NYSE':
            driver.get("https://money.cnn.com/data/markets/nyse/")
        expectedReturnMarket = driver.find_element_by_xpath("//div[@id='wsod_quoteRight']/table/tbody/tr/td/span")
        expectedReturnMarket = float(expectedReturnMarket.text.replace('%',''))
        driver.get("https://money.cnn.com/data/bonds/")
        riskFreeRate = driver.find_element_by_xpath("//table[@id='treasuryYields_datatable']/tbody/tr[3]/td[2]")
        riskFreeRate = float(riskFreeRate.text.replace('%','')) 
        marketRiskPremium = expectedReturnMarket - riskFreeRate
        expectedReturnAsset = riskFreeRate + float(beta)*(marketRiskPremium)
        view.viewCAPM(expectedReturnMarket, riskFreeRate, beta, expectedReturnAsset)




    
