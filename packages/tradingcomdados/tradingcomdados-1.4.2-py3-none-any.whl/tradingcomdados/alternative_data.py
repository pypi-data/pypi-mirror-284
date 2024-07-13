import pandas as pd
import requests 
import zipfile  
import numpy as np
import urllib.request
from pathlib import Path
from datetime import datetime
import urllib3


#path = 'https://raw.githubusercontent.com/victorncg/financas_quantitativas/main/Data%20Extraction/Stock%20Exchange/Index%20Composition/'
#file = 'backend_index.py'

# DEACTIVETED FOR FIXING BUGS - JULY 11
#with urllib.request.urlopen(path + file) as response:
#    py_content = response.read().decode('utf-8')

#exec(py_content)


def _return_index(index:str):

    conversion = {'ibov':'eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ==',
                 'ibra':'QlJB',
                 'ifix': 'eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJRklYIiwic2VnbWVudCI6IjEifQ==',
                  'idiv': 'RElW'}

    # Desabilitar avisos de verificação SSL
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Configurar sessão para não verificar SSL
    session = requests.Session()
    session.verify = False
    
    # URLs
    url1 = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/'
    url2 = conversion[index] 
    
    # Fazer a requisição
    response = session.get(url1 + url2)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        dados = pd.DataFrame(response.json()["results"])
    else:
        print(f"A biblioteca está funcionando mas houve erro na requisição a partir da B3, código: {response.status_code}")

    return dados


def _parse_ibov():

    try:

        url = "https://raw.githubusercontent.com/victorncg/financas_quantitativas/main/IBOV.csv"
        df = pd.read_csv(
            url, encoding="latin-1", sep="delimiter", header=None, engine="python"
        )
        df = pd.DataFrame(df[0].str.split(";").tolist())

        return df

    except:

        print("An error occurred while parsing data from IBOV.")



def _standardize_ibov():

    try:
        df = _parse_ibov()
        df.columns = list(df.iloc[1])
        df = df[2:][["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
        df.reset_index(drop=True, inplace=True)

        return df
    except:

        print("An error occurred while manipulating data from IBOV.")



def _standardize_sp500():
    """
    This function fetches the updated composition of the S&P 500 index. 
    
    Parameters
    ----------
    
    """

    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = table[0]

    return df



def _adapt_index(
    index: object, assets: object = "all", mode: object = "df"
):
    """
    This function processes the data from the latest composition of either IBOV or S&P 500. 
    
    Parameters
    ----------
    index : choose the index to be returned, if IBOV or S&P 500
    ativos : you can pass a list with the desired tickets. Default = 'all'.
    mode: you can return either the whole dataframe from B3, or just the list containing the tickers which compose IBOV. Default = 'df'.
    
    """

    if index == "sp500":

        df = _standardize_sp500()

        if assets != "all":
            df = df[df["Symbol"].isin(assets)]

        if mode == "list":
            df = list(df.Symbol)

    else:

        df = _return_index(index)

        if assets != "all":
            df = df[df["cod"].isin(assets)]

        if mode == "list":
            df = list(df.cod)
    
    return df



def index_composition(
    index: object, assets: object = "all", mode: object = "df"
):
    """
    This function captures the latest composition of either IBOV or S&P 500. It is updated every 4 months.
    
    Parameters
    ----------
    index : choose the index to be returned, if IBOV or S&P 500
    ativos : you can pass a list with the desired tickets. Default = 'all'.
    mode: you can return either the whole dataframe from B3, or just the list containing the tickers which compose IBOV. Default = 'df'.
    
    """

    df = _adapt_index(index, assets, mode)

    return df



def B3_DataProcessing(df):
    """
    It is used in the function get_sectors in order to processing 
    the zipfile data fetched from the url. 
    objective: clearing the columns and split informations into specific columns; 
    """
                  

    
    df.rename(columns = {'LISTAGEM': 'CÓDIGO', 'Unnamed: 4':'SEGMENTO B3'}, inplace = True)
        
    df['NOME NO PREGÃO'] = df['SEGMENTO'].copy()
        
    df.dropna(subset = ['NOME NO PREGÃO'], inplace = True)
    indexNames = df[df['SETOR ECONÔMICO'] == 'SETOR ECONÔMICO'].index
    df.drop(indexNames, inplace=True)
        
    df['SEGMENTO'] = np.where(df['CÓDIGO'].isna(),df['NOME NO PREGÃO'],pd.NA )    
    df['SETOR ECONÔMICO'] = df['SETOR ECONÔMICO'].ffill()
    df['SUBSETOR'] = df['SUBSETOR'].ffill()
    df['SEGMENTO'] = df['SEGMENTO'].ffill()
    df.dropna(subset = ['CÓDIGO'], inplace = True)

    df.reset_index(drop=True, inplace=True)

    df = df[['SETOR ECONÔMICO','SUBSETOR','SEGMENTO','NOME NO PREGÃO','CÓDIGO','SEGMENTO B3']]
    
    return df


def get_sectors(stock_exchange:object, *tickers):
    """
    This fuction gets the economic and activity sectors classification 
    of the companies listed on Nasdaq or Brazilian stock exchange (B3). 


    You can leave the  'tickers' parameter empty if you wish to return all companies, or 
    specify a variable number of tickers. 
    
    Parameters:
    ----------
    stock_exchange: you have to specify the stock exchange code ('NASDAQ' or 'B3'). 
    tickers : you can pass a specific company's ticker. For brazilian companies you can pass
    the symbol with the B3 segment number (e.g. 'PETR4') or w/o it (e.g. 'PETR')

    """ 
    
    
    stock_exchange = stock_exchange.upper()
      
    if stock_exchange == 'B3':

        url_dataset = r"https://www.b3.com.br/data/files/57/E6/AA/A1/68C7781064456178AC094EA8/ClassifSetorial.zip"

        download = requests.get(url_dataset)
        with open('ClassifSetorial.zip', "wb") as dataset_B3:
            dataset_B3.write(download.content)
        arquivo_zip = zipfile.ZipFile('ClassifSetorial.zip')
        dataset = arquivo_zip.open(arquivo_zip.namelist()[0])

        df = pd.read_excel(dataset, header = 6)
        
        df = B3_DataProcessing(df)   

        if not tickers:
            df = df

        else:
            tickers = list(tickers)
            tickers = [ ticker[:4].upper() for ticker in tickers]
            df = df.loc[df['CÓDIGO'].isin(tickers)]
            
        df.rename(columns = {'SETOR ECONÔMICO': 'sector', 'SUBSETOR':'industry',
                             'SEGMENTO':'subsector','NOME NO PREGÃO': 'name',
                             'CÓDIGO': 'symbol', 'SEGMENTO B3':'B3 listing segment'}, inplace = True)
            
    elif stock_exchange == 'NASDAQ':
        url = \
        'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true'
        headers = {'Accept-Language': 'en-US,en;q=0.9',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'User-Agent': 'Java-http-client/'}

        response = requests.get(url, headers=headers)

        json = response.json()

        df = pd.DataFrame(json['data']['rows'])
        
        df = df[['sector', 'industry', 'name', 'symbol', 'country']]
        
        if not tickers:
            df = df
            
        else:
            tickers = list(tickers)
            tickers = [ticker.upper() for ticker in tickers]
            df = df.loc[df['symbol'].isin(tickers)]
    
    return df

  

# Define the function to fetch historical data
def get_historical_klines(symbol, interval, start_time, end_time=None):
    base_url = 'https://api.binance.com'
    endpoint = '/api/v3/klines'
    
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
    }
    
    if end_time:
        params['endTime'] = end_time
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
     # Convert data to DataFrame
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    
    # Convert timestamp to readable date
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    return df

def get_histdata_binance(symbol, interval, start_time, end_time):
    """
    This function returns Crypto Historical Data from Binance
    
    Parameters
    ----------
    symbol     : 'BTCUSDT'      - string format
    interval   : '1m' '5m' '1d' - string format
    start_time : '2024-01-01'   - '%Y-%m-%d' - string format
    end_time   : '2024-03-01'   - '%Y-%m-%d' - string format
    
    """
    all_data = []
    start_time = int((datetime.strptime(start_time, '%Y-%m-%d')).timestamp() *1000)
    end_time = int((datetime.strptime(end_time, '%Y-%m-%d')).timestamp() *1000)
    while start_time < end_time:
        df = get_historical_klines(symbol, interval, start_time, end_time)
        if df.empty:
            break
        all_data.append(df)
        start_time = int(df['timestamp'].iloc[-1].timestamp() * 1000) + 1  # move to the next interval
    
    return pd.concat(all_data)

