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

Sumber data: Dataset internal perusahaan dengan lebih dari 1000 karyawan, berisi 35 fitur terkait karakteristik karyawan, kepuasan kerja, kompensasi, dan histori pekerjaan.

Setup environment:

```
Tools yang digunakan:
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit)
- Looker Studio (untuk visualisasi dashboard)
- Jupyter Notebook (untuk eksplorasi dan modelling)
```
## Business Dashboard
Business dashboard dibuat menggunakan Looker Studio, dengan fokus utama pada analisis visual terhadap faktor-faktor penyebab attrition. Beberapa visualisasi yang ditampilkan antara lain:

- Distribusi attrition berdasarkan status pernikahan, departemen, dan bidang pendidikan.

- Perbandingan tingkat kepuasan kerja (Job Satisfaction), lingkungan kerja (Environment Satisfaction), dan keseimbangan kerja-hidup (Work Life Balance) antara karyawan yang bertahan dan yang keluar.

- Grafik attrition berdasarkan OverTime, yang menunjukkan dampak beban kerja terhadap keputusan resign.

- Dashboard ini menjadi alat bantu utama bagi tim HR untuk mengidentifikasi area yang memerlukan perhatian khusus dan mengambil tindakan preventif lebih cepat.
  
![Screenshot 2025-05-13 085418](https://github.com/user-attachments/assets/83ce2a58-35fa-4c2a-aa43-701c0b2b7fec)

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
Hasil analisis menunjukkan bahwa attrition di perusahaan Jaya Jaya Maju sangat dipengaruhi oleh faktor internal seperti kepuasan kerja, beban kerja berlebih, dan keseimbangan hidup yang buruk. Selain itu, ditemukan bahwa departemen Sales dan R&D menjadi kontributor terbesar terhadap angka attrition. Faktor sosial juga turut memengaruhi, terlihat dari proporsi tinggi karyawan lajang yang keluar.

Model prediktif yang dikembangkan melalui Streamlit membantu mengidentifikasi karyawan yang berisiko tinggi resign, memungkinkan HR untuk melakukan intervensi dini.

## Rekomendasi Action Items
- Meningkatkan program kesejahteraan karyawan yang fokus pada work-life balance dan lingkungan kerja yang sehat.

- Memberikan perhatian lebih pada departemen dengan attrition tinggi (Sales dan R&D) melalui insentif berbasis performa, pelatihan manajerial, dan evaluasi beban kerja.

- Menyelenggarakan kegiatan sosial internal untuk meningkatkan keterikatan sosial, khususnya bagi karyawan yang belum menikah.

- Menerapkan kebijakan jam kerja fleksibel dan pekerjaan jarak jauh (remote) bagi peran yang memungkinkan.

- Menggunakan sistem prediksi berbasis machine learning untuk memantau dan merespon risiko attrition secara proaktif.
