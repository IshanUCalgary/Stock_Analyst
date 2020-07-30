import sys

if(len(sys.argv) != 2):
    print('Enter a stock ticker. Eg. analyzeStock.py BRK-B')
    exit()
stockSymbol = str(sys.argv[1])
file1 = open(stockSymbol + ".txt","w")

def fileClose():
    file1.close()

def intialTitle(cN, cP, mN):
    file1.write('Stock Report for '+ cN + "\n")
    file1.write("Market: " + mN + "\n")
    file1.write('--------------------------------\n')
    file1.write('\nCurrent Price = ' + str(cP) + "\n")
    file1.write("\n")

def viewCAPM(erm, rfr, beta, eri):
    if(beta == 'N/A'):
        file1.write('** CAPM Analysis Unavailable\n')
        file1.write('\n')
    else:
        file1.write('CAPM Analysis\n')
        file1.write('--------------------------------\n')
        file1.write('ER_i = R_f + Beta * (ER_m - R_f)\n')
        file1.write('ER_i = ' + str(rfr) + ' + ' + str(beta) + ' * ' + ' (' + str(erm) + ' - ' + str(rfr) + ')\n')
        file1.write('Expected Return on ' + stockSymbol + ' = ' + str(eri) + '%\n')
        file1.write("\n")

def viewIV(eB, dcfB, pB, cP):
    file1.write('Intrinsic Value Analysis \n')
    file1.write('--------------------------------\n')
    file1.write('Intrinsic Value DCF (Earnings Based)\n')
    file1.write('--\n')
    if(eB == 0.00):
        file1.write('Value is 0.00, look at others\n')
        file1.write("\n")
    else:
        file1.write('Value is ' + str(eB) + "\n")
        compare = cP/eB
        file1.write('The current price is ' + str(round(compare,2)) + ' times the intrinsic value based on earnings \n')
        if(compare <= 1 and compare > 0):
            file1.write('This company is undervalued based on its intrinsic value. \n')
        file1.write("\n")
    file1.write('Intrinsic Value DCF (FCF Based) \n')
    file1.write('--\n')
    if(dcfB == 0.00):
        file1.write('Value is 0.00, look at others \n')
        file1.write("\n")
    else:
        file1.write('Value is ' + str(dcfB) + "\n")
        compare = cP/dcfB
        file1.write('The current price is ' + str(round(compare,2)) + ' times the intrinsic value based on earnings \n')
        if(compare <= 1 and compare > 0):
            file1.write('This company is undervalued based on its intrinsic value. \n')
        file1.write("\n")
    file1.write('Intrinsic Value Projected FCF\n')
    file1.write('--\n')
    if(pB == 0.00):
        file1.write('Value is 0.00, look at others\n')
        file1.write("\n")
    else:
        file1.write('Value is ' + str(pB) + '\n') 
        compare = cP/pB
        file1.write('The current price is ' + str(round(compare,2)) + ' times the intrinsic value based on earnings \n')
        if(compare <= 1 and compare > 0):
            file1.write('This company is undervalued based on its intrinsic value.\n')
        file1.write("\n")   

def view52Week(week52, cP):
    low = float(week52[0].replace(',',''))
    high = float(week52[1].replace(',',''))
    rangePosition = round(((cP-low)/(high-low)) * 100)
    file1.write('52 Week Range = ' + str(low) + ' - ' + str(high) + "\n")
    file1.write('The stock is ' + str(rangePosition) + '%' + ' up from its 52 week low.\n')
    file1.write("\n")

def viewPE(pe):
    if(pe == 'N/A'):
        file1.write('** P/E Ratio N/A\n')
        file1.write("\n")
    else:
        priceToEarnings = float(pe)
        file1.write('P/E Analysis\n')
        file1.write('--------------------------------\n')
        file1.write('The P/E is ' + str(priceToEarnings) + "\n")
        if(priceToEarnings >= 15):
            file1.write('Analysis: The stock might be over valued\n')
        else:
            file1.write('Analysis: The stock is undervalued, but if its too low it lacks interest\n')
        file1.write("\n")

def viewCurrentRatio(cR):
    if(cR == 'N/A'):
        file1.write('** Current Ratio N/A\n')
        file1.write("\n")
    else:
        currentRatio = float(cR)
        file1.write('Current Ratio Analysis\n')
        file1.write('--------------------------------\n')
        file1.write('The Current Ratio is ' + str(currentRatio) + '\n')
        if currentRatio < 1:
            file1.write('Analysis: The company has debt, look at the industry\n')
        elif currentRatio >= 1 and currentRatio < 1.5:
            file1.write('Analysis: Relatively secure.\n')
        elif currentRatio >= 1.5 and currentRatio <= 2:
            file1.write('Analysis: Good asset management, not prone to bankruptcy\n')
        elif currentRatio > 2:
            file1.write('Analysis: The company might not know what do to with the cash\n')
        file1.write("\n")

def viewBeta(b):
    if(b == 'N/A'):
        file1.write('** Beta N/A\n')
        file1.write("\n")
        beta = 'N/A'
    else:
        beta = float(b)
        file1.write('Beta Analysis\n')
        file1.write('--------------------------------\n')
        file1.write('The Beta is ' + str(beta) + '\n')
        if beta < 1:
            file1.write('Analysis: Low volatility, low risk\n')
        if beta >= 1 and beta < 1.5:
            file1.write('Analysis: Normal levels of market volatility, general risk.\n')
        if beta > 1.5:
            file1.write('Analysis: Highly volatile stock, high risk\n')
        file1.write("\n")

def viewBookValue(bV, cP):
    if(bV == 'N/A'):
        file1.write('** Book Value is N/A\n')
        file1.write("\n")
    else:
        bookValue = float(bV.replace(',',''))
        file1.write('Book Value Analysis\n')
        file1.write('--------------------------------\n')
        file1.write('The Book Value is ' + str(bookValue) + "\n")
        percentage = round(((bookValue/cP)-1) * 100)
        if bookValue < cP:
            file1.write('The Book Value is ' + str(percentage*-1) + '%' +' below the current price\n')
        else:
            file1.write('The Book Value is ' + str(percentage) + '%' +' above the current price\n')
        if abs(percentage) <= 20:
            file1.write('Analysis: This stock can be a good buy\n')
        file1.write("\n")

def viewProfile(sec, ind, desc):
    file1.write("Company Profile\n")
    file1.write('--------------------------------\n')
    file1.write("Sector(s) is " + sec + "\n")
    file1.write("Industry is " + ind  + "\n")
    file1.write("\n")
    file1.write("Description\n")
    file1.write("---\n")
    file1.write(desc  + "\n")

    

    
    
    

    
