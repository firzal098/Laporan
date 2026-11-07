<!-- Halaman 1 -->

## Pemrosesan Bahasa Alami

## Penyusun:

## Dewi Soyusiawaty, S.T., M.T

---

<!-- Halaman 2 -->

## y

## HAK CIPTA

### PETUNJUK PRAKTIKUM PEMROSESAN BAHASA ALAMI

### Copyright© 2026

Dewi Soyusiawaty, S.T., M.T

### Hak Cipta dilindungi Undang-Undang

Dilarang mengutip, memperbanyak atau mengedarkan isi buku ini, baik sebagian maupun seluruhnya, dalam bentuk apapun, tanpa izin tertulis dari pemilik hak cipta dan penerbit.

### Diterbitkan oleh:

### Program Studi Informatika

Fakultas Teknologi Industri Universitas Ahmad Dahlan

Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166

Penulis : Dewi Soyusiawaty, S.T., M.T

Editor : Laboratorium Informatika, Universitas Ahmad Dahlan Desain sampul : Laboratorium Informatika, Universitas Ahmad Dahlan Tata letak : Laboratorium Informatika, Universitas Ahmad Dahlan

Ukuran/Halaman : 21 x 29,7 cm / 91 halaman

### Didistribusikan oleh:

Laboratorium Informatika

Universitas Ahmad Dahlan Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 Indonesia

---

<!-- Halaman 3 -->

## KATA PENGANTAR

Alhamdulillah segala puji dan syukur kehadirat Allah SWT, hanya atas rahmat dan hidayah-

Nyalah akhirnya petunjuk praktikum ini dapat terselesaikan.

Petunjuk praktikum ini digunakan sebagai bahan untuk kegiatan praktikum mata kuliah

Pemrosesan Bahasa Alami sebagai mata kuliah pilihan di Program Studi Informatika.

Petunjuk praktikum ini masih jauh dari sempurna, namun penulis berharap dapat bermanfaatbagi mahasiswa. Saran dan kritik sangat diharapkan untuk perkembangan selanjutnya.

Yogyakarta, 20 September 2026

Penyusun

---

<!-- Halaman 4 -->

### DAFTAR PENYUSUN

### Dewi Soyusiawaty, S.T., M.T

|  | Bidang Minat : Softcomputing dan Multimedia, Bahasa Alami |
| --- | --- |

---

<!-- Halaman 5 -->

## HALAMAN REVISI

Yang bertanda tangan di bawah ini: Nama : Dewi Soyusiawaty, S.T., M.T NIPM : 19760730 200409 011 0951361

Jabatan : Dosen Pengampu Mata Kuliah Pemrosesan Bahasa Alami

### Dengan ini menyatakan pelaksanaan Revisi Petunjuk Praktikum Pemrosesan Bahasa Alami

untuk Program Studi Informatika telah dilaksanakan dengan penjelasan sebagai berikut:

| No | Keterangan Revisi | Tanggal Revisi | Nomor Modul |
| --- | --- | --- | --- |
| 1 | Perubahan software yang digunakan ke Python | 2017 | PP/018/VI/R1 |
| 2 | Penambahan materi pengantar Python | 2018 | PP/018/VI/R2 |
| 3 | Penambahan materi Flask | 2019 | PP/018/VI/R2 |
| 4 | Penambahan materi ekspresi regular,terjemahan | 2021 | PP/018/VI/R2 |
| 5 | Perbaikan semua materi dari semua pertemuan | 2022 | PP/018/VI/R2 |
| 6 | Penambahan materi Statistical Machie Translation pada bab Machine Translation | 2024 | PP/018/VI/R6 |
| 7 |  | 2026 | PP/018/IV/R7 |

Yogyakarta, 20 September 2026

Penyusun

### Dewi Soyusiawaty, S.T., M.T

NIPM. 19760730 200409 011 0951361

---

<!-- Halaman 6 -->

## HALAMAN PERNYATAAN

Yogyakarta, 20 September 2026

Mengetahui, Ketua Program Studi

Kepala Laboratorium S1 Informatika

Dr. Murinto, S.Si., M.Kom. NIPM. 19730710 200409 111 0951298

Murein Miksa Mardhia, S.T., M.T. NIPM : 19891019 201606 011 1236278

---

<!-- Halaman 7 -->

## VISI DAN MISI PRODI INFORMATIKA

VISI

Menjadi Program Studi Informatika yang diakui secara internasional dan unggul dalam bidang Informatika serta berbasis nilai-nilai Islam.

MISI

1. Menjalankan pendidikan sesuai dengan kompetensi bidang Informatika yang diakui nasional dan internasional 2. Meningkatkan penelitian dosen dan mahasiswa dalam bidang Informatika yang kreatif, inovatif dan tepat guna. 3. Meningkatkan kuantitas dan kualitas publikasi ilmiah tingkat nasional dan internasional 4. Melaksanakan dan meningkatkan kegiatan pengabdian masyarakat oleh dosen dan mahasiswa dalam bidang Informatika. 5. Menyelenggarakan aktivitas yang mendukung pengembangan program studi dengan melibatkan dosen dan mahasiswa. 6. Menyelenggarakan kerja sama dengan lembaga tingkat nasional dan internasional. 7. Menciptakan kehidupan Islami di lingkungan program studi.

---

<!-- Halaman 8 -->

### TATA TERTIB LABORATORIUM S1 INFORMATIKA

DOSEN/KOORDINATOR PRAKTIKUM

1. Dosen harus hadir saat praktikum minimal 15 menit di awal kegiatan praktikum untuk mengisi materi dan menandatangani presensi kehadiran praktikum. 2. Dosen membuat modul praktikum, soal seleksi asisten, pre-test, post-test, dan responsi dengan berkoordinasi dengan asisten dan pengampu mata praktikum. 3. Dosen berkoordinasi dengan koordinator asisten praktikum untuk evaluasi praktikum setiap minggu. 4. Dosen menandatangani surat kontrak asisten praktikum dan koordinator asisten praktikum. 5. Dosen yang tidak hadir pada slot praktikum tertentu tanpa pemberitahuan selama 2 minggu berturut-turut mendapat teguran dari Kepala Laboratorium, apabila masih berlanjut 2 minggu berikutnya maka Kepala Laboratorium berhak mengganti koordinator praktikum pada slot tersebut.

PRAKTIKAN

1. Praktikan harus hadir 15 menit sebelum kegiatan praktikum dimulai, dan dispensasi terlambat 15 menit dengan alasan yang jelas (kecuali asisten menentukan lain dan patokan jam adalah jam yang ada di Laboratorium, terlambat lebih dari 15 menit tidak boleh masuk praktikum & dianggap Inhal). 2. Praktikan yang tidak mengikuti praktikum dengan alasan apapun, wajib mengikuti INHAL, maksimal 4 kali praktikum dan jika lebih dari 4 kali maka praktikum dianggap GAGAL. 3. Praktikan yang akan mengikuti inhal diwajibkan mendaftarkan diri dan membayar administrasi inhal kepada laboran inhal paling lambat H-1 jadwal inhal. 4. Praktikan harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut: a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki / Perempuan) dan

Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki / Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 5. Praktikan tidak boleh makan dan minum selama kegiatan praktikum berlangsung, harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di dalam laboratorium (tidak boleh membuang sampah sembarangan baik kertas, potongan kertas, bungkus permen baik di lantai karpet maupun di dalam ruang CPU). 6. Praktikan dilarang meninggalkan kegiatan praktikum tanpa seizin Asisten atau Laboran. 7. Praktikan harus meletakkan sepatu dan tas pada rak/loker yang telah disediakan. 8. Selama praktikum dilarang NGENET/NGE-GAME, kecuali mata praktikum yang membutuhkan atau menggunakan fasilitas Internet. 9. Praktikan dilarang melepas kabel jaringan atau kabel power praktikum tanpa sepengetahuan laboran 10. Praktikan harus memiliki FILE Petunjuk praktikum dan digunakan pada saat praktikum dan harus siap sebelum praktikum berlangsung. 11. Praktikan dilarang melakukan kecurangan seperti mencontek atau menyalin pekerjaan praktikan yang lain saat praktikum berlangsung atau post-test yang menjadi tugas praktikum. 12. Praktikan dilarang mengubah setting software/hardware komputer baik menambah atau mengurangi tanpa permintaan asisten atau laboran dan melakukan sesuatu yang dapat merugikan laboratorium atau praktikum lain. 13. Asisten, Koordinator Praktikum, Kepala laboratorium dan Laboran mempunyai hak untuk menegur, memperingatkan bahkan meminta praktikan keluar ruang praktikum apabila dirasa anda mengganggu

---

<!-- Halaman 9 -->

praktikan lain atau tidak melaksanakan kegiatan praktikum sebagaimana mestinya dan atau tidak mematuhi aturan lab yang berlaku. 14. Pelanggaran terhadap salah satu atau lebih dari aturan diatas maka Nilai praktikum pada pertemuan tersebut dianggap 0 (NOL) dengan status INHAL. 15. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 16. Sebelum pelaksanaan praktikum membaca surat pendek. 17. Praktikan saat memasuki lab wajib menggunakan kaos kaki. 18. Inhal yang diizinkan dapat diikuti oleh praktikan selama periode praktikum adalah maksimal 3 (tiga) kali.

Silakan menggunakan kuota inhal apabila mendapat halangan untuk hadir saat praktikum seperti sakit, izin, atau delegasi lomba. 19. Bagi mahasiswa (asisten praktikum dan praktikan) yang terbukti melakukan pelanggaran akademik akan dikenai sanksi sesuai aturan Fakultas/Universitas yang berlaku, serta digagalkan dari tanggungjawab di matapraktikum yang sedang ditempuh.

ASISTEN PRAKTIKUM

1. Asisten harus hadir 15 Menit sebelum praktikum dimulai (konfirmasi ke koordinator bila mengalami keterlambatan atau berhalangan hadir). 2. Asisten yang tidak bisa hadir WAJIB mencari pengganti, dan melaporkan kepada Koordinator Asisten. 3. Asisten harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut: a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki / Perempuan) dan

Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki / Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 4. Asisten harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di laboratorium, menegur atau mengingatkan jika ada praktikan yang tidak dapat menjaga kebersihan, ketertiban atau kesopanan. 5. Asisten harus dapat merapikan dan mengamankan presensi praktikum, Kartu Nilai serta tertib dalam memasukan/Input nilai secara Online/Offline. 6. Asisten mencatat dan merekap praktikan dengan status INHAL setiap minggu serta wajib mengumumkan mekanisme INHAL di awal pertemuan praktikum. 7. Asisten harus dapat bertindak secara profesional sebagai seorang asisten praktikum dan dapat menjadi teladan bagi praktikan. 8. Asisten harus dapat memberikan penjelasan/pemahaman yang dibutuhkan oleh praktikan berkenaan dengan materi praktikum yang diasisteni sehingga praktikan dapat melaksanakan dan mengerjakan tugas praktikum dengan baik dan jelas. 9. Asisten tidak diperkenankan mengobrol sendiri apalagi sampai membuat gaduh. 10. Asisten dimohon mengkoordinasikan untuk meminta praktikan agar mematikan komputer untuk jadwal terakhir dan sudah dilakukan penilaian terhadap hasil kerja praktikan. 11. Asisten wajib untuk mematikan LCD Projector dan komputer asisten/praktikan apabila tidak digunakan. 12. Asisten tidak diperkenankan menggunakan akses internet selain untuk kegiatan praktikum, seperti

Youtube/Game/Medsos/Streaming Film di komputer praktikan. 13. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 14. Sebelum pelaksanaan praktikum membaca surat pendek.

---

<!-- Halaman 10 -->

15. Praktikan saat memasuki lab wajib menggunakan kaos kaki. 16. Tim asisten sangat direkomendasikan untuk menyeragamkan aturan yang terkait dengan praktikum dalam slot tugasnya masing-masing sesuai dengan tata tertib yang diberlakukan dalam laboratorium. 17. Seluruh asisten praktikum dapat merekomendasikan pemberian reward dan/atau punishment ke sesama asisten praktikum dan/atau  praktikan kepada kepala laboratorium dengan melampirkan bukti pendukung yang relevan. 18. Bagi mahasiswa (asisten praktikum dan praktikan) yang terbukti melakukan pelanggaran akademik akan dikenai sanksi sesuai aturan Fakultas/Universitas yang berlaku, serta digagalkan dari tanggungjawab di matapraktikum yang sedang ditempuh.

LAIN-LAIN

1. Pada Saat Responsi Harus menggunakan Baju Kemeja untuk Laki-laki dan Perempuan untuk Praktikan dan Asisten. 2. Ketidakhadiran praktikum dengan alasan apapun dianggap INHAL. 3. Inhal yang diizinkan dapat diikuti oleh praktikan selama periode praktikum adalah maksimal 3 (tiga) kali. Silakan menggunakan kuota inhal apabila mendapat halangan untuk hadir saat praktikum seperti sakit, izin, atau delegasi lomba. 4. Pelaksanaan (waktu dan metode) INHAL sama seperti praktikum mingguan/reguler. 5. Izin praktikum mengikuti aturan izin SIMERU/KULIAH. 6. Yang tidak berkepentingan dengan praktikum dilarang mengganggu praktikan atau membuat keributan/kegaduhan. 7. Penggunaan lab diluar jam praktikum maksimal sampai pukul 18.15 dengan menunjukkan surat ijin dari Kepala Laboratorium Prodi Informatika.

Yogyakarta, 20 September 2026

Kepala Laboratorium S1 Informatika

Murein Miksa Mardhia, S.T., M.T. NIPM : 19891019 201606 011 1236278

---

<!-- Halaman 11 -->

## DAFTAR ISI

HAK CIPTA ..............................................................................................................................................................................1

KATA PENGANTAR .................................................................................................................................................................2

DAFTAR PENYUSUN ...............................................................................................................................................................3

HALAMAN REVISI ...................................................................................................................................................................4

HALAMAN PERNYATAAN .......................................................................................................................................................5

VISI DAN MISI PRODI INFORMATIKA .....................................................................................................................................6

TATA TERTIB LABORATORIUM S1 INFORMATIKA ..................................................................................................................7

SKENARIO PRAKTIKUM SECARA DARING ............................................................................................................................ 11

## PRAKTIKUM 1: PYTHON UNTUK NLP .................................................................................................................................. 12

## PRAKTIKUM 2: PREPROCESSING (FILTERING DAN TOKENIZATION) ................................................................................... 19

## PRAKTIKUM 3: PREPROCESSING (STEMMING DAN REGULAR EXPRESSION) ..................................................................... 25

## PRAKTIKUM 4: SPELL CHECK .............................................................................................................................................. 31

## PRAKTIKUM 5: PEMBOBOTAN/TF-IDF ................................................................................................................................ 38

## PRAKTIKUM 6: N-GRAM DAN NER ..................................................................................................................................... 44

## PRAKTIKUM 7: PARSING ..................................................................................................................................................... 54

## PRAKTIKUM 8: TEXT SUMMARIZATION.............................................................................................................................. 59

## PRAKTIKUM 9: MACHINE TRANSLATION I .......................................................................................................................... 67

## PRAKTIKUM 10: MACHINE TRANSLATION II ....................................................................................................................... 79

## PRAKTIKUM 11: FLASK ........................................................................................................................................................ 86

---

<!-- Halaman 12 -->

### SKENARIO PRAKTIKUM SECARA DARING

Nama Mata Praktikum : Pemrosesan Bahasa Alami Jumlah Pertemuan 10

### TABEL SKENARIO PRAKTIKUM DARING

| Pertemua nke | Judul Materi | Waktu (Lama praktikum sampai pengumpula n posttest) | Skenario Praktikum dari pemberian pretest, post-test dan pengumpulannya sertamencantumkan metode yang digunakan misal video, whatsapp group, Google meet atau lainnya |
| --- | --- | --- | --- |
| 1 | Pengenalan Python dan Pengolahan Dasar Teks | 90 menit | Pretest dilaksanakan dengan memberikansoal 1 jam sebelum praktikum dimulai dan praktikan mengupload hasil pekerjaan pretest paling lambat sebelum praktikum dimulai. Asisten membuat rekaman kegiatan praktikum dan praktikan menyimakrekaman tersebut. Soal Posttest diberikan 45 menit sebelumpraktikum berakhir dan praktikan mengerjakan sampai batas waktu akhir jam praktikum. |
| 2 | Preprocessing | 90 menit |  |
| 3 | Reguler Expression | 90 menit |  |
| 4 | TF-IDF | 90 menit |  |
| 5 | N Grams | 90 menit |  |
| 6 | Parsing | 90 menit |  |
| 7 | Named Entity Recognition | 90 menit |  |
| 8 | Text Summarization | 90 menit |  |
| 9 | Translator | 90 menit |  |
| 10 | Flask | 90 menit |  |
| 11 | Responsi | 90 menit | Responsi diberikan dalam bentuk tugasproyek yang dipresentasikan. |

---

<!-- Halaman 13 -->

## PRAKTIKUM 1: PYTHON UNTUK NLP

Pertemuan ke 1 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas. |
| --- | --- |
| CPMK-01 | Mampu menjelaskan konsep umum pemrosesan bahasa alami dan ruang lingkup penerapan aplikasinya. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan pemrosesan awal terhadap teks

2. Menerapkan pemrosesan awal terhadap teks

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menjelaskan konsep umum pemrosesan bahasa alami |
| --- | --- | --- |
| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menerapkan konsep umum pemrosesan bahasa alami |

---

<!-- Halaman 14 -->

### 1.3. TEORI PENDUKUNG

### A. Pengenalan Python

Python adalah bahasa pemrograman tingkat tinggi yang populer, mudah dipelajari, dan serbaguna, diciptakan oleh Guido van Rossum pada 1991. Python banyak digunakan untuk analisis data, machine learning, pengembangan web, dan otomatisasi tugas karena sintaksnya yang sederhana, bersih, serta mirip bahasa Inggris, menjadikannya ideal bagi pemula.

### Keunggulan Python:

### a. Interpreted: Kode langsung dijalankan tanpa perlu kompilasi terpisah, mempercepat

proses pengembangan.

### b. Open Source & Gratis: Bebas digunakan dan disebarluaskan.

### c. Lintas Platform: Dapat berjalan di Windows, Mac, dan Linux.

### d. Berorientasi Objek: Mendukung pemrograman berorientasi objek, fungsional, dan

prosedural.

### e. Library yang Berlimpah: Library-library yang telah tersedia sangat banyak dan

memudahkan tugas seorang pengembang.

### Kegunaan Utama:

### a. Data Science & ML: Pustaka (library) seperti NumPy, Pandas, Scikit-Learn.

### b. Pengembangan Web: Framework Django dan Flask.

### c. Otomatisasi (Scripting): Mengotomatiskan tugas harian, pengolahan file.

### Penulisan Syntax Python

### a. Case Sensitive: Artinya variabel dengan nama “PBA” berbeda dengan “Pba”.

### b. Variabel: Dinamis, tidak perlu dideklarasikan tipe datanya dan dapat diubah ketika

program dijalankan. Karakter pertama wajib huruf atau underscore sedangkan

### selanjutnya boleh huruf, underscore, maupun angka.

### c. Komentar Cukup diawali dengan tanda pagar (#), atau jika ingin beberapa garis

### sekaligus gunakan tiga tanda petik (“””) di awal dan di akhir.

### d. Tipe Data: Python memiliki beberapa tipe data yang berbeda jika dibandingkan

### dengan bahasa pemrograman lainnya. Berikut beberapa tipe data pada python:

| Tipe Data | Contoh | Penjelasan |
| --- | --- | --- |

---

<!-- Halaman 15 -->

| Boolean | True atau False | Menyatakan benar (True) yang bernilai 1, atau salah (False) yang bernilai 0. |
| --- | --- | --- |
| String | "Hello Word Python" | Menyatakan karakter/kalimat bisa berupa huruf, angka, dll (diapit di dalam tanda " atau '). |
| Integer | 25 atau 1209 | Menyatakan bilangan bulat. |
| Float | 3.14 atau 0.99 | Menyatakan bilangan yang mempunyai koma. |
| Hexadecimal | 9a atau 1d3 | Menyatakan bilangan dalam format heksa (bilangan berbasis 16). |
| Complex | 1 + 5j | Menyatakan pasangan angka real dan imajiner. |
| List | ['xyz', 768, 3.14] | Data untaian yang menyimpan berbagai tipe data tapi isinya bisa diubah-ubah. |
| Tuple | ('xyz', 768, 3.14) | Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah. |
| Dictionary | {'nama': 'ani', 'umur': 17} | Data untaian yang menyimpan berbagai tipe data berupa pasangan, penunjuk, dan nilai. |

### B. Pengolahan Dasar Teks

Pengolahan teks dalam Python adalah langkah penting dalam Pemrosesan Bahasa

Alami yang akan membersihkan dan mengubah teks mentah menjadi format terstruktur yang sesuai untuk model pembelajaran mesin. Beberapa proses yang biasa dilakukan:

a. Case folding: menyamakan case (lowercase: me-nonkapitalkan semua, uppercase:

mengapitalkan semua) b. Penghapusan karakter tak perlu: menghapus tanda baca, angka, atau karakter lainnya sesuai kebutuhan c. Tokenisasi: memecahkan kalimat menjadi token atau per kata d. Stemming: memotong kata berimbuhan e. Penghapusan kata yang umum muncul: semisal kata "dan", "aku", "kamu" yang merupakan kata umum dan dianggap tidak terlalu berarti dihapus f. Lemmatization: mengembalikkan kata ke bentuk dasar

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

---

<!-- Halaman 16 -->

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-01 | Apa yang kamu ketahui tentang python beserta keunggulannya? | 30 |
| 2 | CPL-03 | CPMK-01 | Apa saja tipe data yang ada pada python? | 30 |
| 3 | CPL-03 | CPMK-01 | Sebutkan dan jelaskan beberapa proses pengolahan dasar teks pada NLP! | 40 |

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Import Library

```
import pandas as pd 
```

Pandas merupakan library yang umum digunakan dalam pengolahan data.

2. Unduh dataset

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

Dataset diunduh langsung dari github.

3. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |
| --- | --- |
|  | df |

### B. Pengolahan Dataset dan Teks

1. Cek nama kolom dan jumlah baris

|  | column name = list(df) _ |
| --- | --- |
|  | row count = len(df) _ |
|  | column count = len(df.columns) _ |
|  |  |
|  | print("Nama kolom pada dataset: ", column name) _ |
|  | print("Jumlah kolom: ", column count, "kolom") _ |
|  | print("Jumlah baris: ", row count, "baris") _ |

list() : menampilkan nama kolom dalam bentuk list len() : menghitung jumlah item dalam suatu objek

---

<!-- Halaman 17 -->

print() : menampilkan/mencetak kalimat

2. Menghapus kolom yang tidak diperlukan

|  | df = df.drop(columns=['conversation id str', 'id str', _ _ _ |  |
| --- | --- | --- |
|  | 'tweet url', 'user id str']) _ _ _ |  |

Menggunakan fungsi .drop menghapus kolom: conversation_id_str, id_str, tweet_url, user_id_str

3. Ganti nama kolom

|  | df = df.rename(columns= |  |
| --- | --- | --- |
|  | { |  |
|  | "created at":"tgl tweet", _ _ |  |
|  | "full text":"tweet", _ |  |
|  | "in reply to screen name":"reply ke" _ _ _ _ _ |  |
|  | }) |  |
|  | df |  |

Mengganti kolom "created_at" menjadi "tgl_tweet", dst

4. Slicing data -> Mengambil bagian tertentu dari data a. Mengambil data teratas

|  | df.head() |  |
| --- | --- | --- |

b. Mengambil data terbawah

```
df.tail() 
```

c. Mengambil rentang data

|  | # Menampilkan data berdasarkan rentang index ke-0 sampai 9 |  |
| --- | --- | --- |
|  | df[:10] |  |
|  | # Menampilkan data dari rentang index ke-10 sampai 23 |  |
|  | df[10:24] |  |
|  | # Menampilkan data dari index ke-30 sampai akhir |  |
|  | df[30:] |  |

d. Mengambil data berdasar label/kelas

|  | # Menampilkan data dari kolom "tweet" |  |
| --- | --- | --- |
|  | df["tweet"] |  |
|  | # Menampilkan data dari kolom "tweet" dalam bentuk tabel |  |
|  | df[["tweet"]] |  |
|  | # Menampilkan data dari kolom "tweet" dan "username" dalam |  |
|  | bentuk tabel |  |
|  | df[["tweet", "username"]] |  |

e. Menggunakan .loc[] dan .iloc[]

---

<!-- Halaman 18 -->

• .loc[ ] mengakses data berdasarkan nama kolom/label, bisa disertai kondisional (sama dengan, lebih dari, kurang dari, dll)

|  | # Menampilkan data yang berada di baris ke-33 |  |
| --- | --- | --- |
|  | df.iloc[33] |  |
|  | # Menampilkan data tweet yang memiliki value/nilai lebih |  |
|  | dari sama dengan 1200 likes menggunakan .loc[] |  |
|  | df.loc[df["favorite count"] >= 1200] _ |  |
|  | # Menampilkan data tweet yang memiliki nilai antara 51 |  |
|  | hingga 100 likes menggunakan .loc[] |  |
|  | df.loc[(df["favorite count"] <= 100) & _ |  |
|  | (df["favorite count"] > 50)] _ |  |
|  | # Menampilkan data pada baris ke-2000 dari kolom |  |
|  | "username" |  |
|  | df.loc[100, "username"] |  |

• .iloc[ ] mengakses data berdasarkan row/index/baris, hanya bisa diisi integer (angka)

|  | # Menampilkan data yang berada di kolom "location" di |  |
| --- | --- | --- |
|  | rentang dari baris/index ke 1001-1010 |  |
|  | # syntax => df.iloc[rentang baris, kolom ke-(dihitung dari |  |
|  | 0 milik "tgl tweet")] _ |  |
|  |  |  |
|  | # cara 1 |  |
|  | df.iloc[1001:1011, 6] |  |
|  |  |  |
|  | # cara 2 |  |
|  | # df.iloc[1001:1011, "location"] |  |

5. Pengurutan Data a. Terkecil ke terbesar

|  | # Mengurutkan data dari yang paling awal |  |
| --- | --- | --- |
|  | df[::1] |  |

b. Terbesar ke terkecil

|  | # Mengurutkan data dari yang paling akhir |  |
| --- | --- | --- |
|  | df[::-1] |  |

c. Pengurutan berdasarkan kondisi tertentu

|  | # Mengurutkan data berdasarkan jumlah likes terbanyak |  |
| --- | --- | --- |
|  | df urut = df.sort values(by=["favorite count"], ascending = _ _ _ |  |
|  | False) |  |
|  |  |  |
|  | df urut _ |  |

### 1.7. POST TEST

---

<!-- Halaman 19 -->

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| Masih dengan dataset yang sama dengan langkah praktikum, kerjakan perintah-perintah berikut: |  |  |  |  |
| 1 | CPL-03 | CPMK-01 | Urutkan data berdasarkan tanggal terlama hingga terbaru, lakukan: | 5 |
|  | CPL-03 | CPMK-01 | a. Ambil dan tampilkan 67 data teratas | 5 |
|  | CPL-03 | CPMK-01 | b. Ambil dan tampilkan data indeks ke 666 hingga 999 | 10 |
|  | CPL-03 | CPMK-01 | c. Ambil dan tampilkan 10 data dengan jumlah “quote count” terbanyak _ | 10 |
|  | CPL-03 | CPMK-01 | d. Ambil dan tampilkan hanya data yang memiliki “reply count” diantara 20 dan 50 _ | 15 |
| 2 | CPL-03 | CPMK-01 | Urutkan data berdasarkan "retweet count " terbanyak _ hingga paling sedikit | 5 |
|  | CPL-03 | CPMK-01 | a. Ambil dan tampilkan 23 data terbawah | 5 |
|  | CPL-03 | CPMK-01 | b. Ambil dan tampilkan hanya kolom “tweet” pada 10 data teratas | 15 |
|  | CPL-03 | CPMK-01 | c. Ambil dan tampilkan hanya kolom username pada data indeks ke 121 hinga 212 | 15 |
|  | CPL-03 | CPMK-01 | d. Ambil dan tampilkan hanya data yang memilik “quote count” lebih dari sama dengan 50 _ | 15 |

---

<!-- Halaman 20 -->

## PRAKTIKUM 2: PREPROCESSING (FILTERING DAN

## TOKENIZATION)

Pertemuan ke 2 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas. |
| --- | --- |
| CPMK-01 | Mampu menjelaskan konsep umum pemrosesan bahasa alami dan ruang lingkup penerapan aplikasinya. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu menjelaskan dan menerapkan pemrosesan awal terhadap teks, terutama filtering dan tokenization.

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menerapkan library NLTK untuk menjalankan pemrosesan awal terhadap teks dengan tokenisasi, casefolding, stopwords dan stemming baik pada teks Bahasa Inggris atau Bahasa Indonesia. |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

Preprocessing adalah langkah pertama dalam pengolahan data yang bertujuan untuk membersihkan, menyiapkan, dan menyusun data mentah. Dengan demikian, data dapat

---

<!-- Halaman 21 -->

diproses, dianalisis, atau digunakan lebih mudah dalam algoritma dan model pembelajaran mesin.

Tujuan Utama Preprocessing:

a. Mengurangi noise atau gangguan dalam data b. Menstandarisasi format data c. Meningkatkan akurasi dan efisiensi model NLP atau algoritma lainnya d. Menyaring informasi yang tidak relevan atau redundan

Dalam Pemrograman Bahasa Alami, preprocessing digunakan untuk membersihkan dan menstrukturkan teks sehingga siap dianalisis. Teks alami biasanya tidak rapi: banyak mengandung simbol, singkatan, ejaan tidak baku, dan kata-kata yang tidak penting.

### A. Filtering

Filtering adalah proses menyaring atau memilih elemen tertentu dari teks berdasarkan kriteria tertentu, untuk menghilangkan kata atau informasi yang tidak

### relevan, tidak penting, atau mengganggu proses analisis.

Filtering biasanya dilakukan setelah tahap tokenization, ketika teks sudah dipecah

### menjadi token-token (kata, kalimat, atau karakter).

### Tujuan Filtering:

### a. Mengurangi noise dalam data teks

### b. Menyimpan hanya kata-kata penting

### c. Meningkatkan kinerja dan akurasi model

### d. Membantu fokus pada fitur-fitur yang relevan

Jenis Filtering:

### a. Stopword Filtering

### b. Length-based Filtering

### c. Part-of-Speech (POS) Filtering

### d. Frequency-based Filtering

### B. Tokenization

Tokenization adalah proses memecah teks yang diberikan dalam pemrosesan bahasa alami menjadi unit terkecil dalam kalimat yang disebut token. Tanda baca, kata, dan angka dapat dianggap sebagai token. Umumnya tokenisasi berguna saat kita ingin mengekstrak makna dari sebuah teks.

---

<!-- Halaman 22 -->

Contohnya dalam sebuah kalimat kita ingin mendeteksi kata benda dan kata kerja yang ada dalam kalimat tersebut, atau kita ingin mencari nama orang yang dimention dalam sebuah kalimat. Maka dengan melakukan pemecahan 1 per 1, sistem dapat melakukan pengecekan 1 per 1 juga terhadap tiap-tiap teks yang ada pada kalimat.

Contoh tokenisasi dengan kalimat “saya suka belajar pba” di pecah menjadi “saya, suka, belajar, pba”.

Menggunakan Distribusi Frekuensi kita dapat menemukan berapa kali sebuah kata digunakan dalam sebuah kalimat, atau kita dapat menghitung kata dalam teks kitamenggunakan Distribusi Frekuensi NLP. Contoh “saya belajar tokenisasi dan saya belajar distibusi frekuensi”. Distribusi frekuensi dari saya adalah 2. Jenis Tokenisasi:

a. Word Tokenization: memecah kalimat menjadi kata b. Sentence Tokenization: memecah paragraph menjadi kalimat c. Character Tokenization: memecah teks menjadi karakter

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-01 | Jelaskan apa yang dimaksud dengan tokenisasi | 20 |
| 2 | CPL-03 | CPMK-01 | Jelaskan apa yang dimaksud dengan distribusi frekuensi | 10 |
| 3 | CPL-03 | CPMK-01 | Jelaskan macam macam cara untuk melakukan tokenisasi dan distribusi frekuensi dalam python | 30 |
| 4 | CPL-03 | CPMK-01 | Jelaskan yang dimaksud dengan case Folding dan stopword? Dan berikan masing2 contohnya | 20 |
| 5 | CPL-03 | CPMK-01 | Jelaskan perbedaan lemmatizer dan stemmer danberikan contohnya | 20 |

---

<!-- Halaman 23 -->

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Import Library

|  | import pandas as pd |  |
| --- | --- | --- |
|  | import numpy as np |  |
|  | import matplotlib.pyplot as plt |  |
|  |  |  |
|  | import nltk |  |
|  | nltk.download('punkt') |  |
|  | nltk.download('stopwords') |  |
|  |  |  |
|  | from nltk.tokenize import sent tokenize, word tokenize _ _ |  |
|  | from nltk.corpus import stopwords |  |
|  | stopwords ind = stopwords.words('indonesian') _ |  |

2. Unduh dataset

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

3. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |  |
| --- | --- | --- |
|  | df |  |

4. Slicing dataset

|  | df2 = df[…] |  |
| --- | --- | --- |
|  | df2 |  |

5. Data Cleaning: melakukan filtering dari data yang telah dislice sebelumnya

|  | filter df = df2[df2[...].str.contains(..., case=False, _ |  |
| --- | --- | --- |
|  | na=False)] |  |
|  | filter df _ |  |
|  | full text column = filter df[...] _ _ _ |  |
|  | print(full text column.head()) _ _ |  |

6. Casefolding

|  | # Membuat function untuk casefolding |  |
| --- | --- | --- |
|  | def casefolding(text): |  |
|  | text = ??? # Mengubah teks menjadi lower case |  |
|  | return text |  |
|  | raw sample = filter df['full text'].iloc[0] _ _ _ |  |
|  | case folding = casefolding(raw sample) _ _ |  |
|  |  |  |

---

<!-- Halaman 24 -->

|  | print('Raw data\t: ', raw sample) _ |
| --- | --- |
|  | print('Case folding\t: ', case folding) _ |

7. Stopwords

|  | # Cek jumlah stopwords berbahasa Indonesia yang disediakan NLTK |
| --- | --- |
|  | len(stopwords ind) _ |
|  | # Lihat daftar stopword yang disediakan NLTK |
|  | stopwords ind[:20] _ |
|  | # Membuat function untuk menghapus stopwords |
|  | def remove stop words(text): _ _ |
|  | clean words = [] _ |
|  | text = text.split() |
|  | for word in text: |
|  | if word not in stopwords ind: _ |
|  | clean words.append(word) _ |
|  | return " ".join(clean words) _ |
|  | raw sample = filter df['full text'].iloc[0] _ _ _ |
|  | case folding = casefolding(raw sample) _ _ |
|  | stopword removal = remove stop words(case folding) _ _ _ _ |
|  |  |
|  | print('Raw data\t\t: ', raw sample) _ |
|  | print('Case folding\t\t: ', case folding) _ |
|  | print('Stopword removal\t: ', stopword removal) _ |

### B. Pengolahan Dataset dan Teks

1. Melakukan filtering berdasarkan suatu kondisi

|  | filter df = df2[df2['full text'].str.contains("efisiensi", _ _ |
| --- | --- |
|  | case=False, na=False)] |
|  | filter df _ |

2. Melakukan tokenisasi dan menghitung frekuensi token

|  | def tokenize text(text): _ |
| --- | --- |
|  | tokens = word tokenize(text) _ |
|  | return tokens |
|  | cek freq = filter df['tokenized text'].explode() _ _ _ |
|  | cek freq = cek freq.value counts () _ _ _ |
|  | cek freq.head(10) _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 25 -->

| 1 | CPL-03 | CPMK-01 | Terapkan preprocessing seperti langkah praktikum (filtering +tokenisasi) pada data dari rentang baris ke 100-200 | 25 |
| --- | --- | --- | --- | --- |
| 2 | CPL-03 | CPMK-01 | Tampilkan hasil akhir preprocessing data | 25 |
| 3 | CPL-03 | CPMK-01 | Jelaskan fungsi-fungsi dari library NLTK yang dipelajari di pertemuan ini dan sebutkan dipakai saat langkah apa saja? | 25 |
| 4 | CPL-03 | CPMK-01 | Jelaskan hasil akhir yang didapat | 25 |

---

<!-- Halaman 26 -->

## PRAKTIKUM 3: PREPROCESSING (STEMMING DAN REGULAR

## EXPRESSION)

Pertemuan ke 3 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematikadasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: languagemodeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan ekspresi regular pada pemrosesan teks

2. Mengimplementasikan ekspresi regular pada pemrosesan teks

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan library re dan spacyuntuk menjalankan ekspresi regular. |
| --- | --- | --- |

---

<!-- Halaman 27 -->

### 1.3. TEORI PENDUKUNG

### A. Stemming

Stemming adalah proses mengubah kata berimbuhan menjadi bentuk dasar tanpa mengetahui konteks dari kata tersebut seperti memotong ujung kata-kata. Proses ini sering digunakan dalam NLP untuk analisis teks degan tujuan agar kata-kata yang mirip dianggap sebagai satu bentuk dasar. Tujuan stemming yaitu untuk mengurangi variasi kata yang harus diproses oleh mesin. Misalnya, “berlari”, “pelari”, dan “berlarian” akan direduksi menjadi “lari”. Ada beberapa algoritma stemming yang populer, yaitu Porter

Stemmer dan Sastrawi.

Porter stemmer adalah salah satu algoritma stemming tertua dan paling banyak digunakan, yang dikembangkan oleh Martin Porter pada tahun 1980. Stemmer ini menggunakan serangkaian aturan untuk menghapus sufiks dari kata-kata Bahasa Inggris.

Sastrawi adalah salah satu algoritma yang memungkinkan kita untuk mengubah kata dalam Bahasa Indonesia ke kata dasarnya.

### B. Regular Expression (RegEx)

Regular Expression (Regex) adalah pola yang digunakan untuk mencari, mencocokkan, atau memanipulasi teks. Dalam NLP, Regex sering dipakai untuk membersihkan data, mengekstrak informasi spesifik, atau memvalidasi format input. Contoh pola Regex yang umum, yaitu:

a. Menghapus angka

```
no_numbers = re.sub(r'\d+', '', text) 
```

b. Menghapus simbol (hanya menyisakan huruf dan spasi)

```
no_symbols = re.sub(r'[^a-zA-Z\s]', '', text) 
```

c. Mencari email

```
emails = re.findall(r'\S+@\S+', text) 
```

d. Mengganti spasi ganda menjadi satu spasi

```
clean_text = re.sub(r'\s+', ' ', text) 
```

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

---

<!-- Halaman 28 -->

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Dalam konteks Natural Language Processing (NLP), apa yang dimaksud dengan Regular Expression (RegEx) dan sebutkan dua contoh penggunaannya dalam tugastugas NLP! | 30 |
| 2 | CPL-03 | CPMK-02 | Sebutkan kode (RegEx) untuk menghapus! | 35 |
| 3 | CPL-03 | CPMK-02 | Tulis kode RegEx untuk menghapus semua angka dari sebuah teks! | 35 |

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Import Library

|  | import pandas as pd |
| --- | --- |
|  | import numpy as np |
|  | import matplotlib.pyplot as plt |
|  |  |
|  | import nltk |
|  | nltk.download('punkt') |
|  | nltk.download('stopwords') |
|  |  |
|  | from nltk.tokenize import sent tokenize, word tokenize _ _ |
|  | from nltk.corpus import stopwords |
|  | stopwords ind = stopwords.words('indonesian') _ |
|  |  |
|  | #Import modul 're' untuk regular expressions |
|  | import re |
|  | from Sastrawi.Stemmer.StemmerFactory import StemmerFactory |
|  |  |
|  | factory = StemmerFactory() |
|  | stemmer = factory.create stemmer() _ |

2. Unduh dataset

---

<!-- Halaman 29 -->

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

Dataset diunduh langsung dari github.

3. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |  |
| --- | --- | --- |
|  | df |  |

### B. Pengolahan Dataset dan Teks

1. Menghapus karakter special menggunakan Regular Expression

|  | def clean text(text): _ |  |
| --- | --- | --- |
|  | text = re.sub(r'http\S+', '', text) # Hapus URLs |  |
|  | text = re.sub(r'@\S+', '', text) #Hapus mentions |  |
|  | (@username) |  |
|  | text = re.sub(r'#\S+', '', text) #Hapus |  |
|  | hashtags (#hashtag) |  |
|  | text = re.sub(r'[^a-zA-Z\s]', '', text) #Hapus special |  |
|  | characters and numbers |  |
|  | text = re.sub(r'\s+', ' ', text).strip() #Hapus extra |  |
|  | whitespaces |  |
|  | return text |  |

2. Menghapus pola email

|  | # Inisialisasi pola regex untuk e-mail |  |
| --- | --- | --- |
|  | email pattern = r'[\w\.-]+@[\w\.-]+\w+' _ |  |
|  |  |  |
|  | # Menghapus Email dalam teks |  |
|  | print(re.sub(email pattern, '', kalimat)) _ |  |

3. Menghapus pola URL

|  | # Inisialisasi pola regex untuk URL |  |
| --- | --- | --- |
|  | url pattern = r'www\|http:\|https:+[^\s]+[\w/]' _ |  |
|  |  |  |
|  | print(re.sub(url pattern,' ', kalimat)) _ |  |

4. Menghapus pola nomor telepon

|  | # Inisialisasi pola regex untuk nomor telepon |  |
| --- | --- | --- |
|  | phone pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[- _ |  |
|  | \.\s]??\d{4,6}\|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4,6}\|\d{3,4}[- |  |
|  | \.\s]??\d{4,6})') |  |
|  |  |  |
|  | print(re.sub(phone pattern, '***', kalimat)) _ |  |

5. Menghapus pola plat motor

|  | # Inisialisasi pola regex untuk nomor telepon |  |
| --- | --- | --- |

---

<!-- Halaman 30 -->

|  | plat pattern = r'[A-Z]{1,2}\s\d{1,4}\s[A-Z]{1,3}' _ |
| --- | --- |
|  |  |
|  | print(re.sub(plat pattern, ' ', kalimat)) _ |

6. Stemming-Sastrawi

|  | def stemming(text): |
| --- | --- |
|  | text = stemmer.stem(text) |
|  | return text |
|  |  |
|  | raw sample = filter df['full text'].iloc[1] _ _ _ |
|  |  |
|  | # Step 1: Case folding |
|  | case folding = casefolding(raw sample) _ _ |
|  |  |
|  | # Step 2: Cleaning |
|  | cleantext = clean text(case folding) _ _ |
|  |  |
|  | # Step 3: Stopword removal |
|  | stopword removal = remove stop words(cleantext) _ _ _ |
|  |  |
|  | # Step 4: Stemming |
|  | text stemming = stemming(stopword removal) _ _ |
|  |  |
|  | # Print hasil setiap tahap |
|  | print('Raw data\t\t: ', raw sample) _ |
|  | print('Case folding\t\t: ', case folding) _ |
|  | print('Cleaning\t\t: ', cleantext) |
|  | print('Stopword removal\t: ', stopword removal) _ |
|  | print('Stemming\t\t: ', text stemming) _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| Lakukan tahapan preprocessing dengan ketentuan data sebagai berikut: |  |  |  |  |
| 1 | CPL-03 | CPMK-02 | Filter data dari rentang 150-400 | 5 |
| 2 | CPL-03 | CPMK-02 | Dari 250 data tersebut, filter lagi data yang hanya memuat kata “rakyat” | 5 |
| 3 | Lakukan tahapan: |  |  |  |
|  | CPL-03 | CPMK-02 | a. Menghapus karakter special | 15 |
|  | CPL-03 | CPMK-02 | b. Menghapus pola email, pola nomor telepon, pola url, dan pola plat nomor | 20 |
|  | CPL-03 | CPMK-02 | c. Casefolding | 5 |
|  | CPL-03 | CPMK-02 | d. Stopword | 5 |

---

<!-- Halaman 31 -->

|  | CPL-03 | CPMK-02 | e. Stemming | 15 |
| --- | --- | --- | --- | --- |
| 4 | CPL-03 | CPMK-02 | Tulis 5 kata berimbuhan dan hasil stemming yang ada dalam data tersebut | 5 |
| 5 | CPL-03 | CPMK-02 | Lakukan tokenisasi | 15 |
| 6 | CPL-03 | CPMK-02 | Tampilkan tiga token teratas yang dominan di data | 10 |

---

<!-- Halaman 32 -->

## PRAKTIKUM 4: SPELL CHECK

Pertemuan ke 4 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan spell check pada pemrosesan teks

2. Mengimplementasikan spell check pada pemrosesan teks

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam mengimplementasikan spell check |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

---

<!-- Halaman 33 -->

Spell check (pemeriksaan ejaan) adalah proses dalam pengolahan bahasa alami untuk mendeteksi dan mengoreksi kesalahan penulisan (typo) dalam teks. Dalam modul ini, kita akan menggunakan pustaka textdistance untuk membandingkan kemiripan antara kata yang salah dengan kata yang benar berdasarkan kamus yang telah ditentukan.

Proses spell check secara umum terdiri dari langkah-langkah berikut:

1. Input Data: Membaca teks mentah atau kumpulan kalimat dari file eksternal.

2. Tokenisasi: Memecah kalimat menjadi kata-kata.

3. Perbandingan dengan Kamus: Setiap kata yang tidak cocok dengan kamus akan dibandingkan jaraknya dengan seluruh kata dalam kamus.

4. Koreksi: Kata diganti dengan kata dalam kamus yang memiliki similarity score tertinggi.

5. Rekonstruksi Teks: Kata-kata hasil koreksi disatukan kembali menjadi kalimat.

Contoh Pemanfaatan Spell Check

1. Cek plagiarisme

2. Cek typo/mispelled words

3. Pencarian kata kunci di web search/e-commerce

4. Pencarian kemiripan nama, dan lain-lain

Metode pengukuran kemiripan kata yang umum digunakan meliputi:

a. Levenshtein Distance: Menghitung jumlah perubahan (insert, delete, replace) minimum yang dibutuhkan untuk mengubah satu string menjadi string lain.

b. Jaro-Winkler dan Hamming juga merupakan metode populer lainnya.

Kita akan menggunakan fungsi dari textdistance untuk menghitung jarak Levenshtein sebagai dasar koreksi ejaan.

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

---

<!-- Halaman 34 -->

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Jelaskan cara kerja Levensthein Distance! | 20 |
| 2 | CPL-03 | CPMK-02 | Jika Levenshtein (“manisan”, “masinan”) = 2, artinya? | 10 |
| 3 | CPL-03 | CPMK-02 | Apa tujuan utama dari spell checker dalam pemrosesan Bahasa alami? | 20 |
| 4 | CPL-03 | CPMK-02 | Sebutkan minimal 3 metode spell check yang diketahui | 30 |

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Install Library

|  | !pip install python-Levenshtein |
| --- | --- |
|  | !pip install textdistance |

2. Import Library

|  | import pandas as pd |
| --- | --- |
|  | import textdistance |
|  |  |
|  | import Levenshtein |
|  |  |
|  | # Menghitung jarak Levenshtein |
|  | distance = Levenshtein.distance("sangad", "sangat") |
|  | print("Distance:", distance) |
|  | import Levenshtein |
|  | Levenshtein.distance("kucing", "kacing") |
|  | import textdistance |
|  | dist lev = textdistance.levenshtein.distance("kucing", "kacing") _ |
|  | # hasil: 1 |
|  | sim lev = _ |
|  | textdistance.levenshtein.normalized similarity("kucing", _ |
|  | "kacing") # hasil: 0.83 |
|  |  |
|  | # Misal mau pakai metode pengukuran lainnya (Jaro-Winkler) |
|  | dist jaro = textdistance.jaro.distance("kucing", "kacing") _ |
|  | sim jaro = textdistance.jaro.normalized similarity("kucing", _ _ |
|  | "kacing") |
|  |  |
|  | print("Distance pakai Levenshtein: ", dist lev) _ |
|  | print("Similarity Levenshtein: ", sim lev) _ |
|  | print() |
|  | print("Distance pakai Jaccard: ", dist jaro) _ |

---

<!-- Halaman 35 -->

| print("Similarity Jaccard: ", sim jaro) _ |  |  |
| --- | --- | --- |
|  | corpus = ["kucing", "anjing", "kuda", "kelinci", "sapi", |  |
|  | "kambing", "gajah"] |  |
|  | misspelled = ["kuncing", "anjin", "kuuda", "kelici", "sappi", |  |
|  | "kmbing", "gajjah"] |  |
|  | def correct levenshtein(word, vocab): _ |  |
|  | return min(vocab, key=lambda x: |  |
|  | textdistance.levenshtein.distance(word, x)) |  |
|  | results = [] |  |
|  | for w in misspelled: |  |
|  | results.append({ |  |
|  | "misspelled": w, |  |
|  | "levenshtein": correct levenshtein(w, corpus), _ |  |
|  |  |  |
|  | }) |  |
|  | results |  |

3. Unduh dataset

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

4. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |  |
| --- | --- | --- |
|  | df |  |

### B. Praktik Spell Check Menggunakan Data Tweet

1. Definisikan kamus kata

|  | # Definisikan kamus kata (bisa ditambah sesuai kebutuhan) |  |
| --- | --- | --- |
|  | kamus = ['efisiensi', 'logika', 'dana', 'penghematan', 'anggaran', |  |
|  | 'kebijakan', 'publik', 'transparansi', 'negara', |  |
|  | 'rakyat', 'subsidi', |  |
|  | 'duit', 'uang', 'biaya', 'salah', 'silap', 'banyak', |  |
|  | 'omong'] |  |

2. Buat fungsi untuk koreksi kata

|  | # Fungsi untuk koreksi kata. Kata akan dicocokkan dengan data |  |
| --- | --- | --- |
|  | pada kamus yang didefinisikan di atas |  |
|  | def koreksi kata(kata, dictionary): _ |  |
|  | return min(dictionary, key=lambda |  |
|  | x:textdistance.levenshtein.normalized distance(kata.lower(), x)) _ |  |
|  |  |  |
|  | # Fungsi untuk koreksi seluruh teks |  |
|  | def correct text(text, dictionary): _ |  |
|  | words = text.split() |  |

---

<!-- Halaman 36 -->

|  | corrected = [ |  |
| --- | --- | --- |
|  | koreksi kata(word, dictionary) if word.lower() not in _ |  |
|  | dictionary else word |  |
|  | for word in words |  |
|  | ] |  |
|  | return ' '.join(corrected) |  |

3. Memproses koreksi kata dan hasilnya

|  | tweets = df['full text'].dropna().sample(10, _ |  |
| --- | --- | --- |
|  | random state=42).tolist() _ |  |
|  |  |  |
|  | # Tampilkan hasil koreksi |  |
|  | for i, tweet in enumerate(tweets): |  |
|  | print(f"Tweet {i+1} Asli : {tweet}") |  |
|  | print(f"Tweet {i+1} Koreksi : {correct text(tweet, _ |  |
|  | kamus)}") |  |
|  | print("-" * 50) |  |

### C. Hasil Spell Check Jika Melalui Tahap Preprocessing

1. Preprocessing

|  | df clean = df.copy() _ |  |
| --- | --- | --- |
|  | df clean = df clean.dropna().sample(10, random state=42) _ _ _ |  |
|  | df clean _ |  |
|  |  |  |
|  | # Karena menggunakan random state, maka 10 data yang ditampilkan _ |  |
|  | di bawah kemungkinan akan berbeda dengan 10 data sebelumnya |  |
|  | (dipilih sample secara acak) |  |
|  | !pip install Sastrawi |  |
|  | import nltk |  |
|  | nltk.download('punkt') |  |
|  | nltk.download('stopwords') |  |
|  |  |  |
|  | from nltk.tokenize import sent tokenize, word tokenize _ _ |  |
|  | from nltk.corpus import stopwords |  |
|  | stopwords ind = stopwords.words('indonesian') _ |  |
|  |  |  |
|  | import re # Import the 're' module for regular expressions |  |
|  | from Sastrawi.Stemmer.StemmerFactory import StemmerFactory # |  |
|  | Import Sastrawi for stemming |  |
|  | df clean['cleaned text'] = _ _ |  |
|  | df clean['full text'].apply(text preprocessing process) _ _ _ _ |  |
|  | df clean[['full text', 'cleaned text']] _ _ _ |  |
|  | Ambil 5 tweet contoh dari kolom 'full text' _ |  |
|  | tweets clean = df clean['cleaned text'].dropna().sample(5, _ _ _ |  |
|  | random state=42).tolist() _ |  |
|  |  |  |
|  | Tampilkan hasil koreksi |  |
|  | for i, tweets in enumerate(tweets clean): _ |  |
|  | print(f"Tweet {i+1} Asli : {tweets}") |  |

---

<!-- Halaman 37 -->

|  | print(f"Tweet {i+1} Koreksi : {correct text(tweets, _ |
| --- | --- |
|  | kamus)}") |
|  | print("-" * 50) |

### D. Cek Skor Similarity Setiap Kata untuk Melihat Perbandingan Skor Kesamaan

### (similarity score) antara 2 kalimat, kita bisa menggunakan format matriks

|  | import textdistance |
| --- | --- |
|  |  |
|  | def levenshtein similarity matrix(text1, text2): _ _ |
|  | words1 = text1.split() |
|  | words2 = text2.split() |
|  |  |
|  | matrix = [] |
|  | for w1 in words1: |
|  | row = [] |
|  | for w2 in words2: |
|  | sim = |
|  | textdistance.levenshtein.normalized similarity(w1, w2) _ |
|  | row.append(round(sim, 2)) |
|  | matrix.append(row) |
|  | return words1, words2, matrix |
|  |  |
|  | # Masukkan contoh kalimat, misal ambil dari hasil Teks Asli 3 dan Teks Koreksi 3 |
|  | teks asli = "kasi gbs pake lift krn efisiensi" _ |
|  | teks koreksi = "subsidi subsidi rakyat logika dana efisiensi" _ |
|  |  |
|  | words1, words2, sim matrix = levenshtein similarity matrix(teks asli, _ _ _ _ |
|  | teks koreksi) _ |
|  |  |
|  | # Display matrix |
|  | import pandas as pd |
|  | matrix kesamaan = pd.DataFrame(sim matrix, index=words1, columns=words2) _ _ |
|  | print(matrix kesamaan) _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Berikan pendapatmu terkait hasil akhir di file python yaitu perbandingan antara tweet asli dan tweet koreksi. Nyatakan kelemahan dari hasil tersebut. | 50 |

---

<!-- Halaman 38 -->

| 2 | CPL-03 | CPMK-02 | Lakukan eksperimen similarity matrix dengan metode selain Levenshtein! | 50 |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 39 -->

## PRAKTIKUM 5: PEMBOBOTAN/TF-IDF

Pertemuan ke 5 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan Menjelaskan dan mengimplementasikan pembobotan dokumen

2. Mengimplementasikan pembobotan dokumen

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam mengimplementasikan pembobotan dokumen dengan tepat. |
| --- | --- | --- |

---

<!-- Halaman 40 -->

### 1.3. TEORI PENDUKUNG

### A. Term Frequency (TF)

Term frequency (TF) adalah nilai frekuensi kemunculan token atau kata dalam sebuah dokumen. Semakin besar jumlah kemunculan suatu term (TF tinggi) dalam dokumen, semakin besar pula bobotnya atau akan memberikan nilai kesesuaian yang semakin besar.

Pada TF terdapat beberapa jenis formula yang dapat digunakan:

### 1. TF biner (Binary TF), hanya memperhatikan apakah suatu kata atau term ada atau

tidak dalam dokumen, jika ada diberi nilai satu (1), jika tidak diberi nilai nol (0).

### 2. TF murni (Raw TF), nilai TF diberikan berdasarkan jumlah kemunculan suatu term di

dokumen. Contohnya, jika muncul lima kali maka kata tersebut akan bernilai lima.

### 3. TF logaritmik, hal ini untuk menghindari dominansi dokumen yang mengandung

sedikit term dalam query, namun mempunyai frekuensi yang tinggi.

### 4. TF normalisasi, menggunakan perbandingan antara frekuensi sebuah term dengan

nilai maksimum dari keseluruhan atau kumpulan frekuensi term yang ada pada suatu dokumen.

Misalnya terdapat 3 dokumen/kalimat seperti berikut:

1. “Hotel sangat bersih, pelayan hotel juga ramah”

2. “Fasilitas hotel yg lumayan lengkap”

3. “Fasilitas di kamar mandi banyak yg rusak”

Nilai term frequency dapat dilihat pada tabel dibawah ini:

| No | Term | Term Frequency |  |  |
| --- | --- | --- | --- | --- |
|  |  | D1 | D2 | D3 |
| 1 | banyak | 0 | 0 | 1 |
| 2 | bersih | 1 | 0 | 0 |
| 3 | di | 0 | 0 | 1 |
| 4 | fasilitas | 0 | 1 | 1 |
| 5 | hotel | 2 | 1 | 0 |
| 6 | juga | 1 | 0 | 0 |
| 7 | kamar | 0 | 0 | 1 |
| 8 | lengkap | 0 | 1 | 0 |
| 9 | lumayan | 0 | 1 | 0 |
| 10 | mandi | 0 | 0 | 1 |
| 11 | pelayan | 1 | 0 | 0 |
| 12 | ramah | 1 | 0 | 0 |

---

<!-- Halaman 41 -->

| 13 | rusak | 0 | 0 | 1 |
| --- | --- | --- | --- | --- |
| 14 | sangat | 1 | 0 | 0 |
| 15 | yg | 0 | 1 | 1 |

### B. Inverse Document Frequency (IDF)

Inverse Document Frequency (IDF) merupakan sebuah perhitungan dari bagaimana term didistribusikan secara luas pada koleksi dokumen yang bersangkutan. IDF menunjukkan hubungan ketersediaan sebuah term dalam seluruh dokumen. Semakin sedikit jumlah dokumen yang mengandung term yang dimaksud, maka nilai IDF semakin besar.

IDF dihitung dengan menggunakan formula sebagai berikut:

𝐼𝐷𝐹𝑗= log( 𝐷

) 𝑑𝑓𝑗

Dimana D adalah jumlah semua dokumen dalam koleksi sedangkan dfj adalah jumlah dokumen yang mengandung term (tj).

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Jelaskan apa yang dimaksud dengan TF dan IDF! | 20 |
| 2 | CPL-03 | CPMK-02 | Apa fungsi TF-IDF pada PBA? | 30 |
| 3 | CPL-03 | CPMK-02 | Hitung TF-IDF secara manual dari dokumen di bawah ini (Tiap dokumen dipisahkan oleh tanda baca titik) Dokumen = “Kebun binatang itu terlihat sangat luas. Berbagai macam binatang terdapat di dalamnya. | 50 |

---

<!-- Halaman 42 -->

|  |  |  | Binatang-binatang di dalam kebun tersebut terlihat gemuk.” |  |
| --- | --- | --- | --- | --- |

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Import Library

|  | from sklearn.feature extraction.text import CountVectorizer, _ |
| --- | --- |
|  | TfidfTransformer |
|  | import pandas as pd |

2. Unduh dataset

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

3. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |
| --- | --- |
|  | df |

### B. Pengolahan Dataset dan Teks

1. Ketahui total kata pada seluruh baris

|  | df['totalwords'] = df['stemmed text'].str.count(' ') + 1 _ |
| --- | --- |
|  | df |

2. Filter data yang hanya memiliki jumlah kata <=10

|  | df = df[df['totalwords'] <= 10.0].reset index() _ |
| --- | --- |
|  | df |

3. Ambil Sebagian data menggunakan iloc

|  | # Dengan iloc, kita bisa mengambil data secara spesifik |
| --- | --- |
|  | berdasarkan index dan kolom |
|  |  |
|  | subset=df.iloc[[41, 55, 99, 118, 142],[11]] |
|  | subset |

4. Konversi data subset di atas ke dalam bentuk list

|  | list dokumen = [item[0] for item in subset.values.tolist()] _ |
| --- | --- |
|  | list dokumen _ |

### C. Penerapan TF-IDF

1. Menghitung jumlah unique term/vocab

---

<!-- Halaman 43 -->

|  | CV = CountVectorizer() |
| --- | --- |
|  | term fit = CV.fit(list dokumen) _ _ |
|  |  |
|  | print(len(term fit.vocabulary )) _ _ |

2. Menampilkan TF dari keseluruhan dokumen

|  | term frequency all = term fit.transform(list dokumen) _ _ _ _ |
| --- | --- |
|  | print(term frequency all) _ _ |

3. Menghitung TF-IDF dari satu kalimat tertentu

|  | komentar term = term fit.transform(list dokumen) _ _ _ |
| --- | --- |
|  | tfidf transformer = TfidfTransformer().fit(komentar term) _ _ |
|  | tfidf = tfidf transformer.transform(term frequency) _ _ |
|  |  |
|  | print(round(tfidf,3)) |

4. Mengetahui nilai IDF dari seluruh vocab/term

|  | print(tfidf transformer.idf ) _ _ |
| --- | --- |

5. Mengetahui nilai IDF untuk vocab/term tertentu

|  | print(tfidf transformer.idf [term fit.vocabulary ['efisiensi']]) _ _ _ _ |
| --- | --- |

6. Menghitung TF-IDF untuk seluruh dokumen

|  | komentar tfidf = tfidf transformer.transform(komentar term) _ _ _ |
| --- | --- |
|  | print(round(komentar tfidf,3)) _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| Pilih 5 kalimat berbeda (subset) dari kumpulan data dengan token kurang dari 10. Dengan catatan, kalimat yang dipilih tidak boleh sama dengan langkah praktikum. |  |  |  |  |
| 1 | CPL-03 | CPMK-02 | Duplikasikan sheet1 dari template manual. Lalu hitung TF-IDF dari dokumen posttestmu. | 30 |
| 2 | CPL-03 | CPMK-02 | Terapkan ke dalam kode langkah praktikum, mulai dari poin B. pada poin “mengetahui nilai IDF untuk vocab term tertentu” silahkan pilih 2 vocab bebas berdasarkan dokumenmu. | 60 |

---

<!-- Halaman 44 -->

| 3 | CPL-03 | CPMK-02 | Apakah ada perbedaan hasil antara hasil TF-IDF yang dihitung secara manual menggunakan rumus dengan hasil TF-IDF coding? Kalau memang ada, analisis dan jelaskan perbedaannya. | 10 |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 45 -->

## PRAKTIKUM 6: N-GRAM DAN NER

Pertemuan ke 6 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan NGrams pada kata dan kalimat untuk unigram, bigram dst.

2. Mengimplementasikan NGrams pada kata dan kalimat untuk unigram, bigram dst.

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan library yang ada di Python untuk melakukan N Grams. |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

### A. N-Grams

---

<!-- Halaman 46 -->

Tahapan pemrosesan untuk mencari N-grams dari teks mentah umumnya melibatkan beberapa langkah, dimulai dari persiapan teks (preprocessing) sebelum menghasilkan N- grams itu sendiri. N-gram sendiri adalah metode dalam pengolahan bahasa alami yang digunakan untuk menganalisis teks. Metode ini akan membagi urutan dari sejumlah N item (simbol, huruf, kata, token) yang berdekatan dalam urutan tertentu.

Berikut adalah tahapan pemrosesan bahasa alami dari teks mentah yang relevan sebelum menghasilkan N-grams, berdasarkan sumber:

1. Pemrosesan Teks (Text Preprocessing): Teks mentah seringkali tidak terstruktur dengan baik dan mengandung noise. Preprocessing mengubah teks mentah menjadi term index atau sekumpulan term index yang dapat mewakili dokumen. Tujuan preprocessing adalah untuk mempersiapkan data teks untuk proses lebih lanjut.

➢ Dokumen atau teks mentah bisa terdiri dari berbagai bahasa, set karakter, dan format. Teks juga bisa mengandung komponen yang tidak berhubungan seperti tag HTML atau link.

2. Langkah-langkah dalam Preprocessing yang relevan:

➢ Parsing Dokumen: Mengenali dan memecah struktur dokumen menjadi komponen terpisah. Ini menentukan mana yang dijadikan satu unit dokumen.

➢ Lexical Analysis / Tokenization (Tokenisasi): Ini adalah proses pemotongan string input berdasarkan tiap kata penyusunnya. Angka, tanda baca, dan karakter selain huruf alfabet biasanya dihilangkan karena dianggap sebagai pemisah kata (delimiter). Tahapan ini juga sering mencakup Case Folding, di mana semua huruf diubah menjadi huruf kecil, dan Cleaning, membersihkan dokumen dari komponen yang tidak berhubungan. Hasil dari tokenisasi disebut

Token, yaitu kata-kata yang dipisah dari teks aslinya tanpa mempertimbangkan duplikasi. Dalam konteks data Twitter, normalisasi data teks juga dilakukan untuk mengubah kata-kata gaul menjadi bentuk normalnya.

➢ Generate N-gram: Proses pembuatan N-gram dilakukan setelah data teks dinormalisasi dan diubah menjadi huruf kecil (transform case), berikutnya yaitu dengan tokenisasi. N-gram dibuat dari token-token hasil tokenisasi dengan mengambil urutan kata atau karakter sejumlah N.

3. Pembuatan N-grams: Setelah teks diubah menjadi urutan token (biasanya kata-kata setelah tokenisasi dan case folding/normalisasi), N-grams dapat dihasilkan. N-grams

---

<!-- Halaman 47 -->

adalah kumpulan item sejumlah N yang disusun secara berurutan dari teks. Item ini bisa berupa kata atau karakter.

a. Berdasarkan nilai N, N-grams diklasifikasikan menjadi:

• Unigram (N=1): Satu kata atau simbol.

• Bigram (N=2): Dua kata atau simbol berurutan.

• Trigram (N=3): Tiga kata atau simbol berurutan.

• Four-grams dan seterusnya: Urutan empat atau lebih kata/simbol.

b. Contoh pembuatan N-grams dari kalimat "Andi suka bermain sepakbola di lapangan Senayan" setelah tokenisasi (misalnya): "Andi", "suka", "bermain",

"sepakbola", "di", "lapangan", "senayan".

• Unigram: andi, suka, bermain, sepakbola, di, lapangan, senayan.

• Bigram: andi suka, suka bermain, bermain sepakbola, sepakbola di, di lapangan, lapangan senayan.

• Trigram: andi suka bermain, suka bermain sepakbola, bermain sepakbola di, sepakbola di lapangan, di lapangan senayan.

c. Contoh pembuatan N-grams dari kata "pemerintah" (karakter):

• Unigram (N=1): p, e, m, e, r, i, n, t, a, h.

• Bigram (N=2): pe, em, me, er, ri, in, nt, ta, ah.

• Trigram (N=3): pem, eme, mer, eri, rin, int, nta, tah.

Meskipun tahapan preprocessing lain seperti Stopword Removal (menghilangkan kata-kata umum) dan Stemming & Lemmatization (mengubah kata berimbuhan menjadi kata dasar) sering dilakukan dalam alur NLP atau text mining, sumber menunjukkan bahwa pembuatan N-grams itu sendiri didasarkan pada urutan token/kata setelah langkah-langkah dasar seperti tokenisasi dan case folding, meskipun N-grams juga dapat dibuat dari hasil stemming (misalnya, N-grams dari stems). Sumber bahkan mencatat contoh pembuatan N-grams tanpa mempertimbangkan penghapusan stopword.

Singkatnya, proses untuk mencari N-grams dari teks mentah dimulai dengan membersihkan dan memecah teks menjadi unit-unit dasar (tokenisasi dan case folding/normalisasi), lalu mengambil urutan item (token) yang berdekatan sebanyak N.

### B. NER

---

<!-- Halaman 48 -->

Teks tersebut adalah survei komprehensif mengenai Named Entity Recognition (NER) dalam Pemrosesan Bahasa Alami (NLP). NER bertujuan untuk mengidentifikasi dan mengkategorikan entitas dalam teks, seperti nama orang, lokasi, dan organisasi. Survei ini membahas berbagai pendekatan tradisional untuk NER, termasuk metode berbasis aturan, pembelajaran tanpa pengawasan, dan pembelajaran terawasi, serta metode berbasis pembelajaran mendalam (deep learning) yang lebih baru. Penulis mengeksplorasi arsitektur deep learning yang umum digunakan untuk NER, termasuk jaringan saraf konvolusional (CNN), jaringan saraf berulang (RNN), dan model berbasis

Transformer, seperti BERT. Teks ini juga menyoroti tantangan NER dalam sumber daya rendah dan penggunaan transfer learning serta large language models (LLMs) untuk mengatasi masalah ini. Terakhir, penulis membandingkan kinerja berbagai kerangka kerja dan algoritma NER menggunakan metrik evaluasi standar seperti F1 score, presisi, dan recall.

Berdasarkan sumber-sumber yang diberikan, proses Named Entity Recognition (NER) dalam Natural Language Processing (NLP) pada dasarnya adalah serangkaian langkah untuk mengidentifikasi dan mengklasifikasikan entitas penting dalam teks yang tidak terstruktur. Ini memungkinkan komputer untuk mengenali dan memahami informasi kunci, yang pada gilirannya mempermudah pencarian, analisis, dan pengorganisasian informasi.

NER adalah bagian penting dalam Natural Language Processing (NLP). Secara umum,

NLP dibagi menjadi sintaksis, semantik, dan pidato, dan NER termasuk dalam kategori semantik. Ini berfokus pada menurunkan makna dan mengidentifikasi hubungan dalam teks.

Tujuan utama NER adalah memungkinkan komputer untuk secara otomatis mengidentifikasi dan memahami entitas-entitas dalam teks. Entitas ini adalah kata atau frasa yang mengidentifikasi satu item dari sekumpulan item serupa, seperti nama organisasi, orang, lokasi dalam domain umum, atau gen, protein, obat, dan penyakit dalam domain biomedis. NER dapat mengenali entitas bernama seperti nama orang, organisasi, lokasi, tanggal, angka, dan sebagainya.

Proses kerja NER, dari teks input hingga output, dapat dijelaskan dalam beberapa langkah:

---

<!-- Halaman 49 -->

### 1. Input teks: Proses dimulai dengan teks tidak terstruktur (kalimat, paragraf, atau

seluruh dokumen) yang mengandung berbagai jenis entitas data.

### 2. Tokenization: Teks dibagi menjadi unit-unit yang lebih kecil, yang disebut token (kata,

subkata, atau karakter). Proses ini membantu analisis teks secara terperinci.

### 3. Part-of-Speech (POS) Tagging: Setiap token diberi label yang menunjukkan kategori

tata bahasa atau jenis kata (kata benda, kata kerja, dll.). Ini membantu memahami struktur sintaksis dan konteks linguistik.

### 4. Feature Extraction: Fitur linguistik (seperti embedding kata atau representasi

kontekstual) diekstraksi dari setiap token. Ini membantu model memahami semantik dan hubungan sintaksis, serta mengenali pola entitas.

### 5. Named Entity Recognition Model: Token dan fiturnya dimasukkan ke dalam model

NER yang telah dilatih (menggunakan sistem berbasis aturan, machine learning, atau deep learning). Model ini memprediksi apakah setiap token adalah bagian dari entitas bernama dan jenisnya.

### 6. Sequence Labeling: Model memberi label khusus pada setiap token, menunjukkan

apakah itu bagian dari entitas bernama dan jenis entitasnya (misalnya, nama orang, tempat). Ini menghasilkan urutan token yang berlabel.

### 7. Pemahaman Kontekstual: Model mempertimbangkan konteks di mana token muncul

(kata-kata dan label di sekitarnya) untuk mengatasi ambiguitas dan meningkatkan akurasi.

### 8. Pemrosesan Akhir: Langkah-langkah dilakukan untuk menyempurnakan hasil, seperti

menangani entitas yang tumpang tindih atau menyelesaikan ambiguitas.

### 9. Output: Hasilnya adalah sekumpulan entitas yang teridentifikasi beserta jenisnya.

Proses ini mempermudah pencarian informasi karena NER membantu sistem NLP untuk lebih presisi memahami konteks dan struktur bahasa dalam teks. Dengan mengenali dan menyoroti entitas penting, NER membantu menyusun informasi yang tidak terstruktur menjadi struktur yang lebih terorganisir dan dapat dicari. Ini memungkinkan sistem untuk dengan cepat dan tepat menemukan dan menyajikan informasi yang relevan.

NER berperan krusial dalam berbagai aplikasi NLP yang melibatkan "pencarian" atau pemahaman informasi dari teks, seperti:

---

<!-- Halaman 50 -->

a. Sistem Pengambilan Informasi (Information Retrieval): NER berkontribusi pada otomatisasi ekstraksi data dari volume besar teks tidak terstruktur.

b. Sistem Tanya Jawab (Question-Answering Systems): NER membantu memahami pertanyaan pengguna dengan mengenali entitas relevan, memungkinkan sistem fokus pada aspek kunci pertanyaan dan memberikan jawaban yang lebih akurat dan relevan.

c. Analisis Sentimen: NER membantu mengekstrak dan memahami entitas yang terkait dengan opini atau perasaan, memberikan konteks lebih dalam tentang sentimen yang diungkapkan.

Dengan demikian, proses NER dalam NLP secara fundamental adalah tentang mengidentifikasi dan mengklasifikasikan entitas bernama dalam teks melalui serangkaian langkah analisis linguistik dan pemodelan, yang secara signifikan meningkatkan kemampuan sistem untuk menemukan, memahami, dan memproses informasi secara efisien.

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Jelaskan apa itu N-Gram dan NER! | 25 |
| 2 | CPL-03 | CPMK-02 | Sebutkan kegunaan dan contoh pendekatan NER! | 25 |
| 3 | CPL-03 | CPMK-02 | Buatlah contoh kalimat sederhana dan tentukan NERnya! | 25 |
| 4 | CPL-03 | CPMK-02 | Buat contoh penggunaan bigram dan trigram dengan menggunakan nama sendiri! | 25 |

---

<!-- Halaman 51 -->

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

1. Import Library

|  | from sklearn.feature extraction.text import CountVectorizer, _ |  |
| --- | --- | --- |
|  | TfidfTransformer |  |
|  | import pandas as pd |  |

2. Unduh dataset

|  | !wget |  |
| --- | --- | --- |
|  | https://raw.githubusercontent.com/jiorjioo/PBA2025/refs/heads/main/tweet efisiensi.csv _ |  |

Dataset diunduh langsung dari github.

3. Load dataset

|  | df = pd.read csv('tweet efisiensi.csv') _ _ |  |
| --- | --- | --- |
|  | df |  |

### B. Pengolahan Dataset dan Teks

1. Cek nama kolom dan jumlah baris

|  | column name = list(df) _ |  |
| --- | --- | --- |
|  | row count = len(df) _ |  |
|  | column count = len(df.columns) _ |  |
|  |  |  |
|  | print("Nama kolom pada dataset: ", column name) _ |  |
|  | print("Jumlah kolom: ", column count, "kolom") _ |  |
|  | print("Jumlah baris: ", row count, "baris") _ |  |

### C. N-Grams

1. Contoh sederhana dengan menggunakan kalimat

|  | #definisikan fungsi untuk perhitungan N-Gram |  |
| --- | --- | --- |
|  | def generate ngrams(text, n): _ |  |
|  | tokens = text.split() # Tokenisasi sederhana berdasarkan |  |
|  | spasi |  |
|  | ngrams = [] |  |
|  | for i in range(len(tokens) - n + 1): |  |
|  | ngram = ' '.join(tokens[i:i+n]) |  |
|  | ngrams.append(ngram) |  |
|  | return ngrams |  |

2. Penggunaan unigram

|  | # Menggunakan fungsi generate ngrams untuk unigram (n=1) _ |  |
| --- | --- | --- |
|  | unigrams = generate ngrams(text1, 1) _ |  |
|  | print("Unigram:", unigrams) |  |
|  |  |  |

---

<!-- Halaman 52 -->

|  | # Menggunakan CountVectorizer dari scikit-learn untuk N-grams |  |
| --- | --- | --- |
|  | vectorizer bigram = CountVectorizer(ngram range=(1, 1)) _ _ |  |
|  | X bigram = vectorizer bigram.fit transform([text1]) _ _ _ |  |
|  | print("\nUnigram (using CountVectorizer):\n", |  |
|  | vectorizer bigram.get feature names out()) _ _ _ _ |  |

3. Penggunaan bigram

|  | # Generate bigram (N=2) |  |
| --- | --- | --- |
|  | bigrams = generate ngrams(text1, 2) _ |  |
|  | print("Bigram:", bigrams) |  |
|  |  |  |
|  | # Define the function to generate character bigrams |  |
|  | def generate char bigrams(text): _ _ |  |
|  | """Menghasilkan bigram (dua karakter berurutan) dari sebuah |  |
|  | teks.""" |  |
|  | bigrams = [] |  |
|  | # Iterate through the text to create character bigrams |  |
|  | for i in range(len(text) - 1): |  |
|  | bigram = text[i:i+2] # Get a slice of two characters |  |
|  | bigrams.append(bigram) |  |
|  | return bigrams |  |
|  |  |  |
|  | # Generate bigram (N=2) using the new function |  |
|  | bigrams = generate char bigrams(text1) _ _ |  |
|  | print("Bigram:", bigrams) |  |
|  | # Menggunakan CountVectorizer dari scikit-learn untuk N-grams |  |
|  |  |  |
|  | vectorizer bigram = CountVectorizer(ngram range=(2, _ _ |  |
|  | 2),analyzer=('char')) #analyzer=('char') untuk pemisahan per |  |
|  | karakter |  |
|  | X bigram = vectorizer bigram.fit transform([text1]) _ _ _ |  |
|  | print("\nBigram (using CountVectorizer):\n", |  |
|  | vectorizer bigram.get feature names out()) _ _ _ _ |  |

4. Penggunaan trigram

|  | # Generate trigram (N=3) |  |
| --- | --- | --- |
|  | trigrams = generate ngrams(text1, 3) _ |  |
|  | print("Trigram:", trigrams) |  |
|  |  |  |
|  | # Menggunakan CountVectorizer dari scikit-learn untuk N-grams |  |
|  |  |  |
|  | vectorizer trigram = CountVectorizer(ngram range=(3, 3)) _ _ |  |
|  | X trigram = vectorizer trigram.fit transform([text1]) _ _ _ |  |
|  | print("\nTrigram (using CountVectorizer):\n", |  |
|  | vectorizer trigram.get feature names out()) _ _ _ _ |  |

### D. NER

1. NLTK

---

<!-- Halaman 53 -->

|  | !pip install svgling |  |
| --- | --- | --- |
|  |  |  |
|  | import nltk |  |
|  | nltk.download('punkt tab') _ |  |
|  | nltk.download('averaged perceptron tagger eng') _ _ _ |  |
|  | nltk.download('tagsets json') _ |  |
|  | nltk.download('maxent ne chunker tab') _ _ _ |  |
|  | nltk.download('words') |  |
|  |  |  |
|  | print(nltk.help.upenn tagset()) _ |  |
|  |  |  |
|  | pos tag = nltk.pos tag(…) _ _ |  |
|  | pos tag _ |  |
|  |  |  |
|  | nltk.help.upenn tagset('NNS') _ |  |
|  |  |  |
|  | named entities = nltk.ne chunk(pos tag) _ _ _ |  |
|  | print("\nNER in Tree format:") |  |
|  | named entities _ |  |

2. Spacy NER English

|  | import spacy |  |
| --- | --- | --- |
|  | from spacy import displacy |  |
|  |  |  |
|  | !python -m spacy download en core web sm _ _ _ |  |
|  |  |  |
|  | # Load the spaCy model |  |
|  | nlp = spacy.load("en core web sm") _ _ _ |  |
|  |  |  |
|  | nlp ner eng = spacy.load('en core web sm') _ _ _ _ _ |  |
|  |  |  |
|  | text = … |  |
|  | # Teks input diprediksi menggunakan model yang sudah di-load |  |
|  | tadi |  |
|  | doc eng = nlp ner eng(text) _ _ _ |  |
|  |  |  |
|  | # Output |  |
|  | print("Entities", [(ent.text, ent.label ) for ent in _ |  |
|  | doc eng.ents]) _ |  |
|  | displacy.render(doc eng, style="ent") _ |  |

3. Spacy NER Indonesia

|  | !wget |  |
| --- | --- | --- |
|  | 'https://github.com/jiorjioo/PBA2025/raw/refs/heads/main/ner- |  |
|  | model-id.zip' |  |
|  | !unzip ner-model-id.zip |  |
|  |  |  |
|  | nlp ner id = spacy.load('nlp id checkpoint 2025 06 01') _ _ _ _ _ _ _ |  |
|  |  |  |

---

<!-- Halaman 54 -->

|  | text = … |
| --- | --- |
|  | # Teks input diprediksi menggunakan model yang sudah di-load |
|  | tadi |
|  | doc id = nlp ner id(text ner id) _ _ _ _ _ |
|  |  |
|  | # Output |
|  | print("Entities", [(ent.text, ent.label ) for ent in _ |
|  | doc id.ents]) _ |
|  | displacy.render(doc id, style="ent") _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Terapkan kode unigram dalam bentuk char dengan memakai dataset tabel [stemmed text] untuk 1 kalimat _ saja! | 20 |
| 2 | CPL-03 | CPMK-02 | Terapkan Kode Trigram dalam bentuk char dengan memakai dataset tabel [stemmed text] (ambil 5 index _ random) antara 1000-2000an | 20 |
| 3 | CPL-03 | CPMK-02 | Sebutkan hal-hal penting yang didapat jika menganalisis teks menggunakan N-GRAM. | 20 |
| 4 | CPL-03 | CPMK-02 | Cari Paragraf biografi dengan kata kunci ‘tokoh inspirasi’ bebas dalam bahasa inggris. bisa diambil dari wikipedia kemudian cantumkan link dimana mengambil datanya. buat Kode untuk proses mencari NER NLTK dan Spacy, terakhir tampilkan hasilnya. | 20 |
| 5 | CPL-03 | CPMK-02 | Setelah mendapat hasil NER pada nomer 4, berikan pendapat mu terkait hasil yang sudah didapatkan! | 20 |

---

<!-- Halaman 55 -->

## PRAKTIKUM 7: PARSING

Pertemuan ke 7 Total Alokasi Waktu 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian 100% • Pre-Test : 20% • Praktik : 30% • Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan parsing dari grammar

2. Mengimplementasikan parsing dari grammar

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan parsing dari grammar |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

---

<!-- Halaman 56 -->

Context Free Grammar (CFG) adalah tata bahasa yang mempunyai tujuan sama seperti halnya tata bahasa regular yaitu merupakan suatu cara untuk menunjukkan bagaimana menghasilkan suatu untai - untai dalam sebuah bahasa.

Context Free Grammar (CFG) menjadi dasar dalam pembentukan suatu parser/proses analisis sintaksis. Bagian sintaks dalam suatu kompilator kebanyakan di definisikan dalam tata bahasa bebas konteks. Pohon penurunan (derivation tree/parse tree) berguna untuk menggambarkan simbol-simbol variabel menjadi simbol-simbol terminal setiap simbol variabel akan di turunkan menjadi terminal sampai tidak ada yang belum tergantikan. CFG berisi aturan grammar yang akan digunakan dalam proses parsing.

Berikut merupakan simbol yang digunakan dalam context free grammar:

|  | Simbol |  |  | Keterangan |  |  | Contoh |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S |  |  | sentence |  |  | The man walked |  |  |
| NP |  |  | noun phrase |  |  | A dog |  |  |
| VP |  |  | verb phrase |  |  | Saw a park |  |  |
| PP |  |  | prepositional phrase |  |  | With a telescope |  |  |
| Det |  |  | determiner |  |  | The |  |  |
| N |  |  | noun |  |  | Dog |  |  |
| V |  |  | verb |  |  | Walked |  |  |
| P |  |  | preposition |  |  | in |  |  |

Dalam proses parsing, Parser melakukan proses kalimat berdasarkan struktur grammar yang sudah diciptakan. Grammar tersebut dideklarasikan secara well-formedness

(berdasarkan aturan grammar yang telah ditentukan). Parser tersebut dapat melakukan cek grammar terhadap kalimat yang dimasukan, dimana kesalahan struktur grammar banyak dialami pada penulisan kalimat yang tidak baku sesuai ketentuan grammar yang telah disepakati. Didalam pemrosesan bahasa alami parsing sering diterapkan pada beberapa kasus, salah satunya pada question answering.

Tahapan proses parsing:

10. Input Teks Masukkan kalimat atau teks mentah.

Contoh: "Andi bermain sepakbola di lapangan."

11. Preprocessing Teks a. Case folding (huruf kecil) b. Tokenisasi (memecah jadi kata)

---

<!-- Halaman 57 -->

c. Penghapusan tanda baca, simbol, dsb.

12. POS Tagging (Part-of-Speech Tagging) yaitu menentukan kelas kata, apakah termasuk kata benda, kata kerja, kata sifat, dan sebagainya. Contoh: Andi->NN (Noun) dan bermain->V (Verb).

13. Parsing (Sintaksis) a. Constituency Parsing → memetakan frasa (NP, VP) b. Dependency Parsing → memetakan relasi antar kata (subjek, objek, dll)

14. Output parsing berupa struktur pohon (parse tree) atau relasi dependensi antar kata.

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Jelaskan apa itu Parsing dan Context Free Grammar! | 25 |
| 2 | CPL-03 | CPMK-02 | Apa fungsi dari Parse Tree/Derivation Tree? | 15 |
| 3 | CPL-03 | CPMK-02 | Buat CFG untuk kalimat “Saya makan nasi” | 30 |
| 4 | CPL-03 | CPMK-02 | Kalimat: “school of dance and music presents wonderfull town” pada kalimat tersebut lakukan langkah membuat CFG secara top-down parsing | 30 |

### 1.6. LANGKAH PRAKTIKUM

1. Import Library

|  | from nltk import CFG |
| --- | --- |
|  | from nltk.parse import RecursiveDescentParser, ShiftReduceParser |

2. Inisiasi rules grammar dan sintaks

|  | grammar = CFG.fromstring( |
| --- | --- |
|  | """ |

---

<!-- Halaman 58 -->

|  | S -> NP VP |  |
| --- | --- | --- |
|  | NP -> N \| N NP \| N Conj \| N PP \| N Conj NP |  |
|  | PP -> P NP |  |
|  | VP -> V NP |  |
|  |  |  |
|  | N -> "school" \| "dance" \| "music" \| "wonderfull" \| "town" |  |
|  | P -> "of" |  |
|  | V -> "presents" |  |
|  | Conj -> "and" |  |
|  | """ |  |
|  | ) |  |

### S -> NP VP

Ini adalah aturan utama. S (Sentence) adalah simbol awal, dan aturan ini menyatakan bahwa sebuah kalimat (S) terdiri dari sebuah Frasa Kata Benda (NP) diikuti oleh

### sebuah Frasa Kata Kerja (VP).

### NP -> N | N NP | N Conj | N PP | N Conj NP

Ini adalah aturan untuk Frasa Kata Benda (NP). Frasa kata benda bisa terdiri dari:

• N: Hanya satu kata benda.

• N NP: Kata benda diikuti oleh frasa kata benda lain.

• N Conj: Kata benda diikuti oleh kata sambung.

• N PP: Kata benda diikuti oleh frasa preposisi.

• N Conj NP: Kata benda diikuti oleh kata sambung dan frasa kata benda lain. Simbol | berarti "atau".

• PP -> P NP: Ini adalah aturan untuk Frasa Preposisi (PP). Frasa preposisi terdiri dari sebuah preposisi (P) diikuti oleh sebuah frasa kata benda (NP).

• VP -> V NP: Ini adalah aturan untuk Frasa Kata Kerja (VP). Frasa kata kerja terdiri dari sebuah kata kerja (V) diikuti oleh sebuah frasa kata benda (NP).

• N -> "school" | "dance" | "music" | "wonderfull" | "town": Ini adalah aturan terminal untuk simbol N (Kata Benda). Kata benda yang dikenali dalam grammar ini adalah

"school", "dance", "music", "wonderfull", dan "town".

• P -> "of": Ini adalah aturan terminal untuk simbol P (Preposisi). Preposisi yang dikenali adalah "of".

• V -> "presents": Ini adalah aturan terminal untuk simbol V (Kata Kerja). Kata kerja yang dikenali adalah "presents".

---

<!-- Halaman 59 -->

• Conj -> "and": Ini adalah aturan terminal untuk simbol Conj (Kata Sambung). Kata sambung yang dikenali adalah "and".

3. Lihat sebaran sintaksis kata

|  | for p in grammar.productions(): |
| --- | --- |
|  | print(p) |

4. Penerapan dalam suatu kalimat utuh dan visualisasi Tree

|  | # Tokenize kalimat |
| --- | --- |
|  | sentence = "school of dance and music presents wonderfull |
|  | town".split() |
|  |  |
|  | rd parser = RecursiveDescentParser(grammar) _ |
|  |  |
|  | # Parsing kalimat dan cetak parse tree |
|  | for tree in rd parser.parse(sentence): _ |
|  | print(tree) |
|  | tree.pretty print() _ |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Kalimat 1: “Mahasiswa belajar komputer di laboratorium pada jam kuliah” Kalimat 2: “MY FRIEND HAD A VACATION AT THE BEACH YESTERDAY” |  |
|  | CPL-03 | CPMK-02 | Pada kalimat di atas, lakukan langkah membuat CFG top-down parsing secara manual | 50 |
|  | CPL-03 | CPMK-02 | Pada kalimat di atas, lakukan langkah membuat CFG secara top-down parsing pada kode program yang sudah dipelajari | 50 |

---

<!-- Halaman 60 -->

## PRAKTIKUM 8: TEXT SUMMARIZATION

Pertemuan ke 8 Total Alokasi Waktu 90 menit • Materi : 15 menit 5. Pre-Test : 15 menit 6. Praktikum : 45 menit 7. Post-Test : 15 menit Total Bobot Penilaian 100% 8. Pre-Test : 20% 9. Praktik : 30% 10. Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan task peringkasan teks

2. Menerapkan sebuah contoh kasus.

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan studi kasus |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

### A. Apa itu Text Summarization?

Text Summarization atau ringkasan teks pertama kali diperkenalkan pada tahun

1950 (Gaikwad & Mahender, 2016), merupakan suatu metode dalam membuat ringkasan

---

<!-- Halaman 61 -->

yang singkat, akurat, dan dapat dicerna dari suatu dokumen teks yang panjang. Gagasan utama di balik text summarization adalah untuk dapat menemukan subset singkat dari informasi paling penting dari seluruh rangkaian dan menyajikannya dalam format yang dapat dibaca manusia. Seiring dengan pertumbuhan data tekstual online, metode text summarization berpotensi sangat membantu karena informasi yang lebih bermanfaat dapat dibaca dalam waktu singkat.

Sedangkan automatic text summarization adalah suatu langkah untuk membuat ringkasan secara otomatis dengan tidak mengubah inti dari suatu dokumen yang diringkas.

Automatic text summarization atau biasa disebut automatic summarization sangat dibutuhkan pada era big data sekarang ini, di mana jumlah data teks setiap hari selalu bertambah dengan sanga tbanyak dan tidak terstruktur sehingga untuk membantu menemukan informasi yang relevan dengan lebih cepat dibutuhkan automatic summarization. Terdapat beberapa hal yang membuat automatic text summarization penting yaitu:

a. Ringkasan mengurangi waktu membaca b. Saat meneliti dokumen, ringkasan membuat proses seleksi lebi mudah c. Automatic Text Summarization meningkatkan efektifitas pengindeksan d. Algoritma Automatic Text Summarization kurang bias dibandingkan peringkasan manusia e. Ringkasan yang dipersonalisasi berguna dalam system penjawab pertanyaan karena memberikan informasi yang dipersonalisasi f. Menggunakan system Automatic Text Summarization atau semi-automatic memungkinkan layanan abstrak komersial untuk meningkatkan jumlah dokumen teks yang dapat mereka proses.

### B. Tipe-Tipe Text Summarization

---

<!-- Halaman 62 -->

Berdasarkan input type:

a. Single-Document, dimana panjang inputnya pendek. Banyak dari sistem peringkasan awal berurusan dengan peringkasan single-document.

b. Multi-Document, dimana inputan dapat panjang secara cuma - cuma.

Berdasarkan purpose (tujuan):

a. Generic, dimana model tidak membuat asumsi tentang domain atau konten teks yang akan diringkas dan memperlakukan semua input sebagai homogen. Sebagian besar pekerjaan yang telah dilakukan berkisar pada ringkasan umum.

b. Domain-specific, dimana model menggunakan pengetahuan khusus domain untuk membentuk ringkasan yang lebih akurat. Misalnya, meringkas makalah penelitian dari domain tertentu, dokumen biomedis, dll.

c. Query-based, dimana ringkasan hanya berisi informasi yang menjawab pertanyaan bahasa alami tentang teks input.

Berdasarkan output type:

a. Extractive, dimana kalimat penting dipilih dari teks input untuk membentuk ringkasan.

Kebanyakan pendekatan peringkasan saat ini bersifat extractive.

b. Abstractive, dimana model membentuk frasa dan kalimatnya sendiri untuk menwarkan ringkasan yang lebih koheren, seperti yang akan dihasilkan manusia.

Pendekatan ini jelas lebih menarik, tetapi jauh lebih sulit daripada ringkasan extractive.

### C. Langkah-Langkah Dalam Melakukan Text Summarization

1. Text cleaning

---

<!-- Halaman 63 -->

2. Sentence tokenization

3. Word tokenization

4. Word-frequency table

5. Summarization

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Apa yang kamu ketahui tentang text summarization? | 25 |
| 2 | CPL-03 | CPMK-02 | Coba jelaskan apa saja tipe text summarization? Gambar dalam bentuk mind mapping! | 45 |
| 3 | CPL-03 | CPMK-02 | Sebutkan dan jelaskan langkah-langkah text summarization yang umum dilakukan! | 30 |

### 1.6. LANGKAH PRAKTIKUM

A. Persiapan

1. Install Library

|  | !pip install -U spacy |
| --- | --- |
|  | !python -m spacy download en core web sm _ _ _ |

spacy: digunakan untuk pemrosesan bahasa alami (NLP), termasuk tokenisasi dan

Named Entity Recognition (NER).

2. Import Library

|  | import spacy |  |
| --- | --- | --- |
|  | from spacy.lang.en.stop words import STOP WORDS |  |
|  | _ _ from string import punctuation |  |
|  | from heapq import nlargest |  |
|  | import re |  |

---

<!-- Halaman 64 -->

3. Inisialisasi data berupa teks

|  | text = """There are broadly two types of extractive |  |
| --- | --- | --- |
|  | summarization tasks depending on what the summarization program |  |
|  | focuses on. The first is generic summarization, which focuses on |  |
|  | obtaining a generic summary or abstract of the |  |
|  | collection(whether documents, or sets of images, or videos, news |  |
|  | stories etc.). |  |
|  | The second is query relevant summarization,sometimes called |  |
|  | query-based summarization, which summarizes objects specific to |  |
|  | a query. Summarization systems are able to create both query |  |
|  | relevant text summaries and generic machine-generated summaries |  |
|  | depending on what the user needs. |  |
|  | An example of a summarization problem is document summarization, |  |
|  | which attempts to automatically produce an abstract from a given |  |
|  | document. |  |
|  | Sometimes one might be interested in generating a summary from a |  |
|  | single source document, while others can use multiple source |  |
|  | documents (for example, a cluster of articles on the same |  |
|  | topic). This problem is called multi-document summarization. |  |
|  | A related application is summarizing news articles. Imagine a |  |
|  | system, which automatically pulls together news articles on a |  |
|  | given topic (from the web), and concisely represents the latest |  |
|  | news as a summary. Image collection summarization is another |  |
|  | application example of automatic summarization. It consists in |  |
|  | selecting a representative set of images from a larger set of |  |
|  | images. |  |
|  | A summary in this context is useful to show the most |  |
|  | representative images of results in an image collection |  |
|  | exploration system. |  |
|  | Video summarization is a related domain, where the system |  |
|  | automatically creates a trailer of a long video. This also has |  |
|  | applications in consumer or personal videos, where one might |  |
|  | want to skip the boring or repetitive actions. Similarly, in |  |
|  | surveillance videos, one would want to extract important and |  |
|  | suspicious activity, while ignoring all the boring and redundant |  |
|  | frames captured.""" |  |

### B. Preprocessing

1. Menyiapkan stopwords, punctuation, dan tokenisasi

|  | stopwords = list(STOP WORDS) |  |
| --- | --- | --- |
|  | _ punctuation = punctuation + '\n' |  |
|  | nlp = spacy.load('en core web sm') _ _ _ |  |

selama analisis frekuensi kata. Daftar ini diambil dari spacy.lang.en.stop_words.STOP_WORDS.

b. punctuation: String yang berisi tanda baca yang akan diabaikan. Ini diambil dari modul `string` dan ditambahkan karakter newline (`\n`).

c. nlp: Objek model bahasa spaCy yang dimuat (`en_core_web_sm`). Objek ini akan digunakan untuk memproses teks, seperti tokenisasi kalimat dan kata.

---

<!-- Halaman 65 -->

2. Text Cleaning

| def clean text(text): _ # Lowercasing text = text.lower() # Remove numbers text = re.sub(r'\d+', '', text) return text | def clean text(text): |  |  |
| --- | --- | --- | --- |
|  |  | _ # Lowercasing |  |
|  |  | text = text.lower() |  |
|  |  | # Remove numbers |  |
|  |  | text = re.sub(r'\d+', '', text) |  |
|  |  | return text |  |

```
text = clean_text(text) 
print("Cleaned Text:") 
print(text) 
```

3. Sentence Tokenization

|  | doc = nlp(text) |  |
| --- | --- | --- |
|  | def tokenize sentences(doc): |  |
|  | _ return [sent for sent in doc.sents] |  |
|  | sentence tokens = tokenize sentences(doc) |  |
|  | _ _ |  |
|  | print("Sentence Tokens:") |  |
|  | print(sentence tokens) _ |  |

4. Word Tokenization

| def tokenize words(doc): _ return [token.text for token in doc] | def tokenize words(doc): |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | _ return [token.text for token in doc] |  |
|  |  | word tokens = tokenize words(doc) |  |  |
|  |  | _ _ |  |  |
|  |  | print("Word Tokens:") |  |  |
|  |  | print(word tokens) _ |  |  |

5. Tabel frekuensi data

|  | def create word frequency table(doc, stopwords, punctuation): |  |
| --- | --- | --- |
|  | _ _ _ word frequencies = {} |  |
|  | _ for word in doc: |  |
|  | if word.text.lower() not in stopwords: |  |
|  | if word.text.lower() not in punctuation: |  |
|  | if word.text not in word frequencies.keys(): |  |
|  | _ word frequencies[word.text] = 1 |  |
|  | _ else: |  |
|  | word frequencies[word.text] += 1 |  |
|  | _ |  |
|  | if not word frequencies: # Handle empty dictionary case |  |
|  | _ return {} |  |
|  |  |  |
|  | print("Frekuensi Kata :\n", word frequencies) |  |
|  | _ print("\n") |  |
|  |  |  |
|  | max frequency = max(word frequencies.values()) |  |
|  | _ _ print("Frekuensi Maksimal :", max frequency) |  |
|  | _ print("\n") |  |

---

<!-- Halaman 66 -->

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | for word in word frequencies.keys(): |  |
|  | _ word frequencies[word] = word frequencies[word] / |  |
|  | _ _ max frequency |  |
|  | _ print("Frekuensi Rata-Rata Kata (Normalisasi) :\n", |  |
|  | word frequencies) |  |
|  | _ print("\n") |  |
|  |  |  |
|  | return word frequencies _ |  |
|  | word frequencies = create word frequency table(doc, stopwords, |  |
|  | _ _ _ _ punctuation) |  |

6. Pemberian skor pada kalimat

|  | def score sentences(sentence tokens, word frequencies): |  |
| --- | --- | --- |
|  | _ _ _ sentences scores = {} |  |
|  | _ for sent in sentence tokens: |  |
|  | _ for word in sent: |  |
|  | if word.text.lower() in word frequencies.keys(): |  |
|  | _ if sent not in sentences scores.keys(): |  |
|  | _ sentences scores[sent] = |  |
|  | _ word frequencies[word.text.lower()] |  |
|  | _ else: |  |
|  | sentences scores[sent] += |  |
|  | _ word frequencies[word.text.lower()] |  |
|  | _ return sentences scores _ |  |
|  | sentences scores = score sentences(sentence tokens, |  |
|  | _ _ _ word frequencies) |  |
|  | _ print("Sentences Scores:") |  |
|  | sentences scores _ |  |

7. Summarization

|  | def summarize text from sentences(sentence tokens, |  |
| --- | --- | --- |
|  | _ _ _ _ sentences scores, summary length percentage): |  |
|  | _ _ _ select length = int(len(sentence tokens) * |  |
|  | _ _ summary length percentage) |  |
|  | _ _ |  |
|  | if select length == 0 and len(sentence tokens) > 0: |  |
|  | _ _ select length = 1 # Ensure at least one sentence is |  |
|  | _ selected if text is not empty |  |
|  | elif select length > len(sentence tokens): |  |
|  | _ _ select length = len(sentence tokens) # Do not exceed the |  |
|  | _ _ number of sentences |  |
|  | print("Jumlah Kalimat yang Dipilih :", select length) |  |
|  | _ |  |
|  | summary sentences = nlargest(select length, sentences scores, |  |
|  | _ _ _ key=sentences scores.get) |  |
|  | _ |  |
|  | final summary = [word.text for word in summary sentences] |  |
|  | _ _ summary = ' '.join(final summary) |  |
|  | _ |  |
|  | return summary |  |
|  | summary = summarize text from sentences(sentence tokens, |  |
|  | _ _ _ _ sentences scores, 0.2) _ |  |
|  | print("Original Text:") |  |
|  | print(text) |  |

---

<!-- Halaman 67 -->

|  | print("Summary:") |  |
| --- | --- | --- |
|  | print(summary) |  |
|  | print("Panjang Kalimat Asli :", len(text)) |  |
|  | print("Panjang Kalimat Ringkasan :", len(summary)) |  |

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| Lakukanlah peringkasan teks: |  |  |  |  |
| 1 | CPL-03 | CPMK-02 | Dengan data teks berita tentang MBG yang ada di internet | 50 |
| 2 | CPL-03 | CPMK-02 | Dengan data teks dari wikipedia, pilih salah satu tema berikut: Politik, Olahraga, atau Hobi | 50 |

---

<!-- Halaman 68 -->

## PRAKTIKUM 9: MACHINE TRANSLATION I

Pertemuan ke 9 Total Alokasi Waktu 90 menit • Materi : 15 menit 11. Pre-Test : 15 menit 12. Praktikum : 45 menit 13. Post-Test : 15 menit Total Bobot Penilaian 100% 14. Pre-Test : 20% 15. Praktik : 30% 16. Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan apa itu Text Translate

2. Menerapkan proses deep translator

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan proses text translate pada deep translator |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

Machine Translation adalah sebuah teknik yang ada di dalam Natural Language

Processing (Pemrosesan Bahasa Alami) digunakan untuk menerjemahkan teks atau ucapan

---

<!-- Halaman 69 -->

dari satu bahasa ke bahasa lainnya. Seiring berkembangnya teknologi, model LLM yang pada dasarnya bersifat general-purpose dapat digunakan untuk tugas penerjemahan yang merupakan salah satu dari berbagai kemampuan bahasa yang dimiliki LLM. Dengan LLM, proses penerjemahan dapat dilakukan secara zero-shot tanpa melakukan pelatihan ulang secara khusus. Selain itu, model LLM juga dapat disesuaikan lebih lanjut melalui proses fine- tuning apabila diperlukan peningkatkan performa pada domain atau pasangan bahasa tertentu.

a. Mekanisme Zero-Shot pada LLM

Zero-shot adalah kemampuan dari LLM untuk melakukan tugas penerjemahan tanpa perlu adanya pelatihan ulang secara khusus pada pasangan bahasa tertentu. Kemampuan ini diperoleh karena LLM dilatih menggunakan korpus teks yang sangat besar dan multibahasa. Dari hasil pelatihan tersebut, model LLM dapat mengenali pola umum bahasa, struktur kalimat, dan hubungan semantik.

b. Prompt Engineering pada LLM

Prompt Engineering adalah proses untuk merancang instruksi dari konteks input agar

LLM dapat menghasilkan terjemahan yang sesuai dengan tujuan, gaya, dan kualitas yang diinginkan. Dalam prompt engineering dibutuhkan instruksi yang jelas dengan menyebutkan tugas dan pasangan bahasa yang akan diterjemahkan.

contohnya:

“Translate the following text from Indonesian to English : Saya sedang Makan” c. Fine-Tuning LLM

Fine-tuning adalah proses melatih ulang model yang telah dilatih (pre-trained model) menggunakan dataset khusus agar model mampu menyelesaikan tugas dengan lebih baik. Dalam konteks machine translation, fine-tuning digunakan untuk melatih model untuk memahami pola terjemahan bahasa tertentu dan meningkatkan kualitas terjemahan pada domain atau bahasa yang spesifik.

Model-model LLM memiliki parameter yang sangat banyak sehingga proses fine- tuningnya memerlukan resource yang besar, yang kurang ideal untuk penelitian skala kecil atau untuk praktikum. Sehingga diperlukan pendekatan Parameter Efficient Fine-Tuning

(PEFT). Salah satu metode dari PEFT adalah Low-Rank Adaptation, yaitu metode yang membekukan (freeze) sebagian parameter asli dari pre-trained model, menyisipkan dua low- rank matriks dan hanya melatih matriks tambahan tersebut sehingga bobot model tidak

---

<!-- Halaman 70 -->

berubah. LoRA ini cocok untuk pelatihan model besar dengan GPU terbatas, karena jumlah parameter saat fine-tuning sangat kecil.

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

4. Pandas

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Jelaskan mekanisme zero-shot pada LLM! | 35 |
| 2 | CPL-03 | CPMK-02 | Apa itu Machine Translation? | 30 |
| 3 | CPL-03 | CPMK-02 | Jelaskan apa itu Low-Rank Adaptation! | 35 |

### 1.6. LANGKAH PRAKTIKUM

### A. Persiapan

a. Login Google dan buka Google Colab. (https://colab.research.google.com/) b. Download file notebook.ipnyb, kemudian upload ke Colab. (File > Upload Notebook

> Cari > Pilih notebook yang sudah didownload > Open

---

<!-- Halaman 71 -->

c. Ubah jenis Runtime colab dengan cara klik segitiga terbalik di pojok kanan atas, kemudian pilih “Ubah Jenis Runtime” d. Matikan authentikasi ke WANDB dengan :

```
import os 
os.environ['WANDB_DISABLED'] = "True"  
#Mematikan authentikasi ke WANDB sehingga tidak akan diminta 
API KEY 
```

### B. Load Pre-Trained Model

```
from transformers import AutoTokenizer, AutoModelForCausalLM 
#Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(Qwen/Qwen2.5-1.5B-
instruct”) 
#Load Model 
model = AutoModelForCausalLM.from_pretrained(“Qwen/Qwen2.5-1.5B-
Instruct”) 
```

Model LLM yang akan digunakan pada praktikum kali ini adalah model Qwen dengan jumlah parameter 1.5 Miliar. Model QWEN didapat dari Hugging Face. Praktikan dapat explore pilihan model lain dan cara menggunakannya di https://huggingface.co/

### C. Load Dataset (20 %)

```
#Import Dataset yang akan digunakan untuk fine tuning  
import pandas as pd  
df = pd.read_excel('/content/bahas minang - indonesia.xlsx')  
df.head() 
```

---

<!-- Halaman 72 -->

```
df = df.sample(frac=0.2, random_state=42) # Ambil 20% data sebagai 
dataset latih 
df.head() #Tampilkan 5 data teratas 
```

Praktikum kali ini menggunakan 20% dari dataset untuk mempersingkat waktu dari pelatihan. Tetapi hal ini dapat menyebabkan model tidak maksimal dalam berlatih.

Praktikan disarankan untuk explore di luar jam praktikum dengan cara melatih model dengan 70%-80% data dari dataset.

### D. Format Dataset

```
from datasets import Dataset 
def formatMessage(indo, minang): #Format prompt sesuai dengan 
inputan untuk model 
  return { 
      "messages": [ 
            { 
                "role": "system", 
                "content": "You are an Indonesian to Minangkabau 
translator." 
            }, 
            { 
                "role": "user", 
                "content": indo 
            }, 
            { 
                "role": "assistant", 
                "content": minang 
            } 
        ] 
  } 
df_cleaned = df.fillna('') #Ganti kolom yang kosong dengan 
string kosong 
data = Dataset.from_pandas(df_cleaned) 
```

---

<!-- Halaman 73 -->

```
dataset = data.map( 
    lambda x: formatMessage(x["indo"], x["minang"]) #Terapkan 
fungsi Format Prompt (Message) untuk setiap element pada dataset 
) 
dataset = dataset.remove_columns(["indo", "minang"])  #Hilangkan 
kolom yang tidak perlu 
```

Dataset perlu diformat kedalam template yang dimengerti model. Dalam praktikum ini, kita memakai QWEN yang dasarnya merupakan model LLM berbasis chat seperti GPT, sehingga data yang akan dimasukkan kedalam model harus mengikuti template chat tersebut.

Fungsi formatMessage adalah fungsi yang akan digunakan untuk merubah semua data pada dataset menjadi format yang diinginkan oleh model. Untuk melihat hasil dari formatMessage tersebut, jalankan kode :

```
dataset[0] #Lihat element pertama pada dataset 
```

### E. Tokenisasi & Pre-processing

```
def preprocess(example): 
    text = tokenizer.apply_chat_template( #Memasukkan prompt 
yang telah diproses sebelumnya kedalam template model 
        example["messages"], #Dataset 
        tokenize=False, 
        add_generation_prompt=False 
    ) 
    tokenized = tokenizer( 
        text, 
        truncation=True, #Teks akan dipotong jika panjangnya 
melebihi max_length 
        max_length=512, 
        padding = 'max_length', #Teks akan ditambahkan token 
padding jika panjangnya kurang dari max_length 
    ) 
```

---

<!-- Halaman 74 -->

```
    tokenized["labels"] = tokenized["input_ids"].copy() 
#Mendefinisikan kolom labels (copy dari kolom train) 
    return tokenized 
tokenized_dataset = dataset.map( 
    preprocess, 
    remove_columns=dataset.column_names  #Menerapkan fungsi 
diatas untuk semua element pada dataset 
) 
```

Setelah semua data di-format, setiap data harus dilakukan tokenisasi. Tokenisasi dilakukan menggunakan tokenizer yang sudah disediakan oleh model.

### F. Load konfigurasi Lora dan Training

```
from peft import LoraConfig, get_peft_model 
lora_config = LoraConfig( 
    r=8, 
    lora_alpha=16, 
    target_modules=["q_proj", "v_proj"], 
    lora_dropout=0.05, 
    bias="none", 
    task_type="CAUSAL_LM" 
) 
model = get_peft_model(model, lora_config) 
model.print_trainable_parameters() #Lihat parameter yang akan ditrain 
dan disesuaikan dengan LoRA 
```

Seperti yang sudah dibahas pada teori, LoRA digunakan ketika fine-tuning untuk menghemat resource ketika pelatihan. Menggunakan konfigurasi diatas, model hanya akan melatih 0,0705% dari 1.5M parameter. Nilai rank (r = 8) digunakan karena  cukup untuk menangkap pola bahasa yang baru pada task translation tanpa menambah parameter secara berlebih. Lora Alpha (lora_alpha = 16) didapat menggunakan rasio

(lora_alpha = 2 x rank). Module yang ditargetkan adalah q_proj dan v_proj. Keduanya merupakan layer penting untuk meningkatkan pemahaman dan kesejajaran konteks

---

<!-- Halaman 75 -->

antar bahasa. Nilai dropout 0.05 dipakai untuk mencegah overfitting pada dataset kecil.

Task_type “CAUSAL_LM”  menyesuakan dengan model yang juga merupakan model

“CAUSAL_LM”

```
import torch 
import gc 
gc.collect() 
torch.cuda.empty_cache() 
torch.cuda.ipc_collect() 
from transformers import TrainingArguments, Trainer, 
DataCollatorWithPadding 
training_args = TrainingArguments( 
    output_dir="./llm-mt-lora", 
    learning_rate=1e-4, #Laju pembelajaran 1 x 10^-4 
    per_device_train_batch_size=2,  #Jumlah batch / training 
    gradient_accumulation_steps=4, 
    num_train_epochs=3, #Banyaknya epoch untuk pelatihan 
    logging_steps=50, #Logging loss setiap 50 steps 
    save_total_limit=2, #Max checkpoint dari model 
    fp16=True, 
    report_to="none" 
) 
trainer = Trainer( 
    model=model, #Definisikan model 
    args=training_args, #Definisikan training args 
    train_dataset=tokenized_dataset, #Definisikan dataset 
training 
    tokenizer=tokenizer #Definisikan Tokenizer 
) 
```

Training argument memiliki beberapa parameter, diantaranya :

---

<!-- Halaman 76 -->

• output_dir = menentukan lokasi penyimpanan hasil training dan checkpoint model

• Learning Rate =  1e-4, dipilih karena umum dan stabil untuk fine-tuning LoRA

• Per_device_train_batch_size = 2, batch training yang digunakan kecil, menyesuaikan keterbatasan memori GPU saat melatih

• Gradient_accumulation_steps = 4, berfungsi sebagai penambal dari keterbatasan train batch size. berfungsi untuk mensimulasikan batch size yang besar, walaupun train batch per device kecil

• Num_train_epochs  = 3, jumlah iterasi training

• Logging_steps  = 50, artinya loss dari training akan di catat per 50 steps

• Save_total_limit = 2, untuk membatasi checkpoint dari model sebanyak 2 untuk menghemat storage

• Fp16 = True, mengaktifkan mixed precision untuk mempercepat training dan menghemat memori GPU

• Report_to  = none, digunakan agar proses training tidak perlu mengirim log ke

WanDB.

### G. Training model

```
trainer.train() 
```

### H. Gunakan model untuk generate hasil

```
import torch 
 #Ambil model yang sudah di Train 
model = trainer.model 
model.eval() 
#Buat prompt untuk menguji 
teks = """ujung silangan bagian dalam dilipatkan membalut ujung 
bagian luar dan selanjutnya dimasukkan ke dalam, sedangkan ujung 
silangan bagian luar dilipatkan ke atas sehingga menutup 
sebagian lubang lingkaran""" 
```

---

<!-- Halaman 77 -->

```
messages = [ 
    { 
        "role": "system", 
        "content": "You are an Indonesian to Minangkabau 
translator" 
    }, 
    { 
        "role": "user", 
        "content": teks 
    } 
] 
# Masukkan prompt kedalam template chat 
prompt = tokenizer.apply_chat_template( 
    messages, 
    tokenize=False, 
    add_generation_prompt=True 
) 
#Tokenize prompt 
inputs = tokenizer( 
    prompt, 
    return_tensors="pt" 
).to(model.device) 
#Feed prompt ke model kemudian generate jawaban dari model 
with torch.no_grad(): 
    outputs = model.generate( 
        **inputs, 
        max_new_tokens=50, 
        temperature=0.2, 
        do_sample=False 
    ) 
# Ambil jawaban dari model 
hasil = tokenizer.decode( 
```

---

<!-- Halaman 78 -->

```
    outputs[0][inputs["input_ids"].shape[-1]:], 
    skip_special_tokens=True 
) 
print(hasil) 
```

### I. Contoh Output

Dapat dilihat dari hasil terjemahan diatas, bahwa model sudah dapat mengenali struktur dari bahasa minang, namun secara translasi kata per kata masih kurang baik.

Hal ini dapat terjadi karena model yang tidak mengetahui bahasa minang dan hanya berlatih dengan data yang sedikit.

---

<!-- Halaman 79 -->

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| Agar praktikan lebih memahami bagaimana proses dari pelatihan LLM dan pengaruh dari data terhadap hasil dari pelatihan. Maka praktikan diminta untuk : |  |  |  |  |
| 1 | CPL-03 | CPMK-02 | Training 80% Data df = df.sample(frac=0.2, random state=42) _ # Ambil 20% data sebagai dataset latih | 50 |
| 2 | CPL-03 | CPMK-02 | Analisa perbedaan hasil antara model yang menggunakan 20% data dengan 80% data, termasuk dengan mencatat lama waktu eksekusi. | 50 |

---

<!-- Halaman 80 -->

## PRAKTIKUM 10: MACHINE TRANSLATION II

Pertemuan ke 9 Total Alokasi Waktu 90 menit • Materi : 15 menit 17. Pre-Test : 15 menit 18. Praktikum : 45 menit 19. Post-Test : 15 menit Total Bobot Penilaian 100% 20. Pre-Test : 20% 21. Praktik : 30% 22. Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas |
| --- | --- |
| CPMK-02 | Mampu menjelaskan metode yang digunakan untuk penyelesaian task: language modeling, POS Tagging, parsing, representasi semantik, dan aplikasi PBA. |

### 1.8. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menjelaskan apa itu Text Translate

2. Menerapkan proses deep translator

### 1.9. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-02 | Kemampuan mahasiswa dalam menerapkan proses text translate pada deep translator |
| --- | --- | --- |

### 1.1. TEORI PENDUKUNG

Setelah pada praktikum sebelumnya kita melatih model. Pada praktikum kali ini kita akan mengevaluasi model yang sudah kita latih tersebut. Evaluasi ini berguna untuk

---

<!-- Halaman 81 -->

mengatahui sebaik apa prediksi model terhadap data. Evaluasi tidak sebatas akurasi saja, tapi evaluasi juga memperlihatkan seberapa baik model dalam menghadapi data dunia nyata.

Evaluasi ini dapat dilakukan secara manual, maupun otomatis menggunakan metrik kuantitatif seperti chrF, BLEU, Dan BERT Score.

a. chrF

Character n-gram F-score (chrF) merupakan metrik yang menghitung kesamaan pada tingkat karakter. chrF mengukur presisi dan recall dari n-gram (kesamaan karakter) antara referensi dan hasil terjemahan, kemudian digabungkan menjadi nilai F-Score.

chrF lebih sensitif terhadap variasi ejaan dan perubahan morfologi sehingga metrik ini sering digunakan untuk evaluasi model yang dilatih dengan bahasa low-resource b. BLEU

Bilingual Evaluation Understudy (BLEU) merupakan salah satu metrik evaluasi yang paling banyak digunakan. BLEU menghitung kesamaan n-gram antara referensi dan terjemahan. Hasil perhitungan tersebut digunakan untuk mencocokan kata atau frasa.

BLEU juga menggunakan brevity penalty untuk menghindari hasil terjemahan yang terlalu pendek dibandingkan referensi. BLEU memiliki keterbatasan yaitu tidak dapat menangkap makna atau konteks karena hanya mengukur kesamaan berbasis kata.

c. BERT Score

Untuk melengkapi kekurangan dari kedua matrik evaluasi diatas kita juga akan menghitung BERT Score pada evaluasi kali ini. BERTScore merupakan metrik yang menggunakan representasi semantik dari model bahasa berbasis transformer. Selain membandingkan kesamaan kata secara literal, BERTScore  juga menghitung kesamaan makna dari kalimat. Metrik ini dapat menangkap hubungan kata seperti sinonim, parafrase dan kesamaan semantik yang tidak dapat diukur dengan metrik BLEU dan chrF.

### 1.2. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Google Colaboratory

4. Pandas

---

<!-- Halaman 82 -->

### 1.3. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | Beri contoh perhitungan salah satu dari metrik evaluasi dari Machine Translation | 100 |

### 1.4. LANGKAH PRAKTIKUM

a. Install Library untuk evaluasi

```
!pip install evaluate 
!pip install bert_score 
!pip install sacrebleu 
```

b. Import library yang diperlukan

```
from google.colab import drive 
from sklearn.model_selection import train_test_split 
import pandas as pd 
from datasets import Dataset 
from transformers import AutoTokenizer, pipeline, 
AutoModelForCausalLM 
import torch 
from tqdm import tqdm 
from tqdm.notebook import tqdm 
from sacrebleu.metrics import BLEU, CHRF 
from bert_score import score as bert_score 
import pandas as pd 
```

c. Load tokenizer dan model yang disimpan di google drive

```
drive.mount("/content/drive") 
#Ambil Tokenizer untuk model yang telah dilatih pada praktikum 
sebelumnya 
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-
Instruct") 
#Load Model yang telah dilatih pada praktikum sebelumnya 
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-
Instruct") 
```

d. Load dataset yang akan digunakan untuk evaluas model

```
#Load Dataset yang akan digunakan untuk mengevaluasi model 
df = pd.read_excel("/content/bahas minang - indonesia.xlsx") 
df = df.sample(frac=0.2, random_state=42) # Ambil 20% data sebagai 
dataset latih 
df.head() #Tampilkan 5 data teratas 
```

---

<!-- Halaman 83 -->

e. Lakukan formatting untuk semua data yang ada didalam dataset menjadi prompt untuk di-generate hasilnya oleh model. Gunakan prompt yang sama dengan prompt yang digunakan ketika melatih model.

```
#Format semua data yang ada di dalam dataset menjadi prompt 
untuk di-generate hasilnya 
def format_message(df): 
    df['formatted_message'] = df.apply( 
        lambda row: { 
            #Pakai prompt yang sama dengan prompt yang digunakan 
ketika melatih model 
            "messages": [ 
                { 
                    "role": "system", 
                    "content": "You are an Indonesian to 
Minangkabau translator." 
                }, 
                { 
                    "role": "user", 
                    "content": f'{row['indo']}' 
                } 
            ] 
        }, 
        axis=1 
    ) 
    return df 
 
df = format_message(df) 
df['formatted_message'][0] 
```

### f. Generate hasil menggunakan model

```
#Generate hasil dengan model 
def generate_response_batch(df, tokenizer, model, batch_size=8): 
    results = [] 
    messages_list = df['formatted_message'].apply(lambda x: 
x['messages']).tolist() 
 
    for i in tqdm(range(0, len(messages_list), batch_size), 
desc="Translating"): 
        batch = messages_list[i:i+batch_size] #Generate respons 
dalam bentuk batch 
 
        inputs = tokenizer.apply_chat_template( 
            batch, 
            add_generation_prompt=True, 
            tokenize=True, 
            padding=True, 
            return_dict=True, 
            return_tensors="pt" 
        ).to(model.device) 
```

---

<!-- Halaman 84 -->

```
        with torch.no_grad():  # Matikan gradient, hemat memori 
& lebih cepat 
            outputs = model.generate( 
                **inputs, 
                max_new_tokens=40, 
                do_sample=False,       # Greedy decoding, lebih 
cepat 
                num_beams=1,           # Matikan beam search 
            ) 
 
        decoded = tokenizer.batch_decode(outputs, 
skip_special_tokens=True) #Ambil output yang diinginkan dari 
response model 
        results.extend(decoded) 
 
    df['translation_result'] = results 
    return df 
 
df = generate_response_batch(df, tokenizer, model) 
df.head() 
```

### g. Lakukan evaluasi model

```
def evaluate(df): 
    references = df['minang'].tolist() #Teks yang benar/hasil 
yang diharapkan 
    prediction = df['translation_result'].tolist() #Teks hasil 
generate model 
    # --- BLEU --- 
    bleu = BLEU() #Gunakan BLEU 
    bleu_score = bleu.corpus_score(prediction, [references]) 
#Hitung Score 
    # --- ChrF --- 
    chrf = CHRF() #Gunakan ChrF 
    chrf_score = chrf.corpus_score(prediction, [references]) 
#Hitung Score 
    # --- BERTScore --- 
    P, R, F1 = bert_score( #Gunakan ChrF 
        prediction, 
```

---

<!-- Halaman 85 -->

```
        references, 
        lang="id",         # Gunakan "id" untuk bahasa 
Indonesia/daerah 
        verbose=True 
    ) 
    results = { 
        "BLEU"      : round(bleu_score.score, 4), 
        "ChrF"      : round(chrf_score.score, 4), 
        "BERTScore P" : round(P.mean().item(), 4), 
        "BERTScore R" : round(R.mean().item(), 4), 
        "BERTScore F1": round(F1.mean().item(), 4), 
    } 
    return pd.Series(results) 
scores = evaluate(df) 
print(scores) 
```

### Contoh Output :

---

<!-- Halaman 86 -->

### 1.5. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-02 | (Lab) Analisa performa model berdasarkan matriks evaluasi. | 50 |
| 2 | CPL-03 | CPMK-02 | (Take Home) Bandingkan performa model yang dilatih dengan 20% dataset dengan 80% dataset | 50 |

---

<!-- Halaman 87 -->

## PRAKTIKUM 11: FLASK

Pertemuan ke 11 Total Alokasi Waktu 90 menit • Materi : 15 menit 23. Pre-Test : 15 menit 24. Praktikum : 45 menit 25. Post-Test : 15 menit Total Bobot Penilaian 100% 26. Pre-Test : 20% 27. Praktik : 30% 28. Post-Test : 50%

### Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas. |
| --- | --- |
| CPMK-03 | Mengembangkan aplikasi dengan metode-metode yang sudah dipelajari dalam penyelesaian permasalahan dalam pemrosesan bahasa alami. |

### 1.1. DESKRIPSI CAPAIAN PEMBELAJARAN

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu menerapkan flask.

### 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-03 | Kemampuan mahasiswa dalam menerapkan flask |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

Flask adalah sebuah kerangka kerja web (web framework) untuk Python. Ia tergolong sebagai "mikro-framework" karena secara sengaja dibuat minimalis. Artinya, saat sebuah proyek baru dimulai, Flask hanya menyediakan komponen-komponen inti yang paling esensial untuk membuat aplikasi web berjalan. Komponen inti tersebut adalah:

---

<!-- Halaman 88 -->

a. Werkzeug: Pustaka yang bekerja di belakang layar untuk menangani hal-hal fundamental seperti permintaan (request) dari browser, respons (response) dari server, dan logika dasar lainnya.

b. Jinja2: Sebuah sistem template yang berfungsi untuk memisahkan kode logika (Python) dari kode tampilan (HTML). Ini membuat proyek lebih rapi dan mudah dikelola.

Di luar dua komponen inti tersebut, Flask tidak menyertakan alat bawaan untuk database, manajemen form, atau autentikasi. Pengembang diberikan kebebasan untuk memilih dan menambahkan sendiri komponen-komponen tersebut.

Filosofi di balik desain Flask berpusat pada tiga hal:

a. Minimalist: Inti framework dijaga agar tetap kecil dan ringan. Proyek hanya dimulai dengan apa yang benar-benar dibutuhkan, sehingga tidak ada kode atau fitur yang tidak terpakai yang membebani proyek.

b. Fleksibel: Karena tidak ada alat yang dipaksakan, pengembang memiliki kontrol penuh untuk menentukan komponen yang akan digunakan, mulai dari pustaka database, validasi form, hingga teknologi lain yang paling sesuai dengan kebutuhan spesifik proyek.

c. Dapat Diperluas (Extensible): Fungsionalitas tambahan dapat diintegrasikan dengan mudah melalui ekstensi. Jika sebuah aplikasi membutuhkan interaksi dengan database, ekstensi seperti Flask-SQLAlchemy dapat dipasang. Jika butuh sistem login, tersedia

Flask-Login. Dengan cara ini, aplikasi dapat tumbuh dari yang sangat sederhana menjadi sangat kompleks secara modular.

Secara teknis, alur kerja dalam aplikasi Flask bergantung pada konsep-konsep berikut:

a. Routing (Pemetaan URL): Ini adalah mekanisme Flask untuk menghubungkan sebuah

URL yang diakses pengguna dengan fungsi Python tertentu. Ketika pengguna mengunjungi situs.com/beranda, sistem routing akan mencari fungsi Python yang telah ditandai untuk menangani alamat /beranda, lalu menjalankan fungsi tersebut.

b. Siklus Request-Response: Semua aplikasi web bekerja dalam siklus ini.

1. Request (Permintaan): Browser pengguna mengirimkan permintaan ke server.

Permintaan ini berisi informasi seperti URL yang dituju dan data lain yang mungkin dikirim. Flask mengemas semua informasi ini ke dalam objek request yang bisa diakses di dalam kode.

---

<!-- Halaman 89 -->

2. Response (Respons): Fungsi Python yang terkait dengan URL tersebut akan berjalan, memproses logika yang diperlukan, dan menghasilkan sebuah keluaran.

Keluaran ini (biasanya HTML) kemudian dikemas oleh Flask menjadi sebuah objek response dan dikirim kembali ke browser untuk ditampilkan.

c. Templates (Sistem Template): Konsep ini bertujuan untuk menjaga agar kode tetap terorganisir. Daripada menulis kode HTML langsung di dalam file Python, kode tersebut ditempatkan di file .html terpisah. Fungsi Python kemudian bertugas menyiapkan data (misalnya daftar produk atau nama pengguna), lalu meneruskan data itu ke file template. Sistem Jinja2 akan memasukkan data tersebut ke dalam placeholder yang sudah disiapkan di HTML, menghasilkan halaman web final.

### 1.4. HARDWARE DAN SOFTWARE

Hardware dan software yang digunakan dalam praktikum ini, yaitu:

1. Komputer

2. Bahasa pemrograman python

3. Visual Studio Code

### 1.5. PRE-TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-03 | Jelaskan apa itu flask dan template! | 40 |
| 2 | CPL-03 | CPMK-03 | Jelaskan tujuan mengapa Flask dibuat! | 40 |
| 3 | CPL-03 | CPMK-03 | Sebutkan cara mengimport package dan class flask di python! | 20 |

### 1.6. LANGKAH PRAKTIKUM

### 1. Pastikan sudah menginstall python.

### 2. Buat terlebih dahulu file dengan <nama_file>.py kemudian isikan kode berikut

### 3. Install library Flask

---

<!-- Halaman 90 -->

4. Import package flask

5. Inisialisasi fungsi Flask()

6. Atur route

7. Buka terminal, jalankan server flask dengan perintah “python <nama_file>.py”. Kalau berhasil, maka akan diberikan link untuk membuka halaman website.

8. Buka link yang diberikan di web browser dan lihat hasilnya.

9. Tambahkan “render_template” pada bagian import

10. Buat folder dengan nama “Template” di direktori yang sama dengan file flask. Lalu buat sebuah file html

---

<!-- Halaman 91 -->

11. Inisialisasi fungsi Flask() dan buat route. Di bagian route, kita return halaman html yang sudah kita buat menggunakan render_template()

12. Buka Halaman “Index.html”, kemudian edit

13. Lihat halaman yang sudah dibuat di web browser

---

<!-- Halaman 92 -->

### 1.7. POST TEST

Jawablah pertanyaan berikut:

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1 | CPL-03 | CPMK-03 | Jelaskan Buatlah biodata diri minimal 5 data yang ditampilkan kemudian jika memungkinkan tambahkan css agar biodata yang dibuat lebih menarik. Lampirkan tangkapan layer untuk hasilnya dan kemudian beri penjelasan untuk setiap gambarnya. | 100 |