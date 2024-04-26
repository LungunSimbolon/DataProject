import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def run():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df1 = pd.read_csv('marketing_campaign.csv')

    # Set style
    sns.set_style('whitegrid')

    st.subheader("Melihat Perbandingan Mampu Bayar dan Tidak")
    st.write("Secara garis besar grafik menunjukkan proporsi antara debitur yang kemungkinan gagal bayar (1) sebesar 21.4% dan mampu bayar (0) di 78.5%.")
    numeric_cols = ['Year_Birth', 'Income', 'Recency', 'MntWines', 'MntFruits', 
                'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 
                'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 
                'NumWebVisitsMonth']
    # Mengatur ukuran gambar
    plt.figure(figsize=(18, 24))
    # Membuat histogram untuk kolom-kolom numerik
    for i, col in enumerate(numeric_cols, +1):
        plt.subplot(6, 4, i)
        sns.histplot(df[col], bins=20, kde=True)
        plt.title(f'{col} Distribution')
        plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()

    st.subheader("Distribusi Data Numerik")
    st.write("Berdasarkan tahun kelahiran, paling banyak ada di antara tahun 1960 - 1980. Distribusi untuk pembelian wine, buah, produk daging, produk ikan, produk makanan manis, perhiasan cenderung turun frekuensinya berbanding dengan jumlah pembelanjaannya.")

    '''Membuat grafik distribusi masing-masing kolom numerikal'''

    #memilih kolom kategorikal
    categorical_cols = ['Education', 'Marital_Status', 'Kidhome', 'Teenhome', 
                        'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5',	'AcceptedCmp1',
                        'AcceptedCmp2',	'Complain', 'Response']

    # Mengatur ukuran gambar
    plt.figure(figsize=(20, 24))

    # Membuat pie chart untuk kolom-kolom kategorikal
    for i, col in enumerate(categorical_cols, 1):
        plt.subplot(6, 4, i)  # Menetapkan subplot sesuai dengan iterasi
        counts = df[col].value_counts()  # Menghitung jumlah nilai unik
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')  # Membuat pie chart
        plt.title(f'{col} Distribution')  # Menambahkan judul subplot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Menyusun legend

    plt.tight_layout()
    plt.show()

    st.subheader("Distribusi Kolom Kategorikal")
    st.write("Pendidikan dari calon customer yang terdata terdiri dari basic, 2n Cycle, Master, PhD, Graduation. Kolom Marital Status memiliki data berupa Absurd dan Yolo. Kedua data tersebut tidak diketahui artinya sehingga akan di drop, sisanya adalah status pernikahan calon customer mulai dari married (menikah), together (tinggal bersama namun tidak menikah), single (lajang), divorced (bercerai), widow (janda), alone (tidak menikah).") 
    st.write("Kolom tersebut didominasi oleh calon customer yang sudah menikah dan disusul dengan yang tinggal bersama namun tidak menikah. Calon customer kebanyakan tidak memiliki anak terlihat dari grafik Kidhome dan Teenhome yang didominasi oleh angka 0. Rata-rata calon customer menerima penawaran ketika ditawari di campaign ke 4 dimana terlihat dari penerimaannya sebesar 7.5%.")

    def_cnt = (df.Response.value_counts(normalize=True)*100)
    def_cnt.plot.bar(figsize=(3,3))
    plt.xticks(fontsize=12, rotation=0)
    plt.yticks(fontsize=12)
    plt.title("Perbandingan Respon Hasil Marketing", fontsize=15)
    for x,y in zip([0,1],def_cnt):
        plt.text(x,y,y,fontsize=12)
    plt.show()
    st.subheader("Distribusi Penerimaan Penawaran")
    st.write("Perbandingan customer yang menerima penawaran adalah 85.089% tidak menerima (0) dan 14.91% menerima penawaran (1).") 
    st.write("Berdasarkan angka tersebut maka perusahaan berusaha untuk meningkatkan conversion rate dengan memprediksi calon customer mana yang memiliki kemungkinan untuk membeli sehingga dalam proses marketing bisa lebih efektif.")

    # Membuat visualisasi dengan cara pertama-tama mengelompokkan berdasarkan kategori dan melakukan perhitungan count
    education_count = df.groupby(['Education', 'Response']).size().reset_index(name='Count').sort_values(by=["Education", "Count"], ascending=True)

    plt.figure(figsize=(4, 4))
    ax = sns.barplot(data=education_count, x='Education', y='Count', hue='Response')
    plt.legend(loc='best', bbox_to_anchor=(0.2, 1), prop={'size': 8})
    plt.xticks(rotation=90)
    plt.title("Distribusi Jumlah Respon Berdasarkan Pendidikan")
    plt.xlabel("Pendidikan")
    plt.ylabel("Jumlah")
    plt.tight_layout()
    # Memunculkan visualisasi
    plt.show()

    st.subheader("Distribusi Jumlah Respon Berdasarkan Pendidikan")
    st.write("Tingkat pendidikan didominasi oleh gelar sarjana (graduation) dengan frekuensi hampir seribu orang dan yang paling sedikit adalah basic.")
    st.write("Penawaran juga paling banyak dilakukan pada calon customer yang bergelar sarjana dimana berbanding lurus dengan persentase penerimaannya paling tinggi diantara tingkat pendidikan lainnya.")

    # Membuat visualisasi dengan cara pertama-tama mengelompokkan berdasarkan kategori dan melakukan perhitungan count
    Marital_Status_count = df.groupby(['Marital_Status', 'Response']).size().reset_index(name='Count').sort_values(by=["Marital_Status", "Count"], ascending=True)

    plt.figure(figsize=(4, 4))
    ax = sns.barplot(data=Marital_Status_count, x='Marital_Status', y='Count', hue='Response')
    plt.legend(loc='best', bbox_to_anchor=(0.2, 1), prop={'size': 8})
    plt.xticks(rotation=90)
    plt.title("Distribusi Jumlah Respon Berdasarkan Status Pernikahan")
    plt.xlabel("Pendidikan")
    plt.ylabel("Jumlah")
    plt.tight_layout()

    # Memunculkan visualisasi
    plt.show()
    st.subheader("Distribusi Jumlah Respon Berdasarkan Pendidikan")
    st.write("Tingkat pendidikan didominasi oleh gelar sarjana (graduation) dengan frekuensi hampir seribu orang dan yang paling sedikit adalah basic.")
    st.write("Penawaran juga paling banyak dilakukan pada calon customer yang bergelar sarjana dimana berbanding lurus dengan persentase penerimaannya paling tinggi diantara tingkat pendidikan lainnya.")

    # Membuat visualisasi dengan cara pertama-tama mengelompokkan berdasarkan kategori dan melakukan perhitungan count
    Marital_Status_count = df.groupby(['Marital_Status', 'Response']).size().reset_index(name='Count').sort_values(by=["Marital_Status", "Count"], ascending=True)

    plt.figure(figsize=(4, 4))
    ax = sns.barplot(data=Marital_Status_count, x='Marital_Status', y='Count', hue='Response')
    plt.legend(loc='best', bbox_to_anchor=(0.2, 1), prop={'size': 8})
    plt.xticks(rotation=90)
    plt.title("Distribusi Jumlah Respon Berdasarkan Status Pernikahan")
    plt.xlabel("Pendidikan")
    plt.ylabel("Jumlah")
    plt.tight_layout()

    # Memunculkan visualisasi
    plt.show()
    st.subheader("Distribusi Jumlah Respon Berdasarkan Status Pernikahan")
    st.write("Penawaran terbanyak dilakukan kepada calon customer yang berstatus menikah disusul oleh 'together' dan single.")
    st.write("Meskipun banyak ditawarkan kepada mereka yang sudah menikah namun tingkat penerimaan lebih besar pada mereka yang berstatus lajang. Hal tersebut mengindikasikan bahwa program kampanye yang dilakukan kemungkinan besar lebih cocok kepada mereka yang berstatus lajang ketimbang dari status pernikahan lainnya, hal ini terlihat dari perbandingan penolakan dan penerimannya. Frekuensi penolakan dari mereka yang lajang berada diurutan ketiga namun penerimaannya berada di urutan pertama.")

    # Membuat visualisasi dengan cara pertama-tama mengelompokkan berdasarkan kategori dan melakukan perhitungan count
    Kidhome_count = df.groupby(['Kidhome', 'Response']).size().reset_index(name='Count').sort_values(by=["Kidhome", "Count"], ascending=True)

    plt.figure(figsize=(4, 4))
    ax = sns.barplot(data=Kidhome_count, x='Kidhome', y='Count', hue='Response')
    plt.legend(loc='best', bbox_to_anchor=(0.2, 1), prop={'size': 8})
    plt.xticks(rotation=90)
    plt.title("Distribusi Jumlah Respon Berdasarkan Jumlah Kepemilikan Anak Kecil")
    plt.xlabel("Jumlah Anak")
    plt.ylabel("Jumlah")
    plt.tight_layout()

    # Memunculkan visualisasi
    plt.show()
    st.subheader("Distribusi Jumlah Respon Berdasarkan Jumlah Kepemilikan Anak Kecil")
    st.write("Berdasarkan data ini ditemukan bahwa calon customer yang tidak memiliki anak kecil di rumah cenderung lebih mudah dalam menerima penawaran dari tim marketing ketimbang mereka yang memiliki anak kecil.")

    # Membuat visualisasi dengan cara pertama-tama mengelompokkan berdasarkan kategori dan melakukan perhitungan count
    Teenhome_count = df.groupby(['Teenhome', 'Response']).size().reset_index(name='Count').sort_values(by=["Teenhome", "Count"], ascending=True)

    plt.figure(figsize=(4, 4))
    ax = sns.barplot(data=Teenhome_count, x='Teenhome', y='Count', hue='Response')
    plt.legend(loc='best', bbox_to_anchor=(1, 1), prop={'size': 8})
    plt.xticks(rotation=90)
    plt.title("Distribusi Jumlah Respon Berdasarkan Jumlah Kepemilikan Anak Remaja")
    plt.xlabel("Jumlah Anak")
    plt.ylabel("Jumlah")
    plt.tight_layout()

    # Memunculkan visualisasi
    plt.show()
    st.subheader("Distribusi Jumlah Respon Berdasarkan Jumlah Kepemilikan Anak Kecil")
    st.write("Grafik ini serupa dengan grafik sebelumnya hanya perbedaannya di grafik sebelumnya membahas kepemilikan anak kecil, untuk grafik ini yang dihitung adalah anak remaja. Terlihat penerimaan paling besar oleh calon customer yang memang tidak memiliki anak remaja di rumahnya.")
