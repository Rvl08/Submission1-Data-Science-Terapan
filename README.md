# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang didirikan pada tahun 2000 dan memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun telah berkembang pesat, perusahaan ini menghadapi tantangan dalam mengelola karyawan, yang menyebabkan tingginya attrition rate, mencapai lebih dari 10%. Untuk mengatasi masalah ini, manajer HR meminta bantuan untuk mengidentifikasi faktor-faktor penyebab tingginya attrition rate dan membuat business dashboard untuk memonitor faktor-faktor tersebut.

### Permasalahan Bisnis
Tingkat attrition rate yang tinggi, dengan lebih dari 10% karyawan meninggalkan perusahaan setiap tahun. Tingginya tingkat attrition ini dapat menimbulkan berbagai masalah, seperti meningkatnya biaya rekrutmen dan pelatihan, penurunan produktivitas, ataupun gangguan operasional.

### Cakupan Proyek
1. Mengidentifikasi faktor-faktor yang mempengaruhi tingkat attrition rate
2. Membuat dashboard untuk memantau faktor-faktor dominan yang mempengaruhi tingkat attrition secara real-time
3. Membuat model machine learning untuk memprediksi attrition karyawan
  
### Persiapan
Sumber data: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)
Setup environment:
1. Install Anaconda atau Miniconda di komputer
2. Buka Terminal / Anaconda Prompt 
3. Buat environment baru dengan perintah `conda create -n env python=3.9`
4. Aktifkan environment yang sudah dibuat menggunakan perintah `conda activate env`
5. Install library yang dibutuhkan `pip install -r requirements.txt`
7. Jalankan Jupyter Notebook dengan perintah `jupyter notebook`
   
## Business Dashboard
Business dashboard akan digunakan untuk visualisasi data karyawan secara interaktif, business dashboard ini juga memberikan wawasan tentang faktor-faktor yang mempengaruhi attrition rate. Dashboard ini mencakup visualisasi seperti jumlah karyawan yang keluar di setiap departemen, jumlah attrition berdasarkan kelompok umur, tingkat attrition berdasarkan job role, dan lain sebagainya.

Link Dashboard:
https://public.tableau.com/views/Submission_17179535733160/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link

## Concluion
Proyek ini memiliki tujuan untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap attrition karyawan di perusahaan Jaya Jaya Maju. Analisis korelasi digunakan untuk melihat korelasi antar variabel, terutama antara variabel Attrition dengan variabel lain, sehingga diperoleh kesimpulan variabel yang paling berpengaruh terhadap Attrition yaitu (StockOptionLevel, TotalWorkingYears, Age, JobLevel, MonthlyIncome, YearsWithCurrManager). Penggunaan model machine learning juga digunakan untuk melakukan prediksi terhadap data baru sesuai dengan variabel-variabel penting yang sudah ditentukan melalui analisis korelasi.

### Rekomendasi Action Item
1. Buat program mentorship yang memasangkan karyawan muda dengan mentor berpengalaman untuk bimbingan dan pengembangan.
2. Berikan program pelatihan gratis untuk karyawan seperti kursus ataupun sertifikasi
3. Berikan opsi kerja jarak jauh bagi karyawan yang sedang berhalangan atau tidak bisa datang langsung ke tempat kerja
4. Lakukan survey secara berkala untuk mengidentifikasi kebutuhan dari setiap kelompok usia karyawan
