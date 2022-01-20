import pandas as pd
import json

df = pd.read_csv('./top-tallest-towers.csv')        

print(json.dumps(df.to_dict('records')))