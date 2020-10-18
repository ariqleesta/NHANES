
#----------------------------- ARIQ SENANG ARIQ BAHAGIA HEHEHEHEH ---------------------------------#
#----------------------------------- WELCOME INDIR, SCOTT, BEL-------------------------------------#

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100)

df = pd.read_csv('nhanes_2015_2016.csv')
print(df.head())

# Pick several columns
print(df.columns) #cek index yang tersedia

# Ambil body measurement saja (BM)
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 
        'BMXARML', 'BMXARMC','BMXWAIST'] 

# Kolom yang di keep ditampilkan isinya
print(df[keep]) 



# Atau dengan cara List Comprehension
keep = [column for column in df.columns if 'BM' in column]
print(df[keep])

# Location function .loc
df_loc = df.loc[:,keep] #.loc[a:b , c:d] a:b range rows, c:d range columns (abcd = strings)

print(df_loc)

# Contoh
# Select same rows, with just 'first_name', 'address' and 'city' columns
# data.loc['Andrade':'Veness', ['first_name', 'address', 'city']]


#index boolean
index_bool = np.isin(df.columns, keep) #isin (a,b) apakah di a ada b, hasil True and False
print(index_bool)

df_iloc = df.iloc[:,index_bool].head() #.iloc[a:b,c:d] range rows, c:d range columns (abcd = integers)
print(df_iloc)

# We want the BMXWAIST > Its median
waist_median = pd.Series.median(df["BMXWAIST"])
print(waist_median)

condition1 = df['BMXWAIST'] > waist_median
df_condition1 = df[condition1]
print(df_condition1.head()) #bakal ngeprint semua value ketika waist > waist median

#jika 2 kondisi
condition2 = df['BMXLEG'] < 32
df_condition1and2 = df[condition1 & condition2] # Use & not 'and'
print(df_condition1and2.head())

#or

print(df.loc[condition1 & condition2,:].head())

# Menganti index dari angka menjadi huruf
df_small = df.head()
print(df_small)
df_small.index = ['a','b','c','d','e']
print(df_small)

print(df_small.loc["a":"c",keep]) #tidak bisa pakai 0 1 2 3 karena index sudah diganti, kecuali pakai iloc
print(df_small.iloc[0:3,index_bool]) #tidak bisa pakai string, keep isinya string

# Returning to list of values
dfbmval = df_small.loc[:,'BMXBMI'].values
print(dfbmval)

#changing the value of 1 category
df['BMXBMI'] = range(df.shape[0])
print(df.BMXBMI)
