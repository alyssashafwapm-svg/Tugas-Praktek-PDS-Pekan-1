import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#1. memasukkan data ke dalam variabel
edu = pd.read_csv('educ_figdp_1_data.csv', #note : data harus berada dalam folder yang sama dgn program
                  na_values=':', #Menandai data yg tidak ada
                  usecols=["TIME", "GEO", "Value"]) #Memilih kolom yang diperlukan

#2. Tata ulang data agar lebih efektif
filtered_data = edu[edu['TIME'] > 2005 ] #memfilter data dgn tahun lebih dari 2005
pivedu = pd.pivot_table(filtered_data,
                        values='Value',
                        index=['GEO'],
                        columns=['TIME']) #membuat tabel pivot
pivedu.head()

#3. Membersihkan data
pivedu = pivedu.drop([ 
    'Euro area (13 countries)',
    'Euro area (15 countries)',
    'Euro area (17 countries)',
    'Euro area (18 countries)',
    'European Union (25 countries)',
    'European Union (27 countries)',
    'European Union (28 countries)',
], axis=0) #membersihkan baris yg mengganggu perhitungan 
pivedu=pivedu.rename(index={'Germany (until 1990 former territory of the FRG)':'Germany'}) #mengganti nama agar lebih mudah dibaca
pivedu = pivedu.dropna() #menghilangkan nilai NaN

#4. Ranking data dan membuat grafik
totalSum = pivedu.sum(axis=1).sort_values(ascending=False) #menjumlahkan nilai tiap baris dan diurutkan dari paling besar ke kecil
print(totalSum.rank(ascending=False, method='dense').sort_values().head()) #memberi peringkat berdasarkan nilainya pada tahun tertentu

##Plot 1 (Bar Plot)
totalSum.plot( 
    kind='bar',
    style='r',
    alpha=0.4,
    title="Total Values for Country"
)

##Plot 2 (Stacked Bar Plot)
my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
ax = pivedu.plot(
    kind='barh',
    stacked=True,
    color=my_colors
)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show() #memunculkan grafik

