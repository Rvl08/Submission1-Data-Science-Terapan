{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "35da34c1-7259-4ef3-8241-4c22658fede3",
   "metadata": {},
   "source": [
    "# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech\n",
    "\n",
    "## Business Understanding\n",
    "Jaya Jaya Maju adalah perusahaan multinasional yang didirikan pada tahun 2000 dan memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun telah berkembang pesat, perusahaan ini menghadapi tantangan dalam mengelola karyawan, yang menyebabkan tingginya attrition rate, mencapai lebih dari 10%. Untuk mengatasi masalah ini, manajer HR meminta bantuan untuk mengidentifikasi faktor-faktor penyebab tingginya attrition rate dan membuat business dashboard untuk memonitor faktor-faktor tersebut.\n",
    "\n",
    "### Permasalahan Bisnis\n",
    "Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.\n",
    "1. Tingginya tingkat attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan)\n",
    "2. Faktor-faktor apa saja yang mempengaruhi tingginya tingkat attrition rate\n",
    "3. Membuat business dashboard untuk memonitor berbagai faktor yang mempengaruhi tingkat attrition rate.\n",
    "\n",
    "### Cakupan Proyek\n",
    "Tuliskan cakupan proyek yang akan dikerjakan.\n",
    "Proyek ini terbatas pada analisis dan pemodelan data karyawan. Tujuan utama adalah untuk memahami faktor-faktor yang mempengaruhi attrition rate dan memberikan rekomendasi untuk mengurangi tingkat attrition.\n",
    "\n",
    "### Persiapan\n",
    "\n",
    "Sumber data: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)\n",
    "\n",
    "Setup environment:\n",
    "\n",
    "1. Install Anaconda atau Miniconda di komputer\n",
    "2. Buka Terminal\n",
    "3. Buat environment baru dengan perintah `conda create -n env python=3.9\r\n",
    "4. Aktifkan environment yang sudah dibuat menggunakan perinta *`conda activate ev*`\n",
    "5. Install library yang dibutuhka *`conda install pandas scikit-learn seaborn matplotlib jupytr*`\n",
    "6 *`pip install joblb*`\n",
    "7. Jalankan Jupyter Notebook dengan perinta *`jupyter notebok*`\n",
    "\n",
    "##BusinessssDashboadrrBusiness dashboard akan digunakan untuk visualisasi data karyawan secara interaktif, business dashboard ini juga memberikan wawasan tentang faktor-faktor yang mempengaruhi attrition rate. Dashboard ini mencakup visualisasi seperti jumlah karyawan yang keluar di setiap departemen, jumlah attrition berdasarkan kelompok umur, tingkat attrition berdasarkan job role, dan lain sebagainay.u\n",
    "Link Dashboard:\n",
    "https://public.tableau.com/views/Submission_17179535733160/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_lin`\n",
    "\n",
    "## Concluion\n",
    "oProyek ini memiliki tujuan untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap attrition karyawan di perusahaan Jaya Jaya Maju. Analisis korelasi digunakan untuk melihat korelasi antar variabel, terutama antara variabel Attrition dengan variabel lain, sehingga diperoleh kesimpulan variabel yang paling berpengaruh terhadap Attrition. Penggunaan model machine learning juga digunakan untuk melakukan prediksi terhadap data baru sesuai dengan variabel-variabel penting yang sudah ditentukan melalui analisis korelasi.\n",
    "\n",
    "### Rekomendasi Action It\n",
    "\n",
    "m1.Terapkan kebijakan yang mempromosikan kesetaraan gender.\n",
    "2.Terapkan program mentorship dan rencana pengembangan karir untuk karyawan muda guna meningkatkan keterlibatan dan retensn.\n",
    "3.Sesuaikan strategi retensi untuk kelompok usia tertentu, seperti peluang kemajuan karir, inisiatif keseimbangan kerja-kehidupan, dan program pengakuan untuk meningkatkan semangat dan keterlibatap.\n",
    "4.Tingkatkan kepuasan kerja melalui desain pekerjaan yang lebih baik, program pengakuan, dan peluang pengembangan profesiona.r\n",
    "5. Promosikan keseimbangan kerja-kehidupan melalui jam kerja yang fleksibel, opsi kerja jarak jauh, dan program kesejahteraan2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49eda7f7-6f30-4bca-b7c1-00bc560a5b9a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
