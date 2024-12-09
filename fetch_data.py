import pandas as pd
import requests

def fetch_global_data ():
     url = "https://disease.sh/v3/covid-19/all"
     response = requests.get(url)
     if response.status_code == 200 :
        data = response.json()
        df = pd.DataFrame([data])
        return df
     else:
        print("Failed to retrieve data: ", response.status_code)   
        return None
     

def fetch_country_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200 :
        data = response.json()
        df = pd.DataFrame([data])
        return df
    else:
        print(f"Failed to retrieve data: for {country} ", response.status_code)   
        return None
    
def fetch_countries_data():
        url = "https://disease.sh/v3/covid-19/countries"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            return df
        else:
            print(f"Failed to retrieve data ", response.status_code)   
            return None
        


# global_df = fetch_global_data()
# print("Global Data")
# print(global_df)


# country_df = fetch_country_data("INDIA")
# print("country data")
# print(country_df)