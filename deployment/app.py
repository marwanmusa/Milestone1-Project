import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Milestone - Statistical Analysis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/',
        'Report a bug': "https://github.com/marwanmusa",
        'About': "# This is our first Milestone Project with Statistical Analysis Topic for Phase 0"
    }
)

st.sidebar.title('MENU')
selected = st.sidebar.radio('Select Page:',['Data Visualization','Statistical Analysis'])

if selected== 'Data Visualization':
    st.title('Visualisasi Kondisi Kasus Kecelakaan di Negara-negara Bagian di U.S')

    DATE_COLUMN = 'timestamp_of_crash'

    @st.cache
    def load_data(nrows):
        data = pd.read_csv('dataset_h8dsft_Milestone1_marwan_musa.csv', nrows=nrows)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN], infer_datetime_format=True)
        data['non_motorist_safety_equipment_use'].replace('Reflective Clothing (Jacket, Backpack, etc.)',\
            'Reflective Clothes', inplace=True)
        data['non_motorist_safety_equipment_use'].replace('Protective Pads (Elbows, Knees, Shins, etc.)',\
            'Protective Pads', inplace=True)
        data['non_motorist_safety_equipment_use'].replace('Other Safety Equipment','Other Eqpmnts', inplace=True)
        data['route_signing_name'].replace('Local Street – Municipality','LocStreet Municipality', inplace=True)
        data['route_signing_name'].replace('Local Street – Township','LStreet Township', inplace=True)
        data['route_signing_name'].replace('Local Street – Frontage Road (Since 1994)','LStreet Frontage R.', inplace=True)
        return data

    data_load_state = st.text('Loading data...')
    data = load_data(18934)
    data_load_state.text("Done! (using st.cache)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
        

    with st.container():
        st.header('Sepuluh Negara Bagian dengan Jumlah Kecelakaan Terbanyak')
        
        colorchoose = st.radio(
            "Pilih warna grafik?",
            ('Blue', 'Green'))
        if colorchoose == 'Blue':
            crash_freq = data['state_name'].value_counts().head(10)
            fig, ax = plt.subplots(figsize=(12.5,5))
            sns.barplot(x=crash_freq.index, 
                    y=crash_freq, ax=ax, 
                    orient='v',
                    color = "royalblue")
            plt.ylabel("Number of Crash")
            plt.title("Ten States with the Most Accidents")
                
        else:
            crash_freq = data['state_name'].value_counts().head(10)
            fig, ax = plt.subplots(figsize=(12.5,5))
            sns.barplot(x=crash_freq.index, 
                    y=crash_freq, ax=ax, 
                    orient='v',
                    color = "seagreen")
            plt.ylabel("Number of Crash")
            plt.title("Ten States with the Most Accidents")
        st.pyplot(fig)    
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        
    with st.container():
        st.header('Relasi Konsumsi Alkohol dengan Rasio Kecelakaan')
        crash_freq_by_alcohol = data['police_reported_alcohol_involvement'].value_counts()

        colorchoose1 = st.radio(
            "Pilih warna grafik?",
            ('Slate Blue', 'Chocolate'),)
        if colorchoose1 == 'Slate Blue':
            fig3, ax3 = plt.subplots(figsize=(12.5,5))
            sns.barplot(x=crash_freq_by_alcohol.index, 
                        y=crash_freq_by_alcohol, ax=ax3, 
                        orient='v',
                        color = "slateblue")
            plt.ylabel("Number of Crash")
            plt.xticks(size=10)
            plt.title("Alcohol Involvement")
                
        else:
            fig3, ax3 = plt.subplots(figsize=(12.5,5))
            sns.barplot(x=crash_freq_by_alcohol.index, 
                        y=crash_freq_by_alcohol, ax=ax3, 
                        orient='v',
                        color = "chocolate")
            plt.ylabel("Number of Crash")
            plt.xticks(size=10)
            plt.title("Alcohol Involvement")

        
        st.pyplot(fig3)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        
    with st.container():
        st.header('Pengaruh Safety Equipment Terhadap Jumlah Kematian Saat Kecelakaan')
        datac = data.copy()
        total_fatal_by_equipment = datac.groupby(['non_motorist_safety_equipment_use'])\
                                            ['number_of_fatalities'].sum().\
                                                sort_values(ascending=False)

        fig4, ax4 = plt.subplots(figsize=(12.5,5))
        colorchoose2 = st.radio(
            "Pilih warna grafik?",
            ('Tomato', 'Teal'),)
        if colorchoose2 == 'Tomato':
            sns.barplot(x=total_fatal_by_equipment.index, 
                        y=total_fatal_by_equipment, ax=ax4, 
                        orient='v',
                        color = "tomato")
        else:
            sns.barplot(x=total_fatal_by_equipment.index, 
                        y=total_fatal_by_equipment, ax=ax4, 
                        orient='v',
                        color = "teal")
        plt.ylabel("Number of Crash")
        plt.xlabel("Safety Equipment")
        plt.xticks(size=10)
        plt.title("Non-Motorist Safety Equipment Use")
        st.pyplot(fig4)
        st.write("")
        st.write("")
        st.write("")
        st.write("")


    with st.container():
        st.header('Tingkat Kecelakaan Berdasarkan Route Sign')
        crash_freq1 = data['route_signing_name'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(12.5,5))
        
        colorchoose3 = st.radio(
            "Pilih warna grafik?",
            ('Green', 'Indigo'),)
        if colorchoose3 == 'Green':
            sns.barplot(x=crash_freq1.index, 
                        y=crash_freq1, ax=ax2, 
                        orient='v',
                        color = "Seagreen")
        else :
            sns.barplot(x=crash_freq1.index, 
                        y=crash_freq1, ax=ax2, 
                        orient='v',
                        color = "Indigo")
            
        plt.ylabel("Number of Crash")
        plt.xticks(size=10)
        plt.title("Route Signing Name")
        st.pyplot(fig2)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
    with st.container():
        st.header('Jumlah Kecelakaan dan Kematian per Bulan')
        st.markdown('#### *Jumlah Kecelakaan per Bulan*')
        hist_values = np.histogram(data[DATE_COLUMN].dt.month, bins=12, range=(0,12))[0]
        
        # Some number in the range 0-12
        month_to_filter = st.slider('month', 0, 12, 6)
        filtered_data = data[data[DATE_COLUMN].dt.month == month_to_filter] 
        st.subheader('Pemetaan Jumlah Kasus Kecelakaan di Bulan %s' % month_to_filter)
        st.map(filtered_data)
        if st.checkbox('Show Data and Histogram'):
            st.subheader('Data')
            st.write(filtered_data)
            st.subheader('Histogram')
            st.bar_chart(hist_values)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        st.markdown("#### *Jumlah Kematian per Bulan*")
        fig1, ax1 = plt.subplots(figsize=(12.5,5))
        fatal_data = data.groupby(['month_of_crash']).agg(Sum=('number_of_fatalities', np.sum))
        sns.lineplot(x=fatal_data.index, y=fatal_data.Sum, ax=ax1, dashes=False, markers=True,)
        plt.ylabel("Number of Fatalities")
        plt.xlabel("Month of Crash")
        plt.title("Monthly Amount of Fatalities")
        st.pyplot(fig1)
        
    
    
else:
    st.title('Statistikal Analisis Kondisi Kasus Kecelakaan di Negara-negara Bagian di U.S')
    
    DATE_COLUMN = 'timestamp_of_crash'

    @st.cache
    def load_data(nrows):
        data = pd.read_csv('dataset_h8dsft_Milestone1_marwan_musa.csv', nrows=nrows)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN], infer_datetime_format=True)
        data['non_motorist_safety_equipment_use'].replace('Reflective Clothing (Jacket, Backpack, etc.)','Reflective Clothes', inplace=True)
        data['non_motorist_safety_equipment_use'].replace('Protective Pads (Elbows, Knees, Shins, etc.)','Protective Pads', inplace=True)
        data['non_motorist_safety_equipment_use'].replace('Other Safety Equipment','Other Eqpmnts', inplace=True)
        data['route_signing_name'].replace('Local Street – Municipality','LocStreet Municipality', inplace=True)
        data['route_signing_name'].replace('Local Street – Township','LStreet Township', inplace=True)
        data['route_signing_name'].replace('Local Street – Frontage Road (Since 1994)','LStreet Frontage R.', inplace=True)
        return data

    data = load_data(18934)
    st.header('*Topik* : Departemen Pengawasan Lalu Lintas Kementerian Perhubungan Amerika Serikat ingin mengetahui\
            kondisi kasus kecelakaan yang terjadi di jalan selama tahun 2016 yang berguna untuk diterapkan kebijakan baru \
                supaya dapat mengurangi angka kecelakaan di kemudian hari.')
    with st.container():
        st.markdown('## *Statistik Deskriptif*')
        st.markdown('1. Berapa minimum, maksimum, median, modus, dan rata-rata usia *occupant* yang terlibat dalam kecelakaan di tiap negara bagian?')
        st.markdown('2. Barapakah rata-rata, variansi dan standar deviasi usia yang terlibat dalam kecelakaan setahun terakhir?')
        st.markdown('### Analisis')
        st.markdown('#### 1. Berapa minimum, maksimum, median, modus, dan rata-rata usia *occupant* yang terlibat dalam kecelakaan di tiap negara bagian?')
        # using agg() function on dropoff_site column
        df_sn = data.groupby(['state_name']).agg(Minimum=('age', np.min),
                                                Maximum=('age', np.max),
                                                Mean=('age', np.mean),
                                                Median=('age', np.median), 
                                                Modus=('age', stats.mode))
                    
        # Displaying result
        st.write(df_sn.sort_values(by='Mean', ascending=False))
        with st.expander("See Insight"):
            st.write("""
                     Rhode Island, Massachusets, dan Wyoming merupakan 3 negara bagian dengan rata-rata usia paling tinggi\
                         yang terlibat dalam kecelakaan (occupants in a crash) yaitu usia 46 sampai 51 tahun (dewasa menuju lansia).\
                             Sedangkan South Dakota merupakan Negara Bagian dengan rata-rata usia occupants 25 tahun (remaja).""")

        st.markdown('#### 2. Barapakah rata-rata, variansi dan standar deviasi usia yang terlibat dalam kecelakaan setahun terakhir?')
        st.write('Minimum Age : ' + str(data['age'].min()))
        st.write('Maximum Age : ' + str(data['age'].max()))
        st.write('Range Age : ' + str(data['age'].max() - data['age'].min()))
        st.write('Variance Age : ' + str('{:0.2f}'.format(data['age'].var())))
        st.write('Standar Deviasi Age : ' + str('{:0.2f}'.format(data['age'].std())))
        with st.expander("See Insight"):
            st.write("""Range usia yang terlibat dalam kecelakaan setahun terakhir adalah adalah 101 tahun (lansia) dengan minimum usia\
                0 (0 hingga 11 bulan) dan maximum 101 tahun. Jika rata-rata usia yang terlibat dalam kecelakaan di U.S adalah 41 tahun,\
                    maka usia occupants lainnya akan berkisar ±20 tahun dari usia rata-rata.""")
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        
        
    with st.container():
        st.markdown('## *Statistik Inferensial*')
        st.markdown('Misalkan selama 1 tahun terakhir, di seluruh Negara Bagian setiap hari jumlah kematian dalam kecelakaan\
            rata-rata 1 orang dan selama sebulan terakhir, jumlah kematian dalam kecelakaan mencapai rata-rata 3 orang per hari.\
                Apakah ini berarti jumlah kematian dalam kecelakaan di seluruh Negara Bagian meningkat secara signifikan?')
        
        daily_fatality = data[['timestamp_of_crash','number_of_fatalities']].groupby('timestamp_of_crash').sum()
        st.write('Average number of fatalities a Day for the last a month: {}'.format(np.round(daily_fatality['number_of_fatalities'].mean())))
        
        st.markdown('Untuk memeriksa apakah daily jumlah kematian dalam kecelakaan meningkat secara signifikan atau tidak,\
            akan dilakukan *single sample one sided* dengan significance level 0,05. Metode ini digunakan karena variabel yang diuji\
                hanya satu dan komparasinya hanya di sampel (data satu bulan terakhir) dan populasi (yang diasumsikan data satu tahun terakhir).')
        st.markdown('Jadi hipotesis untuk kasus ini :')
        st.markdown('**H0: μ <= 3**')
        st.markdown('**H1: μ > 3**')
        st.write('')
        st.write('')
        st.markdown('dan hasil ujinya adalah')
        t_stat,p_val = stats.ttest_1samp(daily_fatality['number_of_fatalities'], 3)
        st.write('P-value:',p_val/2) # The p-value divided by 2 since the output is two-sided p-value
        st.write('t-statistics:',t_stat)
        
        daily_fatality_pop = np.random.normal(daily_fatality['number_of_fatalities'].mean(), daily_fatality['number_of_fatalities'].std(), 10000)

        ci = stats.norm.interval(0.90, daily_fatality['number_of_fatalities'].mean(), daily_fatality['number_of_fatalities'].std())

        fig, ax = plt.subplots(figsize=(16,5))
        sns.distplot(daily_fatality_pop, label='Daily number_of_fatalities (Population)', color='blue', ax=ax)
        ax.axvline(daily_fatality['number_of_fatalities'].mean(), color='red', linewidth=2, label='Daily number_of_fatalities (Mean)')
        ax.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
        ax.axvline(daily_fatality_pop.mean() + t_stat*daily_fatality_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
        ax.legend()
        st.pyplot(fig)
        st.markdown('*p-value lebih besar dari `0.05`, maka fail to reject H0*')
        st.markdown('Sehingga bisa disimpukan bahwa : *"Jumlah rata-rata kematian per kecelakaan di seluruh Negara Bagian di U.S tidak meningkat secara signifikan\
            satu bulan terakhir di 2016, artinya ada kasus kematian rata-rata yang cukup signifikan di bulan lainnya."*')
        
    with st.container():
        st.markdown('## Kesimpulan')
        st.markdown('#### *Setelah dilakukan Analisis melalui visualisasi data, statistik deskriptif dan statistik inferensial,\
            kesimpulan yang bisa kami berikan adalah :*')
        st.markdown('Dari seluruh Negara Bagian di U.S, California menempati rank pertama dengan Jumlah kematian di atas 3000 kasus,\
            kemudian Florida dengan jumlah 2000 kasus dan Texas dengan jumlah hampir setengah kasus yang terjadi di California.')
        st.markdown('Sebenarnya cukup banyak faktor yang sangat berperan dalam terjadinya kecelakaan hingga menyebabkan korban,\
            diantaranya berkendara dalam keadaan mabuk (bagi pengendara) dan alat pelindung bagi occupants atau siapapun yang\
            terlibat dalam kecelakaan itu. Faktor pertama, umumnya keterlibatan alkohol sangat erat dengan ratio kecelakaan,\
            namun untuk semua kasus di Negara-negara bagian di U.S, ternyata pengendara non-alkohol lebih banyak yang mengalami\
            kecelakaan daripada pengendara yang terindikasi dalam keadaan mabuk akibat alkohol yang dikonsumsi sebelum berkendara.')
        st.markdown('Selanjutnya, faktor alat pelindung saat kecelakaan. Banyak kasus kematian tidak diketahui apakah occupants\
            memakai alat pelindung atau semacamnya saat kejadian berlangsung (not reported). Namun, berdasarkan data, dapat disimpulkan bahwa occupants\
            dengan tanpa safety equipment sama sekali probabilitas kematian dalam kecelakaannya meningkat 8 hingga 10 kali lipat dari\
            yang memakai pelindung seperti helmet, reflective clothing dan lain-lain.')
        st.markdown('Berdasarkan klasifikasi jalur atau jalan yang dilewati, di sejumlah Negara Bagian yang ada di U.S, terdapat 3 local street\
            yaitu local street Municipality, local street Township dan local street Frontage Road. Dari ketiga locat street tersebut, Municipality\
            merupakan jalur dengan jumlah kecelakaan terbanyak untuk seluruh Negara Bagian, kemudian State highway dan U.S highway. Sedangkan local\
            street Township dan Frontage Road persentasi kecelakaannya lebih kecil dari Interstate dan County road.')
        st.markdown('Range usia yang terlibat dalam kecelakaan setahun terakhir adalah adalah 101 tahun (lansia) dengan minimum usia\
            0 (0 hingga 11 bulan) dan maximum 101 tahun. Jika rata-rata usia yang terlibat dalam kecelakaan di U.S adalah 41 tahun,\
            maka usia occupants lainnya akan berkisar ±20 tahun dari usia rata-rata.')
        st.markdown('Rhode Island, Massachusets, dan Wyoming adalah 3 negara bagian dengan rata-rata usia paling tinggi yang terlibat\
            dalam kecelakaan (occupants in a crash) yaitu usia 46 sampai 51 tahun (dewasa menuju lansia). Sedangkan South Dakota merupakan\
            Negara Bagian dengan rata-rata usia occupants 25 tahun (remaja). Sehingga ini bisa dijadikan sebagai pertimbangan kedepan\
            bagi pemerintah di tiap-tiap Negara Bagian terutama Departemen Pengawasan Lalu Lintas Kementerian Perhubungan Amerika\
            Serikat untuk mengajukan regulasi tentang pembaharuan tata ruang kota yang lebih aman dan tertata dengan baik sehingga\
            tidak terlalu bahaya bagi orang-orang tua yang yang berkegiatan di jalan raya, walau hanya untuk jalan santai saja.\
            Untuk Negara bagian South Dakota, agar sekiranya Departemen Pengawasan Lalu Lintas juga bisa mensosialisasikan kepada\
            semua orang tua agar memperhatikan atau menasihati anak-anak remajanya untuk lebih aware dengan keadaan di jalan raya\
            atau jalur lalu lintas kota.')
        st.markdown('Mulai awal tahun hingga bulan juni, kasus kematian per bulan meningkat, setelah itu mengalami fluktuasi selama 3 bulan.\
            Menariknya, di bulan oktober kasus kematian mencapai puncak rate tertinggi dengan jumlah lebih dari 2600 jiwa dan menurun\
            hingga 2 bulan berikutnya di bulan desember sekitar 23 persen. Apakah jumlah kasus ini berhubungan erat dengan rata-rata\
            kasus kematian perbulan?')
        st.markdown('Setelah dilakukan uji hipotesis, "Jumlah rata-rata kematian per kecelakaan di seluruh Negara Bagian di U.S tidak\
            meningkat secara signifikan satu bulan terakhir di 2016, artinya ada kasus kematian rata-rata yang cukup signifikan di bulan\
            lainnya." Hasil uji hipotesis ini di dukung oleh analisis sebelumnya bahwa telah diperoleh jumlah kematian paling tinggi selama\
            setahun di 2016 ada di bulan Oktober.')
        
         