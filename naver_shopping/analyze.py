import pandas as pd
import csv

df =pd.read_json("./products.json")

print(df.count())
#
# with open('products.json', 'r', encoding='utf-8') as input_file, open()