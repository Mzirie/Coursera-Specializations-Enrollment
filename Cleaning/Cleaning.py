import pandas as pd
import json

# Opening JSON file
with open('data.json', 'r') as f:
  data = json.load(f)

 

df =pd.DataFrame.from_dict(data[0])

 
df.to_csv('fruits3.csv') # write dataframe to file