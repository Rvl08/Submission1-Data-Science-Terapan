# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang didirikan pada tahun 2000 dan memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun telah berkembang pesat, perusahaan ini menghadapi tantangan dalam mengelola karyawan, yang menyebabkan tingginya attrition rate, mencapai lebih dari 10%. Untuk mengatasi masalah ini, manajer HR meminta bantuan untuk mengidentifikasi faktor-faktor penyebab tingginya attrition rate dan membuat business dashboard untuk memonitor faktor-faktor tersebut.

### Permasalahan Bisnis
1. Tingginya tingkat attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan).
2. Faktor-faktor apa saja yang mempengaruhi tingginya tingkat attrition rate.
3. Membuat business dashboard untuk memonitor berbagai faktor yang mempengaruhi tingkat attrition rate.
   
### Cakupan Proyek
  Proyek ini terbatas pada analisis dan pemodelan data karyawan. Tujuan utama adalah untuk memahami faktor-faktor yang mempengaruhi attrition rate dan memberikan rekomendasi untuk mengurangi tingkat attrition.
  
### Persiapan
Sumber data: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)
Setup environment:
1. Install Anaconda atau Miniconda di komputer
2. Buka Terminal
3. Buat environment baru dengan perintah `conda create -n env python=3.9`
4. Aktifkan environment yang sudah dibuat menggunakan perintah `conda activate env`
5. Install library yang dibutuhkan `conda install pandas scikit-learn seaborn matplotlib jupyter`
6. `pip install joblib`
7. Jalankan Jupyter Notebook dengan perintah `jupyter notebook`
   
## Business Dashboard
Business dashboard akan digunakan untuk visualisasi data karyawan secara interaktif, business dashboard ini juga memberikan wawasan tentang faktor-faktor yang mempengaruhi attrition rate. Dashboard ini mencakup visualisasi seperti jumlah karyawan yang keluar di setiap departemen, jumlah attrition berdasarkan kelompok umur, tingkat attrition berdasarkan job role, dan lain sebagainya.

Link Dashboard:
https://public.tableau.com/views/Submission_17179535733160/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link

## Concluion
Proyek ini memiliki tujuan untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap attrition karyawan di perusahaan Jaya Jaya Maju. Analisis korelasi digunakan untuk melihat korelasi antar variabel, terutama antara variabel Attrition dengan variabel lain, sehingga diperoleh kesimpulan variabel yang paling berpengaruh terhadap Attrition. Penggunaan model machine learning juga digunakan untuk melakukan prediksi terhadap data baru sesuai dengan variabel-variabel penting yang sudah ditentukan melalui analisis korelasi.

### Rekomendasi Action Item
1. Terapkan kebijakan yang mempromosikan kesetaraan gender.
2. Terapkan program mentorship dan rencana pengembangan karir untuk karyawan muda guna meningkatkan keterlibatan dan retensi.
3. Sesuaikan strategi retensi untuk kelompok usia tertentu, seperti peluang kemajuan karir, inisiatif keseimbangan kerja-kehidupan, dan program pengakuan untuk meningkatkan semangat dan keterlibatan.
4. Tingkatkan kepuasan kerja melalui desain pekerjaan yang lebih baik, program pengakuan, dan peluang pengembangan profesional.
5. Promosikan keseimbangan kerja-kehidupan melalui jam kerja yang fleksibel, opsi kerja jarak jauh, dan program kesejahteraan.
