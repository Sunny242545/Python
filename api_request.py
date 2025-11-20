import requests
import pandas as pd

base_url =  'https://jsonplaceholder.typicode.com/posts' #input API


def get_data_api():
    url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        df = response.json()
        data = pd.DataFrame(df)
        data.drop("body", axis =1, inplace = True) # droppped body column from data frame
        data.to_csv("api_file_data.csv", index = False) #this will create a new csv file in your project folder 
        return data.head()


print(get_data_api())