import yfinance as yf

def carregamento_dados(ticker):
    df = yf.Ticker(ticker).history("1y")
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split(".")[0]
    return df

#Ações da Bolsa - Segundo YAHOO FINANCE
weg = carregamento_dados("WEGE3.SA")
sabesp = carregamento_dados("SBSP3.SA")
arezzo = carregamento_dados("ARZZ3.SA")
localiza = carregamento_dados("RENT3.SA")


weg.head()