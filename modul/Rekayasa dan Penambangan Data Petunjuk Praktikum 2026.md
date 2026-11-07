<!-- Halaman 1 -->

## Rekayasa dan

## Penambangan Data

### Penyusun:

### Lisna Zahrotun, S.T., M.Cs.

### Tedi Setyadi, S.T, M.T

### Dwi Normawati, S.T., M.Eng.

### Sheraton Pawestri, S.Kom., M.Cs.

---

<!-- Halaman 2 -->

### HAK CIPTA

### PETUNJUK PRAKTIKUM REKAYASA DAN PENAMBANGAN DATA

Copyright© 2026, Lisna Zahrotun, S.T, M.Cs Tedi Setyadi, S.T, M.T Dwi Normawati, S.T, M.Eng Sheraton Pawestri, S.Kom., M.Cs. Hak Cipta dilindungi Undang-Undang Dilarang mengutip, memperbanyak atau mengedarkan isi buku ini, baik sebagian maupun seluruhnya, dalam bentuk apapun, tanpa izin tertulis dari pemilik hak cipta dan penerbit. Diterbitkan oleh: Program Studi Informatika Fakultas Teknologi Industri Universitas Ahmad Dahlan Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 Penulis :  Lisna Zahrotun, S.T, M.Cs Tedi Setyadi, S.T, M.T Dwi Normawati, S.T, M.Eng Sheraton Pawestri, S.Kom., M.Cs. Editor : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Desain sampul : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Tata letak : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Ukuran/Halaman : 21 x 29,7 cm / 132 halaman Didistribusikan oleh:

### Laboratorium S1 Informatika

### Universitas Ahmad Dahlan 
Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 
Indonesia

---

<!-- Halaman 3 -->

### KATA PENGANTAR

Program studi Informatika pada semester Gasal T.A 2026/2027 sudah menerapkan kurikulum berbasis Outcome Based Education (OBE). Dampak dari penggunaan kurikulum OBE ini adalah adanya perubahan dalam metode asesmen setiap mata kuliah. Oleh karena intu untuk mata kuliah yang mengadakan praktikum tentunya asesmen untuk kegiatan praktikum juga menyesuaikan dengan Rencana Pembelajaran Semester (RPS) OBE.

Dalam mata kuliah data mining terjadi beberapa perubahan yaitu penentuan CPL, CPMK dan Sub-CPMK, tentunya untuk praktikum data mining juga mengalami perubahan pada asesmen yaitu meliputi pretest, pelaksanaan praktikum dan response. Untuk materi dalam praktikum data mining ini ada penambahan materi terkait sentiment analisis dan juga perubahan pada beberapa studi kasus postestnya.

Demikian untuk perubahan dalam petunjuk praktikum Rekayasa dan Penambangan Data pada semester Gasal T.A 2026/2027.

Yogyakarta, 20 September 2026

Lisna Zahrotun, S.T, M.Cs

---

<!-- Halaman 4 -->

### DAFTAR PENYUSUN

### Lisna Zahrotun, S.T., M.Cs.

|  | Penulis merupakan Dosen di prodi Informatika UAD dengan bidang keilmuan Rekayasa Perangkat Lunak dan Data. Mulai mengajar di Informatika sejak Tahun 2009 dengan bidang minat riset di bidang: Data Mining, Test Mining dan Sistem Pendukung Keputusan. |
| --- | --- |

### Drs. Tedi Setyadi, M.T

|  | Penulis merupakan dosen di bidang Teknik Informatika bidang keilmuan Rekayasa Perangkat Lunak dan Data. Bidang minat riset di bidang data mining. Saat ini sedang menempuh S3 di Malaysia. |
| --- | --- |

### Dwi Normawati, S.T., M.Eng.

|  | Penulis merupakan dosen di bidang Teknik Informatika bidang keilmuan system cerdas. Beliau lulus S2 dari Universitas Gadjah Mada dengan topic disertasi Data mining. Saat ini focus penelitian beliau juga dalam data mining. |
| --- | --- |

### Sheraton Pawestri, S.Kom., M.Cs.

|  | Penulis merupakan dosen di bidang Teknik Informatika bidang keilmuan system cerdas. Beliau lulus S2 dari Universitas Gadjah Mada dengan topic disertasi NLP. Saat ini focus penelitian beliau juga dalam data mining. |
| --- | --- |

---

<!-- Halaman 5 -->

### KONTRIBUSI PENULIS

| Nomor Bab | Daftar Penulis |
| --- | --- |
| Bab 1 sampai Bab 11 Perubahan dan penambahan pretest dan Postest Bab 1 sampai 11 | Lisna Zahrotun, S.T, M.Cs |
| Bab 8 bagian sentiment analisis | Tedy Setiadi, S.T, M.T |
| Bab 10 sampai Bab 11 Penambahan materi interface | Dwi Normawati, S.T, M.Eng |
| Penambahan Materi Social Network Analysis | Sheraton Pawestri, S.Kom., M.Cs. |

---

<!-- Halaman 6 -->

### HALAMAN REVISI

Yang bertanda tangan di bawah ini:

Nama : Lisna Zahrotun, S.T., M.Cs.

NIPM : 19840911 200909 011 1058758

Jabatan : Koordinator Mata Kuliah Rekayasa dan Penambangan Data

Dengan ini menyatakan pelaksanaan Revisi Petunjuk Praktikum Rekayasa dan Penambangan Data untuk Program Studi Informatika telah dilaksanakan dengan penjelasan sebagai berikut:

| No |  |  | Keterangan Revisi | Tanggal Revisi |  | Nomor |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Modul |  |
| 1. |  |  | a. Penggantian semua studi kasus untuk setiap teknik data mining b. Penambahan materi praktikum text mining c. Penambahan materi CRM Data mining d. Penambahan 3 materi praktikum yaitu pengujian, text mining, pembuatan user interface menggunakan flash | 2018 | PP/018/VII/R 1 |  |  |
| 2. |  |  | a. Merevisi petunjuk praktikum ke template yang baru. b. Penambahan teori dan petunjuk praktikum pada Materi Interface. | 2019 | PP/018/VII/R 2 |  |  |
| 3. |  |  | a. Penambahan teori pada pembersihan data dan transformasi data b. Penambahan pengujian pada teknik klasifikasi, clustering dan association rule c. Penambahan teori identifikasi data d. Perubahan assemen untuk pretest, langkah praktikum dan postest | 2021 | PP/018/VII/R 3 |  |  |
| 4. |  |  | a. Perubahan ke template terbaru 2023 b. Penambahan materi sentiment analisis pada pertemuan 8 c. Penambahan studi kasus pada postest | 2023 | PP/018/VIII/R 4 |  |  |
|  | 5. |  | Penambahan Materi Social Network Analysis | September2025 | PP/018/IX/R5 |  |  |
| 6. | 6. |  | Penambahan Materi Identifikasi data pada pertemuan 1, Penambahan Materi Clustering DBScan dan AHC dan Penambahan Materi Prediksi menggunakan Regresi Linear | September 2026 | PP/018/IX/R6 |  |  |

Yogyakarta, 20 September 2026

Penyusun

Lisna Zahrotun, S.T, M.Cs NIPM. 19840911 200909 011 1058758

---

<!-- Halaman 7 -->

### HALAMAN PERNYATAAN

Yang bertanda tangan di bawah ini:

Nama : Murein Miksa Mardhia S.T., M.T.

NIPM : 19891019 201606 011 1236278

Jabatan : Kepala Laboratorium S1 Informatika

Menerangkan dengan sesungguhnya bahwa Petunjuk Praktikum ini telah direview dan akan digunakan untuk pelaksanaan praktikum di Semester Gasal Tahun Akademik 2026/2027 di Laboratorium Praktikum S1 Informatika, Program Studi Informatika, Fakultas Teknologi Industri, Universitas Ahmad Dahlan.

Mengetahui,

Yogyakarta, 20 September 2026

Kepala Laboratorium Praktikum

Ketua Program Studi

S1 Informatika

Murein Miksa Mardhia S.T., M.T. NIPM. 19891019 201606 011 1236278

Dr. Murinto, S.Si., M.Kom. NIPM. 19730710 200409 111 0951298

---

<!-- Halaman 8 -->

### VISI DAN MISI PRODI INFORMATIKA

### VISI

Menjadi program studi yang unggul dan inovatif dalam bidang rekayasa perangkat lunak dan sistem cerdas dengan dijiwai nilai-nilai Islam MISI

1. Mengimplementasikan nilai-nilai AIK pada semua aspek kegiatan. 2. Memajukan ilmu pengetahuan dan teknologi Rekayasa Perangkat Lunak dan Sistem cerdas melalui pendidikan, penelitian, dan pengabdian kepada masyarakat. 3. Mengembangkan kerjasama dalam pendidikan, penelitian, dan pengabdian kepada masyarakat di tingkat lokal, nasional, maupun internasional. 4. Menyelenggarakan tata kelola program studi yang unggul dan inovatif. 5. Berperan aktif dalam kegiatan yang menunjang profesi dosen.

---

<!-- Halaman 9 -->

### TATA TERTIB LABORATORIUM S1 INFORMATIKA

DOSEN/KOORDINATOR PRAKTIKUM 1. Dosen harus hadir saat praktikum minimal 15 menit di awal kegiatan praktikum untuk mengisi materi dan menandatangani presensi kehadiran praktikum. 2. Dosen membuat modul praktikum, soal seleksi asisten, pre-test, post-test, dan responsi dengan berkoordinasi dengan asisten dan pengampu mata praktikum. 3. Dosen berkoordinasi dengan koordinator asisten praktikum untuk evaluasi praktikum setiap minggu. 4. Dosen menandatangani surat kontrak asisten praktikum dan koordinator asisten praktikum. 5. Dosen yang tidak hadir pada slot praktikum tertentu tanpa pemberitahuan selama 2 minggu berturut-turut mendapat teguran dari Kepala Laboratorium, apabila masih berlanjut 2 minggu berikutnya maka Kepala Laboratorium berhak mengganti koordinator praktikum pada slot tersebut.

PRAKTIKAN 1. Praktikan harus hadir 15 menit sebelum kegiatan praktikum dimulai, dan dispensasi terlambat 15 menit dengan alasan yang jelas (kecuali asisten menentukan lain dan patokan jam adalah jam yang ada di Laboratorium, terlambat lebih dari 15 menit tidak boleh masuk praktikum & dianggap Inhal). 2. Praktikan yang tidak mengikuti praktikum dengan alasan apapun, wajib mengikuti INHAL, maksimal 4 kali praktikum dan jika lebih dari 4 kali maka praktikum dianggap GAGAL. 3. Praktikan yang akan mengikuti inhal diwajibkan mendaftarkan diri dan membayar administrasi inhal kepada laboran inhal paling lambat H-1 jadwal inhal. 4. Praktikan harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut:

a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki /

Perempuan) dan Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki /

Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 5. Praktikan tidak boleh makan dan minum selama kegiatan praktikum berlangsung, harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di dalam laboratorium (tidak boleh membuang sampah sembarangan baik kertas, potongan kertas, bungkus permen baik di lantai karpet maupun di dalam ruang CPU). 6. Praktikan dilarang meninggalkan kegiatan praktikum tanpa seizin Asisten atau Laboran. 7. Praktikan harus meletakkan sepatu dan tas pada rak/loker yang telah disediakan. 8. Selama praktikum dilarang NGENET/NGE-GAME, kecuali mata praktikum yang membutuhkan atau menggunakan fasilitas Internet. 9. Praktikan dilarang melepas kabel jaringan atau kabel power praktikum tanpa sepengetahuan laboran 10. Praktikan harus memiliki FILE Petunjuk praktikum dan digunakan pada saat praktikum dan harus siap sebelum praktikum berlangsung. 11. Praktikan dilarang melakukan kecurangan seperti mencontek atau menyalin pekerjaan praktikan yang lain saat praktikum berlangsung atau post-test yang menjadi tugas praktikum.

---

<!-- Halaman 10 -->

12. Praktikan dilarang mengubah setting software/hardware komputer baik menambah atau mengurangi tanpa permintaan asisten atau laboran dan melakukan sesuatu yang dapat merugikan laboratorium atau praktikum lain. 13. Asisten, Koordinator Praktikum, Kepala laboratorium dan Laboran mempunyai hak untuk menegur, memperingatkan bahkan meminta praktikan keluar ruang praktikum apabila dirasa anda mengganggu praktikan lain atau tidak melaksanakan kegiatan praktikum sebagaimana mestinya dan atau tidak mematuhi aturan lab yang berlaku. 14. Pelanggaran terhadap salah satu atau lebih dari aturan diatas maka Nilai praktikum pada pertemuan tersebut dianggap 0 (NOL) dengan status INHAL. 15. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 16. Sebelum pelaksanaan praktikum membaca surat pendek. 17. Praktikan saat memasuki lab wajib menggunakan kaos kaki. 18. Inhal yang diizinkan dapat diikuti oleh praktikan selama periode praktikum adalah maksimal 3

(tiga) kali. Silakan menggunakan kuota inhal apabila mendapat halangan untuk hadir saat praktikum seperti sakit, izin, atau delegasi lomba. 19. Bagi mahasiswa (asisten praktikum dan praktikan) yang terbukti melakukan pelanggaran akademik akan dikenai sanksi sesuai aturan Fakultas/Universitas yang berlaku, serta digagalkan dari tanggungjawab di matapraktikum yang sedang ditempuh.

ASISTEN PRAKTIKUM 1. Asisten harus hadir 15 Menit sebelum praktikum dimulai (konfirmasi ke koordinator bila mengalami keterlambatan atau berhalangan hadir). 2. Asisten yang tidak bisa hadir WAJIB mencari pengganti, dan melaporkan kepada Koordinator

Asisten. 3. Asisten harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut:

a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki /

Perempuan) dan Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki /

Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 4. Asisten harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di laboratorium, menegur atau mengingatkan jika ada praktikan yang tidak dapat menjaga kebersihan, ketertiban atau kesopanan. 5. Asisten harus dapat merapikan dan mengamankan presensi praktikum, Kartu Nilai serta tertib dalam memasukan/Input nilai secara Online/Offline. 6. Asisten mencatat dan merekap praktikan dengan status INHAL setiap minggu serta wajib mengumumkan mekanisme INHAL di awal pertemuan praktikum. 7. Asisten harus dapat bertindak secara profesional sebagai seorang asisten praktikum dan dapat menjadi teladan bagi praktikan. 8. Asisten harus dapat memberikan penjelasan/pemahaman yang dibutuhkan oleh praktikan berkenaan dengan materi praktikum yang diasisteni sehingga praktikan dapat melaksanakan dan mengerjakan tugas praktikum dengan baik dan jelas. 9. Asisten tidak diperkenankan mengobrol sendiri apalagi sampai membuat gaduh. 10. Asisten dimohon mengkoordinasikan untuk meminta praktikan agar mematikan komputer untuk jadwal terakhir dan sudah dilakukan penilaian terhadap hasil kerja praktikan.

---

<!-- Halaman 11 -->

11. Asisten wajib untuk mematikan LCD Projector dan komputer asisten/praktikan apabila tidak digunakan. 12. Asisten tidak diperkenankan menggunakan akses internet selain untuk kegiatan praktikum, seperti

Youtube/Game/Medsos/Streaming Film di komputer praktikan. 13. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 14. Sebelum pelaksanaan praktikum membaca surat pendek. 15. Praktikan saat memasuki lab wajib menggunakan kaos kaki. 16. Tim asisten sangat direkomendasikan untuk menyeragamkan aturan yang terkait dengan praktikum dalam slot tugasnya masing-masing sesuai dengan tata tertib yang diberlakukan dalam laboratorium. 17. Seluruh asisten praktikum dapat merekomendasikan pemberian reward dan/atau punishment ke sesama asisten praktikum dan/atau  praktikan kepada kepala laboratorium dengan melampirkan bukti pendukung yang relevan. 18. Bagi mahasiswa (asisten praktikum dan praktikan) yang terbukti melakukan pelanggaran akademik akan dikenai sanksi sesuai aturan Fakultas/Universitas yang berlaku, serta digagalkan dari tanggungjawab di matapraktikum yang sedang ditempuh.

LAIN-LAIN 1. Pada Saat Responsi Harus menggunakan Baju Kemeja untuk Laki-laki dan Perempuan untuk

Praktikan dan Asisten. 2. Ketidakhadiran praktikum dengan alasan apapun dianggap INHAL. 3. Pelaksanaan (waktu dan metode) INHAL sama seperti praktikum mingguan/reguler. 4. Izin praktikum mengikuti aturan izin SIMERU/KULIAH. 5. Yang tidak berkepentingan dengan praktikum dilarang mengganggu praktikan atau membuat keributan/kegaduhan. 6. Penggunaan lab diluar jam praktikum maksimal sampai pukul 18.15 dengan menunjukkan surat ijin dari Kepala Laboratorium Prodi Informatika.

Yogyakarta, 20 September 2026

Kepala Laboratorium Praktikum

S1 Informatika

Murein Miksa Mardhia S.T., M.T. NIPM. 19891019 201606 011 1236278

---

<!-- Halaman 12 -->

### DAFTAR ISI 
 
 
HAK CIPTA 
 ......................................................................................................................................1

KATA PENGANTAR ....................................................................................................................................2

DAFTAR PENYUSUN ..................................................................................................................................3

KONTRIBUSI PENULIS ...............................................................................................................................4

HALAMAN REVISI......................................................................................................................................5

VISI DAN MISI PRODI INFORMATIKA .......................................................................................................7

TATA TERTIB LABORATORIUM S1 INFORMATIKA ....................................................................................8

DAFTAR ISI ................................................................................................................................... 11

DAFTAR GAMBAR .................................................................................................................................. 12

DAFTAR TABEL  ................................................................................................................................... 13

SKENARIO PRAKTIKUM SECARA DARING .............................................................................................. 14

## PRAKTIKUM 1: 
IDENTIFIKASI DATA EDA ............................................................................................ 16

## PRAKTIKUM 2: 
SELEKSI DATA ............................................................................................................. 29

## PRAKTIKUM 3: 
TRANSFORMASI DATA ............................................................................................... 34

## PRAKTIKUM 4: 
IDENTIFIKASI DATA .................................................................................................... 42

## PRAKTIKUM 5: 
KLASIFIKASI ................................................................................................................ 50

## PRAKTIKUM 6: 
CLUSTERING K-MEANS, DBSCAN & AHC ................................................................... 61

## PRAKTIKUM 7: 
ASSOCIATION RULE ................................................................................................... 72

## PRAKTIKUM 8: 
TEXT MINING - PREPROCESING ................................................................................. 82

## PRAKTIKUM 9 : FORCASTING MOVING AVERAGE, LINEAR(Data Time Series) MAD, RMSE ................. 89

## PRAKTIKUM 10: SOCIAL NETWORK ANALYSIS ..................................................................................... 94

## PRAKTIKUM 11: INTERFACE ............................................................................................................... 112

## PRAKTIKUM 12: INTERFACE ............................................................................................................... 119

DAFTAR PUSTAKA ................................................................................................................................ 132

---

<!-- Halaman 13 -->

### DAFTAR GAMBAR

Gambar 1. 1. Model dari klasifikasi (Han & Kamber, 2001) 60 Gambar 1. 2. Contoh pohon keputusan 61 Gambar 1. 3. Proses Jinja 90

---

<!-- Halaman 14 -->

### DAFTAR TABEL

Tabel 4.1. Tipe Fitur data. 23 Tabel 4. 2. Data Siswa 25 Tabel 4. 3 Data Pelanggan 26 Tabel 4. 4. Data Pasien Kejadian Abortus Setelah Proses Pembersihan 27

---

<!-- Halaman 15 -->

### SKENARIO PRAKTIKUM SECARA DARING

Nama Mata Praktikum : Rekayasa dan Penambangan Data Jumlah Pertemuan : 11 kali pertemuan

### TABEL SKENARIO PRAKTIKUM LURING

| Pertemuan ke | Judul Materi | Waktu (Lama praktikum sampai pengumpulan posttest) | Skenario Praktikum dari pemberian preteset, posttest dan pengumpulannya serta mencantumkan metode yang digunakan misal video, whatsapp group, Google meet atau lainnya |
| --- | --- | --- | --- |
| 1 | Import data dan pembersihan data | 1 minggu | 1. Dilakukan sosialisai kegiatan praktikum dan pendataan bagi mahasiswa yang memiliki kendala jaringan untuk mendapatkan waktu khusus dalam pelaksanaan praktikum. 2. Penyampaian materi penganatar praktikum melalui video yang dibuat oleh dosen pengampu. 3. Penyampaian Materi melalui rekaman video yang dibuat oleh asisten praktikum dan link video diberikan dalam Google Classroom 4. Pretest diberikan sesuai jadwal praktikum melalui Google Classroom dan dikumpulkan paling lama 1 hari/ 24 jam dari praktikum dimulai. 5. Posttest diberikan pada saat praktikum melalui Google Classroom dan dikumpulkan kembali paling lama 3 hari melalui Google Classroom. 6. Praktikan yang tidak mengumpulkan pretest dan posttest sampai batas waktu tanpa |

---

<!-- Halaman 16 -->

|  |  |  | pemberitahuan akan dinyatakan inhal. |
| --- | --- | --- | --- |
| 2 | Seleksi Data | 1 minggu | 1. Penyampaian materi penganatar praktikum melalui video yang dibuat oleh dosen pengampu. 2. Penyampaian Materi melalui rekaman video yang dibuat oleh asisten praktikum dan link video diberikan dalam Google Classroom 3. Pretest diberikan sesuai jadwal praktikum melalui Google Classroom dan dikumpulkan paling lama 1 hari/ 24 jam dari praktikum dimulai. 4. Posttest diberikan pada saat praktikum melalui Google Classroom dan dikumpulkan kembali paling lama 3 hari melalui Google Classroom. 5. Praktikan yang tidak mengumpulkan pretest dan posttest sampai batas waktu tanpa pemberitahuan akan dinyatakan inhal. |
| 3 | Transformasi Data | 1 minggu |  |
| 4 | Identifikasi data | 1 minggu |  |
| 5 | KLASIFIKASI C4.5 dan K-NN | 1 minggu |  |
| 6 | CLUSTERING Fuzzy C Means _ & AHC | 1 minggu |  |
| 7 | ASSOCIATION RULE Apriori dan FP Growth | 1 minggu |  |
| 8 | Text Mining | 1 minggu |  |
| 9 | Forecasting | 1 minggu |  |
| 11 | Social Network Analysis | 1 Minggu |  |
| 10 | Interface | 1 minggu |  |
| 12 | Interface | 1 minggu |  |

---

<!-- Halaman 17 -->

## PRAKTIKUM 1:  IDENTIFIKASI DATA EDA

Pertemuan ke : 1 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL-03 | Mampu menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas. |
| --- | --- |
| CPMK-01 | Mahasiswa dapat melakukan proses dalam tahap data mining membedakan penambagan data dan bukan penambangan data serta mmeyebutkan teknikteknik penambangan data |

1.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan asesmen praktik dan posttest. 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menerapkan proses penambangan data dan bukan penambangan data |
| --- | --- | --- |
| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menerapkan penambangan data dalam berbagai disiplin ilmu |
| CPL-03 | CPMK-01 | Kemampuan mahasiswa dalam menyebutkan teknik-teknik penambangan data |

---

<!-- Halaman 18 -->

1.3. TEORI PENDUKUNG Identifikasi Data dan Exploratory Data Analysis (EDA)

Identifikasi data merupakan tahap paling awal dalam proses data mining, dilakukan sebelum data masuk ke tahap pembersihan (cleaning), seleksi, dan transformasi. Tahap ini juga dikenal dengan istilah Exploratory Data Analysis (EDA), yaitu proses mengenali karakteristik suatu dataset sebelum dianalisis lebih lanjut. Menurut Han & Kamber (2006), sebelum data diolah, seorang analis perlu memahami terlebih dahulu jenis objek data, atribut yang dimilikinya, ukuran statistik dasar, serta kualitas data tersebut. Tanpa tahap identifikasi ini, proses data mining berisiko menghasilkan kesimpulan yang keliru karena data yang digunakan belum diketahui kelengkapan dan kewajarannya.

Secara umum, EDA pada tahap identifikasi data bertujuan untuk menjawab beberapa pertanyaan mendasar berikut:

• Berapa jumlah baris (record) dan kolom (atribut) pada dataset?

• Apa tipe data dari masing-masing atribut (nominal, ordinal, interval, rasio)?

• Bagaimana sebaran/statistik dasar setiap atribut (rata-rata, median, standar deviasi, nilai minimum-maksimum)?

• Apakah ada data yang hilang (missing value)?

• Apakah ada data yang tidak wajar (anomali/outlier)?

Dataset terdiri atas objek data (data object), yaitu entitas yang direpresentasikan, misalnya mahasiswa, pasien, atau transaksi penjualan. Setiap objek data dijelaskan oleh atribut (attribute), yaitu bidang data yang mewakili karakteristik atau fitur dari objek tersebut. Istilah atribut, dimensi, fitur, dan variabel sering digunakan secara bergantian; bidang pembelajaran mesin cenderung menyebutnya fitur, sedangkan bidang statistik menyebutnya variabel.

### Tipe Data dalam Data Mining

Pemilihan teknik identifikasi, visualisasi, maupun ukuran statistik yang tepat sangat bergantung pada tipe data dari setiap atribut. Secara umum tipe data dibedakan menjadi dua kelompok besar, yaitu data kategorikal (kualitatif) dan data numerik (kuantitatif), sebagaimana dirangkum pada Tabel 1.1 berikut.

---

<!-- Halaman 19 -->

Tabel 1.1. Tipe Data dalam Data Mining

| Kolom 1 | Kolom 2 | Kolom 3 | Kolom 4 |
| --- | --- | --- | --- |
|  |  |  |  |
| Kelompok | Tipe Fitur | Penjelasan | Contoh |
|  |  |  |  |
| Kategorikal (kualitatif) | Nominal | Nilai berupa nama/label yang hanya berfungsi membedakan satu kategori dengan kategori lain, tanpa urutan (operator = , ≠). | Jurusan, jenis kelamin, kode pos, nomor induk mahasiswa |
|  | Ordinal | Nilai berupa kategori yang memiliki urutan/peringkat bermakna, namun jarak antar kategori tidak diketahui pasti (operator <, ≤, >, ≥). | Predikat kelulusan (memuaskan, sangat memuaskan, cumlaude), tingkat pendidikan |
| Numerik (kuantitatif) | Interval | Nilai numerik yang selisih antar nilainya bermakna, tetapi tidak memiliki titik nol mutlak (operator +, -). | Tanggal, suhu tubuh/ruangan (°C, °F) |
|  | Rasio | Nilai numerik yang memiliki titik nol mutlak sehingga selisih maupun rasio antar nilai bermakna (operator *, /). | Usia, tinggi badan, IPK, gaji, jumlah barang |

Kesalahan dalam mengenali tipe data akan berdampak pada tahap berikutnya. Sebagai contoh, menghitung rata-rata (mean) pada atribut nominal seperti kode pos secara matematis dapat dilakukan, tetapi hasilnya tidak memiliki makna apa pun. Sebaliknya, mengukur outlier pada atribut ordinal tidak dapat menggunakan pendekatan standar deviasi seperti pada data rasio, melainkan cukup dengan melihat proporsi/frekuensi tiap kategori.

---

<!-- Halaman 20 -->

### Statistik Deskriptif untuk Identifikasi Data

Setelah tipe data diketahui, langkah berikutnya adalah menghitung ukuran statistik dasar untuk memahami sebaran data numerik, di antaranya:

• Central tendency: mean (rata-rata), median (nilai tengah), dan modus (nilai yang paling sering muncul).

• Dispersion (sebaran): nilai minimum, maksimum, rentang (range), kuartil (Q1, Q2, Q3), dan standar deviasi.

• Jumlah data (count) dan jumlah nilai unik (unique), terutama untuk atribut kategorikal.

Pada praktikum ini, statistik deskriptif diperoleh secara otomatis menggunakan fungsi describe() dari library pandas.

### Identifikasi Missing Value

Missing value adalah kondisi ketika suatu atribut pada suatu objek data tidak memiliki nilai. Pada Python, data yang hilang umumnya direpresentasikan dengan NaN (Not a Number) atau None. Missing value dapat terjadi karena kesalahan input, kegagalan alat pengumpul data, maupun data yang memang sengaja tidak diisi oleh responden. Identifikasi missing value dilakukan sebelum data masuk ke tahap pembersihan data (data cleaning) pada bab berikutnya, sehingga mahasiswa dapat menentukan strategi penanganannya, misalnya dihapus (dropna) atau diisi dengan nilai tertentu (fillna, mean, don’t care method).

### Deteksi Outlier dan Anomali Data

Outlier adalah data yang nilainya menyimpang cukup jauh dari sebagian besar data lain dalam dataset, sehingga dicurigai bukan merepresentasikan pola data yang sebenarnya (misalnya akibat kesalahan input atau kejadian yang memang tidak biasa). Dua pendekatan yang paling umum digunakan untuk mendeteksi outlier pada data numerik (interval/rasio) adalah:

a. Metode Z-Score

Z-score mengukur seberapa jauh (dalam satuan standar deviasi) suatu nilai data terhadap rata-ratanya, dengan rumus:

Z = (x - μ) / σ dengan x adalah nilai data, μ adalah rata-rata (mean), dan σ adalah standar deviasi. Data umumnya dianggap sebagai outlier apabila nilai |Z| > 2 atau |Z| > 3, tergantung tingkat kehati- hatian yang diinginkan.

b. Metode IQR (Interquartile Range)

Metode ini menggunakan kuartil pertama (Q1) dan kuartil ketiga (Q3) untuk menentukan batas bawah dan batas atas data wajar:

• IQR = Q3 − Q1

---

<!-- Halaman 21 -->

• Batas bawah = Q1 − 1,5 × IQR

• Batas atas = Q3 + 1,5 × IQR

Data yang berada di luar rentang batas bawah dan batas atas tersebut dikategorikan sebagai outlier. Metode ini menjadi dasar visual dari diagram boxplot, di mana outlier ditampilkan sebagai titik-titik di luar “kumis” (whisker) boxplot.

Visualisasi Singkat untuk Tiap Tipe Data

Visualisasi bukan tujuan utama pada tahap identifikasi data, namun sangat membantu untuk memberikan gambaran awal (sekilas) mengenai sebaran maupun kewajaran suatu atribut sebelum dilakukan pembersihan data secara mendalam pada bab berikutnya. Pemilihan jenis grafik disesuaikan dengan tipe data pada Tabel 1.1, sebagaimana dicontohkan pada Gambar 1.1 sampai Gambar 1.4 berikut, yang dibuat menggunakan dataset contoh 40 mahasiswa (data_mahasiswa.csv).

Gambar 1.1. Contoh visualisasi data nominal (diagram batang frekuensi kategori Jurusan)

Data nominal (contoh: Jurusan) divisualisasikan dengan diagram batang (bar chart) berdasarkan frekuensi tiap kategori. Urutan batang tidak memiliki makna khusus karena kategori nominal tidak memiliki tingkatan.

---

<!-- Halaman 22 -->

Gambar 1.2. Contoh visualisasi data ordinal (diagram batang terurut Predikat Kelulusan)

Data ordinal (contoh: Predikat Kelulusan) juga divisualisasikan dengan diagram batang, namun kategori pada sumbu-x disusun sesuai urutan tingkatannya (Memuaskan → Sangat Memuaskan → Cumlaude), berbeda dengan data nominal yang urutannya bebas.

Gambar 1.3. Contoh visualisasi data interval (histogram Suhu Tubuh)

Data interval (contoh: suhu tubuh dalam °C) divisualisasikan dengan histogram untuk melihat bentuk sebaran datanya. Garis putus-putus menunjukkan nilai rata-rata sebagai acuan awal, salah satunya untuk melihat apakah ada nilai suhu yang tampak tidak wajar (anomali).

---

<!-- Halaman 23 -->

Gambar 1.4. Contoh visualisasi data rasio (boxplot Usia Mahasiswa)

Data rasio (contoh: usia mahasiswa) divisualisasikan dengan boxplot karena boxplot langsung menampilkan Q1, median, Q3, serta titik-titik di luar whisker sebagai indikasi outlier, sehingga sekaligus berfungsi sebagai alat bantu deteksi anomali sebagaimana dijelaskan pada sub-bab 1.3.5.

1.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer/Laptop.

2. Anaconda app (Jupyter Notebook).

3. Dataset (contoh: data_mahasiswa.csv).

4. Library Python: pandas, numpy, matplotlib.

1.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan |
| --- | --- | --- | --- |
| 1. | CPL-03 | CPMK-01 | 1. Jelaskan apa yang dimaksud dengan identifikasi data dan Exploratory Data Analysis (EDA)! |
| 2. | CPL-03 | CPMK-01 | 2. Sebutkan dan jelaskan empat tipe data (nominal, ordinal, interval, rasio) beserta masing-masing satu contohnya! |
| 3. | CPL-03 | CPMK-01 | 3. Jelaskan perbedaan missing value dan outlier pada suatu dataset! |
| 4. | CPL-03 | CPMK-01 | 4. Jelaskan cara kerja metode Z-score dan metode IQR dalam mendeteksi outlier! |

---

<!-- Halaman 24 -->

### 1.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL-03 | CPMK-01 | 1. Selesaikan langkah praktikum 1 – 11 | Hasil praktikum langkah 1 – 11 | 100 |

Ikuti langkah praktikum berikut ini:

Dataset yang digunakan pada praktikum ini adalah data_mahasiswa.csv, berisi 40 record data mahasiswa dengan atribut seperti pada Tabel 1.2 berikut. Dataset ini sengaja memuat beberapa missing value dan nilai tidak wajar (outlier) agar dapat dipraktikkan proses identifikasi sekaligus pembersihannya.

Tabel 1.2. Contoh Dataset Mahasiswa (data_mahasiswa.csv)

| Kolom 1 | Kolom 2 | Kolom 3 | Kolom 4 | Kolom 5 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Nama | Jurusan (Nominal) | Predikat Kelulusa _ n (Ordinal) | Suhu Tubuh C _ _ (Interval) | Usia Tahun _ (Rasio) |
|  |  |  |  |  |
| Mhs 01 _ | Informatika | Sangat Memuaskan | 36.4 | 24 |
| Mhs 04 _ | Teknik Elektro | Sangat Memuaskan | (kosong) | 22 |
| Mhs 10 _ | Sistem Informasi | Sangat Memuaskan | 36.7 | 41 (dicurigai outlier) |
| … | … | … | … | … |

Ikuti langkah praktikum berikut ini:

1. Membuka Anaconda Jupyter Notebook, kemudian mengimpor library yang akan digunakan.

import pandas as pd import numpy as np import matplotlib.pyplot as plt

---

<!-- Halaman 25 -->

Keterangan: pandas digunakan untuk mengolah data terstruktur, numpy untuk komputasi numerik (statistik, Z-score), dan matplotlib untuk visualisasi.

2. Mengimpor dataset data_mahasiswa.csv ke dalam DataFrame.

df = pd.read_csv('data_mahasiswa.csv') df.head()

Keterangan: menampilkan 5 baris pertama dataset untuk memastikan data telah terbaca dengan benar.

3. Mengidentifikasi struktur dan tipe data pada setiap atribut.

print('Jumlah baris & kolom:', df.shape) df.info()

Keterangan: df.shape menampilkan jumlah baris dan kolom, sedangkan df.info() menampilkan nama atribut, jumlah data non-null, dan tipe data (dtype) Python-nya (object, float64, dsb). Tipe dtype Python ini kemudian perlu dipetakan mahasiswa ke tipe data nominal/ordinal/interval/rasio sesuai Tabel 1.1.

4. Menampilkan statistik deskriptif untuk atribut numerik (interval/rasio).

df[['Suhu_Tubuh_C', 'Usia_Tahun']].describe()

Keterangan: menampilkan count, mean, std, min, kuartil (25%, 50%, 75%), dan max. Nilai max Usia_Tahun = 41 dan min = 17 patut dicurigai sebagai outlier karena jauh dari rentang usia mahasiswa pada umumnya (20–23 tahun).

5. Mengidentifikasi frekuensi kategori pada atribut nominal dan ordinal.

print(df['Jurusan'].value_counts()) print(df['Predikat_Kelulusan'].value_counts())

Keterangan: value_counts() menghitung jumlah kemunculan tiap kategori, digunakan sebagai dasar pembuatan Gambar 1.1 dan Gambar 1.2.

6. Mengidentifikasi missing value pada setiap atribut.

df.isnull().sum()

Keterangan: menampilkan jumlah data kosong (NaN) pada tiap kolom. Pada dataset contoh terdapat 2 missing value pada Suhu_Tubuh_C dan 2 missing value pada Usia_Tahun.

7. Mendeteksi outlier pada atribut rasio (Usia_Tahun) menggunakan metode Z-score.

---

<!-- Halaman 26 -->

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | mean usia = df['Usia Tahun'].mean() _ _ |  |
|  | std usia = df['Usia Tahun'].std() _ _ |  |
|  | df['zscore usia'] = (df['Usia Tahun'] - mean usia) / std usia _ _ _ _ |  |
|  |  |  |
|  | outlier zscore = df[df['zscore usia'].abs() > 2] _ _ |  |
|  | print(outlier zscore[['Nama', 'Usia Tahun', 'zscore usia']]) _ _ _ |  |
|  |  |  |

Keterangan: baris dengan |Z| > 2 ditampilkan sebagai data yang dicurigai outlier, misalnya mahasiswa dengan usia 41 tahun dan 17 tahun.

8. Mendeteksi outlier pada atribut rasio (Usia_Tahun) menggunakan metode IQR.

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | Q1 = df['Usia Tahun'].quantile(0.25) _ |  |
|  | Q3 = df['Usia Tahun'].quantile(0.75) _ |  |
|  | IQR = Q3 - Q1 |  |
|  | batas bawah = Q1 - 1.5 * IQR _ |  |
|  | batas atas = Q3 + 1.5 * IQR _ |  |
|  |  |  |
|  | outlier iqr = df[(df['Usia Tahun'] < batas bawah) \| (df['Usia Tahun'] > batas atas)] _ _ _ _ _ |  |
|  | print('Batas bawah - atas:', batas bawah, '-', batas atas) _ _ |  |
|  | print(outlier iqr[['Nama', 'Usia Tahun']]) _ _ |  |
|  |  |  |

Keterangan: hasil deteksi IQR dibandingkan dengan hasil Z-score pada langkah 7 untuk melihat konsistensi kedua metode.

9. Menangani missing value hasil identifikasi pada langkah 6 (cleaning).

Terdapat tiga strategi umum yang dapat dipilih sesuai kondisi atributnya: menghapus baris yang kosong (dropna), mengisi dengan nilai statistik seperti mean/median (fillna).

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | # Cek ulang baris mana saja yang mengandung missing value |  |
|  | print(df[df.isnull().any(axis=1)]) |  |
|  |  |  |
|  | # Dropna: menghapus baris yang memiliki missing value |  |
|  | df dropna = df.dropna() _ |  |
|  | print('Jumlah baris setelah dropna:', len(df dropna)) _ |  |
|  |  |  |
|  | # Fillna: mengisi missing value numerik dengan nilai mean kolomnya |  |
|  | df fillna = df.copy() _ |  |
|  | df fillna['Suhu Tubuh C'] = _ _ _ |  |
|  | df fillna['Suhu Tubuh C'].fillna(df fillna['Suhu Tubuh C'].mean()) _ _ _ _ _ _ |  |
|  | df fillna['Usia Tahun'] = _ _ |  |
|  | df fillna['Usia Tahun'].fillna(df fillna['Usia Tahun'].median()) _ _ _ _ |  |
|  | print(df fillna.isnull().sum()) _ |  |
|  |  |  |

---

<!-- Halaman 27 -->

Keterangan: dropna cocok bila jumlah data hilang sedikit dan data lain masih representative. fillna(mean/median) cocok agar jumlah baris tetap utuh untuk atribut numerik.

10. Menangani data outlier hasil deteksi pada langkah 7 dan 8 (cleaning).

Setelah outlier teridentifikasi, mahasiswa perlu memutuskan perlakuan terhadap data tersebut. Tiga pendekatan yang umum digunakan adalah: menghapus data outlier, melakukan capping (membatasi nilai ekstrem ke batas wajar hasil perhitungan IQR), atau menandai (flagging) data tersebut untuk ditinjau kembali kebenarannya sebelum dihapus/diubah.

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | # Menghapus baris yang terdeteksi outlier (metode IQR) |  |
|  | df no outlier = df[(df['Usia Tahun'] >= batas bawah) & (df['Usia Tahun'] <= _ _ _ _ _ |  |
|  | batas atas) \| (df['Usia Tahun'].isnull())] _ _ |  |
|  | print('Jumlah baris setelah outlier dihapus:', len(df no outlier)) _ _ |  |
|  |  |  |
|  | # Capping: membatasi nilai ekstrem ke batas bawah/atas IQR |  |
|  | df capping = df.copy() _ |  |
|  | df capping['Usia Tahun'] = df capping['Usia Tahun'].clip(lower=batas bawah, _ _ _ _ _ |  |
|  | upper=batas atas) _ |  |
|  | print(df capping.loc[[9, 30], ['Nama', 'Usia Tahun']]) _ _ |  |
|  |  |  |
|  | # Flagging: menandai baris outlier tanpa mengubah/menghapus nilainya |  |
|  | df['flag outlier usia'] = np.where( _ _ |  |
|  | (df['Usia Tahun'] < batas bawah) \| (df['Usia Tahun'] > batas atas), _ _ _ _ |  |
|  | 'Outlier', 'Wajar' |  |
|  | ) |  |
|  | print(df[['Nama', 'Usia Tahun', 'flag outlier usia']]) _ _ _ |  |
|  |  |  |

Keterangan: menghapus data cocok bila outlier dipastikan berasal dari kesalahan input. capping cocok agar data tidak hilang namun pengaruh nilai ekstrem berkurang. flagging cocok sebagai langkah awal agar outlier tidak langsung dihapus/diubah sebelum dikonfirmasi ke sumber data. Prinsip yang sama juga berlaku untuk atribut interval (Suhu_Tubuh_C) maupun atribut numerik lainnya.

11. Menyusun ringkasan hasil identifikasi dan pembersihan data.

| Kolom 1 | Kolom 2 | Kolom 3 |
| --- | --- | --- |
|  |  |  |
|  | ringkasan = { |  |
|  | 'Jumlah baris awal' : len(df), |  |
|  | 'Jumlah kolom' : df.shape[1], |  |
|  | 'Missing value (sebelum)' : df[['Suhu Tubuh C', _ _ |  |
|  | 'Usia Tahun']].isnull().sum().sum(), _ |  |
|  | 'Outlier terdeteksi (IQR)' : len(outlier iqr), _ |  |
|  | 'Jumlah baris setelah dropna': len(df dropna), _ |  |
|  | } |  |
|  | for k, v in ringkasan.items(): |  |
|  | print(f'{k:28s}: {v}') |  |
|  |  |  |

---

<!-- Halaman 28 -->

Keterangan: ringkasan ini menjadi bahan laporan mahasiswa sebelum data digunakan pada Bab 2 Pembersihan Data dan tahapan data mining berikutnya.

Berdasarkan hasil identifikasi dan pembersihan data pada langkah 1–11, mahasiswa diminta menuliskan ringkasan temuan yang memuat: jumlah baris dan kolom, tipe data tiap atribut, jumlah dan lokasi missing value beserta strategi penanganannya, serta daftar data yang terdeteksi sebagai outlier beserta metode deteksi dan perlakuan (hapus/capping/flagging) yang dipilih.

### 1.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL-03 | CPMK-01 | 1. Buka sebuah dataset Identifikasilah jumlah baris, jumlah kolom, dan tipe data (nominal/ordinal/interval/rasio) dari setiap atributnya! | 25 |
|  |  |  | 2. Dari dataset yang sama, tampilkan statistik deskriptif (describe()) dan identifikasi apakah terdapat missing value pada dataset tersebut! | 25 |
|  |  |  | 3. Lakukan deteksi outlier pada salah satu atribut numerik menggunakan metode Zscore dengan threshold \|Z\| > 2! | 25 |
|  |  |  | 4. Lakukan deteksi outlier pada atribut yang sama menggunakan metode IQR, bandingkan hasilnya dengan hasil pada nomor 3, kemudian lakukan penanganan (cleaning) terhadap outlier tersebut (pilih salah satu: hapus/capping/flagging) beserta alasannya! | 25 |

### 1.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 01-S01 | CPMK-5.9.1 | 20% |  |  |
| 2. | Praktik | CPL 01-S01 | CPMK-5.9.1 | 30% |  |  |
| 3. | Post-Test | CPL 01-S01 | CPMK-5.9.1 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 29 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 30 -->

## PRAKTIKUM 2: SELEKSI DATA

Pertemuan ke : 2 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 01-S01 | Mampu Menjunjung tinggi nilai kemanusiaan untuk menjalankan tugas berdasarkan agama, moral, etika, dan bernegara berdasarkan Pancasila dengan menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri maupun berkelompok dalam kehidupan bermasyarakat. |
| --- | --- |
| CPMK-5.9.1 | Mahasiswa mampu menjelaskan konsep dasar data mining |
| Sub-CPMK 5.9.1.1 | Mampu menjelaskan konsep data mining, data set, dan preprocesing data merepresentasikan data untuk menyelesaikan masalah yang digunakan dalam data mining |

2.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan asesmen praktik dan postes. 2.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 01S01 | CPMK5.9.1 | Kemampuan mahasiswa dalam memahami konsep data selection dan melakukan proses data selection pada studi kasus menggunakan phyton |
| --- | --- | --- |

Seleksi data menurut Han dan Kamber (2006) Data yang terdapat dalam database datawarehouse kemudian direduksi dengan berbagai teknik. Proses reduksi diperlukan untuk

---

<!-- Halaman 31 -->

mendapatkan hasil yang lebih akurat dan mengurangi waktu komputasi terutama untuk masalah dengan skala besar (large scale problem).

Beberapa cara seleksi, antara lain :

1. Sampling, adalah seleksi subset representative dari populasi data yang besar.

2. Denoising, adalah proses menghilangkan noise dari data yang akan ditransformasikan.

3. Feature extraction, adalah proses membuka spesifikasi data yang signifikan dalam konteks tertentu.

2.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 2.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | 1. Jelaska maksud dari seleksi data! 2. Sebtkan beberapa proses seleksi data! 3. jelaskan cara melakukan seleksi data melalui Jupiter notebook! | 30 30 40 |

### 2.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | Selesaikan langkah praktikum 1 – 6 | Hasil praktikum langkah 1 – 6 | 100 |

Ikuti langkah praktikum berikut ini:

1. Jika akan dilakukan analisis data mining menggunakan Data Alumni untuk mengetahui hubungan antara Tempat & tanggal lahir, Tahun masuk, Tahun lulus, Status pekerjaan,

Lama masa tunggu, Nilai TOEFL dan IPK. Maka lakukanlah analisis Data Alumni untuk kemudian dilakukan proses seleksi data.

### 2. Buka data set alumni dengan nama Data Alumni.xlxs

3. Perhatikan record-record pada tabel tersebut.

4. Lakukan proses seleksi data menggunakan Anaconda Jupyter Notebook.

---

<!-- Halaman 32 -->

### Seleksi data”sampling”

a. Menampilkan data pada kolom Nama dan TTL.

### Seleksi data“Feature extraction”

a. Mencari umur

Untuk mencari umur, kita bisa menggunakan kolom TTL/Tempat dan tanggal Lahir.

Dari kolom TTL, kita akan mengambil nilai tahun atau 4 karakter dari belakang.

Kemudian kita akan hitung dengan menggunkan rumus, Tahun sekrag dikurangi dengan tahun lahir.

- Mengambil 4 karakter terakhir dari kolom TTL, dan memasukkan ke dalam kolom

Tahun Lahir.

- Setelah tahun lahir didapatkan, langkah berikutnya adalah mencari tahun sekarang, kemudian mengurangi tahun sekarang dengan tahun lahir untuk mendapatkan umur.

b. Mencari Masa Studi

Untuk mencari masa studi yaitu didapatkan dari tahun lulus dikurangi dengan tahun masuk.

5. Untuk seleksi data denoising sama dengan sampling.

6. Sebutkan data-data yang diseleksi, mengapa dan berikan penjelasannya!

---

<!-- Halaman 33 -->

### 2.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | 1. Lakukanlah seleksi data pada setiap atribut menggunakan dataset siswa.xlsx. 2. Analisis dan berikan penjelasan hasil dari seleksi data pada no.1 ! 3. Lakukanlah seleksi data pada data set pasien.xlsx! 4. Analisis dan berikan penjelasan hasil dari seleksi data pada no.2 ! | 30 20 30 20 |

### 2.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 01-S01 | CPMK-5.9.1 | 20% |  |  |
| 2. | Praktik | CPL 01-S01 | CPMK-5.9.1 | 30% |  |  |
| 3. | Post-Test | CPL 01-S01 | CPMK-5.9.1 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 34 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 35 -->

## PRAKTIKUM 3: TRANSFORMASI DATA

Pertemuan ke : 3 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 01-S01 | Mampu Menjunjung tinggi nilai kemanusiaan untuk menjalankan tugas berdasarkan agama, moral, etika, dan bernegara berdasarkan Pancasila dengan menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri maupun berkelompok dalam kehidupan bermasyarakat. |
| --- | --- |
| CPMK-5.9.1 | Mahasiswa mampu menjelaskan konsep dasar data mining |
| Sub-CPMK 5.9.1.1 | Mampu menjelaskan konsep data mining, data set, dan preprocesing data merepresentasikan data untuk menyelesaikan masalah yang digunakan dalam data mining |

3.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan posttest. 3.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 01S01 | CPMK5.9.1 | Kemampuan mahasiswa dalam menerapkan konsep data transformation dan jenis data transformation yaitu proses centering, normalisasi, scaling dan transformasi menggunakan phyton |
| --- | --- | --- |

---

<!-- Halaman 36 -->

1. smoothing (binning, clustering dan regresi)

2. agregasi (summarize, menggunakaan dimensi yang lebih general (cube construction ))

3. generalisasi, misal menggunakan dimensi propinsi daripada kabupaten atau grouping

(hirarki konsep)

4. Normalisasi, mengelompokkan data sesuai skala tertentu, misal IPK.

5. Normalisasi min-max, standarisasi data dengan menempatkan data dalam range 0 sampai

1, nilai terkecil sebagai 0, dan nilai terbesar sebagai 1. nilai baru = ((nilai lama – nilai minimal) / (nilai maksimal – nilai minimal)) (range maksimal – range minimal) + range minimal. range minimal = 0, range maksimal = 1.

6. normalisasi z-index, nilai baru = (nilai lama – rata-rata)/standar deviasi

7. normalisasi skala desimal, nilai baru = nilai lama / 10 ^ x,

8. Centering, mengurangi setiap data dengan rata-rata dari setiap atribut yang ada.

9. Normalization, membagi setiap data yang di centering denga standar deviasi dari atribut bersangkutan.

10. Scalling, mengubah data sehingga berada dalam skala tertentu.

One-Hot encoding adalah proses di mana variabel kategori diubah menjadi bentuk yang dapat diberikan ke algoritme ML untuk melakukan pekerjaan yang lebih baik dalam prediksi. One Hot Encoding bisa dilakukan dengan 2 cara yaitu melalui Library Scikit-Learn atau dengan method Get Dummies dari pandas

3.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 3.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | 1. Jelaskan tahap data mining transformasi data! 2. Sebutkan cara-cara melakukan tranformasi data menggunakan Jupiter notebook! 3. Jelaskan cara kerja dari Transformasi data menggunakan metode one hot encoding! | 30 40 30 |

### 3.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

---

<!-- Halaman 37 -->

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | Selesaikan langkah praktikum 1 – 4 (a-g) | Hasil praktikum langkah 1 – 4(a-g) | 100 |

Ikuti langkah praktikum berikut ini:

1. Jika akan dilakukan analisi data mining menggunakan Data Alumni untuk mengetahi hubungan antara IPK, TOEFL, Waktu mendapatkan pekerjaan, Lama studi, Umur, Gaji.

Maka lakukanlah analisis Data Alumni untuk kemudian dilakukan proses transformasi data.

### 2. Buka data set alumni dengan nama Data Alumni.xlxs

3. Perhatikan record-record pada tabel tersebut

4. Lakukan proses transformasi data menggunakan Anaconda Jupyter Notebook.

a. IPK

Nilai IPK dikategorikan menjadi 3, seperti yang terlihat pada tabel dibawah ini:

- Merubah format data pada kolom IPK.

- Mengkategorikan IPK menjadi 3, seperti pada tabel b. TOEFL

Nilai Toefl dikategorikan menajdi 3, seperti yang terlihat pada tabel dibawah ini:

---

<!-- Halaman 38 -->

maka dapat di terapkan pada syntax seperti berikut ni :

c. Waktu mendapatkan pekerjaan

Nilai waktu tunggu mendapatkan pekerjaan dikategorikan menjadi 4, seperti yang terlihat pada tabel dibawah ini :

Maka dapat diterapkan seperti ini pada syntax:

d. Lama studi

Nilai lama studi dikategorikan menajdi 2, seperti yang terlihat pada tabel dibawah ini:

---

<!-- Halaman 39 -->

Maka dapat diterapkan seperti ini pada syntax:

e. Umur

Nilai umur dikategorikan menjadi 2, seperti yang terlihat pada tabel dibawah ini:

Maka dapat diterapkan pada syntax seperti berikut ini :

f. Gaji

Nilai gaji dikategorikan menjadi 2, seperti yang terlihat pada tabel dibawah ini :

---

<!-- Halaman 40 -->

Maka dapat diterpakan di dalam syntax seperti berikut :

### Transformasi menggunakan One-Hot Encoding.

### g. Mencari nilai dummies pada kolom status.

- function get_dummies pada library pandas untuk mencari nilai dummies pada

### kolom status.

- Menggunakan One Hot Encoding akan menambah kolom sesuai dengan status yang ada di kolom status. Nilai 1 menunjukan bahwa pada rows tersebut terdapat data status tersebut sedangkan nilai 0 menunjukan sebaliknya. Untuk contoh praktikum kali ini terdapat 5 data status yaitu (Freelance, Guru, Mahasiswa, Swasta Dan

Wiraswasta)

### 3.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | 1. Lakukan Transformasi data menggunakan metode normalisasi dan one hot encoding pada file mahasiswa.xlsx menggunakan python 2. Analisis hasil dari prose trasnformasi pada no.1! 3. Lakukan Transformasi data menggunakan metode normalisasi dan one hot encoding pada data pasien.xlsx menggunakan python _ 4. Analisis hasil dari prose trasnformasi pada no.3! | 30 20 30 20 |

---

<!-- Halaman 41 -->

### 3.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 01-S01 | CPL 01-S01 | 20% |  |  |
| 2. | Praktik | CPL 01-S01 | CPL 01-S01 | 30% |  |  |
| 3. | Post-Test | CPL 01-S01 | CPL 01-S01 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 42 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 43 -->

## PRAKTIKUM 4: IDENTIFIKASI DATA

Pertemuan ke : 4 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 01-S01 | Mampu Menjunjung tinggi nilai kemanusiaan untuk menjalankan tugas berdasarkan agama, moral, etika, dan bernegara berdasarkan Pancasila dengan menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri maupun berkelompok dalam kehidupan bermasyarakat. |
| --- | --- |
| CPMK-5.9.1 | Mahasiswa mampu menjelaskan konsep dasar data mining |
| Sub-CPMK 5.9.1.1 | Mampu menjelaskan konsep data mining, data set, dan preprocesing data merepresentasikan data untuk menyelesaikan masalah yang digunakan dalam data mining |

4.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan posttest. 4.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 01S01 | CPMK5.9.1 | Kemampuan mahasiswa dalam menerapkan proses data integration pada studi kasus menggunakan phyton |
| --- | --- | --- |

---

<!-- Halaman 44 -->

Atribut adalah bidang data, mewakili karakteristik atau fitur dari objek data. Atribut nominal, dimensi, fitur, dan variabel sering digunakan secara bergantian dalam literatur. Pada pembelajaran mesin cenderung menggunakan istilah fitur, sementara ahli statistik lebih memilih variable.

Tabel 4.1. Tipe Fitur data.

| Tipe fitur |  | Penjelasan | Contoh |
| --- | --- | --- | --- |
| Kategorikal (kualitatif) | Nominal | Nila fitur bertipe nominal memberikan nilai berupa nama, dengan nama inilah sebuah fitur membedakan dirinya pada vector yang satu dengan yang lain (=,≠) | Kode pos, nomer ktp, nomor induk mahasiswa, jenis kelamin |
|  | Ordinal | Nilai fitur bertipe ordinal mempunyai nilai berupa nama yang mempunyai arti informasi yang terurut (<,≤,>.≥) | Predikat kelulusan (cum laude, sangat memuaskan), suhu(dingin, normal, panas) |
| Numerik (kuantitatif) | Interval | Nilai fitur di mana perbedaan di antara dua nilai mempunyai makna yang berarti (+,-) | Tanggal, suhu(dalam Celcius, Farhenheit) |
|  | Rasio | Nilai fitur yang dimana perbedaan di antara dia nilai dan rasio dua nilai mepunyai makna yang berarti (*,/) | Umur, panjang, tinggi, rata-rata |

### Proximity Measures for Binary Attributes

Perbedaan dan kesamaan kesamaan untuk objek yang dijelaskan oleh atribut biner simetris atau asimetris. Ingat bahwa atribut biner hanya memiliki satu dari dua status: 0 dan 1, di mana 0 berarti atribut tersebut tidak ada, dan 1 berarti atributnya ada. Dengan atribut perokok yang menggambarkan pasien, misalnya, 1 menunjukkan bahwa pasien merokok, sedangkan 0 menunjukkan bahwa pasien tidak merokok. Proximity Measures for Ordinal Attributes

Nilai-nilai atribut ordinal memiliki urutan atau peringkat yang berarti tentang mereka, namun besarnya antara nilai-nilai berturut-turut tidak diketahui. Contohnya termasuk urutan kecil, sedang, besar untuk atribut ukuran. Atribut ordinal juga dapat diperoleh dari diskritisasi atribut numerik dengan membagi rentang nilai ke dalam sejumlah kategori. Kategori-kategori ini disusun dalam peringkat. Yaitu, rentang atribut numerik dapat dipetakan ke atribut ordinal f yang memiliki status Mf. Misalnya, kisaran suhu atribut skala-skala (dalam Celcius) dapat diatur ke dalam status

---

<!-- Halaman 45 -->

berikut: −30 hingga −10, −10 hingga 10, 10 hingga 30, masing-masing mewakili kategori suhu dingin, suhu sedang, dan suhu hangat

### Dissimilarity of Numeric Data

Dissimilarity of numeric Data merupakan ukuran jarak yang umumnya digunakan untuk menghitung perbedaan objek yang dijelaskan oleh atribut numerik. Beberapa diantaranya adalah penghitungan jarak  Euclidean, Manhattan, dan Minkowski.

### Cosine Similarity

Kesamaan cosine adalah ukuran kesamaan yang dapat digunakan untuk membandingkan dokumen atau, katakanlah, memberikan peringkat dokumen sehubungan dengan vektor kata permintaan yang diberikan. Biarkan x dan y menjadi dua vektor untuk perbandingan. Menggunakan ukuran cosinus sebagai berikut [2]

### RFM ( Recency, Frequency dan Monetery )

Mengungkapkan bahwa Salah satu metric yang cukup banyak digunakan oleh pemasar untuk mengsegmentasikan pelanggan adalah RFM ( Recency, Frequency , dan Monetery) Recency  menggambarkan waktu pembelian akhir dari  customer,  Frequency menggambarkan kedatangan  customer dan  Monetery menggambarkan jumlah uang yang dibelanjakan oleh customer (Aviliani 2011).

Rumus untuk melakukan analisis metode RFM.

𝑏𝑢𝑙𝑎𝑛 𝑝𝑒𝑟𝑡𝑎𝑚𝑎 𝑏𝑒𝑙𝑖 a. Recency adalah R = 𝑏𝑢𝑙𝑎𝑛 𝑡𝑒𝑟𝑎𝑘ℎ𝑖𝑟 𝑏𝑒𝑙𝑖 𝑙𝑎𝑚𝑎 𝑗𝑎𝑑𝑖 𝑝𝑒𝑙𝑎𝑛𝑔𝑔𝑎𝑛 b. Frequency adalah , F = 𝑗𝑢𝑚𝑙𝑎ℎ 𝑏𝑎𝑟𝑎𝑛𝑔 𝑙𝑎𝑚𝑎 𝑗𝑎𝑑𝑖 𝑝𝑒𝑙𝑎𝑛𝑔𝑔𝑎𝑛 c. Monetary adalah M = 𝑗𝑢𝑚𝑙𝑎ℎ 𝑢𝑎𝑛𝑔

4.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 4.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | 1. Jelaskan tentang dataset dan atribut! 2. Sebutkan tipe-tipe fitur yang ada pada data! 3. Jelaskan hal-hal dibawah ini: | 30 20 50 |

---

<!-- Halaman 46 -->

|  |  |  | a. Proximity Measures for Binary Attributes (10) b. Proximity Measures for Ordinal Attributes (10) c. Dissimilarity of Numeric Data (10) d. Cosine Similarity (10) e. RFM (10) |  |
| --- | --- | --- | --- | --- |

|  | Proximity Measures for Binary Attributes (10) |
| --- | --- |
| b. Proximity Measures for Ordinal Attributes (10) |  |
| c. Dissimilarity of Numeric Data (10) |  |
| d. Cosine Similarity (10) |  |
| e. RFM (10) |  |

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | Selesaikan langkah praktikum 1 – 6 | Hasil praktikum langkah 1 – 6 | 100 |

Ikuti langkah praktikum berikut ini:

1. Perhatikan data siswa pada Tabel 4.2

2. Lakukan analisis data dan transformasi menggunakan one encoding untuk atribut pekerjaan wali dan pend, serta cari usia ketika lulus agar dapat dilakukan proses asosiation rule mining!

Tabel 4. 2. Data Siswa

| Tgl Lahir | Pekerjaan Wali | Pend | Thn msk | lulus | UAS |
| --- | --- | --- | --- | --- | --- |
| 6-Apr-93 | Petani | SLTP | 2000 | 2008 | 18.3 |
| 9-Aug-94 | Petani | SD | 2001 | 2008 | 16.45 |
| 25-May-95 | Petani | SD | 2001 | 2008 | 23.2 |
| 26-Jun-95 | Petani | SD | 2001 | 2008 | 18.75 |
| 14-Sep-95 | Wiraswasta | SPG | 2002 | 2008 | 23.1 |
| 3-Oct-95 | Wiraswasta | SLTP | 2002 | 2008 | 21.85 |
| 27-Jan-95 | Petani | SD | 2002 | 2008 | 23.2 |
| 29-Oct-96 | Wiraswasta | SMA | 2002 | 2008 | 22.95 |
| 20-Apr-96 | Petani | SD | 2002 | 2008 | 23.15 |
| 28-Apr-96 | Wiraswasta | STM | 2002 | 2008 | 22.25 |
| 10-May-96 | Petani | SD | 2002 | 2008 | 25.35 |
| 23-Dec-94 | PNS | D III | 2002 | 2008 | 23.1 |
| 27-Jun-95 | Pedagang | SD | 2002 | 2008 | 23.35 |
| 25-Aug-95 | Wiraswasta | SD | 2002 | 2008 | 25.9 |
| 16-Apr-96 | Wiraswasta |  | 2002 | 2008 | 23.65 |
| 7-Nov-96 | ABRI | SLTA | 2002 | 2008 | 25.45 |
| 10-Dec-95 | Petani | SD | 2002 | 2008 | 20.75 |
| 3-Mar-95 | Petani |  | 2002 | 2008 | 24.1 |
| 20-Feb-96 | Wiraswasta | SLTP | 2002 | 2008 | 26.95 |
| 27-Jun-96 | Wiraswasta | SLTA | 2002 | 2008 | 27.2 |
| 27-Apr-96 | Wiraswasta | SLTP | 2002 | 2008 | 17.25 |

---

<!-- Halaman 47 -->

3. Buka data pelanggan

4. Lakukan Analisa data menggunakan metode RFM agar dapat dilakukan proses data mining yaitu teknik clustering

| NO | Nama | Alamat | Bulan | jumlah barang | Nama Barang | Jumlah | jenis Barang |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Dwi Lita | Yogyakarta | Mei 2015 | 1 | Sepatu flat laser krem 39 | 100000 | Sepatu |
| 2 | Indri Karina | Aceh | Mei 2015 | 1 | Sepatu flat laser krem 40 | 100000 | Sepatu |
| 3 | Mba Novana | Yogyakarta | Mei 2015 | 1 | Aimee top milo | 130000 | Baju |
| 4 | Azkaqezanaza | Banjarmasin Timur | Mei 2015 | 1 | Couple yar'i mom kid toscajersey | 160000 | Baju |
| 5 | Yulia Rere | Jakarta | Mei 2015 | 1 | Set hijab benhor biru | 125000 | Jilbab |
| 6 | Eka Tiana | Bogor | Mei 2015 | 1 | Set hijab fitri flower | 100000 | Jilbab |
| 7 | Eka Tiana | Bogor | Mei 2015 | 1 | Rak jibab ungu | 80000 | Rak jilbab |
| 8 | Dewy Felis Shoe | Semarang | Mei 2015 | 1 | Princess set biru | 100000 | Baju |
| 9 | Dewy Liza Gamis | Magelang | Mei 2015 | 1 | Couple mom kids marun | 160000 | Baju |
| 10 | Tya Shop | Yogyakarta | Mei 2015 | 1 | Fairy dress tosca | 95000 | Baju |
| 11 | Tya Shop | Yogyakarta | Mei 2015 | 1 | Helena dress dusty | 125000 | Baju |
| 12 | Endang Suparjiman | Surabaya | Mei 2015 | 1 | Blus jumbo kartika | 90000 | Baju |
| 13 | Endang Suparjiman | Surabaya | Mei 2015 | 1 | Blus jumbo parem | 90000 | Baju |
| 14 | Bunda Fatimah | Ambon | Mei 2015 | 1 | Syar'i agatha pink | 130000 | Baju |
| 15 | Lo Wahyu Pratiwi | Aceh | Mei 2015 | 1 | Kalea top abu | 90000 | Baju |
| 16 | Lo Wahyu Pratiwi | Aceh | Mei 2015 | 1 | Delia tunik 3 pcs x 95 | 285000 | Baju |
| 17 | Inne | Garut | juni 2015 | 1 | Mesin jahit mini 3 pcs x 210 | 630000 | Mesin jahit |
| 18 | Bunda Dian | Bandung | juni 2015 | 1 | HPO mokamula 5 pcs x 95 | 475000 | Dompet |
| 19 | Lenie Btpn | Bandung | juni 2015 | 1 | Ziggi cardi hitam | 100000 | Baju |
| 20 | Dwi Susilowati | Papua | juni 2015 | 1 | Babydoll set toska | 120000 | Baju |

Tabel 4. 3 Data Pelanggan

---

<!-- Halaman 48 -->

5. Buka data pasien seperti pada Tabel 4.3

Tabel 4. 4. Data Pasien Kejadian Abortus Setelah Proses Pembersihan

| No . | No. Register | Nama Pasien | Alamat | Usia Ibu | Usia Kehamila n | HB | Jarak | Riwayat |  | Gejala | Jenis Abortus | Tindakan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Penyakit | Abortus |  |  |  |
| 1 | 432514 | Ny. Neni | cimanggu RT 01/01 | 20 | 10 | > 11 gr% | > 2 th | tidak ada | tidak ada | pendarahan ringan | AB Iminens | Tidak Curret |
| 2 | 440068 | Ny. Ratini | cipari RT 05/03 | 33 | 5 | < 11 gr% | < 2 th | tidak ada | tidak ada | pendarahan,keramperu t | AB Incomplit | Curret |
| 3 | 432557 | Ny. Tarmi | cilopadang RT 07/05 | 32 | 12 | < 11 gr% | < 2 th | diabetes | tidak ada | pendarahan, lemas | AB Incomplit | Curret |
| 4 | 432812 | Ny. Ida | sadahayu RT 03/03 | 29 | 6 | > 11 gr% | >2 th | tidak ada | tidak ada | keram rahim | AB Complit | Tidak Curret |
| 5 | 432920 | Ny.Susilowat i | margasari RT 01/01 | 27 | 3 | < 11 gr% | < 2 th | asma | 1x | flek, tegang payudara | AB Insipien | Curret |
| 6 | 33311 | Ny. Ambar | panetasan RT 02/08 | 37 | 9 | < 11 gr% | < 2 th | diabetes | tidak ada | pendarahan banyak, nyeri perut | AB Insipien | Curret |
| 7 | 440392 | Ny. Ratna | segaralangu RT 05/02 | 26 | 2 | < 11 gr% | < 2 th | tbc | 2x | Perut kosong, kehamilan menghilang | Miss Abortion | Curret |
| 8 | 426672 | Ny. Venti | cikalong RT 03/07 | 24 | 4 | > 11 gr% | >2 th | toksoplasma | tidak ada | Infeksi, pendarahan | AB Iminens | Tidak Curret |
| 9 | 443308 | Ny.Suheni | sepatnunggal RT 04/01 | 34 | 15 | > 11 gr% | >2 th | hipertensi | tidak ada | pendarahan | AB Complit | Tidak Curret |
| 10 | 443306 | Ny. Ira | pahonjean RT 07/07 | 29 | 11 | < 11 gr% | < 2 th | asma | 1x | pendarahan, keram perut | AB Incomplit | Curret |

6. Lakukan analisis data (pembersihan data, seleksi data dan transformasi data) pada Tabel 4.3 agar dapat dilakukan proses data mining yaitu teknik klasifikasi

---

<!-- Halaman 49 -->

48 4.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK5.9.1 | Tugas ini merupakan awal dari satu rangkaian tugas akhir dikelas dan juga sebagai response praktikum data mining. 1. Carilah salah satu topk/ studi kasus data mining! 2. Carilah data set minimal 50 data dengan minimal 7 atribut lakukanlah import data dari data set tersebut! 3. Dari data set tersebut lakukanlah pembersihan data, seleksi data dan trasnformasi data dan analisis hasilnya! 4. Lakukan analisis dari data tersebut dengan metode apakah nantinya akan di proses dengan data mining! | 10 20 30 40 |

### 4.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 01-S01 | CPMK-5.9.1 | 20% |  |  |
| 2. | Praktik | CPL 01-S01 | CPMK-5.9.1 | 30% |  |  |
| 3. | Post-Test | CPL 01-S01 | CPMK-5.9.1 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 50 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 51 -->

## PRAKTIKUM 5: KLASIFIKASI

Pertemuan ke : 5 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05KU03 | Mempunyai kemampuan dalam mendefinisikan kebutuhan pengguna atau pasar terhadap kinerja (menganalisis, mengevaluasi dan mengembangkan) algoritma/metode berbasis komputer untuk mengambil keputusan secara tepat dalam konteks penyelesaian masalah di bidang Rekayasa Perangkat Lunak serta Data dan Sistem Cerdas maupun bidang lainnya, berdasarkan hasil analisis informasi dan data. |
| --- | --- |
| CPMK 5.9.2 | Mampu memahami, menerapkan dan menganalisis teknik klasifikasi dalam data mining untuk studi kasus tertentu |
| SubCPMK 5.9.2.1 | Mampu memahami, menerapkan dan menganalisis teknik klasifikasi dalam data mining untuk studi kasus tertentu |

5.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui asessmen Pretest, praktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi asessmen Pretest, praktik dan post test. 5.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05KU03 | CPMK 5.9.2 | Kemampuan mahasiswa meningkat dalam memahami konsep machine learning khususnya klasifikasi serta dapat berfikir logis yang diterapkan |
| --- | --- | --- |

---

<!-- Halaman 52 -->

|  |  | dengan cara menerapkan studi kasus dan meningkat dalam mengidentifikasi dan memecahkan masalah studi kasus klasifikasi data |
| --- | --- | --- |

1. Definisi

Teknik klasifikasi merupakan suatu pendekatan sistematis untuk membangun model klasifikasi dari suatu himpunan masukan data (Hermawati, 2013). Model dari klasifikasi ditampilkan dalam Gambar 7.

Menurut Jianwei Han, 2001, klasifikasi merupakan proses menemukan kumpulan pola atau fungsi -fungsi yang mendeskripsikan dan memisahkan kelas data satu dengan lainnya, untuk dapat digunakan untuk memprediksi data yang belum memiliki kelas data tertentu. Jadi secara singkatnya, klasifikasi adalah proses untuk membedakan / memisahkan kelas.

Gambar 7. 1. Model dari klasifikasi (Han & Kamber, 2001)

### 2. Pohon Keputusan (Decision Tree)

Salah satu teknik dalam klasifikasi adalah pohon keputusan. Beberapa teknik dalam klasifikasi pohon keputusan adalah : Hunt’s Algorithm (one of the earliest),

CART, ID3, C4.5 dan SLIQ, SPRINT. Decision Tree (Pohon Keputusan) adalah pohon dimana setiap cabangnya menunjukkan pilihan diantara sejumlah alternatif pilihan yang ada, dan setiap daunnya menunjukkan keputusan yang dipilih. Decision tree biasa digunakan untuk mendapatkan informasi untuk tujuan pengambilan sebuah keputusan.

---

<!-- Halaman 53 -->

Pohon atau tree adalah sebuah struktur data yng terdiri dari simpul (node) dan rusuk (edge). Simpul pada sebuah pohon dibedakan menjadi tiga yaitu, simpul akar

(root node) sebagai titik awal, simpul percabangan/internal (branch/internal node) sebagai perantara berhubungan dengan suatu pertanyaan atau pengujian dan simpul daun (leaf node) sebagai suatu akhir / kelas target. Contoh Pohon keputusan ditampilkan dalam Gambar 8.

Gambar 7. 2. Contoh pohon keputusan

Pemilihan atribut untuk menjadi rootnode atau internal node sebagai atribut test berdasarkan atas ukuran impurity dari masing–masing atribut. Ukuran–ukuran impurity yang umumnya digunakan adalah information gain, gain ratio dan gini index.

Atribut yang memiliki nilai impurity tertinggi akan dipilih sebagai atribut test.

Adapun pengujian yang digunakan pada proses klasifikasi yaitu menggunakan confusion matrix.

### Confusion matrix adalah suatu metode yang biasanya digunakan untuk melakukan

perhitungan akurasi pada konsep data mining. Rumus ini melakukan perhitungan dengan

4 keluaran, yaitu: recall, precision, acuraccy dan error rate.

● Recall adalah proporsi kasus positif yang diidentifikasi dengan benar.

Rumus dari recall = d/(c+d)

● Precision adalah proporsi kasus dengan hasil positif yang benar.

Rumus dari Precision = d/(b+d)

● Accuracy adalah perbandingan kasus yang diidentifikasi benar dengan jumlah semua kasus   Rumus dari accuracy= (a+c)/(a+b+c+d)

---

<!-- Halaman 54 -->

● - Error Rate adalah kasus yang diidentifikasi salah dengan sejumlah semua kasus

Rumus dari Error Rate = (b+c)/(a+b+c+d)

Keterangan:

a. Jika hasil prediksi negatif dan data sebenarnya negatif.

b. Jika hasil prediksi positif sedangkan nilai sebenarnya negatif.

c. Jika hasil prediksi negatif sedangkan nilai sebenarnya positif.

d. Jika hasil prediksi positif dan nilai sebenarnya positif.

5.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 5.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05KU03 | CPMK 5.9.2 | 1. Jelaskan apa itu Klasifikasi! 2. Gambarkan model dari klasifikasi? | 20 30 |
| 2. | CPL 05KU03 | CPMK 5.9.2 | 1. Jelaskan salah satu teknik dalam klasifikasi! 2. Sebutkan dan jelaskan pengujian yang digunakan pada klasifikasi! | 20 30 |

### 5.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05KU03 | CPMK 5.9.2 | Selesaikan langkah praktikum 1 – 4 | Hasil praktikum langkah 1 – 4 | 50 |
| 2. | CPL 05KU03 | CPMK 5.9.2 | Selesaikan proses klasifikasi langkah i-xviii | Hasil praktikum langkah i-xviii | 50 |

Ikuti langkah praktikum berikut ini:

1. Jika akan dilakukan analisis data mining menggunakan Data Alumni untuk mengetahui hubungan antara NIM, UMUR, IPK, MASA STUDI, LAMA TUNGGU, GAJI,

TOEFL, dan MASA TUNGGU. Maka lakukanlah analisis Data Alumni untuk kemudian dilakukan proses klasifikasi data

### 2. Buka data set siswa dengan nama Data Alumni.xlxs

3. Perhatikan record-record pada table tersebut

4. Lakukan proses klasifikasi data dengan langkah-langkah berikut :

---

<!-- Halaman 55 -->

i. Load library yang akan digunakan

Keterangan:

### - pandas merupakan data structure yang sering digunakan untuk data analysis

pada bahasa pemrograman python

### - openpyxl merupakan class library untuk membuka file excel kedalam python

### - IPython.display import Image merupakan class library untuk menampilkan

image atau gambar.

### - sklearn.preprocessing import imputer merupakan class library untuk

melengkapi nilai yang hilang (NaN).

### - sklearn import tree merupakan import class library untuk Decision Tree.

### - sklearn.metrics import confusion_matrix, accuracy_score, recall_score,

### precision_score, classification_report merupakan class library untuk Confusion

Matrix.

### - subprocess import check_call dignakan untuk menjalankan perintah dengan

argument ii. Mengatur nama file excel dan sheet yang digunakan.

Keterangan:

- wb adalah variable data alumni pelatihan phiton

- sheet_ranges adalah variable data alumni excel pdaa sheet 1

- df adalah dataframe pandas yg digunakan untuk menampung data alumni pada sheet 1 iii. Seleksi kolom dari dataframe yang akan dilakukan klasifikasi.

Keterangan :

- d = df[baris][[kolom]] merupakan seleksi baris dan kolom yang ingin ditampilkan

- d.columns merupakan penamaan header setiap kolom yang telah diseleksi

---

<!-- Halaman 56 -->

- d.dropna melakukan penghapusan baris pada data yang kosong dari dataframe.

- d merupakan show table d iv. dtypes Checking datatipe yang ada pada kolom

Jika telah sesuai berarti data telah siap untuk di lakukan klasifikasi.

v. Ubah index dataframe agar lebih memudahkan dalam melakukan klasifikasi

Syntax diatas merupakan reset index pada dataframe. Kemudian akan muncul data dengan index dimulai dari 0.

vi. Membuat class label klasifikasi untuk lama masa tunggu kerja.

Dengan menggunakan kolom lama tunggu, disini akan dibuat 3 class yaitu:

- Cepat untuk masa tunggu kerja kurang dari 1 bulan.

- Sedang untuk masa tunggu kerja lebih dari atau sama dengan 1 bulan.

- Lama untuk masa tunggu kerja lebih dari atau sama dengan 2 bulan.

Dari rule diatas, akan dibuat kolom baru untuk class label klasifikasi, seperti berikut vii. Menentukan kolom yang digunakan sebagai class target atau label.

Kolom LamaTunggu digunakan sebagai class label dan dimasukkan ke dalam variable y. Values digunakan untuk mengambil nilai dari kolom.

viii. Menentukan kolom apa saja yang digunakan sebagai fitur-fitur.

Kolom IPK, TOEFL, Masa Studi, Umur digunakan sebagai fitur untuk klasifikasi.

Fitur-fitur tersebut dimasukkan ke dalam variable features.

ix. Jika dalam fitur terdapat nilai yang hilang (NaN) dapat menggunakan fungsi

### imputer, fungsi ini akan mengganti nilai NaN dengan nilai rata-rata kolom.

---

<!-- Halaman 57 -->

fit_transform digunakan untuk mempelajari kamus dan mengembalikan nilai ke dalam matriks, kemudian fitur dimasukkan ke dalam variable X.

x. membagi data menjadi set pelatihan dan pengujian

### Keterangan:

| train test split | function yang akan digunakan untuk membagi data secara acak |
| --- | --- |

ke dalam pelatihan dan pengujian set.

| test size | parameter menentukan rasio set pengujian, yang kami gunakan untuk |
| --- | --- |

membagi 40% data menjadi set pengujian dan 60% untuk pelatihan.

xi. Melakukan pelatihan menggunakan Decision Tree Scikit Learn untuk membuat

### model klasifikasi.

Keterangan:

- tree.DecisionTreeClassifier merupakan fungsi sklearn yang digunakan untuk memanggil Decision Tree

- criterion fungsi untuk mengukur kualitas split. Kriteria yang didukung adalah

"gain" dan "entropy"

- fit digunakan untuk membuat model klasifikasi decision tree dari set pelatihan

(x_train, y_train) atau dari data fitur dan class label

- clf merupakan variable yang digunakan untuk menyimpan model klasifikasi.

- Predict digunakan untuk membuat prediksi pada data pengujian.

xii. Memvisualisasikan decision tree ke dalam graph.

Keterangan:

- Clf merupakan variable yang menyimpan model atau classifier

- Out_file untuk mengatur nama file keluaran

- Features_names untuk menyimpan nama kolom yang dijadikan sebagai fitur

- Filled untuk memberikan warna pada node

---

<!-- Halaman 58 -->

- Rounded untuk membuat sudut node membulat

- Special_character untuk karakter khusus untuk kompatibilitas PostScript.

xiii. Convert file .dot ke file PNG.

Melakukan konversi file dari .dot ke .png diperlukan suatu aplikasi yang bernama

Graphviz, yang berguna untuk memvisualisasikan graph. Kemudian install aplikasi

Graphviz sampai selesai. Setelah aplikasi Graphviz terinstall, langkah berikutnya adalah melakukan pengaturan path pada system operasi kita.

xiv. Melakukan konversi file dari .dot ke .png.

xv. Untuk Menampilkan graph tree yang sudah di convert ke dalam .png. Hasil:

### PENGUJIAN CONFUSION MATRIX

xvi. Visualisasi model confusion matrix.

Hasil:

---

<!-- Halaman 59 -->

xvii. Menghitung keakuratan dari model yang sudah dibuat dengan performance

### metrics seperti: accuracy, recall, dan precision.

Hasil:

xviii. Menghitung akurasi skor

5.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL-03 | CPMK-02 | Lakukan proses klasifikasi terhadap data siswa seperti pada langkah praktikum! | 80 |
| 2. | CPL-08 | CPMK-03 | Analisis hasil pengujian menurut sepemahaman anda! | 20 |

### 5.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05KU03 | CPMK 5.9.2 | 20% |  |  |
| 2. | Praktik | CPL 05KU03 | CPMK 5.9.2 | 30% |  |  |

---

<!-- Halaman 60 -->

| 3. | Post-Test | CPL 05KU03 | CPMK 5.9.2 | 50% |  |  |
| --- | --- | --- | --- | --- | --- | --- |

---

<!-- Halaman 61 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 62 -->

## PRAKTIKUM 6: CLUSTERING K-MEANS, DBSCAN & AHC

Pertemuan ke : 6 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 07P02 | Memiliki pengetahuan yang memadai terkait dengan cara kerja sistem komputer dan mampu merancang dan mengembangkan berbagai algoritma/metode untuk memecahkan masalah. |
| --- | --- |
| CPMK 5.9.3 | Mampu memahami, menerapkan dan menganalisis teknik clustering, assosiation rule dan hight utility item set dalam data mining untuk studi kasus tertentu. |
| SubCPMK 5.9.3.1 | Mampu memahami, menerapkan dan menganalisis teknik clustering, assosiation rule dan hight utility item set dalam data mining untuk studi kasus tertentu. |

6.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui asessmen Pretest, praktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui asessmen Pretest, praktik dan post test. 6.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 07-P02 | CPMK 5.9.3 | • Kemampuan mahasiswa meningkat dalam memahami pengertian data clustering, metode – metode clustering serta dapat berfikir logis yang diterapkan dengan cara |
| --- | --- | --- |

---

<!-- Halaman 63 -->

|  |  | menerapkan studi kasus dengan metode clustering menggunakan software python dan uji clustering • Kemampuan mahasiswa meningkat dalam mengidentifikasi dan memecahkan masalah studi kasus data clustering |
| --- | --- | --- |

6.3. TEORI PENDUKUNG Analisis kelompok (cluster analisis) adalah pekerjaan mengelompokkan data (objek) yang didasarkan hanya pada informasi yang ditemukan dalam data yang menggambarkan objek tersebut dan hubungan diantaranya (Tan, 2006 dalam buku Prasetyo, 2012). Tujuannya adalah agar objek-objek yang bergabung dalam sebuah kelompok merupakan objek-objek yang mirip (atau berhubungan) satu sama lain dan berbeda (atau tidak berhubungan) dengan objek dalam kelompok dan lebih besar perbedaannya diantara kelompok yang lain.

K-Means merupakan algoritma clustering yang berulang-ulang. Algoritma K-Means dimulai dengan pemilihan secara acak K, K disini merupakan banyaknya cluster yang ingin dibentuk. Kemudian tetapkan nilai-nilai K secara random, untuk sementara nilai tersebut menjadi pusat dari cluster atau biasa disebut dengan centroid, mean atau “means”. Hitung jarak setiap data yang ada terhadap masing-masing centroid menggunakan rumus Euclidian hingga ditemukan jarak yang paling dekat dari setiap data dengan centroid. Klasifikasikan setiap data berdasarkan kedekatannya dengan centroid.

Lakukan langkah tersebut hingga nilai centroid tidak berubah (stabil) (Pralita, 2010).

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) merupakan algoritma clustering yang mengelompokkan data berdasarkan kepadatan (density) titik-titik data, sehingga jumlah cluster tidak perlu ditentukan di awal seperti pada K-Means. DBSCAN menggunakan dua parameter utama, yaitu Epsilon (eps) sebagai radius pencarian tetangga suatu titik, dan MinPts (min_samples) sebagai jumlah minimum tetangga yang harus ada dalam radius eps agar suatu titik dianggap sebagai titik inti

(core point). Titik yang bukan core point maupun tetangga dari core point akan dianggap sebagai noise/outlier dan diberi label -1.

AHC (Agglomerative Hierarchical Clustering) merupakan algoritma clustering berbasis hirarki dengan pendekatan bottom-up. Pada awalnya setiap data dianggap sebagai satu cluster tersendiri, kemudian pada tiap iterasi dua cluster yang memiliki jarak paling dekat akan digabungkan, hingga terbentuk jumlah cluster yang diinginkan. Jarak antar cluster dapat dihitung menggunakan beberapa metode linkage, di antaranya single linkage, complete linkage, average linkage, dan ward linkage. Hasil penggabungan cluster pada AHC dapat divisualisasikan dalam bentuk dendrogram, yaitu diagram pohon yang menunjukkan urutan dan jarak penggabungan tiap cluster.

---

<!-- Halaman 64 -->

Terdapat beberapa pengujian yang di gunakan pada metode clustering untuk memastikan hasil dari pengolahan data tersebut, yaitu:

### 1. Silhouette

Silhouette berfungsi untuk menguji kualitas dari cluster yang dihasilkan. Metode ini merupakan metode validasi cluster yang menggabungkan metode cohesion dan Separation. Untuk menghitung nilai silhoutte coefisient diperlukan jarak antar dokumen dengan menggunakan rumus

EuclideanDistance. Setelah itu tahapan untuk menghitung nilai silhoutte coeffisien adalah sebagai berikut:

a. Untuk setiap objek i, hitung rata-rata jarak dari objek i dengan seluruh objek yang berada dalam satu cluster. Akan didapatkan nilai rata-rata yang disebut ai.

b. Untuk setiap objek i, hitung rata-rata jarak dari objek i dengan objek yang berada di cluster lainnya.

Dari semua jarak rata-rata tersebut ambil nilai yang paling kecil. Nilai ini disebut bi.

c. Setelah itu maka untuk objek i memiliki nilai silhoutte coefisien: Si= (bi – ai) / max(ai, bi)

Hasil perhitungan nilai silhoutte coeffisien dapat bervariasi antara -1 hingga 1. Hasil clustering dikatakan baik jikai nilai silhoutte coeffisien bernilai positif (ai< bi) dan ai mendekati 0, sehingga akan menghasilkan nilai silhoutte coeffisien yang maksimum yaitu 1 saat ai = 0. Maka dapat dikatakan, jika si = 1 berarti objek i sudah berada dalam cluster yang tepat. Jika nilai si = 0 maka objek i berada di antara dua cluster sehingga objek tersebut tidak jelas harus dimasukan ke dalam cluster A atau cluster

B. Akan tetapi, jika si = -1 artinya struktur cluster yang dihasilkan overlapping, sehingga objek i lebih tepat dimasukan ke dalam cluster yang lain.

Khusus untuk DBSCAN, titik yang berlabel -1 (noise/outlier) sebaiknya dikeluarkan terlebih dahulu sebelum perhitungan silhouette dilakukan, agar hasil pengujian tetap representatif.

### 2. Purity

Purity adalah sebagai evaluasi kinerja algoritma clustering. Purity akan menghasilkan persentase akurasi kinerja clustering. Cara kerja purity ini adalah mengambil nilai maksimal dari elemen cluster yang terbentuk dan kemudian nilai perwakilan cluster tersebut akan dijumlahkan dengan elemen cluster yang terbentuk dari cluster yang lain sebagai perwakilan setiap cluster, Setelah itu dibagi dengan jumlah seluruh elemen data.

6.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset

---

<!-- Halaman 65 -->

4. Library scikit-learn (sklearn.cluster: KMeans, DBSCAN, AgglomerativeClustering) untuk proses clustering.

6.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 07P02 | CPMK 5.9.3 | 1. Jelaskan pengertian clustering! 2. Jelaskan apa yang dimaksud dengan K-Means? 3. Jelaskan apa yang dimaksud dengan DBSCAN dan AHC (Agglomerative Hierarchical Clustering)! | 15 20 25 |
| 2. | CPL 07P02 | CPMK 5.9.3 | 1. Sebut dan jelaskan metode yang digunakan utuk pengolahan data pada metode clustering! | 40 |

### 6.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 07P02 | CPMK 5.9.3 | Selesaikan langkah praktikum 1 – 3 (K-Means, DBSCAN, dan AHC) | Hasil praktikum langkah 1 – 3 | 60 |
| 2. | CPL 07P02 | CPMK 5.9.3 | Tambahkan fungsi purity dan lakukan analisis dari clustering yang telah dihasilkan. | Hasil praktikum langkah 4 – 6 | 40 |

Ikuti langkah praktikum berikut ini:

Ikuti langkah praktikum berikut ini:

1. Jika akan dilakukan analisis data mining menggunakan data alumni untuk mengetahui hubungan antara 'Nim','Ipk','Umur','Masa Studi','Lama Tunggu','Gaji','Toefl'. Maka lakukanlah analisis data alumni untuk kemudian dilakukan proses clustering data.

2. Buka dataset siswa dengan nama Data Alumni.xlsx yang digunakan pada praktikum sebelumnya.

3. Lakukan proses clustering data menggunakan python.

a. Melakukan Import Library yang akan digunakan untuk clustering:

from sklearn.cluster import KMeans import matplotlib.pyplot as plt

Keterangan:

• from sklearn.cluster import KMeans merupakan import class library KMeans

• import matplotlib.pyplot as plt merupakan class library untuk ploting data kedalam graph

---

<!-- Halaman 66 -->

b. Seleksi kolom dari data frame yang akan dilakukan clustering:

dTable = df[['Masuk','Lulus','IPK','Masa Studi']] dTable.dtypes

• df[['Masuk','Lulus','IPK','Masa Studi']] merupakan kolom yang akan digunakan untuk proses clustering.

• Checking datatipe yang ada pada kolom. Jika tipe data sudah sesuai maka dapat di proses untuk ke tahap selanjutnya.

c. Ubah index dataframe agar lebih memudahkan dalam melakukan clustering:

dTable = dTable.reset_index(drop=True)

Keterangan: .reset_index(drop=True) merupakan reset index pada dataframe.

d. Ambil data IPK dan MASA STUDI untuk dilakukan cluster:

X = dTable[['IPK','Masa Studi']].values

Keterangan: .values merupakan konversi dataframe ke format matrix.

e. Proses clustering, clustering akan dilakukan pada data alumni dengan 2 jumlah feature diantaranya IPK dan MASA STUDI. Jumlah cluster yang ditentukan adalah 3. Dengan ploting graph 2 dimensi, dikarenakan menggunakan 2 jumlah feature. Perintah dapat dilihat sebagai berikut.

kmeans = KMeans(n_clusters=3) kmeans.fit(X) centroids = kmeans.cluster_centers_ labels = kmeans.labels_ colors = ['g.','r.','b.'] plt.figure(figsize=(15,10)) for i in range(len(X)): print('coordinate %s'%i, X[i], 'labels %s'%labels[i]) plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10) list_cluster = dTable[(dTable['IPK'] == X[i][0]) & (dTable['Masa Studi'] == X[i][1])].index.tolist() plt.text(X[i][0], X[i][1], '%s'%(list_cluster)) plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s=50, linewidths=5, zorder=10) plt.show()

Keterangan:

• kmeans = KMeans(n_clusters=3) merupakan penentuan jumlah Cluster (3)

• kmeans.fit(X) adalah data X dipresisikan pada algoritma kmeans

• centroids = kmeans.cluster_centers_ merupakan hasil titik tengah

• labels = kmeans.labels_ merupakan hasil labels

---

<!-- Halaman 67 -->

• colors = ['g.','r.','b.'] warna berdasarkan jumlah 3 cluster

• plt.figure(figsize=(15,10)) merupakan ukuran graph

• for i in range(len(X)): looping jumlah data

• print('coordinate %s'%i, X[i], 'labels %s'%labels[i]) print data

• plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10) ploting titik pada graph

• list_cluster = dTable[(dTable['IPK'] == X[i][0]) & (dTable['Masa Studi'] == X[i][1])].index.tolist() ambil index sesuai IPK dan MASA STUDI, kemudian masukan dalam list

• plt.text(X[i][0], X[i][1], '%s'%(list_cluster)) cetak list_cluster kedalam titik graph

• plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'x', s=50, linewidths=5, zorder=10) cetak titik tengan cluster pada graph

• plt.show() merupakan perintah show graph f. Proses clustering menggunakan DBSCAN. DBSCAN dilakukan pada data yang sama (IPK dan

MASA STUDI), tanpa perlu menentukan jumlah cluster di awal:

from sklearn.cluster import DBSCAN dbscan = DBSCAN(eps=0.5, min_samples=5) dbscan.fit(X) labels_dbscan = dbscan.labels_ plt.figure(figsize=(15,10)) plt.scatter(X[:,0], X[:,1], c=labels_dbscan) plt.title('Hasil Clustering DBSCAN') plt.show()

Keterangan:

• from sklearn.cluster import DBSCAN merupakan import class library DBSCAN

• DBSCAN(eps=0.5, min_samples=5) menentukan radius tetangga (eps) dan jumlah minimum tetangga (min_samples) agar suatu titik menjadi core point

• dbscan.fit(X) adalah data X diproses pada algoritma DBSCAN

• labels_dbscan = dbscan.labels_ merupakan hasil label cluster, dengan label -1 menandakan noise/outlier

• plt.scatter(X[:,0], X[:,1], c=labels_dbscan) ploting hasil cluster berdasarkan warna label g. Proses clustering menggunakan AHC (Agglomerative Hierarchical Clustering). Sebelum menentukan jumlah cluster, tampilkan terlebih dahulu dendrogram untuk melihat struktur hirarki data:

---

<!-- Halaman 68 -->

from scipy.cluster.hierarchy import dendrogram, linkage from sklearn.cluster import AgglomerativeClustering Z = linkage(X, method='ward') plt.figure(figsize=(15,10)) dendrogram(Z) plt.title('Dendrogram AHC') plt.show() agg = AgglomerativeClustering(n_clusters=3, linkage='ward') labels_ahc = agg.fit_predict(X) plt.figure(figsize=(15,10)) plt.scatter(X[:,0], X[:,1], c=labels_ahc) plt.title('Hasil Clustering AHC') plt.show()

Keterangan:

• from scipy.cluster.hierarchy import dendrogram, linkage merupakan import fungsi untuk membentuk dan menampilkan dendrogram

• linkage(X, method='ward') menghitung jarak penggabungan antar cluster menggunakan metode ward

• dendrogram(Z) menampilkan diagram pohon (dendrogram) hasil penggabungan cluster

• AgglomerativeClustering(n_clusters=3, linkage='ward') memotong dendrogram sehingga terbentuk 3 cluster akhir

• labels_ahc = agg.fit_predict(X) merupakan hasil label cluster dari AHC

### Fungsi untuk menjalankan pengujian silhouette dan purity

from __future__ import print_function from sklearn.metrics import silhouette_samples, silhouette_score import matplotlib.cm as cm import numpy as np print(__doc__) def silhoutte_test(X, range_n_clusters): for n_clusters in range_n_clusters: fig, (ax1, ax2) = plt.subplots(1, 2) fig.set_size_inches(18, 7) ax1.set_xlim([-0.1, 1]) ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

---

<!-- Halaman 69 -->

clusterer = KMeans(n_clusters=n_clusters, random_state=10) cluster_labels = clusterer.fit_predict(X) silhouette_avg = silhouette_score(X, cluster_labels) print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg) sample_silhouette_values = silhouette_samples(X, cluster_labels) y_lower = 10 for i in range(n_clusters): ith_cluster_silhouette_values = \ sample_silhouette_values[cluster_labels == i] ith_cluster_silhouette_values.sort() size_cluster_i = ith_cluster_silhouette_values.shape[0] y_upper = y_lower + size_cluster_i color = cm.nipy_spectral(float(i) / n_clusters)  # cm.spectral sudah dihapus di matplotlib terbaru ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7) ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i)) y_lower = y_upper + 10 ax1.set_title("The silhouette plot for the various clusters.") ax1.set_xlabel("The silhouette coefficient values") ax1.set_ylabel("Cluster label") ax1.axvline(x=silhouette_avg, color="red", linestyle="--") ax1.set_yticks([]) ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1]) colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters) ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7, c=colors) centers = clusterer.cluster_centers_ ax2.scatter(centers[:, 0], centers[:, 1], marker='o', c="white", alpha=1, s=200) for i, c in enumerate(centers): ax2.scatter(c[0], c[1], marker='%𝑑' % i, alpha=1, s=50) ax2.set_title("The visualization of the clustered data.") ax2.set_xlabel("Feature space for the 1st feature") ax2.set_ylabel("Feature space for the 2nd feature") plt.suptitle(("Silhouette analysis for KMeans clustering on sample data " "with n_clusters = %d" % n_clusters), fontsize=14, fontweight='bold') plt.show()

---

<!-- Halaman 70 -->

Rumus Silhouette

Range_n_cluster = [2,3,4,5,6,7,8] – adalah jumlah clusternya. Akan dilakukan test terhadap data alumni.xlsx dan percobaan menggunakan jumlah cluster = 2,3,4,5,6,7. Dari jumlah cluster tersebut akan dilihat nilai rule terbaik dan yang akan dijadikan cluster sebenarnya.

Fungsi silhoutte_test() di atas dicontohkan untuk KMeans, dan dapat digunakan dengan cara yang sama untuk menguji hasil clustering DBSCAN maupun AHC dengan mengganti clusterer sesuai algoritma yang diuji (khusus DBSCAN, keluarkan dahulu titik berlabel -1/noise sebelum pengujian).

Selanjutnya buka file python clasification untuk menerapkan rumus purity.

4. Lakukan langkah yang sama diatas, tambahkan fungsinya.

5. Tambahkan rumus purity dibawah ini

Rumus Purity import numpy as np def purity_score(cluster, classes): cluster = np.array(cluster) classes = np.array(classes) total = 0 for c in set(cluster): idx = np.where(cluster == c) total += np.max(np.bincount(classes[idx])) return total / len(cluster)

Def purity_score (cluster, classes): - yaitu fuction untuk menghitung nilai purity pada data test. Dan untuk menghitung nilai purity yang dipengaruhi oleh jumlah cluster dan class.

Classes - adalah nilai data training. Kemudian data ini akan di bandingkan dengan data test yang di dapatkan menggunakan function diatas. Hasil dari perbandingan ini yaitu jarak antara data training dan data test semakin kecil nilai accuratenya maka pengujian kemurniannya semakin bagus antara nilai training dan test sama. Fungsi purity_score ini dapat digunakan untuk mengevaluasi hasil clustering dari K-Means, DBSCAN, maupun AHC.

### 6.       Lakukan analisis hasil clustering pada no.3, meliputi hasil K-Means, DBSCAN, dan AHC.

### 6.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 71 -->

| 1. | CPL 07P02 | CPMK 5.9.3 | Diketahui akan dilakukan analisis data mining pada dataset Mahasiswa.csv untuk mengetahui clustering salah satu atribut dengan atribut lain maka gunakan langkah yang sama seperti pada saat praktikum (K-Means, DBSCAN, dan AHC), lakukanlah pengelompokan data dari dataset. NOTE: Jumlah cluster tidak boleh sama dengan contoh praktikum. | 75 |
| --- | --- | --- | --- | --- |
| 2. | CPL 07P02 | CPMK 5.9.3 | Analisis hasil pengujian menggunakan Silhouette dan Purity | 25 |

### 6.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 07-P02 | CPMK 5.9.3 | 20% |  |  |
| 2. | Praktik | CPL 07-P02 | CPMK 5.9.3 | 30% |  |  |
| 3. | Post-Test | CPL 07-P02 | CPMK 5.9.3 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 72 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 73 -->

## PRAKTIKUM 7: ASSOCIATION RULE

Pertemuan ke : 7 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 07P02 | Memiliki pengetahuan yang memadai terkait dengan cara kerja sistem komputer dan mampu merancang dan mengembangkan berbagai algoritma /metode untuk memecahkan masalah. |
| --- | --- |
| CPMK 5.9.3 | Mampu memahami, menerapkan dan menganalisis teknik clustering, assosiation rule dan hight utility item set dalam data mining untuk studi kasus tertentu |
| SubCPMK 5.9.3.1 | Mampu memahami, menerapkan dan menganalisis teknik clustering, assosiation rule dan hight utility item set dalam data mining untuk studi kasus tertentu |

7.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui asessmen Pretest, praktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui asessmen Pretet, praktik dan post test. 7.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 07P02 | CPMK 5.9.3 | ● Kemampuan mahasiswa dalam memahami pengertian association rule mining, memahami frequent item set, rule generation serta dapat berfikir logis yang diterapkan dalam representasi pengetahuan dan evaluasi pola dari studi kasus menggunakan association rule. |
| --- | --- | --- |

---

<!-- Halaman 74 -->

|  |  | ● Kemampuan mahasiswa meningkat dalam mengidentifikasidan memcahkan studi kasus association rule menggunakan software python |
| --- | --- | --- |

### 7.3. TEORI PENDUKUNG

Association Rule adalah teknik data mining yang berguna untuk menemukan suatu korelasi atau pola yang terpenting/menarik dari sekumpulan data besar (Margaret, 2003).

Motivasi awal Association Rule berasal dari keinginan untuk menganalisa data transaksi supermarket ditinjau dari perilaku pelanggan dalam membeli produk. Association Rule menjelaskan seberapa sering suatu produk dibeli secara bersamaan. Sebagai contoh: seorang pelanggan membeli sabun maka seberapa mungkin juga ia membeli pasta gigi (Kuswardani dkk, 2011)

Dengan pengetahuan tersebut, pemilik pasar swalayan orang dapat mengatur penempatan barangnya atau merancang kampanye pemasaran memakai kupon diskon untuk kombinasi barang tertentu. Penting tidaknya suatu aturan asosiatis dapat diketahui dengan dua parameter, support yaitu persentase kombinasi item tersebut. Dan confidence yaitu kuatnya hubungan antar item dalam aturan asosiatif. Penting tidaknya suatu aturan assosiatif dapat diketahui dengan dua parameter, support yaitu persentase kombinasi item tsb. Dalam database dan confidence yaitu kuatnya hubungan antar item dalam aturan assosiatif (Ernawati,2007).

Adapun pengujian yang digunakan pada proses association rule adalah menggunakan pengujian Lift Rasio.

Lift Ratio adalah parameter penting selain support dan confidence dalam association rule. Lift

Ratio mengukur seberapa penting rule yang telah terbentuk berdasarkan nilai support dan confidence. Lift Ratio merupakan nilai yang menunjukkan kevalidan proses transaksi dan memberikan informasi apakah benar produk A dibeli bersamaan dengan produk B. Lift

### /Improvement Ratio dapat dihitung dengan rumus:

7.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 7.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 75 -->

| 1. | CPL 07P02 | CPMK 5.9.3 | Jelaskan pengertian association rules! | 30 |
| --- | --- | --- | --- | --- |
| 2. | CPL 07P02 | CPMK 5.9.3 | 1. Jelaskan pengertian support dan confidence! 2. Jelaskan tentang pengujian lift ratio | 40 30 |

### 7.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 07P02 | CPMK 5.9.3 | Selesaikan langkah praktikum 1 – 9 | Hasil praktikum langkah 1 – 9 | 70 |
| 2. | CPL 07P02 | CPMK 5.9.3 | Selesaikan langkah praktikum 10 | Hasil praktikum langkah 10 | 30 |

Ikuti langkah praktikum berikut ini:

1. Jika akan dilakukan analisis data mining menggunakan data alumni untuk mengetahui

### hubungan antara fasilitas memadai, sdm berpengaruh, kerja sesuai jurusan dan

### kurikulum sesuai dengan dunia kerja. Maka lakukanlah analisis data alumni untuk

kemudian dilakukan proses Asosiasi/Apriori data.

2. Buka data set siswa dengan nama Data Alumni.xlxs

3. Lakukan proses clustering data menggunakan python.

4. Melakukan Import Library yang akan digunakan untuk clustering:

5. Load data excel yang akan dilakukan proses asosiasi:

Output:

---

<!-- Halaman 76 -->

6. Templating data yang dibutuhkan kedalam format tabel.

7. Kemudian import library untuk menyelesaikan algoritma apriori def subsets(arr):

""" Returns non empty subsets of arr""" return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)]) def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):

"""calculates the support for items in the itemSet and returns a subset of the itemSet each of whose elements satisfies the minimum support"""

_itemSet = set() localSet = defaultdict(int) for item in itemSet:

for transaction in transactionList:

---

<!-- Halaman 77 -->

if item.issubset(transaction):

freqSet[item] += 1 localSet[item] += 1 for item, count in localSet.items():

support = float(count)/len(transactionList) if support >= minSupport:

_itemSet.add(item) return _itemSet def joinSet(itemSet, length):

"""Join a set with itself and returns the n-element itemsets""" return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length]) def getItemSetTransactionList(data_iterator):

transactionList = list() itemSet = set() for record in data_iterator:

transaction = frozenset(record) transactionList.append(transaction) for item in transaction:

itemSet.add(frozenset([item]))              # Generate 1-itemSets return itemSet, transactionList def runApriori(data_iter, minSupport, minConfidence):

""" run the apriori algorithm. data_iter is a record iterator

Return both:

- items (tuple, support)

- rules ((pretuple, posttuple), confidence)

""" itemSet, transactionList = getItemSetTransactionList(data_iter)

---

<!-- Halaman 78 -->

freqSet = defaultdict(int) largeSet = dict()

# Global dictionary which stores (key=n-itemSets,value=support)

# which satisfy minSupport assocRules = dict()

# Dictionary which stores Association Rules oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet) currentLSet = oneCSet k = 2 while(currentLSet != set([])):

largeSet[k-1] = currentLSet currentLSet = joinSet(currentLSet, k) currentCSet = returnItemsWithMinSupport(currentLSet, transactionList, minSupport, freqSet) currentLSet = currentCSet k = k + 1 def getSupport(item):

"""local function which Returns the support of an item""" return float(freqSet[item])/len(transactionList) toRetItems = [] for key, value in largeSet.items():

toRetItems.extend([(tuple(item), getSupport(item)) for item in value])

---

<!-- Halaman 79 -->

toRetRules = [] for key, value in largeSet.items()[1:]:

for item in value:

_subsets = map(frozenset, [x for x in subsets(item)]) for element in _subsets:

remain = item.difference(element) if len(remain) > 0:

confidence = getSupport(item)/getSupport(element) if confidence >= minConfidence:

toRetRules.append(((tuple(element), tuple(remain)), confidence)) return toRetItems, toRetRules def printResults(items, rules):

"""prints the generated itemsets sorted by support and the confidence rules sorted by confidence""" dSupport = {} for item, support in sorted(items, key=lambda (item, support): support):

dSupport[item] = support print("item: %s , %.3f" % (str(item), support)) for rule, confidence in sorted(rules, key=lambda (rule, confidence): confidence):

pre, post = rule tempRule=() tempRule+=pre tempRule+=post supportAimplikasiB = getSupportAimplikasiB(tempRule, dSupport) lift = supportAimplikasiB/(dSupport[pre]*dSupport[post]) print("Rule: %s ==> %s : [confidence is %.3f, lift is %.3f]" % (str(pre), str(post), confidence, lift)) def getSupportAimplikasiB(A, B):

rule = list(A) dict_support = B

---

<!-- Halaman 80 -->

result = 0 for index_dict_support in dict_support:

list_index_dict_support = list(index_dict_support) check = [] for data_index in list_index_dict_support:

if data_index in rule and len(list_index_dict_support) >= len(rule):

check.append(True) else:

check.append(False) if(reduce(mul, check, 1)==True):

#             print(list_index_dict_support)

#             print(dict_support[index_dict_support]) result = dict_support[index_dict_support] return result def dataFromFile(fname):

"""Function which reads from the file and yields a generator""" file_iter = open(fname, 'rU') for line in file_iter:

line = line.strip().rstrip(',')                         # Remove trailing comma record = frozenset(line.split(',')) yield record

8. Lakukan konversi data kedalam format  yang siap untuk dilakukan asosiasi:

---

<!-- Halaman 81 -->

9. Panggil fungsi  runApriori dengan   parameter masukan variable list_data hasil dari konversi sebelumnya, minSupport = 0.1, minConfidence = 0.2. dapat dilihat sebagai berikut.

10. Lakukan analisis rule yang dihasilan pada langkah praktikum ini. 7.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 07P02 | CPMK 5.9.3 | Lakukan proses asosiasi dari dataset siswa dan uji hasil menggunakan lift ratio! | 70 |
| 2. | CPL 07P02 | CPMK 5.9.3 | Buatlah Analisis dari hasil pengujian! | 30 |

### 7.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 07-P02 | CPMK 5.9.3 | 20% |  |  |
| 2. | Praktik | CPL 07-P02 | CPMK 5.9.3 | 30% |  |  |
| 3. | Post-Test | CPL 07-P02 | CPMK 5.9.3 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 82 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 83 -->

## PRAKTIKUM 8: TEXT MINING - PREPROCESING

Pertemuan ke : 8 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.9.4 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining , sosial Network Analisis dan tern data mining saat ini. |
| SubCPMK 5.9.4.1 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining dan sosial Network Analisis |

8.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 8.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09KK02 | CPMK 5.9.4 | Kemampuan mahasiswa meningkat dalam mnerapkan data visualization, dan evaluasi pola pada studi kasusu menggunakan python |
| --- | --- | --- |

1. Preprocessing

Preprocessing merupakan tahapan awal dalam mengolah data input sebelum memasuki proses tahapan utama dari metode lantent semantic analysis (LSA)

---

<!-- Halaman 84 -->

Tahapan ini dilalukan agar data menjadi terstruktur. Menyeragamkan dan memudahkan dalam pembacaan serta proses LSA.

Adapun tahapan preprocessing pada umumnya adalah sebagai berikut:

### a. Tokenizing

Tahap tokenizing / parsing adalah tahap pemotongan string input berdasarkan tiap kata yang menyusunnya (Triawati, 2009). Selain itu, spasi digunakan untuk memisahkan antar kata tersebut. Contoh:

### b. Filtering

Tahap filtering adalah tahap mengambil kata - kata penting dari hasiltokenizing.

Proses filtering dapat menggunakan algoritma stoplist (membuang kata yang kurang penting) atau wordlist (menyimpan kata penting). Stoplist / stopword adalah kata-kata yang tidak deskriptif yang dapat dibuang dalam pendekatan bag-of-words. Contoh stopword adalah “yang”, “dan”, “di”, “dari” dan lain – lain. (Triawati, 2009). Contoh:

### c. Stemming

Stemming adalah proses mengubah kata berimbuhan menjadi kata dasar. Aturan- aturan bahasa diterapkan untuk menanggalkan imbuhan-imbuhan pada kata.

Contoh:

### 2. Tf-Idf

### Tf menyatakan jumlah berapa banyak keberadaan suatu term dalam satu dokumen

dan kemudian dilogaritmikan agar mengurangi besarnya bilangan, dimana logaritmik suatu bilangan akan mengurangi digit jumlah, misalnya 1000 dengan log

(1000) hanya menghasilkan angka tiga. Rumus Tf adalah sebagai berikut:

---

<!-- Halaman 85 -->

### Jadi jika suatu term terdapat dalam suatu dokumen sebanyak 5 kali maka diperoleh

bobot = 1 + log (5) =1.699. Tetapi jika term tidak terdapat dalam dokumen tersebut, bobotnya adalah nol.

| Inverse Document Frequency (Idf) |  |
| --- | --- |
| Terkadang suatu term muncul di hampir sebagian besar dokumen mengakibatkan |  |
| proses pencarian term unik terganggu. Idf berfungsi mengurangi bobot suatu term |  |
| jika kemunculannya banyak tersebar di seluruh koleksi dokumen kita. Rumusnya |  |
| adalah dengan inverse document frequency. Document frequency adalah seberapa |  |
| banyak suatu term muncul di seluruh document yang diselidiki. |  |
|  |  |
| Sehingga bobot akhir suatu term adalah dengan mengalikan keduanya yaitu tf x idf. |  |

8.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 4. Komputer. 5. Anaconda app 6. Dataset 8.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Jelaskan apa itu preprocessing data! 2. Sebut dan jelaskan tahapan preprocessing beserta contohnya! 3. Jelaskan pengertian dari: a. TF (10) b. IDF (10) c. TF-IDF (10) | 20 50 30 |

### 8.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |

---

<!-- Halaman 86 -->

| 1. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum 1 – 5 | Hasil praktikum langkah 1 – 5 | 100 |
| --- | --- | --- | --- | --- | --- |

Ikuti langkah praktikum berikut ini:

1. Buka file baru pada python, praktikum kali ini berbeda dengan sebelumnya. Jika sebelumnya kita inputkan file maka praktikum kali ini akan kita coba untuk menginpukan data secara manual.

Pertama kita buat kalimat terlebih dahulu yang akan di proses menggunakan preprocessing. Contoh kalimat =[ 'belajar preprocessing yang lebih sederhana ,'

'preprocessing data pada text mining  ']

2. Tokenisasi

-lakukan tokenisasi pada kalimat di atas dengan cara sebagai berikut:

from nltk.tokenize import word_tokenize

- From nltk.tokenize import word_tokenize yaitu library yang di gunakan untuk melakukan token atau memecah kalimat menjadi kata.

list_token = [] for reviews in kalimat:

word_token = word_tokenize(reviews) list_token.append(word_token) print (word_token)

- List_token = [] :untuk menampung setiap dokumen yang akan diolah

- Kemudian memecah kalimat menjadi kata dengan acuan spasi sebagai pemisahnya.

3. Filtersasi data_stopword = ["yg", "yang", "lah", "juga","adalah","pada",",",'.'] list_sentence = [] for reviews in list_token:

data_clean = []

---

<!-- Halaman 87 -->

for review in reviews:

if review not in data_stopword:

data_clean.append(review) print (data_clean) list_sentence.append(data_clean)

- Filter yaitu menghilangkan kata hubung yang terdapat pada kalimat.

- Data_stopword[] : yaitu database untuk kata hubung yang akan di hilangkan.

- List_sentence[] :untuk menampung array filter/stopword

4. Stemming

Library yang digunakan untuk stemming yaitu Sastrawi, sebelum menggunakan sastrawi pada jupyter sastrawi tharus di install terlebih dahulu, cara:

- Buka jendela anaconda prompt baru.

- Ketik (dengan syarat koputer harus terhubung dengan jaringan)

- Setelah berhasil lalu ketiklah library stemmer sibawah ini:

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory factory = StemmerFactory() stemmer = factory.create_stemmer() list_stem = [] for reviews in list_token:

data_clean = [] for review in reviews:

if review not in data_stopword:

data_clean.append(stemmer.stem(review)) print (data_clean) list_stem.append(data_clean)

- List_stem [] : untuk menampung array stemming

- Kemudian dilakukan pengecekan pada setiap kata, jika terdapat kata berimbuhan maka akan diproses untuk menghilangkan kata berimbuhan tersebut.

---

<!-- Halaman 88 -->

- Maka kata dalalm kalimat tersebut sudah menjadi kata dasar

5. Tf-Idf

- Tf-idf dilakukan untuk menghitung nilai bobot setiap kata dalam kalimat.

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

- from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer :

adalah library yang digunkan untuk menghitung bobot kata.

CV = CountVectorizer() term_fit=CV.fit(data_clean) print (len(term_fit.vocabulary_))

- untuk menghitung kata yang sudah di preprocessing, dan jika terdapat kata yang sama makan akan di hitung menjadi 1.

print (term_fit.vocabulary_)

- term_fit.vocabulary_: yaitu untuk memunculkan kata dasar hasil dari pengolahan preprocessing.

term_frekuency = term_fit.transform(kalimat) print (term_frekuency) term = term_fit.transform(data_clean) tfidf_transformer = TfidfTransformer().fit(term) #untuk menampung sumua kata tfidf = tfidf_transformer.transform(term_frekuency) #menampung semua tapi hanya ingiin menampilkan term frekuensi print (tfidf)

- term_frekuency : untuk menghitung kata yang sering muncul

- tfidf_transformer : untuk merubah kata menjadi angka berdasarkan bobot kata dalam kalimat

- tfidf: menghitung bobot kata berdasarkan kemunculan kata tersebut dalam kalimat.

### 8.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 89 -->

| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. D1: Teknik Informatika merupakan bidang ilmu yang mempelajari bagaimana menggunakan teknologi komputer secara optimal guna menangani masalah transformasi atau pengolahan data dengan proses logika. D2: Selama kuliah kamu akan banyak mengkaji pemrograman dan komputasi. Tentunya kamu akan dibekali dengan keterampilan merancang perangkat lunak. - Jika diketahui akan dilakukan analisis data mining pada dataset tersebut, maka gunakan langkah yang sama seperti pada saat praktikum, lakukanlah preprocessing data dari dataset. 2. Dengan menggunakan dataset pada nomor 1, hitunglah nilai bobot menggunakan Microsoft Excel! | 50 50 |
| --- | --- | --- | --- | --- |

|  | Teknik Informatika merupakan bidang ilmu |
| --- | --- |
| yang mempelajari bagaimana menggunakan |  |
| teknologi komputer secara optimal guna |  |
| menangani masalah transformasi atau pengolahan |  |
| data dengan proses logika. |  |

|  | Selama kuliah kamu akan banyak mengkaji |
| --- | --- |
| pemrograman dan komputasi. Tentunya kamu |  |
| akan dibekali dengan keterampilan merancang |  |
| perangkat lunak. |  |

### 8.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.9.4 | 20% |  |  |
| 2. | Praktik | CPL 09KK02 | CPMK 5.9.4 | 30% |  |  |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.9.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 90 -->

## PRAKTIKUM 9 : FORCASTING MOVING AVERAGE, LINEAR(Data

### Time Series) MAD, RMSE

Pertemuan ke : 9 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.9.4 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining , sosial Network Analisis dan tern data mining saat ini. |
| SubCPMK 5.9.4.1 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining dan sosial Network Analisis |

9.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui asessmen Pretest, praktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui asessmen Pretet, praktik dan post test. 9.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09KK02 | CPMK 5.9.4 | ● Kemampuan mahasiswa dalam memahami pengertian dan konsep forecasting dalam datamining serta mampu menerapkan salah satu algoritma forecasting dalam suatu studi kasus |
| --- | --- | --- |

---

<!-- Halaman 91 -->

|  |  | ● Kemampuan mahasiswa meningkat dalam mengidentifikasidan memcahkan studi kasus forecasting menggunakan software python |
| --- | --- | --- |

A. Forecasting

Forecasting dapat diartikan sebagai suatu proses untuk memperkirakan atau memprediksikan nilai pada masa depan menggunakan data historis - data yang memiliki informasi tentang rentang waktu. Metode ini sering diaplikasikan pada beberapa bidang, seperti keuangan, logistik, pertanian, hingga peramalan harga suatu komoditas. Untuk membangun model forecasting, biasa dilakukan dengan pendekatan statistikal (exponential smoothing, ARIMA), machine learning (SVM, Linear Regression, dsb), dan deep learning (RNN, GRU). Kemudian beberapa kata kunci yang biasanya lekat dengan forecasting adalah sebagai berikut:

a. Time series: Data berasal dari runtutan waktu yang tersusun rapi dengan interval yang seragam. b. Forecast origin: Titik waktu terakhir pada data historis yang digunakan untuk forecasting. c. Forecast horizon: Titik waktu masa depan yang ingin diketahui.

B. Metriks Evaluasi Forcasting

Untuk mengukur kinerja model forecasting dapat dilakukan dengan beberapa metode, misalnya MAE, MAD, MSE, dan RMSE.

a. MAD - Mean Absolute Deviation

Metriks ini mengukur seberapa jauh data hasil peramalan menyimpang dari titik data sebenarnya menggunakan nilai absolut rata-rata. Rumus:

∑ |𝑥𝑖−𝑥| 𝑛

𝑀𝐴𝐷=

Keterangan:

1. n adalah banyak data

2. 𝑥𝑖 adalah data ke-i

3. 𝑥 adalah rata-rata data b. MSE - Mean Squared Error

Metriks ini menghitung rata-rata dari selisih kuadrat antara nilai aktual dan nilai prediksi. Rumus:

𝑛

𝑀𝑆𝐸= 1

(𝑦𝑖−𝑦̂𝑖)2 𝑛∑ 𝑖=1

Keterangan:

● n adalah banyak data ● 𝑦𝑖 adalah nilai aktual untuk titik data ke-i ● 𝑦̂𝑖 adalah nilai yang diprediksi untuk titik data ke-i 9.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer.

---

<!-- Halaman 92 -->

2. Anaconda app 3. Dataset 9.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Ketika kamu memiliki data historis dan ingin meramalkan jumlah penjualan di masa depan, metode komputasi apa yang paling tepat untuk dilakukan? Jelaskan alasannya! | 50 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | 2. Setelah kamu berhasil membangun metode komputasi tersebut, bagaimana kamu akan menguji dan menginterpretasikan hasil yang telah kamu dapat? | 50 |

### 9.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum 1 – 4 | Hasil praktikum langkah 1 – 4 | 70 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum 1-8 pada bagian testing | Hail langkah praktikum 1-8 | 30 |

Ikuti langkah praktikum berikut ini:

1. Pada praktikum ini, unduh dan gunakan data historis berikut https://www.kaggle.com/datasets/tevecsystems/retail-sales-forecasting 2. Buka dan unduh kode berikut https://www.kaggle.com/code/yogaarifin/lp-9- forecasting-praktikan 3. Kode yang diberikan masih rumpang, ikuti petunjuk berikut:

a. Ubah variabel new_columns_new menjadi:

new_columns_name = {

"data": "date",

"venda": "sales",

"estoque": "stock",

"preco": "price"

} b. Ubah kode train_size agar membagi data menjadi 8:2 train_size = int(len(model_df) * 0.8) c. Isi ukuran window dengan nilai 7 window = 7 d. Isi variabel rmse rmse = np.sqrt(mse) e. Isi variabel model model = LinearRegression() 4. Jalankan semua kodenya, lalu lakukan analisis terhadap hasil yang didapatkan!

---

<!-- Halaman 93 -->

### 9.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Lakukan pemodelan dengan moving average menggunakan a. Ukuran window 2 dan 5 b. Pembagian 7:3 untuk data latih banding data tes Analisis hasilnya! Jelaskan pengaturan window mana yang lebih baik! 2. Lakukan uji coba terhadap salah satu metode dengan memanfaatkan library yang ada di https://scikitlearn.org/stable/api/index.html untuk melakukan forecasting! | 70 30 |

### 9.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.9.4 | 20% |  |  |
| 2. | Praktik | CPL 09KK02 | CPMK 5.9.4 | 30% |  |  |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.9.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 94 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 95 -->

## PRAKTIKUM 10: 
SOCIAL NETWORK ANALYSIS

Pertemuan ke : 10 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.9.4 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining , sosial Network Analisis dan tern data mining saat ini. |
| SubCPMK 5.9.4.1 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining dan sosial Network Analisis |

10.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area informatika terkait matematika dasar dan ilmu computer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui asessmen Pretest, praktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui asessmen Pretet, praktik dan post test. 10.2. DESKRIPSI CAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09KK02 | CPMK 5.9.4 | ● Kemampuan mahasiswa dalam memahami pengertian dan konsep forecasting dalam datamining serta mampu menerapkan salah satu algoritma forecasting dalam suatu studi kasus |
| --- | --- | --- |

---

<!-- Halaman 96 -->

|  |  | ● Kemampuan mahasiswa meningkat dalam mengidentifikasidan memcahkan studi kasus forecasting menggunakan software python |
| --- | --- | --- |

### 10.3. TEORI PENDUKUNG

### A. Definisi Social Network Analysis (SNA)

Dalam beberapa tahun terakhir, kemunculan dan perkembangan pesat media sosial seperti Facebook, Twitter (yang sekarang telah berubah menjadi ‘X’), Instagram, dan Tiktok telah merubah cara manusia untuk saling berinteraksi dan berkomunikasi. Media sosial tidak hanya memungkinkan individu untuk terhubung secara instan dengan orang lain di seluruh dunia, tetapi juga menciptakan jaringan hubungan yang kompleks dan dinamis. Seseorang bisa menghabiskan berjam-jam waktu mereka untuk bermedia sosial. Berbagai macam kegiatan bisa dilakukan di media sosial seperti mengunggah kegiatan sehari-hari, mendapatkan reaksi atas unggahan tersebut, berkomentar pada akun seseorang, dan sebagainya. Pengaruh besar media sosial ini memunculkan metode analisis khusus untuk menganalisis media sosial, salah satunya adalah Social Network Analysis (SNA).

Social Network Analysis (SNA) adalah metode analisis yang digunakan untuk mempelajari struktur dan pola interaksi di antara individu, organisasi, atau entitas lainnya dalam suatu jaringan sosial dengan memanfaatkan teori graf. SNA menggambarkan kata percakapan dalam media sosial sebagai node/vertex (simpul) dan hubungan antar kata tersebut adalah edge (sisi). Bisa juga node adalah individu dan edge adalah hubungan antar individu tersebut. SNA muncul sebagai pendekatan untuk memahami pola interaksi dan struktur jaringan yang terbentuk di platform-platform media sosial ini. SNA dapat memetakan dan menganalisis hubungan sosial dan memungkinkan peneliti untuk mengidentifikasi pengaruh, interaksi, dan penyebaran informasi dalam lingkup yang besar. Dengan pertumbuhan media sosial yang pesat, penerapan teori SNA semakin penting untuk mengungkap bagaimana jaringan digital ini membentuk perilaku, opini, dan bahkan dinamika sosial secara keseluruhan.

Pentingnya Social Network Analysis (SNA) dapat dilihat dari beberapa aspek utama yang menjadikannya tools yang untuk memahami jaringan sosial dan pengaruhnya dalam berbagai konteks seperti memahami struktur sosial yang terjadi di masyarakat, eksplorasi hubungan yang kompleks pada media sosial, berbagai macam aplikasi di berbagai bidang, serta membantu pengambilan keputusan dan implementasi program. Contohnya nyata pada kehidupan sehari-hari adalah adalah SNA dapat membantu menentukan peringkat industri internet WI-FI pada media sosial. Gambaran dari node dan edge dapat ditunjukkan pada gambar berikut.

Node dan Edge (medium.com/@emreeyukseel)

---

<!-- Halaman 97 -->

### B. Beberapa Konsep Penting dalam SNA dan Cara Kerja SNA

Beberapa kosakata yang sering muncul pada SNA:

1. Node (simpul) : Individu atau entitas dalam jaringan. Bisa juga disebut dengan actor. 2. Edge (sisi) : Hubungan antara node, yang bisa berupa interaksi, aliran informasi, atau koneksi lainnya. Bisa juga disebut dengan relation tie. 3. Relation : List/kumpulan dari relation tie. 4. Group : Kumpulan dari beberapa aktor. 5. Centrality : Ukuran seberapa penting atau sentral suatu node dalam jaringan, berdasarkan jumlah atau kekuatan hubungannya. 6. Clustering : Pengelompokan node yang saling terhubung erat di dalam jaringan. 7. Path : Jalur yang menghubungkan dua node melalui serangkaian hubungan.

Cara SNA bekerja adalah dengan cara sebagai berikut:

1. Mengumpulkan data : data yang diambil bisa dari berbagai macam sumber, misal media sosial, berita, karingan komunikasi, dan sebagainya. 2. Analisis struktur jaringan/graf : dianalisis menggunakan berbagai ukuran dan teknik statistik, seperti centrality, clustering, path, dan lain-lain. 3. Pemodelan hubungan sosial : menggunakan model grafis untuk memetakan hubungan, di mana teknik-teknik seperti teori graf, model probabilistik diterapkan, dan lainnya untuk menggambarkan dan menganalisis dinamika interaksi sosial 4. Visualisasi data jaringan : hasil analisis jaringan sering divisualisasikan dalam bentuk grafik, yang mempermudah interpretasi pola hubungan yang kompleks. Ini membantu dalam mengidentifikasi kelompok atau entitas yang paling berpengaruh dalam jaringan gephi auto algoritma louvein 10.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Dataset 3. Gephi app (download link: https://gephi.org/users/download/)

10.5. PRETEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Jelaskan apa itu Social Network Analysis (SNA)! 2. Bagaimana cara kerja dari SNA? 3. Mengapa SNA penting untuk dilakukan? 4. Sebutkan dan jelaskan 3 contoh penerapan SNA dalam kehidupan sehari-hari menurut Anda! | 20 25 25 30 |

---

<!-- Halaman 98 -->

10.6. LANGKAH PRAKTIKUM Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Selesaikan langkah praktikum SNA Using Gephi | Hasil praktikum langkah 1 – 13 | 100 |

### Ikuti langkah praktikum berikut ini:

### COLLECTING DATA

Silakan download dataset dari link yang telah disediakan. Bisa juga download manual pada link https://networkrepository.com/soc-dolphins.php

### SNA USING GEPHI

1. Buka Gephi, masuk ke New Project karena kita akan membuat proyek baru seperti gambar di bawah

### 2. Jika terdapat tulisan seperti ‘apakah ingin save?’, maka klik saja yes dan akan muncul

### gambar seperti di bawah. Ketik saja “Praktikum12_NAMA_NIM”. Untuk NAMA dan

### NIM sesuaikan dengan nama dan NIM kalian. Lalu klik Save.

---

<!-- Halaman 99 -->

### 3. Masuk ke Data Laboratory seperti pada gambar di bawah.

### 4. Lalu akan muncul seperti gambar di bawah dan klik Import Spreadsheet.

---

<!-- Halaman 100 -->

5. Setelah itu, import dataset yang telah diunduh tadi.

### 6. Setelah itu akan muncul tulisan seperti pada gambar di bawah. Tekan OK.

### ● Graph Type menunjukkan tipe graf yang dapat dibuat oleh Gephi.

○ Undirected artinya graf tidak berarah, menandakan node satu dengan node lainnya berhubungan atau tidak.

○ Directed artinya berarah, menandakan hubungan antara node satu dengan yang lainnya seperti apa.

● Nodes dan Edges menunjukkan banyaknya node dan egde dalam dataset tersebut.

● Dataset ini dapat disimpan pada workspace yang telah dibuat sebelumnya,

### namun jika tidak ingin overwrite, dapat memilih New workspace saja.

7. Setelah itu muncul pada bagian Data Laboratory seperti gambar di bawah ini.

---

<!-- Halaman 101 -->

### 8. Setelah itu masuk ke tab Overview di samping Data Laboratory, lalu tampilan akan

menjadi seperti gambar di bawah ini.

### 9. Lalu ubah Layout menjadi Fruchterman Reingold lalu klik Run. Fruchterman

### Reingold tidak bisa stop kecuali kita stop manual. Stop saat gambar sudah tidak ada

### perubahan. Speed, Area, dan Gravity bisa diubah untuk menyesuaikan bentuk dari

graf. Bentuk dari graf akan berubah seperti gambar di bawah.

---

<!-- Halaman 102 -->

10. Tambahkan label untuk masing-masing node dengan cara klik tombol T di kiri bawah.

Sehingga akan muncul seperti pada gambar di bawah.

11. Jika label belum muncul, maka masuk pada tab Data Laboratory dan lihat apakah kolom

### label kosong atau tidak. Jika kosong, klik tombol Copy data to other column, pilih

kolom yang dimaksud dan copy ke kolom label.

12. Ubah warna dan sesuaikan bentu graf dengan yang kita inginkan. Pada tab sesuai gambar di bawah.

---

<!-- Halaman 103 -->

### Nodes untuk mengubah tampilan node (titik) dan Edges untuk mengubah tampilan edge

### (penghubung). Tab tersebut mempunyai beberapa menu seperti Unique, Partition, dan

### Ranking.

### ● Unique mengubah tampilan node/edge menjadi satu warna/ukuran yang kita

pilih.

### ● Partition mengubah sebagian node/edge.

### ● Ranking dapat mengubah tampilan sesuai dengan ranking. Misal ranking

berdasarkan degree. Semakin besar degree, semakin besar pula node nya.

Beberapa hal yang dapat diubah adalah warna, ukuran, warna label, ukuran label. Hal tersebut bisa dilihat pada menu di bawah.

13. Sesuaikan dengan bentuk seperti di bawah dengan warna dan ukuran bebas. Sesuai dengan kreasi masing-masing mahasiswa

---

<!-- Halaman 104 -->

### Ubah Color Nodes, Color Edge, Size Nodes, dan Size Edge semua berdasarkan

### Ranking. Semakin besar node, semakin besar degree-nya. Semakin besar tulisan,

semakin besar degree-nya. Eksplorlah untuk visualisasi graf.

### Kesimpulan yang ada pada gambar: label Grin, Topless, dan SN4 merupakan label

terbanyak yang muncul (paling sering muncul/populer).

### SNA USING PYTHON

1. Buka Google Colab. Isi file anda dengan PRAKTIKUM12_NAMA_NIM sesuai nama dan NIM Anda. Masukkan library yang diperlukan.

```
#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
""" 
Created on Thu Apr 22 12:58:27 2021 
@author: tedysetiadi 
""" 
# import the library 
import networkx as nx 
import matplotlib.pyplot as plt 
from networkx.algorithms import community 
```

---

<!-- Halaman 105 -->

2. Mount dataset yang sudah download tadi. Dan masukkan pada Google Colab seperti pada gambar di bawah.

Code untuk mount data pada Colab adalah seperti berikut

```
# mount your data 
from google.colab import drive 
drive.mount('/content/drive') 
```

3. Tuliskan code untuk membaca file seperti berikut

```
# 1. Membaca dataset (Edge List) dari file dan membuat graf 
def read_graph(file_path): 
    G = nx.read_edgelist(file_path, nodetype=int) 
    return G 
```

4. Tuliskan code untuk menampilkan visualisasi seperti berikut

```
# 2. Menampilkan graf dalam bentuk visualisasi 
def plot_graph(G): 
    pos = nx.spring_layout(G)  # Menentukan tata letak node dalam graf 
    plt.figure(figsize=(8, 6)) 
    # Menggambar node dan edges 
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, 
edge_color='gray', font_size=10) 
    plt.title('Visualisasi Jaringan') 
```

---

<!-- Halaman 106 -->

```
    plt.show() 
```

5. Tuliskan code untuk menghitung centrality dari graf seperti berikut

```
# 3. Menghitung berbagai Centrality Measures 
def calculate_centrality(G): 
    # Degree Centrality 
    degree_centrality = nx.degree_centrality(G) 
    print("\nDegree Centrality:") 
    for node, centrality in degree_centrality.items(): 
        print(f"Node {node}: {centrality:.3f}") 
    # Betweenness Centrality 
    betweenness_centrality = nx.betweenness_centrality(G) 
    print("\nBetweenness Centrality:") 
    for node, centrality in betweenness_centrality.items(): 
        print(f"Node {node}: {centrality:.3f}") 
    # Closeness Centrality 
    closeness_centrality = nx.closeness_centrality(G) 
    print("\nCloseness Centrality:") 
    for node, centrality in closeness_centrality.items(): 
        print(f"Node {node}: {centrality:.3f}") 
```

6. Tuliskan code untuk mendeteksi komunitas dengan algoritma louvein seperti berikut

```
# 4. Deteksi Komunitas dengan Algoritma Louvain 
def detect_communities(G): 
    communities_generator = community.louvain_communities(G, seed=42) 
    # Mencetak komunitas yang terdeteksi 
    print("\nKomunitas yang terdeteksi:") 
```

---

<!-- Halaman 107 -->

```
    for i, community_nodes in enumerate(communities_generator): 
        print(f"Komunitas {i + 1}: {list(community_nodes)}") 
    # Mewarnai graf berdasarkan komunitas 
    pos = nx.spring_layout(G) 
    plt.figure(figsize=(8, 6)) 
    for i, community_nodes in enumerate(communities_generator): 
        nx.draw_networkx_nodes(G, pos, nodelist=community_nodes, 
node_color=plt.cm.jet(i / len(communities_generator)), label=f'Community {i + 
1}') 
    nx.draw_networkx_edges(G, pos, alpha=0.5) 
    plt.title("Deteksi Komunitas dengan Algoritma Louvain") 
    plt.legend() 
    plt.show() 
```

7. Tuliskan code untuk main program seperti berikut

```
# Main Program 
if __name__ == "__main__": 
    # 1. Membaca dan membuat graf dari dataset 
    file_path = nx.read_gml('/content/dolphins.gml') 
    # baca data graf dolphin 
    G = nx.karate_club_graph() 
    # 2. Menampilkan graf 
    plot_graph(G) 
    # 3. Menghitung centrality 
    calculate_centrality(G) 
```

---

<!-- Halaman 108 -->

```
    # 4. Deteksi komunitas 
    detect_communities(G) 
```

8. Jalankan satu-satu code yang sudah anda buat pada colab. Kemudian akan menghasilkan output seperti gambar di bawah.

---

<!-- Halaman 111 -->

10.7. POSTTEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | 1. Cari dataset media sosial yang ingin dianalisis (format dataset dapat berupa csv) Note → Dataset bebas. Referensi dataset: ● https://www.kaggle.com/ ● https://snap.stanford.edu/data/ ● https://networkrepository.com/ ● https://github.com/ ● dll. | 25 |
|  |  |  | 2. Dari dataset yang telah Anda cari, lakukan cleaning data sehingga sesuai dengan yang diinginkan. | 25 |
|  |  |  | 3. Lakukan proses SNA menggunakan Gephi. Explore dataset dan Gephi Anda. Selain explore, hitunglah nilai-nilai berikut: a. Berapa jumlah node dan edgenya b. Node mana dengan nilai degree tertinggi c. Berapa nilai diameter edgenya? d. Berapa rata-rata densitasnya? | 25 |
|  |  |  | 4. Buatlah kesimpulan berupa hasil analisis kalian serta tunjukkan hasil visualisasi kalian. | 25 |

10.8. HASIL CAPAIAN PRAKTIKUM Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.9.4 | 20% |  |  |
| 2. | Praktik | CPL 09KK02 | CPMK 5.9.4 | 30% |  |  |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.9.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 112 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 113 -->

## PRAKTIKUM 11: 
INTERFACE

Pertemuan ke : 11 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.9.4 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining , sosial Network Analisis dan tern data mining saat ini. |
| SubCPMK 5.9.4.2 | Mampu menerapkan, mengembangkan dan menganalisis tren data mining pada studi kasus tertentu |

11.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui assesmen Pretes, parktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui assesmen pretest, praktik dan post test. 11.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09KK02 | CPMK 5.9.4 | ● Kemampuan mahasiswa dalam memahami penerapan salah satu algoritma data mining serta dapat berfikir logis yang diterapkan dalam representasi pengetahuan dan evaluasi pola dari studi kasus menggunakan salah satu software |
| --- | --- | --- |

---

<!-- Halaman 114 -->

|  |  | ● Kemampuan mahasiswa meningkat dalam mengidentifikasidan memcahkan studi kasus |
| --- | --- | --- |

### 11.3. TEORI PENDUKUNG

1. Interface

### Interface (antarmuka) adalah bentuk tampilan grafis yang berhubungan

langsung dengan pengguna (user). Antarmuka pengguna berfungsi untuk menghubungkan antara pengguna dengan sistem. Lebih menekankan pada tampilan visual yang langsung bisa dilihat / dirasakan oleh pengguna. Menghasilkan antarmuka yang mudah, efisien dan enak dinikmati sehingga penggunaan sistem bia memenuhi tujuan pengguna.

2. Flask

Flask adalah micro web framework yang ditulis dalam bahasa pemrograman Python dan berdasarkan Werkzeug toolkit dan template engine Jinja2 berlisensi BSD. Flask disebut micro framework karena tidak membutuhkan alat-alat tertentu atau pustaka. Micro framework Flask bertujuan menjaga core agar tetap simple akan tetapi dapat dikembangkan dalam skala besar. Flask tidak memiliki database abstraction layer, validasi form, atau komponen lain di mana sudah ada pustaka pihak ketiga yang menyediakan fungsi umum. Namun, Flask mendukung ekstensi yang dapat menambahkan fitur aplikasi seolah-olah mereka diimplementasikan dalam Flask itu sendiri. Ekstensi yang ada untuk object-relational mapper, validasi form, penanganan unggahan, berbagai teknologi otentikasi terbuka, dan beberapa alat-lata yang terkait kerangka umum. Ekstensi diperbarui jauh lebih teratur daripada inti program Flask.

Pada dasarnya ada paradigm umum yang digunakan pada hampir setiap

Framework, yaitu MVC (Model – View – Controller). Pada Flask ataupun Django juga dikenal konsep demikian, yaitu MTV ( Model – Template – View). MVC maupun

MTV adalah sebuah metode dalam membuat aplikasi dengan memisahkan pengembangan aplikasi berdasarkan komponen utama yang membangun sebuah aplikasi seperti manipulasi data, antarmuka pengguna, dan bagian yang menjadi kontrol utama aplikasi.

3. Jinja 2

Jinja2 adalah template engine berfitur lengkap untuk Python yang berlisensi BSD (Barkeley Software Distribution). Jinja2 memiliki Unicode support penuh dan memiliki opsi untuk terintegrasi dengan lingkungan eksekusi sandbox.

---

<!-- Halaman 115 -->

{{ … }} untuk ekspresi yang akan di print di template output

{% … %} untuk statement (percabangan, perulangan)

{# … #} untuk komentar yang tidak diperlukan di template output

Gambar 10.1. Proses Jinja

11.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 11.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Jelaskan yang anda ketahui mengenai interface! | 35 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | 1. Jelaskan pengertian dari Flask! 2. Jelaskan mengenai Jinja-jinja! | 35 30 |

### 11.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

---

<!-- Halaman 116 -->

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum A | Hasil praktikum langkah A | 50 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | Selesaiakn langkah praktikum B | Hasil praktikum langkah B | 50 |

Ikuti langkah praktikum berikut ini:

### A. Installasi dependencies

1. Installing Flask pip install Flask

Buka anaconda promt lalu ketikkan perintah berikut :

2. Installing pymongo

Buka anaconda promt lalu ketikkan perintah berikut :

pip install pymongo

### B. Dasar Flask

Mari kita mulai dengan membuat Hello World dengan Flask.

### 1. Buat satu folder untuk mengerjakan project kita, misalnya kita sebut

### DataMining

### 2. Buat folder app

### a. Buat ﬁle __init__.py

Sehingga app akan menjadi sebuah package python. File init ini diisi dengan:

Keterangan:

Membuat sebuah objek Flask di sebuah variabel app, kemudian mengimport modul views. Views ini adalah program yang menangani request dari web browser. Setiap fungsi view bisa jadi satu atau lebih URL.

### b. Buat ﬁle views.py

---

<!-- Halaman 117 -->

Pada kode di atas, ada dua URL yang dipetakan dengan decorator route, yaitu / dan /index.

### 3. Isi folder app dengan folder static dan templates

1. static : berisi file static, yang berhubungan dengan support template diantaranya file css dan javascript

2. templates : berisikan file-file html yang digunakan untuk view kedalam web pages.

### 4. Run Flask

Buat sebuah script run.py pada folder root (DataMining) untuk menjalankan web server kita. Kita isi run.py dengan kode berikut ini:

Buka terminal sistem operasi/terminal conda:

Kemudian masuk kedalam folder aplikasi flask yang telah dibuat melewati terminal

### Jalankan file run.py dengan perintah sebagai berikut: python run.py

### 5. Web Access

Maka port 5000 akan membuka dan menyediakan web server untuk aplikasi tadi.

### Kemudian kita buka saja http://localhost:5000/ atau http://localhost:5000/index di

browser maka akan ditampilkan sebuah halaman dengan tulisan Hello, World!

Saat command prompt menjalankan web server.

### 11.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Buatlah biodata diri yang mencakup (NIM, NAMA, PRODI) | 50 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | Buatlah perhitungan sederhana menggunakan flask! | 50 |

### 11.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

---

<!-- Halaman 118 -->

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.9.4 | 20% |  |  |
| 2. | Praktik | CPL 09KK02 | CPMK 5.9.4 | 30% |  |  |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.9.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 119 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 120 -->

## PRAKTIKUM 12: 
INTERFACE

Pertemuan ke : 12 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.9.4 | Mampu memahami, menerapkan dan menganalisis teknik forecasting, text mining , sosial Network Analisis dan tern data mining saat ini. |
| SubCPMK 5.9.4.2 | Mampu menerapkan, mengembangkan dan menganalisis tren data mining pada studi kasus tertentu |

12.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menerapkan konsep teoritis bidang area Informatika terkait matematika dasar dan ilmu komputer untuk memodelkan masalah dan meningkatkan produktivitas dengan menggunakan assesmen praktik dan post test. 2. Berpikir logis, kritis, sistematis dan inovatif, dan mampu mengambil keputusan secara tepat di bidang keahliannya melalui assesmen Pretes, parktik dan post test. 3. Merancang dan mengimplementasikan algoritma/metode dalam mengidentifikasi dan memecahkan masalah yang melibatkan perangkat lunak dan pemikiran komputasi melalui assesmen pretest, praktik dan post test. 12.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09KK02 | CPMK 5.9.4 | ● Kemampuan mahasiswa dalam memahami penerapan salah satu algoritma data mining serta dapat berfikir logis yang diterapkan dalam representasi pengetahuan dan evaluasi pola dari studi kasus menggunakan salah satu software |
| --- | --- | --- |

---

<!-- Halaman 121 -->

|  |  | ● Kemampuan mahasiswa meningkat dalam mengidentifikasidan memcahkan studi kasus |
| --- | --- | --- |

### 12.3. TEORI PENDUKUNG

1. Interface

### Interface (antarmuka) adalah bentuk tampilan grafis yang berhubungan

langsung dengan pengguna (user). Antarmuka pengguna berfungsi untuk menghubungkan antara pengguna dengan sistem. Lebih menekankan pada tampilan visual yang langsung bisa dilihat / dirasakan oleh pengguna. Menghasilkan antarmuka yang mudah, efisien dan enak dinikmati sehingga penggunaan sistem bia memenuhi tujuan pengguna.

2. Flask

Flask adalah micro web framework yang ditulis dalam bahasa pemrograman Python dan berdasarkan Werkzeug toolkit dan template engine Jinja2 berlisensi BSD. Flask disebut micro framework karena tidak membutuhkan alat-alat tertentu atau pustaka. Micro framework Flask bertujuan menjaga core agar tetap simple akan tetapi dapat dikembangkan dalam skala besar. Flask tidak memiliki database abstraction layer, validasi form, atau komponen lain di mana sudah ada pustaka pihak ketiga yang menyediakan fungsi umum. Namun, Flask mendukung ekstensi yang dapat menambahkan fitur aplikasi seolah-olah mereka diimplementasikan dalam Flask itu sendiri. Ekstensi yang ada untuk object-relational mapper, validasi form, penanganan unggahan, berbagai teknologi otentikasi terbuka, dan beberapa alat-lata yang terkait kerangka umum. Ekstensi diperbarui jauh lebih teratur daripada inti program Flask.

Pada dasarnya ada paradigm umum yang digunakan pada hampir setiap

Framework, yaitu MVC (Model – View – Controller). Pada Flask ataupun Django juga dikenal konsep demikian, yaitu MTV ( Model – Template – View). MVC maupun

MTV adalah sebuah metode dalam membuat aplikasi dengan memisahkan pengembangan aplikasi berdasarkan komponen utama yang membangun sebuah aplikasi seperti manipulasi data, antarmuka pengguna, dan bagian yang menjadi kontrol utama aplikasi.

3. Pengertian Microframework

Micro tidak berarti semua aplikasi web dapat dijadikan kedalam satu file

Python, seperti itu bukan berarti kekurangan dalam fungsionalitas. Micro

---

<!-- Halaman 122 -->

framework (Flask) bertujuan menjaga core agar tetap simple akan tetapi dapat dikembangkan dalam skala yang besar. Flask tidak ingin membuat banyak aturan untuk seorang developer, seperti contoh database apa yang akan digunakan, aturan template engine apa yang harus digunakan. Sehingga developer bebas memilih apapun segalanya yang dibutuhkan dan  apa  yang  tidak dibutuhkan.

Secara default, didalam Flask tidak tersedia database abstraction layer, validation form atau sesuatu yang lain dimana macam – macam library sudah tersedia dan dapat segera dipakai. Flask mendukung pengembangan untuk penambahan fungsionalitas kebutuhan. Meskipun flask adalah “micro”, akan tetapi siap digunakan untuk berbagai macam kebutuhan.

### 4. 
Blueprint

Blueprint adalah salah satu Flask extensions yang dimana mendukung pengaturan modular aplikasi dalam sekala yang besar. Dengan menggunakan blueprint maka beberapa fungsionalitas yang kompleks dapat dipecah kedalam beberapa modul yang saling terkait. Konsep blueprint itu sendiri adalah dengan mendaftarkan setiap alamat url dari modular  yang telah dibentuk, sehingga setiap modular dapat diakses secara terpisah meskipun berada dalam file routing yang berbeda.

5. Jinja 2

Jinja2 adalah template engine berfitur lengkap untuk Python yang berlisensi BSD (Barkeley Software Distribution). Jinja2 memiliki Unicode support penuh dan memiliki opsi untuk terintegrasi dengan lingkungan eksekusi sandbox.

{{ … }} untuk ekspresi yang akan di print di template output

{% … %} untuk statement (percabangan, perulangan)

{# … #} untuk komentar yang tidak diperlukan di template output

---

<!-- Halaman 123 -->

12.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Anaconda app 3. Dataset 12.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Jelaskan yang anda ketahui mengenai interface! | 30 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | 1. Jelaskan pengertian dari Blueprint! 2. Jelaskan mengenai microframework! | 35 35 |

### 12.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum 1 – 5 | Hasil praktikum langkah 1 – 5 | 50 |
| 2. | CPL 09KK02 | CPMK 5.9.4 | Selesaikan langkah praktikum 6-11 | Hasil praktikum langkah 6-11 | 50 |

Ikuti langkah berikut ini:

### 1. Buatlah satu folder untuk mengerjakan project, missal kita sebut Flask

### 2. Buat Folder ‘app’ di dalam Folder ‘Flask’ yang telah kita buat sebelumnya dan buat

### File ‘run.py’ dan File ‘config.py’

---

<!-- Halaman 124 -->

Keterangan :

- config.py merupakan file untuk menyimpan konfigurasi didalam Flask (DEBUG, Secret Key, Database Connection).

- run.py merupakan file dimana untuk menjalankan aplikasi

Flask

### 3. Isi file config.py

Keterangan :

- DEBUG merupakan konfigurasi debuging (aplikasi dalam proses pengembangan)

- SECRET_KEY merupakan enkripsi prosesing flask

### 4. Isi file run.py

### Keterangan :

app.run merupakan konfigurasi untuk setting microserver dengan host ‘0.0.0.0’ dan port yang digunakan adalah 8080,  sehingga nantinya apabila dilakukan akses didalam browser menjadi http://0.0.0.0:8080

### 5. Isi folder ‘app’:

### File modul, static, template, upload_data serta file ‘   init   .py’berada ada didalam

folder app, apabila masuk kedalam folder app maka akan ada folder dan file sebagai berikut:

---

<!-- Halaman 125 -->

Keterangan:

- modul : berisikan beberapa modul yang diterapkan kedalam sistem, beberapa contoh modul dalam sistem yang diterapkan:

● cleaning (modul cleaning data mentah)

● cluster (modul proses clustering)

● purity (modul validity test purity)

● upload (modul untuk upload file)

- static : berisi file static, yang berhubungan dengan support template diantaranya file css dan javascript

- templates : berisikan file-file html yang digunakan untuk view kedalam web pages.

- upload_data : berisikan untuk menampung file upload, (data Excel (Mentah))

### 6. Penerapan modul

Setiap modul akan berisi controller dengan opsional dbmodel ataupun file-file pendukung lainnya. (mengambil contoh module upload). Di dalam folder modul

### terdapat folder foder baru dengan nama upload dan file ‘   init    .py’. Buat file ‘ init

### .py’ dan buat file ‘controllers.py’ didalam folder upload

didalam folder upload berisikan controllers.py digunakan untuk routing pages upload dalam proses upload file.

### b. Isi dependencies yang dipakai

#Import flask dependencies from flask import Blueprint, request, render_template from openpypxl import load_workbook from werkzeug import secure_filename import pandas as pd import os

---

<!-- Halaman 126 -->

### c. Create Blueprint router

Keterangan :

- mod_upload adalah nama modul index upload

- mod_uploader adalah nama modul prosesing upload

- url_prefix merupakan alias untuk address page di browser

### d. Create Method dari setiap modul

Untuk method mod_upload:

Keterangan :

- MainTitle adalah variable

- methods = [‘GET’,’POST’] (methods tersebut merupakan jenis request access yang dilayani oleh routers mod_upload)

- def upload_file adalah method yang dimiliki mod_upload

- render_template adalah render seluruh prosesing dalam router untuk ditampilkan kedalam file template dengan nama ‘upload/upload.html’

---

<!-- Halaman 127 -->

### e. Create method dari setiap modul yang telah dibuat. Untuk method

### mod_uploader

```
@mod_uploader.route('', methods = ['GET', 
'POST']) def upload_file(): 
i
f request.method == 
'POST': subTitle = 
("Data Excel") f = 
request.files['file'] 
f.save(os.path.join('app/upload_data', 
'DATA EXCEL.xlsx')) 
wb = load_workbook(filename = 
'app/upload_data/DATA EXCEL.xlsx') sheet_ranges = wb['Sheet5'] 
data = 
pd.DataFrame(sheet_ranges.values) 
button = [(str(request.url_root))] 
return 
render_template('upload/tables.html', 
tables=[data.to_html 
(classes='Alumni')]
text = [mainTitle
subTitle]
button=button
```

### 7. Penerapan Folder Static

Pada folder static berisi template atau boostrap (berisi bootstrap & jquery) untuk memperindah tampilan.

contoh potongan source code dapat dilihat sebagai berikut

### Keterangan : 
- url_for digunakan untuk accessing path file (dengan contoh access static path

### file)

### 8. Penerapan Folder Templates

Pada folder templates digunakan untuk membuat tampilan dari proses yang ada di

### dalam folder modul. Buat Folder ‘upload’ dan file ‘404.html’. Pada Folder ‘upload’

### isikan file ‘upload.html’ dan ‘tables.html’.

### ⮚ Isi dari File “upload.html”

---

<!-- Halaman 128 -->

```
<!doctype html> 
<link rel="stylesheet" type="text/css" href="{{url_for('static', 
filename='bootstrap/css/bootstrap.min.css')}}"> 
<link rel=stylesheet type=text/css href="{{ url_for('static', 
filename='style.css') }}"> 
<html> 
<body> 
<div class="container"> 
<div class="row"> 
<h1>Clustering 
[KMeans]</h1> 
</div> 
<div class="row"> 
<form action="http://localhost:8080/mod_uploader" 
method="POST" enctype="multipart/form-data"> 
<div 
class="form-group row"> 
<h4>Sila
hkan Upload Data</h4> 
</div> 
<div 
class="form-group row"> 
div class="col-sm-2"> 
input type = "file" name = "file" /> 
</div> 
<div 
class="col-sm-5"> 
button type="submit" class="btn btn- 
primary">Upload Data</button> 
</div> 
</div> 
</form> 
```

---

<!-- Halaman 129 -->

### ⮚ Isi file “tables.html”

```
<!doctype html> 
<link rel="stylesheet" type="text/css" href="{{url_for('static', 
filename='bootstrap/css/ 
bootstrap.min.css')}}"> 
<link rel=stylesheet type=text/css href="{{ url_for('static', 
filename='style.css') }}"> 
<html> 
<
body> 
<div class="container"> 
<div class="row"> 
<h1>{{t
ext[0]}}</h1> 
</div> 
<div class="row"> 
<div 
class="col-sm-12"> 
{% endif %} 
</div> 
</div> 
</form> 
</div> 
</div> 
<div class="row"> 
```

---

<!-- Halaman 130 -->

### 9. Register blueprint kedalam init.py yang ada didalam folser app:

```
# Import flask and 
template operators from 
flask import Flask, 
render_template 
# Define the WSGI 
application object app = 
Flask( name ) 
# Configurations 
app.config.from_object('config') 
# Sample HTTP 
error handling 
@app.errorhandler(40 
4) 
def not_found(error): 
return render_template('404.html'), 404 
# Import a module / component using its
```

### 10. Run Flask

Buka terminal sistem operasi/terminal conda:

Kemudian masuk kedalam folder aplikasi flask yang telah dibuat melewati

### terminal Jalankan file run.py dengan perintah sebagai berikut:

### python

### 11. Web Pages Access

Buka browser kemudian akses alamat url : http://0.0.0.0:8080/mod_upload maka

### akan muncul halaman website sebagai berikut.

---

<!-- Halaman 131 -->

### 12.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL-03 | CPMK-02 | Buatlah web sederhana menggunakan python dan tampilkan data studi kasus kalian seperti pada contoh praktikum | 70 |
| 2. | CPL-08 | CPMK-03 | Buatlah web yang dapt menampilkan biodata seperti pada posttest praktikum sebelumnya | 30 |

### 12.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL-03 CPL-08 | CPMK-02 CPMK-03 | 20% |  |  |
| 2. | Praktik | CPL-03 CPL-08 | CPMK-02 CPMK-03 | 30% |  |  |
| 3. | Post-Test | CPL-03 CPL-08 | CPMK-02 CPMK-03 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

---

<!-- Halaman 132 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 133 -->

### DAFTAR PUSTAKA 
 
 
1. Han, Jiawei and Kamber, Micheline, 2006, Data Mining Concept and Techniques, Morgan

Kaufmann Publishers

2. Hermawati, F., 2013, Data Mining, Penerbit Andi dan Universitas 17 Agustus 1945

Surabaya.