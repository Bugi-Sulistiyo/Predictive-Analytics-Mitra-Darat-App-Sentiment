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

Dataset ini terdiri dari 1902 ulasan yang diberikan oleh 1890 pengguna berbeda. Distribusi ulasan berdasarkan sentimen yang didapatkan dengan bantuan lexicon adalah sebagai berikut:
- **Positif**: 344 ulasan (21,01%)
- **Negatif**: 1118 ulasan (68,25%)
- **Netral**: 176 ulasan (10,74%)

Distribusi ulasan berdasarkan sentimen yang didapatkan dari score rating adalah sebagai berikut:
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
Proses data preparation dilakukan melalui beberapa tahapan untuk memastikan kualitas data sebelum diterapkan ke model machine learning.

1. **Pembersihan Data**<br>
  Langkah awal yang dilakukan adalah menghapus nilai **null** setelah proses pra-pemrosesan teks selesai, dan menghilangkan duplikasi data sebelum memulai pra-pemrosesan.

2. **Pra-pemrosesan Teks**<br>
  Semua teks ulasan melalui proses pra-pemrosesan, termasuk:
    - Mengubah teks menjadi huruf kecil.
    - Menghapus tanda baca, karakter spesial, dan angka menggunakan **regex**.
    - Melakukan **stemming** dengan bantuan paket **Sastrawi** untuk mengubah kata-kata ke bentuk dasarnya.
    - Menghilangkan kata-kata umum yang tidak berpengaruh (**stopwords**) menggunakan paket **nltk**.

3. **Konversi Bahasa Gaul**<br>
  Ulasan yang mengandung bahasa gaul atau informal dikonversi ke bentuk formal dengan menggunakan fungsi kustom yang dibuat untuk tujuan ini.

4. **Tokenisasi**<br>
  Teks dipecah menjadi token menggunakan **nltk.tokenizer** untuk mempermudah analisis.

5. **Pelabelan Sentimen**<br>
  Sentimen diberi label menggunakan metode **score rating** dari nilai ulasan dan juga dibandingkan dengan metode berbasis **lexicon**. Berdasarkan evaluasi, metode **lexicon** menunjukkan hasil yang lebih baik.

6. **Pembagian Data**<br>
  Dataset dibagi menjadi data latih, dan uji dengan rasio 80:20 menggunakan **train_test_split**.

1. **Penilaian Lexicon**<br>
  Skor dari metode lexicon juga diperoleh sebagai salah satu fitur tambahan.

Dengan serangkaian proses ini, data siap digunakan untuk pemodelan machine learning.

## Modeling

Model machine learning yang digunakan untuk menyelesaikan permasalahan analisis sentimen pada aplikasi MitraDarat adalah Random Forest Classifier, Logistic Regression, Decision Tree Classifier, dan model LSTM.

### Model yang Digunakan

1. **Random Forest Classifier**
2. **Logistic Regression**
3. **Decision Tree Classifier**
4. **Model LSTM**:
   - Arsitektur:
     ```python
     model = Sequential([
         Embedding(vocab_size, embedding_dim, input_length=max_length),
         LSTM(64, return_sequences=True),
         BatchNormalization(),
         Dropout(0.5),
         LSTM(32),
         BatchNormalization(),
         Dropout(0.5),
         Dense(32, activation="relu", kernel_regularizer=l2(0.001)),
         Dropout(0.6),
         Dense(3, activation="softmax")
     ])
     model.compile(loss="sparse_categorical_crossentropy", optimizer=Adam(learning_rate=0.0004), metrics=["accuracy"])
     ```

### Hasil Evaluasi Model

Metrik evaluasi yang digunakan untuk mengukur kinerja model yang telah diterapkan dalam analisis sentimen ulasan aplikasi MitraDarat adalah **akurasi**, yang merupakan indikator utama dalam pengukuran kinerja klasifikasi.

1. **Akurasi**: 
   - Akurasi dihitung sebagai proporsi prediksi yang benar dari total prediksi. Dalam konteks ini, akurasi menunjukkan seberapa baik model dalam mengklasifikasikan sentimen menjadi kategori positif, negatif, dan netral.

### Analisis Hasil

- **Random Forest Classifier**: 
  - Akurasi: 79.27%
- **Logistic Regression**: 
  - Akurasi: 76.42%
- **Decision Tree Classifier**: 
  - Akurasi: 69.11%
- **Model LSTM**: 
  - Akurasi: 84.96% (pada epoch ke-31)

Model LSTM menunjukkan performa terbaik dengan akurasi 84.96%, menjadikannya model yang paling efektif untuk klasifikasi sentimen dalam dataset ini. Sebaliknya, Decision Tree Classifier memiliki akurasi terendah, yang mungkin disebabkan oleh kecenderungan untuk overfitting pada data pelatihan. 

Akurasi yang lebih tinggi pada model LSTM dapat dikaitkan dengan kemampuannya dalam memahami konteks dan urutan kata dalam ulasan, serta penanganan data yang lebih kompleks dibandingkan dengan model tradisional lainnya.

Secara keseluruhan, hasil evaluasi ini menunjukkan bahwa penggunaan model berbasis deep learning, seperti LSTM, lebih efektif dalam analisis sentimen dibandingkan dengan model machine learning yang lebih sederhana.

## Kesimpulan
Berdasarkan hasil analisis sentimen terhadap ulasan pengguna aplikasi MitraDarat, dapat disimpulkan bahwa mayoritas ulasan bersentimen positif, namun terdapat juga bagian signifikan dari ulasan yang bersentimen negatif. Dari hasil evaluasi model, model LSTM menunjukkan performa terbaik dengan akurasi 84.96%, menjadikannya model yang paling efektif dalam mengklasifikasikan sentimen ulasan pengguna dibandingkan model lain seperti Random Forest Classifier, Logistic Regression, dan Decision Tree Classifier.

Kesimpulan ini mengindikasikan bahwa aplikasi MitraDarat telah memberikan kontribusi positif kepada sebagian besar penggunanya, khususnya dalam fitur-fitur seperti pelacakan bus online. Namun, ada juga ulasan negatif yang perlu diperhatikan lebih lanjut, yang menunjukkan adanya area yang perlu diperbaiki untuk meningkatkan pengalaman pengguna secara keseluruhan.

Dengan hasil ini, pihak pengelola aplikasi, yaitu Dinas Perhubungan, dapat menggunakan informasi dari analisis sentimen ini untuk mengidentifikasi area peningkatan pada aplikasi, terutama untuk mengatasi keluhan yang sering disampaikan pengguna. Dengan demikian, diharapkan aplikasi dapat semakin memenuhi kebutuhan masyarakat dan meningkatkan kepuasan pengguna secara lebih luas.