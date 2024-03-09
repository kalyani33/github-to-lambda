import json
import requests
import pandas as pd

def handler_handler(event,context):
    print("Event data -> ",event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1':[1,2],'col2':[3,4]}
    df = pd.Dataframe(d)
    print(df)
    print("Done !!!")