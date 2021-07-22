import pandas as pd

df = pd.read_csv('file_name.csv', sep=';', encoding='PT154', header=5, usecols=[18,19])
df.to_numpy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
n=len(df)
df.drop(df.tail(n-37).index, inplace=True)
df=df[df['Длинные']!='x']
print(df)
df = df.replace(r'\s+','',regex=True)
df['Длинные']=pd.to_numeric(df['Длинные'], errors='coerce')
df['Короткие']=pd.to_numeric(df['Короткие'], errors='coerce')
for i in df:
    df=df[df < 0] = df.abs()
