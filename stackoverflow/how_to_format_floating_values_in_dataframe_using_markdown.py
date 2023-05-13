import requests
import pandas as pd
import io

url = "https://coinmarketcap.com/new/"
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=1)
pagedata = page.text
usecols = ["Name", "Price", "1h", "24h", "MarketCap", "Volume"]

df = pd.read_html(pagedata)[0]
df[["Name", "Symbol"]] = df["Name"].str.split(r"\d+", expand=True)
df = df.rename(columns={"Fully Diluted Market Cap": "MarketCap"})[usecols]

numcols = df.columns[df.columns != 'Name']
df[numcols] = df[numcols].apply(lambda c:pd.to_numeric(c.str.replace(r'[^\d.]|(?<!\d)\.|\.(?!\d)', '', regex=True)))
df = df.sort_values('24h', ascending=False)

formatted_df = df.to_markdown(floatfmt=".12f", index=True)
# print(formatted_df)

df = pd.read_table(io.StringIO(formatted_df), sep='|', index_col=False)
df = df.dropna(axis=1, how='all')
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.replace({'---:': '', '-----------------': '', '--------------------------:': '', '   ': '', ':-': '', '--':'', '-':''}, regex=True)
print(df)

