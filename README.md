## Latar Belakang
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
Dataset yang digunakan dalam proyek ini diambil dari ulasan aplikasi **MitraDarat** di Google Play Store dengan menggunakan **Google Play API** melalui alat bantu `reviews` dengan bahasa pemrograman **Python**. Dataset ini terdiri dari **1902** baris ulasan yang diberikan oleh **1890** pengguna yang berbeda, dan terdiri dari **3** kolom: `content` (teks ulasan), `score` (nilai rating), dan `at` (tanggal ulasan). Proses pengumpulan data dilakukan dari tanggal **2023-02-28** hingga **2024-10-09**.

Kondisi data secara umum cukup bersih, namun dilakukan beberapa tahap preprocessing seperti pembersihan teks dari karakter non-alfabet dan penghilangan duplikasi. Hanya dua variabel yang digunakan dalam analisis sentimen ini, yaitu:
- **content**: Teks ulasan yang diberikan oleh pengguna.
- **score**: Skor rating ulasan yang menunjukkan kepuasan pengguna (1 hingga 5).
Selain itu, variabel `at` digunakan untuk melacak rentang waktu ulasan tersebut dikumpulkan.

Berikut distribusi ulasan berdasarkan skor rating:
- **Skor 5**: 833 ulasan
- **Skor 1**: 426 ulasan
- **Skor 3**: 160 ulasan
- **Skor 2**: 114 ulasan
- **Skor 4**: 105 ulasan

Dataset dikumpulkan secara langsung melalui scraping menggunakan API dengan source coder seperti berikut:
```
scrapped_data, _ = reviews(
    "ngi.muchi.hubdat",
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=5000
)
```
Dataset tersebut dapat diakses pada link Google Drive berikut:
- [folder dataset submission](https://drive.google.com/drive/folders/1nDzTTgG7EorNZ7h3tYmoTst0plM4Ou0a?usp=sharing)
- [raw dataset](https://drive.google.com/file/d/1BHCgeUwFyJHVaskBLJnD5mUeKx6VbGvh/view?usp=drive_link)
- [cleaned dataset](https://drive.google.com/file/d/1weaYqI7CCJpNEdiUM5OlDtFrrn1KcOp-/view?usp=drive_link)
- [processed dataset](https://drive.google.com/file/d/1NAR4wt4SwX9FQT1jG7kuEoO97RlrPsVx/view?usp=drive_link)
- [labeled dataset](https://drive.google.com/file/d/1j_22mTMkXKylnquZa6lnjyS9eMq7H00K/view?usp=drive_link)

## Data Preparation
Proses data preparation dilakukan melalui beberapa tahapan untuk memastikan kualitas data sebelum diterapkan ke model NLP. Tahapan yang dilakukan adalah sebagai berikut:

1. **Data Exploration**
   <br>Pada tahap ini explorasi secara singkat dilakukan untuk memahami fitur data apa saja yang dapat dilakukan dan informasi umum lainnya seperti jumlah dataset, rentang waktu dataset, dan jumlah user yang berkontribusi pada dataset ini

2. **Pembersihan Data**
   <br>Langkah selanjutnya adalah pembersihan data yang dilakukan untuk mencegah terjadinya error pada tahapan selanjutnya dan menjaga dataset untuk memiliki pola yang baik. pembersihan data yang dilakukan adalah:
     - Menghilangkan nilai null
     - Menghilangkan nilai duplikat pada dataset
     - Menghilangkan fitur data yang tidak digunakan atau tidak relevan
  
3. **Pra-pemrosesan Teks**
   <br>Dataset yang digunakan secara umum melewati 4 tahapan pra-pemrosesan data, yaitu:
      - **Text Cleaning:**  mengubah teks menjadi huruf kecil danmenghilangkan karakter non-alfabet (tanda baca), extra whitespace, karakter non-ASCII, serta angka menggunakan package `regex`
      - **Stopword Removal:** menggunakan package `NLTK` untuk menghilangkan stopwords
      - **Stemming:** menggunakan package `Sastrawi` untuk melakukan teknik stemming pada data yang tersimpan dalam Bahasa Indonesia.
      - **Konversi Bahasa Gaul:** mengubah ulasan yang mengandung bahasa gaul atau singkatan ke bentuk baku menggunakan fungsi kustom ini.

4. **Pelabelan Sentimen**
   <br>Ulasan diberi label menggunakan metode **score rating** dari nilai ulasan dan juga dibandingkan dengan metode berbasis **lexicon**. Berdasarkan evaluasi performa model, metode **lexicon** menunjukkan hasil yang lebih baik pada saat pelatihan, oleh karena itu sentiment hasil metode ini digunakan dan diberi nama `sentiment_by_content` pada dataset. Hasil pelabelan menggunakan metode berbasis **lexicon** adalah sebagai berikut:

    | sentiment_by_score | count_score | sentiment_by_content | count_content | gap |
    | ------------------ | ----------- | -------------------- | ------------- | --- |
    | positive           | 938         | positive             | 344           | 594 |
    | negative           | 542         | negative             | 1120          | 578 |
    | neutral            | 160         | neutral              | 176           | 16  |

5. **Pembagian Data**
   <br> Dataset dibagi menjadi data latih dan data uji dengan rasio 80:20 menggunakan `train_test_split` dari package `scikit-learn`. Pembagian data ini juga menggunakan metode stratify shuffle split untuk memastikan distribusi label pada data latih dan data uji dipertimbangkan pada saat pembagian data berlangsung.

6. **Embedding**
   <br>Embedding dilakukan menggunakana bantuan API `TensorFlow` dan `Keras`. Proses embedding dilakukan dengan konfigurasi sebagai berikut:
   - `vocab_size = 10000`
   - `embedding_dim = 150`
   - `max_length = 100`
   - `trunch_type = "post"`
   - `oov_tok = "<OOV>"`

Dengan serangkaian proses ini, data siap digunakan untuk pemodelan machine learning.

## Model Development

Pada tahap ini, digunakan dua jenis model yaitu **machine learning** dan **deep learning**. Setiap model dijelaskan dengan cara kerjanya dan parameter yang digunakan.

### Model yang Digunakan

1. **Random Forest Classifier**:
   - **Cara Kerja**: Random Forest adalah model ensambel yang bekerja dengan membangun beberapa pohon keputusan selama proses pelatihan dan menggabungkan hasil dari setiap pohon untuk membuat prediksi akhir. Setiap pohon keputusan dalam Random Forest dibangun dari subset acak dari data latih, sehingga mengurangi risiko overfitting.
   - **Parameter yang Digunakan**: Model ini menggunakan parameter default dari package `scikit-learn`, seperti  `n_estimators=100` dan `criterion="gini"`.

2. **Logistic Regression**:
   - **Cara Kerja**: Logistic Regression adalah model linier yang digunakan untuk klasifikasi. Model ini menghitung probabilitas suatu sampel termasuk dalam satu dari beberapa kelas yang ada dengan fungsi logistik. Dalam kasus ini, model digunakan untuk klasifikasi sentimen ke dalam tiga kategori: positif, negatif, dan netral.
   - **Parameter yang Digunakan**: Model ini menggunakan parameter default dari `scikit-learn`, dengan solver `lbfgs` untuk optimasi dan `multi_class="auto"` untuk menangani lebih dari dua kelas.

3. **Decision Tree Classifier**:
   - **Cara Kerja**: Decision Tree membagi data secara rekursif berdasarkan fitur-fitur tertentu hingga menghasilkan simpul keputusan akhir. Pohon keputusan bekerja dengan membagi ruang fitur menjadi region terpisah berdasarkan kriteria tertentu (misalnya, Gini impurity atau entropy).
   - **Parameter yang Digunakan**: Model ini menggunakan parameter default dari `scikit-learn`, dengan kriteria pembagian node menggunakan impurity Gini (`criterion="gini"`) dan tanpa batas kedalaman pohon (`max_depth=None`).

4. **LSTM (Long Short-Term Memory)**:
   - **Cara Kerja**: LSTM adalah jenis jaringan saraf tiruan yang cocok untuk memproses data sekuensial, seperti teks ulasan. LSTM memiliki mekanisme memori yang memungkinkan model untuk mengingat informasi jangka panjang, sehingga sangat efektif dalam memahami konteks urutan kata dalam teks.
   - **Arsitektur**: Model ini terdiri dari lapisan embedding untuk mewakili kata dalam vektor numerik, dua lapisan LSTM, dan beberapa lapisan dropout serta normalisasi batch untuk mengurangi overfitting. Lapisan dense terakhir dengan aktivasi softmax digunakan untuk klasifikasi menjadi tiga kelas (positif, negatif, netral).
   
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

### Kelebihan dan Kekurangan Model

1. **Random Forest Classifier**:
   - **Kelebihan**:
     - Tahan terhadap overfitting, terutama pada dataset besar.
     - Memberikan akurasi yang tinggi dan dapat menangani variabel yang tidak relevan.
     - Dapat memberikan fitur penting dari data yang digunakan.
   - **Kekurangan**:
     - Model dapat menjadi kompleks dan lambat dalam prediksi ketika jumlah pohon meningkat.
     - Interpretasi model lebih sulit dibandingkan dengan model yang lebih sederhana.

2. **Logistic Regression**:
   - **Kelebihan**:
     - Sederhana dan mudah diinterpretasikan, cocok untuk klasifikasi biner.
     - Memungkinkan pemodelan hubungan linear antara fitur dan target.
   - **Kekurangan**:
     - Tidak efektif jika ada hubungan non-linear yang kuat antara fitur.
     - Mungkin tidak menangkap interaksi antara fitur tanpa teknik pengolahan data tambahan.

3. **Decision Tree Classifier**:
   - **Kelebihan**:
     - Mudah dipahami dan divisualisasikan, sehingga dapat menjelaskan keputusan model dengan jelas.
     - Tidak memerlukan skala data dan dapat menangani data kategorikal dengan baik.
   - **Kekurangan**:
     - Rentan terhadap overfitting, terutama pada dataset kecil atau ketika kedalaman pohon terlalu dalam.
     - Stabilitas rendah, karena perubahan kecil pada data dapat menghasilkan pohon keputusan yang sangat berbeda.

4. **LSTM (Long Short-Term Memory)**:
   - **Kelebihan**:
     - Efektif dalam menangkap urutan dan konteks dalam data teks, sangat cocok untuk analisis sentimen.
     - Dapat menangani masalah vanishing gradient, memungkinkan pembelajaran dari urutan yang lebih panjang.
   - **Kekurangan**:
     - Memerlukan lebih banyak data untuk pelatihan dan waktu pelatihan yang lebih lama dibandingkan model tradisional.
     - Kompleksitas model yang lebih tinggi membuat tuning hyperparameter menjadi tantangan.

## Evaluasi

Pada tahap ini, kinerja model yang telah diterapkan dalam analisis sentimen dievaluasi menggunakan metrik **akurasi**. Akurasi dihitung sebagai proporsi prediksi yang benar dari total prediksi. Dalam konteks ini, akurasi menunjukkan seberapa baik model dalam mengklasifikasikan sentimen menjadi kategori positif, negatif, dan netral.

### Metrik Evaluasi

- **Akurasi**:
  - Didefinisikan sebagai:
  
  \[
  \text{Akurasi} = \frac{\text{Jumlah Prediksi Benar}}{\text{Total Prediksi}} \times 100\%
  \]
  
  - Metrik ini memberikan gambaran umum tentang seberapa baik model bekerja dalam mengklasifikasikan data ke dalam kategori yang benar.

### Hasil Evaluasi Model

Berikut adalah hasil akurasi untuk setiap model yang digunakan dalam analisis sentimen:

1. **Random Forest Classifier**: 
   - Akurasi: 79.27%
  
2. **Logistic Regression**: 
   - Akurasi: 76.42%
  
3. **Decision Tree Classifier**: 
   - Akurasi: 69.11%
  
4. **Model LSTM**: 
   - Akurasi: 84.96% (pada epoch ke-31)

### Analisis Hasil

Model LSTM menunjukkan performa terbaik dengan akurasi 84.96%, menjadikannya model yang paling efektif untuk klasifikasi sentimen dalam dataset ini. Sebaliknya, Decision Tree Classifier memiliki akurasi terendah, yang mungkin disebabkan oleh kecenderungan untuk overfitting pada data pelatihan.

Akurasi yang lebih tinggi pada model LSTM dapat dikaitkan dengan kemampuannya dalam memahami konteks dan urutan kata dalam ulasan, serta penanganan data yang lebih kompleks dibandingkan dengan model tradisional lainnya.

Secara keseluruhan, hasil evaluasi ini menunjukkan bahwa penggunaan model berbasis deep learning, seperti LSTM, lebih efektif dalam analisis sentimen dibandingkan dengan model machine learning yang lebih sederhana.

## Kesimpulan
Berdasarkan hasil analisis sentimen terhadap ulasan pengguna aplikasi MitraDarat, dapat disimpulkan bahwa mayoritas ulasan bersentimen positif, namun terdapat juga bagian signifikan dari ulasan yang bersentimen negatif. Dari hasil evaluasi model, model LSTM menunjukkan performa terbaik dengan akurasi 84.96%, menjadikannya model yang paling efektif dalam mengklasifikasikan sentimen ulasan pengguna dibandingkan model lain seperti Random Forest Classifier, Logistic Regression, dan Decision Tree Classifier.

Kesimpulan ini mengindikasikan bahwa aplikasi MitraDarat telah memberikan kontribusi positif kepada sebagian besar penggunanya, khususnya dalam fitur-fitur seperti pelacakan bus online. Namun, ada juga ulasan negatif yang perlu diperhatikan lebih lanjut, yang menunjukkan adanya area yang perlu diperbaiki untuk meningkatkan pengalaman pengguna secara keseluruhan.

Dengan hasil ini, pihak pengelola aplikasi, yaitu Dinas Perhubungan, dapat menggunakan informasi dari analisis sentimen ini untuk mengidentifikasi area peningkatan pada aplikasi, terutama untuk mengatasi keluhan yang sering disampaikan pengguna. Dengan demikian, diharapkan aplikasi dapat semakin memenuhi kebutuhan masyarakat dan meningkatkan kepuasan pengguna secara lebih luas.