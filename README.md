# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju
## Business Understanding
Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh wilayah Indonesia. Meskipun telah berkembang pesat, perusahaan menghadapi tantangan signifikan dalam mengelola sumber daya manusia. Salah satu indikator yang menunjukkan adanya masalah adalah tingginya attrition rate atau tingkat keluar masuk karyawan, yang telah melebihi 10%. Hal ini dapat berdampak pada produktivitas, stabilitas tim, dan biaya rekrutmen yang meningkat.

## Permasalahan Bisnis
Beberapa permasalahan utama yang dihadapi perusahaan, berdasarkan analisis data, meliputi:

- Tingginya attrition rate di departemen tertentu, khususnya Sales dan Research & Development.

- Rendahnya tingkat kepuasan terhadap lingkungan kerja dan keseimbangan kehidupan kerja (work-life balance) pada karyawan yang keluar.

- Persentase tinggi karyawan lajang yang mengalami attrition, menunjukkan kemungkinan kurangnya dukungan sosial di tempat kerja.

- Belum adanya sistem prediktif untuk mengantisipasi karyawan yang berisiko tinggi untuk resign.

## Cakupan Proyek
Proyek ini mencakup:

Analisis eksploratif terhadap data HR untuk mengidentifikasi pola dan faktor penyebab attrition.

- Pembuatan business dashboard interaktif menggunakan Looker Studio untuk memvisualisasikan faktor-faktor utama attrition.

- Pengembangan aplikasi prediktif berbasis Streamlit untuk mengklasifikasikan kemungkinan karyawan akan keluar, berdasarkan data historis.

Persiapan

[Sumber data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee): Dataset internal perusahaan dengan lebih dari 1000 karyawan, berisi 35 fitur terkait karakteristik karyawan, kepuasan kerja, kompensasi, dan histori pekerjaan.

Setup environment:

```
Tools yang digunakan:
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit)
- Looker Studio (untuk visualisasi dashboard)
- Jupyter Notebook (untuk eksplorasi dan modelling)
```
## Setup menggunakan Google colab 
```
!pip install -r requirements.txt
```
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup dengan pipenv (alternatif)
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install --python 3.9
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run app.py
```

## Business Dashboard
Business dashboard dibuat menggunakan Looker Studio, dengan fokus utama pada analisis visual terhadap faktor-faktor penyebab attrition. Beberapa visualisasi yang ditampilkan antara lain:

- Distribusi attrition berdasarkan status pernikahan, departemen, dan bidang pendidikan.

- Perbandingan tingkat kepuasan kerja (Job Satisfaction), lingkungan kerja (Environment Satisfaction), dan keseimbangan kerja-hidup (Work Life Balance) antara karyawan yang bertahan dan yang keluar.

- Grafik attrition berdasarkan OverTime, yang menunjukkan dampak beban kerja terhadap keputusan resign.

- Dashboard ini menjadi alat bantu utama bagi tim HR untuk mengidentifikasi area yang memerlukan perhatian khusus dan mengambil tindakan preventif lebih cepat.
  
![image](https://github.com/user-attachments/assets/6fc0206d-a4d7-4f3b-abfa-acd1e8f724ed)


[Link Business Dashboard](https://lookerstudio.google.com/reporting/6c5a2346-bbd8-41fd-97e1-827e9939a4e9)
## Model Prediction

- Dalam Prediksi ini. HR hanya perlu memasukkan ID dari pekerja, kemudian disini akan memperlihatkan presentase prediksi apakah memiliki kemungkinan keluar tinggi atau tidak.
![Screenshot 2025-05-13 081946](https://github.com/user-attachments/assets/0451977e-2fd7-43a2-8168-c596ca211ef6)

- ini adalah contoh jika prediksi mendapati bahwa Employee dengan ID 12 memiliki kemungkinan keluar yang tinggi.
![Screenshot 2025-05-13 082042](https://github.com/user-attachments/assets/20e899d7-585e-43a0-b18b-70db4d85765f)

- Pada Halaman ini juga terdapat Dashboard untuk HR mempertimbangkan prediksi dan juga Employee bagaimana untuk mempertahankan dan menciptakan ruang kerja yang lebih baik.
![Screenshot 2025-05-13 082131](https://github.com/user-attachments/assets/b2a19572-b9cc-423c-ae3b-162b79675285)
![Screenshot 2025-05-13 082138](https://github.com/user-attachments/assets/083a679a-edd3-41f6-a027-0b1d157fda16)
![Screenshot 2025-05-13 082148](https://github.com/user-attachments/assets/02e92c06-abfb-403c-a64e-f1201fe2acdb)


[Link Streamlit](https://humanrecourse-2cglzs2f3lvwggixfsusrn.streamlit.app/)

## Conclusion
Hasil analisis menunjukkan bahwa attrition di perusahaan Jaya Jaya Maju dipengaruhi oleh kombinasi faktor internal dan sosial. Beberapa faktor utama yang berkontribusi terhadap keputusan karyawan untuk keluar dari perusahaan meliputi rendahnya kepuasan kerja, beban kerja yang tinggi, dan buruknya keseimbangan antara kehidupan kerja dan pribadi. Selain itu, faktor sosial seperti status pernikahan juga berpengaruh, di mana proporsi karyawan lajang yang mengalami attrition jauh lebih tinggi dibandingkan kelompok lainnya.

Dari sisi departemen, Sales dan R&D merupakan dua divisi dengan tingkat attrition tertinggi. Hal ini menunjukkan bahwa mungkin terdapat tekanan kerja atau kurangnya dukungan organisasi yang perlu ditangani secara khusus di kedua departemen tersebut.

Karakteristik umum dari karyawan yang mengalami attrition antara lain:

- Berusia muda (25–35 tahun)

- Belum menikah

- Bekerja di departemen Sales atau R&D

- Memiliki jam kerja yang panjang (>50 jam per minggu), dimana disini banyak yang overtime.

- Memiliki kepuasan kerja yang rendah

Model prediktif yang dikembangkan dengan algoritma machine learning dan diimplementasikan melalui aplikasi Streamlit mampu mengidentifikasi karyawan dengan risiko tinggi untuk resign. Dengan adanya sistem ini, departemen HR dapat melakukan intervensi lebih dini, seperti menawarkan program kesejahteraan karyawan, penyesuaian beban kerja, atau pendekatan personal bagi karyawan yang terdeteksi berisiko.

Rekomendasi utama bagi perusahaan adalah meningkatkan kualitas lingkungan kerja dan keseimbangan hidup karyawan, khususnya bagi karyawan muda dan lajang, serta melakukan evaluasi mendalam terhadap kondisi kerja di departemen dengan tingkat attrition tinggi.

## Rekomendasi Action Items
Berdasarkan hasil analisis pada dashboard, berikut adalah rekomendasi tindakan yang disarankan untuk menurunkan angka attrition di perusahaan Jaya Jaya Maju:

### 1. Kendalikan Jam Lembur (Overtime)
  Grafik menunjukkan bahwa lebih dari dua kali lipat jumlah karyawan yang lembur mengalami attrition dibandingkan dengan yang tidak. Oleh karena itu:

  * Batasi jam kerja maksimal menjadi ≤ 45 jam/minggu, terutama pada departemen Sales dan R&D.

  * Rekomendasi awal adalah mengurangi lembur hingga 30% dari kondisi saat ini, dengan memantau dampaknya dalam 3 bulan.

  * Terapkan skema kompensasi lembur yang adil dan pantau work-load melalui aplikasi monitoring internal.

### 2. Fokus pada Departemen Sales dan R&D
  Pie chart menunjukkan bahwa Sales (39.9%) dan R&D (58.2%) menyumbang hampir seluruh attrition. Rekomendasi:
  
  * Lakukan audit beban kerja dan distribusi tugas di dua departemen ini.

  * Berikan training manajemen stres dan leadership untuk supervisor/manager.

  * Tawarkan jalur pengembangan karier yang lebih jelas untuk mengurangi stagnasi profesional.

### 3. Optimalkan Program Kesejahteraan
  Berdasarkan grafik Environment, Job, dan Work-Life Balance:

  * Mayoritas karyawan yang keluar memberikan skor 1–2 (rendah) pada ketiga aspek ini.

  * Rekomendasi: Tawarkan fleksibilitas kerja (hybrid), sesi counseling bulanan, dan cuti tambahan untuk keseimbangan hidup.

### 4. Intervensi Sosial untuk Karyawan Lajang
  Pie chart menunjukkan bahwa 52.5% dari karyawan yang keluar adalah lajang. Ini menunjukkan perlunya dukungan sosial di tempat kerja:
  
  * Adakan kegiatan seperti team bonding, komunitas minat, mentoring lintas divisi, atau volunteer day.

  * Tawarkan sesi “HR one-on-one” untuk mendengarkan aspirasi pribadi dan meningkatkan sense of belonging.
  
### 5. Implementasi Sistem Prediksi Attrition
  Aplikasi prediktif yang dibuat dapat mengenali profil karyawan berisiko tinggi berdasarkan faktor-faktor seperti:

  * Status lajang, kerja lembur, skor kepuasan rendah, dan departemen kerja.

  * Gunakan sistem ini secara berkala (bulanan) untuk melakukan intervensi seperti coaching, diskusi karier, atau rotasi pekerjaan.
