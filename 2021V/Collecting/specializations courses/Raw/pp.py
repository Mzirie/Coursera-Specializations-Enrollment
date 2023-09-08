import pandas as pd
df = pd.read_json (r"C:\Users\PC\Desktop\Projects\[Data Analytic] Coursera Spe\Collecting\RawsCourses Enroll.json")
df.to_csv (r'C:\Users\PC\Desktop\Projects\[Data Analytic] Coursera Spe\Collecting\Raws\New_Products.csv', index = None)