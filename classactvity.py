# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# query = f"(iso_a3)" == 'NZL' or f"(iso_a3)" == 'DNK'

# df_result = df.query(query)

# mean_dollar_price = df_result['dollar_price'].mean

# print(df_result['dollar_price'].min())
# print(df_result['dollar_price'].max())
# print(df_result['dollar_price'].mean())
# print(df_result['dollar_price'].median())



import csv 
import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

new_query = f"date >= '2000-01-01' and date <= '2000-12-31' and iso_a3 == 'CHL')"

df_by_date = df.query(new_query)
print (df_by_date)
print(df)

# import pandas as pd
# df = pd.read_csv('big-mac-full-index.csv')

