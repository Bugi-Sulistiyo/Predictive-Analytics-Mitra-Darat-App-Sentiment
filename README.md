# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek
MitraDarat merupakan aplikasi milik Dinas Perhubungan Republik Indonesia yang menyediakan layanan informasi terkait transportasi darat, termasuk fitur utama seperti pelacakan bus kota secara real-time. Fitur ini sangat krusial bagi masyarakat pengguna transportasi umum di kota-kota besar. Proyek ini bertujuan untuk menganalisis sentimen masyarakat terhadap aplikasi MitraDarat, guna mengetahui tingkat kepuasan pengguna serta mengidentifikasi potensi perbaikan pada fitur-fitur yang ada. Data yang digunakan diperoleh dari ulasan pengguna di Google Play melalui Google Play API.

## Business Understanding
Aplikasi MitraDarat berperan penting dalam menunjang layanan transportasi yang terintegrasi, terutama dalam pelacakan bus kota secara real-time. Namun, persepsi dan pengalaman pengguna terhadap aplikasi ini belum sepenuhnya dipahami. Analisis sentimen ulasan pengguna dapat membantu mengidentifikasi potensi masalah dan kebutuhan akan perbaikan, sehingga aplikasi ini dapat terus memenuhi harapan masyarakat.

### Problem Statements
1. Bagaimana persepsi dan sentimen pengguna terhadap aplikasi MitraDarat, terutama terkait fitur pelacakan bus kota?
2. Apakah ada tren umum dalam ulasan pengguna yang menunjukkan masalah teknis atau keluhan spesifik terhadap fitur-fitur tertentu?
3. Apakah aplikasi MitraDarat membutuhkan peningkatan lebih lanjut berdasarkan umpan balik pengguna?

### Goals

1. Mengidentifikasi dan memahami sentimen masyarakat terhadap aplikasi MitraDarat berdasarkan ulasan yang tersedia di Google Play.
2. Mengungkap tren atau pola utama dalam komentar yang menunjukkan area yang perlu diperbaiki atau dikembangkan.
3. Memberikan rekomendasi berdasarkan hasil analisis sentimen untuk meningkatkan kualitas layanan aplikasi MitraDarat, terutama pada fitur pelacakan bus.

## Data Understanding
Data yang digunakan dalam proyek ini diambil dari ulasan aplikasi MitraDarat di Google Play Store menggunakan Google Play API melalui alat bantu `reviews` dengan bahasa pemrograman Python. Data tersebut mencakup berbagai informasi terkait ulasan pengguna, namun hanya variabel `content` (teks ulasan) dan `score` (nilai rating) yang digunakan untuk analisis sentimen. Selain itu, variabel `at` digunakan untuk mendapatkan rentang waktu ulasan yang dikumpulkan, yaitu dari 2023-02-28 hingga 2024-10-09.

Dataset ini terdiri dari 1902 ulasan yang diberikan oleh 1890 pengguna berbeda. Distribusi ulasan berdasarkan sentimen yang didapatkan dari score rating adalah sebagai berikut:
- **Positif**: 960 ulasan (57,83%)
- **Negatif**: 540 ulasan (32,53%)
- **Netral**: 160 ulasan (9,64%)

Distribusi berdasarkan skor rating menunjukkan kecenderungan mayoritas ulasan berada di skor 5 dan 1:
- **Skor 5**: 833 ulasan
- **Skor 1**: 426 ulasan
- **Skor 3**: 160 ulasan
- **Skor 2**: 114 ulasan
- **Skor 4**: 105 ulasan

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
