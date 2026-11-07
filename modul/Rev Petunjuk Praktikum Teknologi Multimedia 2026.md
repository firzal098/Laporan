<!-- Halaman 1 -->

## Teknologi Multimedia

### Penyusun:

### Ir. Ika Arfiani, S.T., M.Cs.

### Ir. Dinan Yulianto, S.T., M.Eng.

### Bambang Robi’in, S.T., M.T.

---

<!-- Halaman 2 -->

### HAK CIPTA

### PETUNJUK PRAKTIKUM TEKNOLOGI MULTIMEDIA

Copyright© 2026, Ir. Ika Arfiani, S.T., M.Cs. Ir. Dinan Yulianto, S.T., M.Eng. Bambang Robi’in, S.T., M.T. Hak Cipta dilindungi Undang-Undang Dilarang mengutip, memperbanyak atau mengedarkan isi buku ini, baik sebagian maupun seluruhnya, dalam bentuk apapun, tanpa izin tertulis dari pemilik hak cipta dan penerbit. Diterbitkan oleh: Program Studi Teknik Informatika Fakultas Teknologi Industri Universitas Ahmad Dahlan Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 Penulis : Ika Arfiani,S.T., M.Cs. Dinan Yulianto. S.T., M.Eng. Bambang Robi’in, S.T., M.T. Editor : Laboratorium Teknik Informatika, Universitas Ahmad Dahlan Desain sampul : Laboratorium Teknik Informatika, Universitas Ahmad Dahlan Tata letak : Laboratorium Teknik Informatika, Universitas Ahmad Dahlan Ukuran/Halaman : 21 x 29,7 cm / 111 halaman Didistribusikan oleh:

### Laboratorium Teknik Informatika 
Universitas Ahmad Dahlan 
Jalan Ring Road Selatan, Tamanan, Banguntapan, Bantul Yogyakarta 55166 
Indonesia

---

<!-- Halaman 3 -->

### KATA PENGANTAR

Assalamu’alaikum Wr. Wb

Alhamdulillahi rabbil allamin, puji dan syukur kami panjatkan kehadirat Allah SWT yang telah melimpahkan rahmat dan hidayah-Nya, sholawat dan salam tetap tercurahkan pada junjungan Nabi Besar Muhammad SAW yang membawa petunjuk dan penerang bagi semesta alam.

Atas izin Allah SWT yang Maha Rahman dan Rahim, sehingga kami dapat menyelesaikan Modul Praktikum Teknologi Multimedia ini.

Materi dan tugas dalam modul ini merupakan implementasi dari teori dan konsep yang disampaikan dalam kuliah Teknologi Multimedia. Harapan yang ingin dicapai dengan disusunnya modul ini ialah praktikan mampu menerapkan konsep atau pemahaman tentang berbagai teknik dalam multimedia dan mengimplementasikannya secara langsung, sehingga praktikan mempunyai gambaran bagaimana multimedia secara teori dan aplikasi.

Mengingat masih terbatasnya pengetahuan, kemampuan dan pengalaman penulis menyadari bahwa masih banyak kekurangan dalam penyusunan Modul Praktikum ini. Karena itu penulis mengharapkan saran dan kritik yang membangun demi melengkapi kekurangan ini untuk dapat kami revisi di lain waktu.

Wassalau’alaikum Wr.Wb.

Yogyakarta, 20 September 2026

Penyusun

---

<!-- Halaman 4 -->

### DAFTAR PENYUSUN

### Ir. Ika Arfiani, S.T., M.Cs.

|  | Bidang Keahlian : Rekayasa Perangkat Lunak dan Data |
| --- | --- |

### Dinan Yulianto, S.T., M.Eng.

|  | Bidang Minat : Multimedia, Interaksi Manusia dan Komputer, dan IT in Education |
| --- | --- |

### Bambang Robi’in, S.T., M.T.

|  | Bidang Minat: AI, Multimedia, Game Design And Development |
| --- | --- |

---

<!-- Halaman 5 -->

### HALAMAN REVISI

Yang bertanda tangan di bawah ini:

Nama : Ir. Ika Arfiani, S.T., M.Cs.

NIPM : 19870920 201606 011 1095511

Jabatan : Dosen Pengampu Mata Kuliah Teknologi Multimedia

Dengan ini menyatakan pelaksanaan Revisi Petunjuk Praktikum Teknologi Multimedia untuk Program Studi Teknik Informatika telah dilaksanakan dengan penjelasan sebagai berikut:

|  | No |  |  | Keterangan Revisi |  |  | Tanggal Revisi |  |  | Nomor Modul |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  | a. Pertemuan Ke-1. Pengenalan Komponen Multimedia b. Pertemuan Ke-2. Pre Processing Image (Teknik Pengambilan Gambar) c. Pertemuan Ke-3. Post Processing Image (Editing Gambar) d. Pertemuan Ke-4. Pre Processing Video (Teknik Pengambilan Video) e. Pertemuan Ke-5. Post Processing Video (Editing Video) f. Pertemuan Ke-6. Pemodelan Pembuatan Karakter g. Pertemuan Ke-7. Teknik Animasi h. Pertemuan Ke-8. Action Script i. Pertemuan Ke-9. Recording Dan Editing Audio j. Pertemuan Ke-10. Integrasi Multimedia |  |  | 1 Agustus 2010 |  |  | PP/018/V/R1 |  |  |
| 2 |  |  | a. Pertemuan Ke-1. Pengenalan Komponen Multimedia b. Pertemuan Ke-2. Pre Processing Image And Video (Teknik Pengambilan Gambar Dan Video) c. Pertemuan Ke-3. Post Processing Image (Editing Gambar) d. Pertemuan Ke-4. Post Processing Video (Editng Video) e. Pertemuan Ke-5. Pemodelan Karakter (Animasi 2d) f. Pertemuan Ke-6. Teknik Animasi 2d Dan Action Script |  |  | 1 Agustus 2014 |  |  | PP/018/V/R2 |  |  |

---

<!-- Halaman 6 -->

|  |  |  | g. Pertemuan Ke-7. Pemodelan Karakter Dan Pengenalan Script Mel (Maya Embedded Language) (Animasi 3d) h. Pertemuan Ke-8. Teknik Animasi 3d i. Pertemuan Ke-9. Recording Dan Editing Audio j. Pertemuan Ke-10. Integrasi Multimedia |  |  |
| --- | --- | --- | --- | --- | --- |
| 3 |  |  | a. Pertemuan Ke-1. Pengenalan Komponen Multimedia b. Pertemuan Ke-2. Pre & Post Processing Image And Video c. Pertemuan Ke-3. Post Processing Video (Editng Video) d. Pertemuan Ke-4. Pemodelan Karakter (Animasi 2d) e. Pertemuan Ke-5. Teknik Animasi 2d Dan Action Script f. Pertemuan Ke-6. Pemodelan Karakter Dan Pengenalan Script Mel (Maya Embedded Language) (Animasi 3d) g. Pertemuan Ke-7. Teknik Animasi 3d (Shading, Rigging, Skinning) h. Pertemuan Ke-8 Augmented Reality i. Pertemuan Ke-9. Recording Dan Editing Audio j. Pertemuan Ke-10. Integrasi Multimedia | 1 Agustus 2016 | PP/018/V/R2 |
|  | 4 |  | Perubahan template ke OBE | 1 Agustus 2021 | PP/018/V/R2 |
|  | 5 |  | Perubahan sampul | 10 Februari 2024 | PP/018/V/R3 |
| 6 | 6 |  | Perubahan RPS, CPL dan CPM | 28 September 2026 | PP/018/IX/R6 |

Yogyakarta, 20 September 2026

Penyusun

Ir. Ika Arfiani, S.T., M.Cs NIPM. 19870920 201606 011 1095511

---

<!-- Halaman 7 -->

### HALAMAN PERNYATAAN

Yang bertanda tangan di bawah ini:

Nama : Murein Miksa Mardhia S.T., M.T.

NIPM : 19891019 201606 011 1236278

Jabatan : Kepala Laboratorium S1 Informatika

Menerangkan dengan sesungguhnya bahwa Petunjuk Praktikum ini telah direview dan akan digunakan untuk pelaksanaan praktikum di Semester Gasal  Tahun Akademik 2026/2027 di Laboratorium Praktikum S1 Informatika, Program Studi Informatika, Fakultas Teknologi Industri, Universitas Ahmad Dahlan.

Yogyakarta, 20 September 2026

Mengetahui,

Ketua Pogram Studi

Kepala Laboratorium S1 Informatika

Murein Miksa Mardhia, S.T., M.T. NIPM. 19891019 201606 011 1236278

Dr. Murinto, S.Si., M.Kom.,s. NIPM. 19730710 200409 111 0951298

---

<!-- Halaman 8 -->

### VISI DAN MISI PRODI TEKNIK INFORMATIKA

### VISI

Menjadi Program Studi Informatika yang diakui secara internasional dan unggul dalam bidang Informatika serta berbasis nilai-nilai Islam.

### MISI

1. Menjalankan pendidikan sesuai dengan kompetensi bidang Informatika yang diakui nasional dan internasional 2. Meningkatkan penelitian dosen dan mahasiswa dalam bidang Informatika yang kreatif, inovatif dan tepat guna. 3. Meningkatkan kuantitas dan kualitas publikasi ilmiah tingkat nasional dan internasional 4. Melaksanakan dan meningkatkan kegiatan pengabdian masyarakat oleh dosen dan mahasiswa dalam bidang Informatika. 5. Menyelenggarakan aktivitas yang mendukung pengembangan program studi dengan melibatkan dosen dan mahasiswa. 6. Menyelenggarakan kerja sama dengan lembaga tingkat nasional dan internasional. 7. Menciptakan kehidupan Islami di lingkungan program studi.

---

<!-- Halaman 9 -->

### TATA TERTIB LABORATORIUM TEKNIK INFORMATIKA

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

Praktikan dan Asisten. 2. Ketidakhadiran praktikum dengan alasan apapun dianggap INHAL. 3. Inhal yang diizinkan dapat diikuti oleh praktikan selama periode praktikum adalah maksimal 3

(tiga) kali. Silakan menggunakan kuota inhal apabila mendapat halangan untuk hadir saat praktikum seperti sakit, izin, atau delegasi lomba. 4. Pelaksanaan (waktu dan metode) INHAL sama seperti praktikum mingguan/reguler. 5. Izin praktikum mengikuti aturan izin SIMERU/KULIAH. 6. Yang tidak berkepentingan dengan praktikum dilarang mengganggu praktikan atau membuat keributan/kegaduhan. 7. Penggunaan lab diluar jam praktikum maksimal sampai pukul 18.15 dengan menunjukkan surat ijin dari Kepala Laboratorium Prodi Informatika.

Yogyakarta, 20 September 2026 Kepala Laboratorium Informatika Murein Miksa Mardhia, S.T., M.T. NIPM : 19891019 201606 011 1236278

---

<!-- Halaman 12 -->

### DAFTAR ISI

### HAK CIPTA ................................................................................................................................................1

KATA PENGANTAR ....................................................................................................................................2

DAFTAR PENYUSUN ..................................................................................................................................3

HALAMAN REVISI......................................................................................................................................4

HALAMAN PERNYATAAN ..........................................................................................................................6

VISI DAN MISI PRODI TEKNIK INFORMATIKA ...........................................................................................7

TATA TERTIB LABORATORIUM TEKNIK INFORMATIKA .............................................................................8

DOSEN/KOORDINATOR PRAKTIKUM .....................................................................................................8

PRAKTIKAN ............................................................................................................................................8

ASISTEN PRAKTIKUM ............................................................................................................................9

LAIN-LAIN ........................................................................................................................................... 10

DAFTAR ISI ............................................................................................................................................. 11

DAFTAR GAMBAR .................................................................................................................................. 12

DAFTAR TABEL ....................................................................................................................................... 12

SKENARIO PRAKTIKUM SECARA DARING .............................................................................................. 17

## PRAKTIKUM 1: 
PENGENALAN KOMPONEN MULTIMEDIA .............................................................. 21

## PRAKTIKUM 2: 
AKUISISI DAN PENGOLAHAN CITRA ........................................................................ 37

## PRAKTIKUM 3: 
RECORDING & EDITING AUDIO ............................................................................... 46

## PRAKTIKUM 4: 
EDITING DAN POST-PROCESSINg VIDEO ................................................................. 52

## PRAKTIKUM 5: 
KOMPRESI DAN STREAMING VIDEO ....................................................................... 61

## PRAKTIKUM 6: 
PEMODELAN KARAKTER 2D .................................................................................... 68

## PRAKTIKUM 7: 
TEKNIK ANIMASI 2D INTERAKTIF ............................................................................ 72

## PRAKTIKUM 8: 
PEMODELAN KARAKTER 3D .................................................................................... 83

## PRAKTIKUM 9: 
TEKNIK ANIMASI 3D (SHADING, RIGGING, SKINING) .............................................. 90

## PRAKTIKUM 10: 
INTEGRASI MULTIMEDIA PADA AR/VR ................................................................... 96

DAFTAR PUSTAKA ................................................................................................................................ 111

---

<!-- Halaman 13 -->

### DAFTAR GAMBAR

### DAFTAR TABEL

---

<!-- Halaman 14 -->

### SKENARIO PRAKTIKUM SECARA DARING

Nama Mata Praktikum : Teknologi Multimedia Jumlah Pertemuan : 10

### TABEL SKENARIO PRAKTIKUM DARING

| Praktikum Pertemuan ke | Judul Materi | Waktu (Lama praktikum) | Jenis Tugas | Skenario Praktikum |
| --- | --- | --- | --- | --- |
| 1 overview 22/3/2021 sampai 27/3/2021 | Penjelasan Tugas akhir kelas + sebagai pengganti responsi praktikum | Maksimum dikumpul sekitar Bulan JUNI 2021 | Tugas akhir/tugas proyek kelas | Tugas akhir pada matakuliah pengantar multimedia ini adalah membuat video animasi yang berkaitan dengan pandemi covid-19. a. Kreasikan kreatifitas anda semenarik mungkin yang didalamnya memuat berbagai komponen multimedia. (minimal : teks, gambar/foto, audio, video/animasi) b. Durasi maksimal 5 menit dan dibuat dalam bentuk mp4. |
|  | Pretest materi 1 | 22-27/3/2021 | Pretest praktikum | Mahasiswa mengerjakan pretest 1. |
|  | Dasar- dasar multimedia (materi 1) | 30 menit |  | Asisten menjelaskan berbagai software yang biasa digunakan untuk memproduksi aplikasi multimedia. |
|  |  | Maks 27/3/2021 jam 24.00 | Postest praktikum | Mahasiswa mengerjakan postest dengan didampingi asisten melalui chat grup WA : Aplikasi Multmedia yang baik adalah memenuhi aspek user friendly, teknik tata letak komponen dan pewarnaan sebuah aplikasi sangat penting untuk diperhatikan. Tuliskan penilaian Anda terhadap aplikasi yang dipakai menyangkut 3 aspek penting ini, jika memungkinkan ada yang lebih bagus dari aplikasi yang disebutkan di atas silahkan kemukakan pendapat atau alasan Anda. (dikumpul melalui drive) |

---

<!-- Halaman 15 -->

| 2 29/3/20213/4/2021 | Pretest materi 2 | 29/3/20213/4/2021 | Pretest praktikum | Mahasiswa mengerjakan pretest pertemuaan 2 |
| --- | --- | --- | --- | --- |
|  | Akuisisi dan Pengolahan Citra | 30 menit |  | Asisten menerangkan terkait pre & post processing image melalui video tutorial |
|  |  | Mulai 29 Maret sampai maks 3 April 2021 Jam 24.00 | Postest praktikum | Mahasiswa mengerjakan postest dengan didampingi asisten melalui chat grup WA : Cari objek di sekitar anda terkait pandemi atau permasalahan covid ini yang menurut Anda menarik untuk diambil gambarnya, kemudian lakukan pengambilan gambar/foto & video. Dari gambar/image yang telah dihasilkan, |
| 3 5-10/4/2021 | Pretest materi 3 | 5-10/4/2021 | Pretest praktikum | Mahasiswa mengerjakan pretest pertemuaan 3 |
|  | Recording dan Editing Audio | 30 menit |  | Asisten menerangkan terkait pre & post processing video melalui video tutorial |
|  |  |  | Postest praktikum | Mahasiswa mengerjakan postest dengan didampingi asisten melalui chat grup WA : lakukan proses editing gambar tersebut semenarik mungkin untuk nantinya disusun berbarengan dengan videonya menjadi sebuah video tutorial atau iklan terkait permasalahan pandemi covid. |
| 4 12-17/4/2021 | Pretest materi 4 |  | Pretest praktikum | Mahasiswa mengerjakan pretest pertemuaan 4 |
|  | Editing dan PostProcessing Video | 30 menit |  | Asisten menerangkan terkait pemodelan karakter melalui video tutorial |
|  |  |  | Postest praktikum | Pada praktikum ini, lakukanlah tugas berikut : a. Carilah minimal satu perancangan karakter mulai dari sketsa sampai pewarnaan di internet, unduhlah gambarnya. b. Lakukan analisis pada langkah-langkah pembuatan karakter tersebut. c. Tulislah hasil analisis anda d. Buatlah karakter model untuk tugas proyek anda(boleh tulis dikertas kemudian foto & dijadikan 1 file dengan hasil analisa anda diatas) atau screenshoot dari adobe flash anda juga boleh. |

---

<!-- Halaman 16 -->

| 5 19-24/4/2021 | Pretest materi 5 |  | Pretest praktikum | Mahasiswa mengerjakan pretest pertemuaan 5 |
| --- | --- | --- | --- | --- |
|  | Kompresi dan Streaming Video | 30 menit |  | Asisten menerangkan terkait teknik animasi 2D & action script |
|  |  |  | Postest praktikum | Buatlah rangkaian animasi sederhana mengguakan model yang telah dibuat sebelumnya, jangan lupa untuk memberikan action script pada animasi yang nada buat. |
| 6 | Pretest materi 6 |  |  | Mahasiswa mengerjakan pretest pertemuaan 6 |
|  | Pemodelan Karakter 2D | 30 menit |  | Asisten menerangkan terkait teknik animasi 3D |
|  |  |  | Postest praktikum | Buatlah karakter 2D awal anda kedalam bentuk 3D dalam sebuah kertas atau tools yang ada. |
| 7 | Pretest materi 7 |  |  | Mahasiswa mengerjakan pretest pertemuaan 7 |
|  | Teknik animasi 2D Interaktif | 30 menit |  | Asisten menerangkan terkait Teknik animasi 3D |
|  |  |  | Postest praktikum | Buatlah animasi 3D gerakan langkah kaki berjalan |
| 8 | Pretest materi 8 | 15-20 Juni 2020 | Pretest praktikum | Mahasiswa mengerjakan 2 kali pretest (pertemuaan 4 dan pertemuan 6) di elearning. |
|  | Pemodelan Karakter 3D | 30 menit |  | Asisten menerangkan terkait pemodelan karakter melalui video tutorial |
|  |  | Mulai 15 Juni sampai maks 20 Juni 2020 Jam 24.00 | Postest praktikum | Buatlah storyboard aplikasi AR beserta material yang dibutuhkan, |
| 9 | Pretest materi 9 | 22-27 Juni 2020 | Pretest praktikum | Mahasiswa mengerjakan 2 kali pretest (pertemuaan 5 dan pertemuan 7) di elearning. |

---

<!-- Halaman 17 -->

|  | Teknik animasi 3D (Shading, Rigging, Skining) | 30 menit |  | Asisten menerangkan terkait teknik animasi 2D-3D & action script |
| --- | --- | --- | --- | --- |
|  |  | Mulai 22 Juni sampai maks 27 Juni 2020 Jam 24.00 | Postest praktikum | Buatlah rangkaian animasi sederhana(pendukung tugas proyek anda) yang didalamnya terdapat salah satu atau lebih teknik animasi dan tambahkan Action Script pada rangkaian animasi sederhana yang telah dibuat. |
| 10 | Pretest materi 19 | 29 Juni – 4 juli 2020 | Pretest praktikum | Mahasiswa mengerjakan 2 kali pretest (pertemuaan 8 dan pertemuan 9) di elearning. |
|  | Integrasi Multimedia pada Aplikasi AR/VR | 30 menit |  | Asisten menerangkan terkait Record & editing audio |
|  |  | Mulai 29 Juni sampai maks 4 Juli 2020 Jam 24.00 | Postest praktikum | Melakukan recording dan editing audio pada Adobe Soundbooth CS3 atau aplikasi yg lain kemudian implementasikan ke dalam animasi yang sudah dibuat sebelumnya. |
| Inhal& responsi | Pretest materi 10 | 6-11 Juli 2020 | Pretest praktikum | Mahasiswa mengerjakan pretest pertemuaan 10. |
|  | Integrasi multimedia (materi 10) | 30 menit |  | Asisten menerangkan terkait Integrasi multimedia |
|  |  | Mulai 6 Juli sampai maks 11 Jul i 2020 Jam 24.00 | Postest praktikum | Melakukan proses penyatuan komponen-komponen animasi pada praktikumpraktikum sebelumnya dengan menggunakan karakter dan sound. Simpanlah dengan format MPEG-1/mp4. |

---

<!-- Halaman 18 -->

## PRAKTIKUM 1: PENGENALAN KOMPONEN MULTIMEDIA

Pertemuan ke : 1 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsipprinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan komputasi yang kompleks. |
| --- | --- |
| CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |

1.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menjelaskan berbagai macam komponen yang ada dalam sebuah multimedia. 2. Menjelaskan berbagai macam tools yang di gunakan untuk memproduksi multimedia. 3. Mengimplementasikan berbagai macam komponen dengan tools yang tepat. 1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |
| --- | --- | --- |

Multimedia berasal dari kata multi dan medium. Multi yang berarti banyak atau lebih dari satu. Medium yang berarti perantara atau suatu perantara yang digunakan untuk menghantar atau menyampaikan sesuatu seperti komunikasi  massa.

Multimedia adalah Informasi di dalam komputer yang direpresentasikan ke dalam bentuk audio, video, animasi dan media lain (graphics, images, text, dsb). Seiring dengan kemajuan teknologi informasi, saat ini konsep multimedia telah menjadi TREND di kalangan masyarakat. Multimedia saat ini telah di aplikasikan di berbagai bidang, mulai dari penanganan image dalam dunia fotografi, animasi, audio, video, film bahkan sampai pada konsep smart house. Dalam multimedia terdapat empat komponen penting yakni :

a. Adanya komputer sebagai suatu alat yang dapat berinteraksi dengan user.

---

<!-- Halaman 19 -->

b. Adanya link yang menghubungkan user dengan informasi. c. Adanya alat navigasi yang memandu, menjelajah jaringan informasi yang saling terhubung.

Multimedia menyediakan tempat kepada user untuk mengumpulkan, memproses, dan menghubungkan informasi dan ide user sendiri. (M. Suyanto, 2004)

Untuk membuat atau mengolah berbagai macam unsur yang ada dalam sebuah multimedia di perlukan berbagai macam tools yang sesuai dengan spesifikasi yang di butuhkan. Dalam praktikum pengantar multimedia ini akan di gunakan beberapa software yang terkait dengan pembuatan/produksi sebuah multimedia. 1.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu: 1. Komputer. 2. Adobe Photoshop/Corel Draw 3. Adobe Flash 4. Adobe Soundbooth 5. Corel Video Studio 6. Blender 1.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan berbagai obyek/elemen multimedia yang dapat digunakan untuk memebangun sebuah produk multimedia! 2. Jelaskan serta berikan implementasi teknologi multimedia dalam berbagai 5 bidang kehidupan! 3. Sebutkan 3 tren teknologi multimedia pada masa mendatang! | 20 50 30 |

### 1.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua panduan pada langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

Cara Pengggunaan tools-tools pendukung multimedia Penggunaan tools produksi multimedia: 1. Mencoba Adobe Photoshop untuk mengolah gambar

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 20 -->

Gambar 1.1 Tampilan Awal Adobe Photoshop

Photoshop adalah sebuah image editor, atau program penyunting gambar yang berfungsi untuk membuat, menyunting, dan memodifikasi gambar digital yang terdapat di dalam komputer.

### Mengganti Warna dengan Hue/Saturation

• Buka foto/image ke dalam Photoshop. • Kemudian Pilih Menu Image > Adjustments > Hue/Saturation (Ctrl+U).

### Gambar 1.2 Tampilan Menu Hue/Saturation

• Pada kotak dialog Hue/Saturation, atur warna foto dengan mengeser slider Hue/Saturation- nya dan klik OK bila warna yang diinginkan telah sesuai.

Gambar 1.3 Tampilan Menu konfigurasi Hue/Saturation

• Lihat hasilnya, warna foto / image berubah warna. 2. Mencoba Corel Video Studio untuk mengolah video

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 21 -->

Gambar 1.4 Tampilan Awal Corel VideoStudio X6 Pro

Corel Video Studio dapat digunakan untuk video editing, mulai dari memasukkan data video yang berasal dari perangkat handycam, kamera digital, handphone, dsb hingga melakukan proses burning ke CD untuk dapat dimainkan di video player. Corel Video Studio termasuk video editor yang mudah digunakan dan mempunyai beragam fitur yang lengkap untuk pembuatan video.

### Memotong video

Pada Timeline terdapat 2 view untuk editing yaitu Storyboard View dan Timeline View. Gunakan Timelie View untuk lebih mudah dalam proses editing. Proses memotong video akan ditunjukkan pada gambar berikut:

### Gambar 1.5 Tampilan Memotong Video

### Cara memotong video dari awal waktu, yaitu:

• Tempatkan kursor pada nomor 1 (lihat gambar yang ditandai (1)). • Drag-drop mengikuti arah panah untuk set waktu awal video baru. • Untuk lebih detail dalam menyesuaikan awal waktu video, gunakan editing waktu seperti yang ditunjukan pada nomor 2. 3. Mencoba Krita untuk Animasi

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 22 -->

Gambar 1.6 Tampilan Awal Krita

Krita juga masuk dalam daftar software animasi 2D terbaik yang bisa diunduh secara gratis. Software besutan Krita Foundation ini sering digunakan untuk membuat konsep seni, ilustrasi, komik, dan memberi sentuhan lanjutan pada animasi.

### 4. Mencoba Adobe Soundbooth untuk mengolah audio

Adobe Soundbooth merupakan produk dari adobe inc yang didesain khusus untuk pengolahan sound atau audio. Salah satu cara menggunakan software ini adalah sebagai berikut :

1. Buka Adobe Soundbooth 2. Klik "File","Open" dan load file audio atau file video.

Maklumat audiowave di-load ke dalam sebagian besar dari screen di sebelah kanan sementara gambar video kecil muncul di sudut kiri bawah sekitar file video. 3. Klik dan tarik control point orange yang ditemui di audiowave tersebut. Hal ini menunjukkan au- dio mulai dimainkan. Tekan space bar untuk berhenti dan kembali memainkan audio. 4. Tekan "I" untuk membuat in point dan tekan "O" untuk membuat out point. 5. Pilih tab "Effects" di tengah sisi kiri screen, kemudian pilih menu pull-down. Di sini Anda boleh memilih berbagai audio yang berbeda untuk diterapkan pada audio track. 6. Klik "Apply to file" dan klik "save" kemudian pilih lokasi untuk menyimpan file audio.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 23 -->

Gambar 1.7 Tampilan Adobe Soundbooth

Selain sounbooth, software pengolah audio lain yang versi free software adalah audacity.

### 5. Mencoba Aplikasi Blender untuk pembuatan animasi

Gambar 1.8 Tampilan Utama Blender

### Secara umum tampilan blender terdiri dari beberapa elemen dasar:

• Info Window : Menu utama Blender yang terdiri atas File, Add, Render, dan Help. • 3D View/Viewport : Tampilan yang terdiri dari objek 3D atas objek lainnya. • Toolbar : Terdiri atas daftar tools yang memiliki sifat dinamis menurut objeknya. • Outliner : Struktur data dari objek pada Blender. • Properties : Panel yang memuat berbagai macam perintah untuk memodiﬁkasi objek atau animasi dan bersifat dinamis mengikuti objek atau tools yang sedang aktif. • Timeline : Instruksi yang terkait dengan frame animasi atau untuk sequencer

Blender adalah salah satu software open source yang digunakan untuk membuat konten multi-media khususnya 3 Dimensi. Blender digunakan dalam industri film, game, Web3D dan TV, dan juga untuk permainan video komputer. Tahapan proses belajar pada Blender dibagi menjadi beberapa bagian:

### 1. Modeling

Proses pembuatan model objek dalam bentuk 3D di komputer. Model bisa berupa karakter (makhluk hidup) seperti manusia, hewan, atau tumbuhan atau berupa benda mati, seperti rumah, mobil, peralatan, dan lain-lain. 2. Texturing

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 24 -->

Proses pembuatan dan pemberian warna dan material(texture) pada objek yang telah dimo- delkan sebelumnya sehingga akan tampak suatu kesan yang nyata. Pemberian material atau texture pada objek 3D akan mendefinisikan rupa dan jenis bahan dari objek 3D. 3. Rigging

Proses ini adalah proses pembuatan tulang pada objek. 4. Lighting

Proses pembuatan dan pemberian cahaya pada model sehingga diperoleh kesan visual yang realistis karena terdapat kesan kedalaman ruang dan pembayangan(shadow) objek. 5. Animation

Proses pembuatan animasi untuk model. Animasi berupa gerakan baik gerakan objek/model atau gerakan kamera untuk menciptakan animasi.

### Membuat dan Mengedit Objek dengan Blender :

• Buka Software Blender yang sudah ter-install.

Gambar 1.9 Tampilan Awal Blender

• Klik di luar kotak Blender 2.7.2. Tekan tombol TAB untuk ke Objek Mode

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 25 -->

Gambar 1.10 Tampilan Objek Kubus

• Tekan tombol S(Scale) pada keyboard kemudian tombol Y untuk membuat kubus yang telah ada tadi menjadi sebuah balok fungsinya memanjangkan objek ke sumbu Y.

Gambar 1.11 Tampilan Proses Mengubah Skala Sumbu Y

• Tekan tombol S(Scale) pada keyboard kemudian tombol X untuk membuat memanjang-kan lebar balok fungsinya memanjangkan objek ke sumbu X.

Gambar 1.12 Tampilan Proses Mengubah Skala Sumbu X

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 26 -->

• Tekan tombol S(Scale) pada keyboard kemudian tombol Z untuk meninggikan balok fungsi- nya memanjangkan objek ke sumbu Z.

Gambar 1.13 Tampilan Proses Mengubah Skala Sumbu Z

• Tekan tombol G(Grab) pada keyboard kemudian tombol Z untuk memindahkan balok ter- sebut ke atas, fungsinya memindahkan Objek menggunakan sumbu Z sebagai patokan.

Gambar 1.14 Tampilan Memindahkan Objek Mengunakan Sumbu Z

• Pilih face select pada toolbar yang terdapat di bawah kemudian dengan menggunakan tom- bol CTRL + R pada keyboard yaitu berfungsi untuk Loop Cut (memotong) caranya pilih tengah objek sebagai patokan klik kanan dan geser sesuai keinginan sehingga seperti gambar di bawah menggunakan tampilan CTRL + NUM 7 (tampilan bawah) yang nantinya akan menjadi kaki meja.

### Gambar 1.15 Tampilan Bawah Objek

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 27 -->

• Pilih face select pada toolbar yang terdapat di bawah kemudian tekan dan tahan tombol Shift lalu pilih menggunakan dengan mouse bagian yang ingin dijadikan sebagai kaki meja klik kanan pada mouse untuk memilih.

Gambar 1.16 Tampilan Seleksi Face dari Objek

• Setelah memilih dengan langkah sebelumnya tekan tombol E untuk Extrude region (meman- jangkan) kemudian geser mouse ke arah bawah untuk membuat tinggi kaki meja yang diing- inkan.

### Gambar 1.17 Tampilan Menambah Kaki Meja

• Pilih face select pada toolbar yang terdapat di bawah kemudian tekan dan tahan tombol Shift lalu pilih menggunakan dengan mouse bagian kaki meja sebagai pijakan kaki meja klik kanan pada mouse untuk memilih. Setelah memilih dengan langkah sebelumnya tekan tombol E untuk Extrude region(memanjangkan) kemudian geser mouse ke arah bawah untuk membuat tinggi kaki meja yang diinginkan.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 28 -->

### Gambar 1.18 Tampilan Memanjangkan Kaki Meja

• Setelah selesai extrude pijakan kaki meja langkah selanjutya adalah membuat lebar pijakan tersebut caranya pilih salah satu pijakan kaki meja Ketik Tombol S di keyboard yaitu berfungsi untuk melebarkan Scale kemudian tekan tombol 2 pada keyboard sebagai ukuran lakukan langkah ini untuk membuat 3 pijakan kaki meja selanjutnya sehingga seperti gambar di bawah.

Gambar 1.19 Tampilan Membuat Pijakan Kaki Meja

• Pilih face select pada toolbar yang terdapat di bawah kemudian dengan menggunakan tom- bol CTRL + R pada keyboard yaitu berfungsi untuk Loop Cut (memotong) caranya pilih tengah objek sebagai patokan klik kanan dan geser sesuai keinginan sehingga seperti gambar di bawah yang fungsinya membuat kerangka untuk laci dari meja.

### Gambar 1.20 Tampilan Membuat Kerangka Laci

• Pilih face select pada toolbar yang terdapat di bawah kemudian pilih bagian laci yang ingin di duplikat sebagai laci caranya tekan dan tahan tombol shift pilih dengan menggunakan mouse klik kanan setelah itu shift D untuk menduplikat setelah diduplikat langkah selanjutnya ada-lah dengan menekan tombol G kemudian X agar permukaan laci maju ke arah depan.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 29 -->

### Gambar 1.21 Tampilan Menduplikat Laci

• Pilih face select pada toolbar yang terdapat di bawah kemudian tekan dan tahan tombol Shift lalu pilih menggunakan dengan mouse bagian laci yang ingin di-extrude. Shift dan klik kanan pada mouse untuk memilih. Setelah memilih tekan tombol E untuk Extrude region (meman- jangkan) kemudian geser mouse ke arah depan untuk membuat bagian laci.

### Gambar 1.22 Tampilan Membuat Bagian Laci

• Bagian laci yang telah di-extrude pada langkah sebelumnya kemudian tekan I untuk Insert Keyframe menu kemudain hasilnya di-extrude dengan cara tekan tombol E untuk Extrude region kemudian geser mouse ke arah bawah untuk membuat bagian dalam laci.

### Gambar 1.23 Tampilan Membuat Bagian Dalam Laci

• Untuk membuat tempat laci, cara yang dilakukan adalah dengan memilih permukaan laci pada meja yang ingin dibentuk pilih face select pada toolbar yang terdapat di bawah kemu-dian tekan dan tahan tombol Shift lalu pilih menggunakan dengan mouse bagian laci yang ingin di-

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 30 -->

extrude ke dalam. Shift dan klik kanan pada mouse untuk memilih. Setelah memilih tekan tombol E untuk Extrude region kemudian geser mouse ke arah belakang meja untuk membuat kerangka laci. Agar lebih mudah dalam melihatnya tekan tombol Z(Mode Kerangka /Bentuk).

### Gambar 1.24 Tampilan Mode Kerangka

• Langkah selanjutnya yang dilakukan adalah membuat pegangan lacinya dengan cara tekan tombol A di keyboard 2 kali untuk Deselect all. Pilih add lalu cylinder pada toolbar bagian kiri bawah setelah itu tekan S(scale)  pada keyboard untuk mengatur ukuran pegangan tersebut. Setelah di-scale lalu di rotate terhadap sumbu X.

### Gambar 1.25 Tampilan Membuat Pegangan Laci

• Kemudian untuk membuat pegangan laci lainnya tidak perlu melakukan tahap sebelumnya lagi namun menggunakan perintah Duplikat. Caranya Shift + D kemudian geser terhadap sumbu Y letakkan di tengah-tengah laci.

Gambar 1.26 Tampilan Duplikat Pegangan Laci

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 31 -->

• Langkah selanjutnya yang dilakukan adalah memisahkan objek antara meja dan lacinya agar hasil pada animasi berjalan baik. Caranya dengan men-select laci caranya dengan menekan tombol B di keyboard kemudian block semua komponen yang ada pada laci tersebut setelah semua komponen laci telah terpilih tekan tombol P(separate) untuk memisahkan dengan mejanya.

### Gambar 1.27 Tampilan Memisahkan Objek Meja dengan Laci

• Proses selanjutnya adalah membuat animasi laci menutup dan membuka. Buat posisi awal dari lacinya caranya pilih pada klik frame 0 kemudian ketik I location.

### Gambar 1.28 Tampilan Membuat Animansi Membuka dan Menutup Laci

• Pilih pada frame 60 kemudian klik lacinya, tekan tombol G pada keyboard untuk Grab (me- mindahkan) dan tombol X agar laci berpindah menggunakan patokan sumbu X geser mouse sampai laci tertutup kemudian ketik  I pilih location fungsi ini digunakan untuk animasi menu- tup laci.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 32 -->

### Gambar 1.29 Tampilan Membuat Animasi Membuka dan Menutup Laci

• Pilih pada frame 120 kemudian klik lacinya, tekan tombol G pada keyboard untuk Grab (me- mindahkan) dan tombol X agar laci berpindah menggunakan patokan sumbu X geser sampai laci terbuka kemudian ketik I pilih location fungsi ini digunakan untuk animasi membuka laci.

### Gambar 1.30 Tampilan Membuat Animasi Membuka dan Menutup Laci

### 1.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Lakukan produksi multimedia untuk menghasilkan aset 3 dimensi sederhana seperti garpu dan sendok! | 100 |

### 1.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 33 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 34 -->

## PRAKTIKUM 2: AKUISISI DAN PENGOLAHAN CITRA

Pertemuan ke : 2 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsipprinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan komputasi yang kompleks. |
| --- | --- |
| CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |

2.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Mengerti berbagai macan kamera untuk pengambilan gambar dan video 2. Menjelaskan berbagai macam teknik dalam pengambilan gambar dan video yang baik 3. Menggunakan kamera dengan berbagai teknik dalam pengambilan gambar dan video 4. Mengerti antarmuka salah satu software pengolahan gambar 5. Menggunakan software pengolahan gambar untuk memproduksi karya gambar digital 2.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN

Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menggunakan berbagai macam teknik pengambilan gambar |
| --- | --- | --- |
| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menghasilkan pengolahan produk gambar digital |

|  | atau metode untuk menghasilkan gambar atau foto dari suatu |
| --- | --- |
| obyek dengan merekam pantulan cahaya yang mengenai obyek tersebut pada media yang peka ter- |  |
| hadap cahaya [3]. Alat paling populer untuk menangkap cahaya ini yaitu kamera. Tanpa cahaya dapat |  |
| dikatakan tidak ada foto yang bisa dibuat. |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 35 -->

### 1. Bagian-bagian dari kamera yakni :

a. Lensa terdiri dari:

1) Ring Focus  : Berkaitan dengan daerah ketajaman gambar 2) Zoom : Berkaitan antara jarak subjek dengan lensa 3) Apature    : Berkaitan dengan besar kecil cahaya yang masuk melalui lensa b. Body terdiri dari :

1) View Finder : Monitor berukuran kecil yang terdapat pada kamera yang berfungsi untuk melihat hasil gambar bidikan lensa 2) Instrument : Terdiri dari white balance, gain, shutter speed(kecepatan) 3) Recorder key : Tombol untuk melakukan perekaman maupun menghentikan perekaman (Rec-pause) 4) Switch on-off : Saklar untuk mnghidupkan dan mematikan kamera 5) Instrument VTR  :Terdiri dari: Play, Stop, FF, RW, Pause, Inset, Dubbling, Date/ time, Tele, Wede 6) Docking : Tempat kaset untuk merekam dan memutar kembali 7) Microphone : Pengeras suara yang berfungsi untuk merekam suara 8) Magazine Battery : Tempat battery dipasang

Gambar 2.1 Tampak Depan Handycam

Gambar 2.2 Tampak Belakang Handycam

### 2. Teknik Pengambilan Gambar :

1) Planning : Pergerakan kamera kesamping(kiri-kanan) 2) Tiltting : Pergerakan kamera keatas-bawah 3) Tracking : Pergerakan kamera maju-mundur 4) Zooming : Pergerakan lensa kamera(zoom in-zoom out)

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 36 -->

Garis imajiner sebagai batas perekam dialog. Garis imaginer berfungsi untuk menjaga konsisteni posisi objek antar frame.

Gambar 2.3 Ilustrasi Garis Imajiner

Berbagai variasi gerakan kamera video

Gambar 2.4 Ilustrasi Gerakan Kamera

### 3. Framing (Bidang Pandang)

Framing adalah pembingkaian gambar hasil shot yang ingin ditampilkan sehingga saat kita melakukan proses pembingkaian harus dilakukan secara baik, jelas, karena pada umum-nya kita memindahkan bentuk tiga dimensi/nyata ke dalam suatu frame atau batasan yaitu layer(monitor).

Kompoisisi adalah pengaturan, penyusunan dan pengorganisasian unsur dasar atau elemen gambar dalam sebuah frame dimana gambar tersebut sebaiknya memenuhi kriteria: kesatuan, adanya hubungan psikologi antar elemen dan menciptakan ruang, penonjolan informasi adegan yang menuntun kepada penonton, keserasian dan ciptakan gambar yang mempunyai nilai estetis. 1) Extream Long Shot : Shot sangat jauh, bidang pandang luas, objek lain tampak kecil alam hubungannya dengan latar belakang. 2) Long Shot Shot : Bidang pandang lebih dekat dibanding ELS, objek masih didominasi oleh latar belakang yang luas. 3) Medium Long : Shot yang menghasilkan bidang pandang lebih dekat daripada LS objek manusia biasanya di atas lutut sampai kepala atas. 4) Medium Shot : Objek lebih besar dan dominan, objek manusia nampak dari atas pinggang sampai atas kepala, latar belakang masih sebanding objek. 5) Medium Close UP : Shot agak dekat, objek dada dari dada sampai atas kepala. 6) Close UP Shot : Objek jadi titik perhatian utama dalam shot. Objek manusia biasanya wajah dari bahu sampai atas kepala.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 37 -->

7) Big Close UP : Shot yang menampilkan bagian tertentu dari tubuh manusia, Objek akan mengisi penuh layar lebih jelas dan detail. 8) Two Shot 9) Tree Shot 10) Over Shoulder Shot : Objek utama menghadap kamera, dengan bingkai sampingkiri atau kanan nampak bahu dan sebagian kepala objek lawan bicara. MENGENAL ADOBE PHOTOSHOP

### 1. Toolbox (Window | Tools)

Proses membuat atau meng-edit gambar tentu dibutuhkan peralatan yang memadai. Toolbox dalam Adobe Photoshop berisi sekumpulan tools yang sering dipakai dan memiliki fungsi berbeda-beda.

### Gambar 2.5 Tampilan Toolbox Adobe Photoshop

### 2. Option Bar

Setiap tool(alat) pada toolbox memiliki setting yang bisa diubah sesuai dengan kebu-tuhan untuk itu disediakan Option Bar(Window | Options). Berikut adalah contoh Option Bar pada Rectangular Marquee Tool .

### Gambar 2.6 Tampilan Option Bar

Fungsional Option bar memungkinkan kita untuk mengganti setting seperti: • Membuat seleksi baru • Menggabungkan seleksi yang sudah ada dengan seleksi yang akan dibuat • Mengurangi seleksi yang sudah ada dengan seleksi yang akan dibuat, dll 3.  Palet

Palet digunakan sebagai perangkat bantu sehingga gambar bisa di-edit lebih mudah dan cepat. Palet yang ada pada Photoshop, antara lain: Navigator, Info, Color, Swatches, Styles, History, Actions, Layers, Channels, Paths, Paragraph, Tool Preset dan Character.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 38 -->

### OPERASI DASAR DENGAN PHOTOSHOP

Hasil manipulasi gambar yang bagus pada dasarnya dibuat dengan melakukan operasi-operasi dasar dalam urutan tertentu. Berikut adalah beberapa operasi dasar yang sering digunakan:

### 1. Seleksi, digunakan untuk memilih area gambar yang akan di-edit. Dengan demikian, manipulasi

yang dilakukan pada gambar hanya akan berpengaruh pada bagian yang diseleksi saj 2. Menulis, digunakan untuk membuat tulisan pada gambar. Anda bisa menggunakan Type Tool horizontal (tulisan mendatar), vertical (tulisan vertikal), horizontal mask (seleksi dengan bentuk tulisan mendatar) dan vertical mask (seleksi dengan bentuk tulisan vertikal). Untuk memanipulasi huruf dan paragraf lebih lanjut, Anda bisa mengguna-kan palet Character dan Paragraph. 3. Menggambar, digunakan untuk menggambar. 4. Pewarnaan, digunakan untuk meramu warna. 5. Perpindahan, digunakan untuk memindahkan gambar atau bagian yang diseleksi. Bisa dilakukan dengan tombol panah pada keyboard dan move tool. 6. Transformasi, digunakan untuk mengubah posisi, ukuran atau bentuk gambar. Modifikasi yang

### bisa dilakukan melalui menu Edit | Free Transform atau Edit | Transform antara lain:

• Scale, mengubah besar skala/ukuran gambar • Rotate, memutar gambar • Skew, pergeseran. Misalnya mengubah bujur sangkar menjadi jajaran genjang • Distort, kombinasi antara skew dan scale • Perspective, sebagai contoh membuat bujur sangkar menjadi segitiga sama kaki atau jajaran genjang • Flip, mencerminkan gambar baik secara horizontal maupun vertikal 7. Cropping, digunakan untuk mengubah gambar berupa memotong ataupun memperluas area-nya.

Selain itu bisa ditentukan resolusi, panjang dan lebar gambar yang baru pada hasil cropping.

Dilakukan dengan Crop Tool . 8. Duplikasi. Digunakan untuk menduplikat(menggandakan) gambar atau pattern (pola).

2.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Kamera 3. Handycamp 4. Adobe Photoshop 2.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Sebutkan setiap jenis lensa berdasarkan fungsinya! 2. Sebutkan setiap jenis kamera berdasarkan fungsinya! 3. Sebutkan 3 aplikasi dengan lisesnsi open source dan lisensi berbayar untuk melakukan proses pengolahan gambar! | 30 30 40 |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 39 -->

### 2.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

### Latihan Membuat Tulisan Kreatif:

### 1. Buat sebuah file baru dengan luas 250*150 pixel dengan warna background putih (File | New).

Setelah itu buatlah sebuah tulisan yang anda inginkan dengan Type Tool. 2. Pilih menu Layer | Type | Render Layer…

Select | All Edit | Cut Edit | Paste 3. Tekan dan tahan tombol Ctrl dan klik pada palette layer sebuah layer yang berisi teks, selanjutnya pilih menu Select | Save Selection dan save as “New”. Ctrl+D(deselect) dan hapus layer yang berisi teks tersebut. 4. Pilih panel “Channel-Palette” dengan pilihan yang telah anda simpan tadi (new). 5. Pilih menu Filter | Blur | Gaussian Blur dengan nilai 2,5. 6. Pilih menu Filter | Stylize | Glowing Edges dengan nilai“Edge width=1”, “Edge brightness=8”,

“Smoothness=3”. 7. Ambil channel tersebut sebagai pilihan dengan mengklik tombol “Load channel as selection" di bawah channel palette. 8. Kembali ke layer palette, pilih menu Layer | New Layer dengan nama “madvis”, pastikan layer baru ini sedang di-edit. Pilih menu Edit | Fill, set “Use”’ ke “Black”. Ctrl+D(deselect). 9. Pilih menu Layer | Duplicate Layer.., pastikan “madvis” beserta duplikatnya sedang di-edit dan pastikan juga checkbox ”preserve transparency” juga tidak terpilih. Selanjutnya pilih menu Filter | Other | Offset dengan nilai 2 dan 2. Latihan Mengubah Komposisi Warna:

1. Siapkan gambar yang telah dihasilkan pada aktifitas praktikum sebelumnya. 2. Buka file gambar yang akan di-edit. Ubah warna gambar dengan Hue/Saturation.

Gunakan menu Image | Adjustments | Hue/Saturation dengan nilai “Saturation=100”, tanpa Colorize.* 3. Ubah lagi komposisi warna dengan color balance. Gunakan menu Image | Adjustments | Color

Balance. Pada Tone Balance: Midtones, pilih nilai “Cyan=46” dan “Yellow =33”.* *Keterangan: komposisi warna disesuaikan agar menghasilkan kualitas gambar yang lebih optimal Latihan Memproduksi Video

1. Buka penutup lensa

Gambar 2.7 Operasional penutup lensa

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 40 -->

2. Buka layar LCD dan nyalakan handycam

Gambar 2.8 Operasional layar LCD

3. Tekan Start untuk memulai rekaman

Gambar 2.9 Operasional Rekam Video

4. Tekan Stop untuk mengakhiri rekaman Latihan Memproduksi Foto

1. Buka penutup lensa 2. Buka layar LCD dan nyalakan handycam 3. Pilih mode perekaman foto pada layar LCD

Gambar 2.10 Operasional Pilihan Mode Foto

4. Tekan tombol foto

Gambar 2.11 Operasional Foto Objek

5. Setelah memahami operasional alat, lakukan produksi foto dan video di lingkungan kampus.

Hasil produksi aset multimedia kemudian disimpan pada perangkat komputer laboratorium untuk digunakan pada pertemuan berikutnya.

### TOOLS AI

Dalam mengolah citra digital juga dapat menggunakan tools AI seperti ChatGBT, Firefly dan lan sebagainya.

ChatGPT susun prompt (screenshot), Firefly Generate, gabung foto+AI masking, label AI Generated.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 41 -->

### 2.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Lakukan produksi multimedia untuk menghasilkan poster digital dengan tema Sustainable Development Goals | 100 |

### 2.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 42 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 43 -->

## PRAKTIKUM 3: RECORDING & EDITING AUDIO

Pertemuan ke : 3 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsipprinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan komputasi yang kompleks. |
| --- | --- |
| CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |

3.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Mengerti layar kerja dari salah suata software untuk membuat dan mengoptimalkan aset audio 2. Menerapkan suatu teknologi untuk memproduksi aset audio yang berkualitas

1.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam merekam dan mengoptimalkan kualitas audio untuk diintegrasikan ke dalam film animasi |
| --- | --- | --- |

### 1. DASAR AUDIO

Proses pengolahan audio atau sound untuk pengisian suara pada pembuatan film kartun ada 2 metode yaitu menggunakan istilah proses dubbing kering atau tanpa visual dan menggunakan proses dubbing basah atau menggunakan visual. Dubber basah, yaitu membuat animasi terlebih dulu pada Macromedia Flash, setelah penganimasian selesai baru melakukan perekaman suara dan di-edit dengan menggunakan Adobe Soundbooth.

Sekarang ini file-file audio telah begitu banyak dihasilkan oleh peranti teknologi yang bermacam- macam, seperti handphone, kamera digital, handycam, Mp3 player, Mp4 player dan lain sebagainya.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 44 -->

Namun, hasilnya mungkin juga belum sesuai dengan yang diinginkan, misalnya terdapat bunyi desis atau noise yang sangat mengganggu. Proses Penggunaan Adobe Soundbooth atau Audacity, dapat melakukan edit-ing sekaligus memperbaiki file suara atau audio menjadi lebih optimal.

### 2. KOMPRESI AUDIO

Kompresi audio merupakan salah satu solusi yang cukup populer untuk digunakan terkait dengan masalah storage dan akses secara real-time. Teknik kompresi digunakan se-optimal mungkin dengan memperhatikan beberapa aspek sehingga menghasilkan teknik kompresi yang lossless dan lossy. Untuk kebutuhan sehari – hari teknik lossy banyak digunakan, mengingat rasio kompresi yang besar sehingga sangat berpengaruh pada aspek storage dan keterbatasan kemampuan telinga manusia.

Pada teknik kompresi lossless terdapat teknik Free Lossless Audio Codec (FLAC) yang memanfaat- kan tingginya korelasi antara sampel pada audio. Pada teknik kompresi lossy terdapat LPC, CELP, dan MPEG. merupakan teknologi kuno yang digunakan untuk suara manusia. Kendala kompresi audio: • Perkembangan sound recording yang cepat dan beranekaragam • Nilai dari audio sample berubah dengan cepat Losless audio codec tidak mempunyai masalah dalam kualitas suara, penggunaannya dapat difokuskan pada: • Kecepatan kompresi dan dekompresi • Derajat kompresi • Dukungan hardware dan software Lossy audio codec penggunaannya difokuskan pada: • kualitas audio • faktor kompresi • kecepatan kompresi dan dekompresi • inherent latency of algorithm (penting bagi real-time streaming) • dukungan hardware dan software Metode Kompresi Audio: • Metode Transformasi Menggunakan algoritma seperti MDCT (Modified Discreate Cosine Transform) untuk mengkonversi gelombang bunyi ke dalam sinyal digital agar tetap dapat didengar oleh manusia (20 Hz s/d 20kHz) yaitu menjadi frekuensi 2 s/d 4kHz dan 96 dB. • Metode Waktu Menggunakan LPC (Linier Predictive Coding) yaitu digunakan untuk speech (pidato), dimana LPC akan menyesuaikan sinyal data pada suara manusia, kemudian mengirimkannya ke pendengar. Jadi seperti layaknya komputer yang berbicara dengan bahasa manusia dengan kecepatan 2,4 kbps PENGENALAN SOFTWARE

Perangkat lunak editing video digunakan untuk melakukan edit pada video yang meliputi : pe- motongan, penambahan transisi, penambahan teks, penambahan grafik atau gambar, penambahan suara, penambahan animasi dan share ke berbagai format video. Saat ini, banyak perangkat lunak yang tersedia. Pada praktikum ini, akan digunakan Corel Video Studio X6. Terdapat 3 jendela utama pada Corel Video Studio X6, yaitu (1) Preview Window, (2) Library, dan (3) Timeline

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 45 -->

### Gambar 3.1 Tampilan Utama Corel Video Studio X6

1.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. File video 3. Corel Video Studio X6 1.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan proses yang dilakukan dalam tahap recording audio! 2. Jelaskan proses yang dilakukan dalam tahap editing audio! 3. Jelaskan proses yang dilakukan dalam tahap mixing audio! 4. Jeaskan proses yang dilakukan dalam tahap mastering audio! | 25 25 25 25 |

### 1.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

### 1. Merekam Suara

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 46 -->

Proses merekam suara dapat dilakukan dengan menggunakan software Audio Adobe Sound- booth CS3. Langkah-langkahnya sebagai berikut:

1. Pastikan kabel headseat telah terpasang pada soundcard dengan benar dan telah diaktifkan.

2. Kemudian buat file baru dengan cara klik File Record (Ctrl+R).

3. Atur setting-nya sesuai dengan sumber suara dan akhiri dengan menekan tombol Start

Recording.

4. Setelah selesai merekam suara, kemudian klik tombol Stop Recording.

### 2. Mengurangi Noise

Noise adalah gangguan-gangguan suara yang muncul dari luar yang tidak diharapkan pada saat proses perekaman suara, misalnya suara komputer, kipas angin, kendaraan atau hujan. Langkah-langkahnya :

1. Klik menu Task Clean Up Audio Capture Noise Print.

2. Sekarang blok semua layer, klik tombol Noise.

3. Pastikan pilihan Use Captured Noise Print tercentang

4. Klik Preview untuk melihat hasil sementara, kemudian klik OK.

### 3. Memberikan efek audio

1. Setelah file audio dimuat ke Soundbooth, Anda dapat mulai mengedit. Anda dapat memotong bagian yang tidak diinginkan, menyesuaikan volume, menambahkan efek, dan lain-lain. 2. Untuk memotong bagian yang tidak diinginkan, pilih alat potong di toolbar dan pilih area yang ingin Anda hapus, lalu tekan tombol Hapus. di keyboard Anda. 3. Jika Anda ingin mengatur volume, pilih bagian audio yang ingin Anda ubah dan buka Efek di menu atas. Di sana Anda akan menemukan opsi untuk menambah atau mengurangi volume. 4. Untuk menambahkan efek, buka “Efek” di menu atas. Anda dapat memilih dari berbagai efek, seperti reverb, echo, equalization, dan banyak lagi. 5. Setelah Anda selesai mengedit audio, pastikan untuk menyimpan perubahan

Anda. Buka "File" di menu atas dan pilih "Simpan" atau "Simpan Sebagai" untuk menyimpan file yang telah diedit. 6. Siap! Anda telah berhasil mengedit file Anda audio dengan Adobe Soundbooth.

### 1.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 47 -->

| 1. | CPL 05P01 | CPMK 5.4 | Lakukan produksi aset audio mulai dari recording sampai mixing untuk mendukung hasil praktikum terkait animasi!. audio 30-60 dtk recording sampai mixing untuk animasi, narasi sendiri + 1 musik/SFX legal, MP3. | 100 |
| --- | --- | --- | --- | --- |

### 1.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 48 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 49 -->

## PRAKTIKUM 4: EDITING DAN POST-PROCESSING VIDEO

Pertemuan ke : 4 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 |  | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsip- |  |
| --- | --- | --- | --- |
|  |  | prinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan |  |
|  |  | komputasi yang kompleks. |  |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

4.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Mahasiswa mengerti antarmuka software editing video yaitu Corel Video Studio. 2. Mahasiswa meng-edit file video, mulai dari memotong video, menambahkan transisi, teks, image, suara, animasi, dan menambahkan filter. 3. Mahasiswa mampu menyatukan komponen video(rendering).

4.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menerapkan pemodelan karakter 2D |
| --- | --- | --- |

### 4.3. TEORI PENDUKUNG

1. KOMPRESI VIDEO Kompresi video yaitu salah satu bentuk kompresi data yang bertujuan untuk mengecilkan ukuran file video. Video kompresi mengacu untuk mengurangi jumlah data yang digunakan untuk mewakili video digital gambar, dan merupakan kombinasi dari ruang kompresi gambar dan temporal kompresi gerak. Tujuan dari pemampatan/kompresi video yakni:

a. Minimisasi bit rate dalam penyajian digital sinyal video b. Memelihara tingkat kualitas sinyal yang dikehendaki c. Meminimalkan kompleksitas codec (coder dan decoder-penyandi dan pengurai) d. Kandungan delay atau penundaan

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 50 -->

Dalam melakukan kompresi video, pemilihan metode pemampatan yang akan digunakan melibat-kan tukar tambah (trade off) pada empat dimensi yakni Efisiensi, Kualitas Sinyal, Kompleksitas, Tindaan Pengkodean. Tidak memaksakan untuk bagus disemua dimensi ini. Tetap ada yang harus dikorbankan, tergantung kebutuhan kompresi yang dilakukan. Sinyal Video cocok untuk dimampatkan karena beberapa faktor, yaitu: a. Korelasi Spasial : Korelasi antar piksel-piksel tetangga b. Korelasi Spektral : Citra-citra berwarna c. Korelasi temporal : Korelasi antara piksel pada frame yang berbeda Serta terdapat informasi yang sangat tidak relevan (dari sudut pandang perseptual) dalam data video. Dalam mengkompresi data baik audio maupun video terdapat dua jenis kompresi yaitu: 1.  Pengkodean Losless merupakan proses yang dapat dibolak-balik pemulihan sempurna sebelum dan sesudah memiliki nilai yang sama persis. Dalam menggunakan pengkodean ini biasanya tidak mem- perdulikan media. Proses penguraian mengembalikan kembali ke asal secara penuh misalnya RLC, Huffman Codding, Arithmetic Coding. 2. Pengkodean Lossy Merupakan proses yang tidak dapat dibolak-balik, pemulihannya tidak sesempurna video hasil rekonstruksi secara numerik. Dalam menggunakan pengkodean ini mempe- dulikan semantik dari data yang bersangkutan. Teknik Video Coding:

• H.261 dan H.263 • Dirancang untuk video conferencing, aplikasi video telepon menggunakan jaringan telepon ISDN • Kecepatan bitrate antara p x 64 Kbps, dimana p adalah frame rate (antara 1 sampai 30) • Mempunyai 2 tipe frame yaitu: Intra-frame (I-frame) dan Interfame (P frame) • MPEG audio-video • Standar audio video transmission • MPEG bertujuan membuat kualitas VHS pada VCD dengan ukuran 352 x 240. 2. PENGENALAN SOFTWARE

Perangkat lunak editing video digunakan untuk melakukan edit pada video yang meliputi : pe- motongan, penambahan transisi, penambahan teks, penambahan grafik atau gambar, penambahan suara, penambahan animasi dan share ke berbagai format video. Saat ini, banyak perangkat lunak yang tersedia. Pada praktikum ini, akan digunakan Corel Video Studio X6. Terdapat 3 jendela utama pada Corel Video Studio X6, yaitu (1) Preview Window, (2) Library, dan (3) Timeline

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 51 -->

Gambar 4.1 Tampilan Utama Corel Video Studio X6 4.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. File video 3. Corel Video Studio X6 4.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Sebutkan minimal 3 aplikasi untuk melakukan proses pengolahan video! 2. Jelaskan faktor yang mempengaruhi kualitas hasil produksi editing video! 3. Jelaskan terkait terminologi kompresi audio dan video! | 30 40 30 |

### 4.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

1. Editing Video Melakukan serangkaian aktifitas untuk membuat video menjadi lebih interaktif. Proses memulai peng- edit-an, membutuhkan data seperti video, sound dan lainnya. Masukkan data yang akan di-edit dengan

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 52 -->

cara Insert Media File To Library melalui menu File atau shortcut gambar folder yang telah disediakan. Perhatikan gambar berikut:

Gambar 4.2 Tampilan Menambahkan Aset Video Mulailah editing dengan menambahkan data ke Timeline. Berikut contohnya:

Gambar 4.3 Tampilan Menambahkan Aset Video ke Timeline a. Memotong Video Pada Timeline terdapat 2 view untuk editing yaitu: Storyboard View dan Timeline View. Gunakanlah Timelie View untuk lebih mudah dalam proses editing. Proses memotong video di-tunjukkan gambar berikut:

Gambar 4.4 Tampilan Memotong Video Cara memotong video dari awal waktu, yaitu:

1) Tempatkan kursor pada nomor 1 (lihat gambar yang ditandai (1)). 2) Drag-drop mengikuti arah panah untuk set waktu awal video baru.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 53 -->

3) Untuk lebih detail dalam menyesuaikan awal waktu video, gunakan editing waktu seperti yang ditunjukan pada nomor 2. Untuk pemotongan video dari akhir waktu,

1) Tempatkan kursor pada tanda akhir video. 2) Drag-drop ke arah awal waktu. 3) Untuk lebih detail dalam menyesuaikan awal waktu video, gunakan editing waktu seperti yang ditunjukan pada nomor 2.

b. Menambahkan Transisi. Transisi digunakan sebagai tambahan efek penghubung diantara 2 video yang digabung. Beri-kut langkah-langkah dalam menambahkan transisi:

1) Tempatkan 2 video pada Timeliene. 2) Drag-drop efek transisi ke posisi antar 2 video.

Gambar 4.5 Tampilan Menambahkan Transisi c. Menambahkan Teks Untuk membuat video lebih interaktif, bisa ditambahkan serangkaian teks. Langkah-langkah penambahan teks adalah sebagai berikut:

1) Pilih ikon huruf "T"/ Title. 2) Double klik pada Preview Window. 3) Tambahkan teks. Adapun cara lainnya:

1) Pilih ikon huruf "T"/ Title. 2) Drag-drop file teks pada Library. 3) Double klik pada Preview Window. 4) Tambahkan teks.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 54 -->

Gambar 4.6 Tampilan Menambahkan Teks d. Menambahkan Image Selain bisa menambahkan teks agar video lebih interaktif, bisa pula menambahkan beberapa image. Langkahnya dengan melakukan drag-drop file image dari Library ke bagian Timeline.

Gambar 4.7 Tampilan Menambahkan Image e. Menambahkan Suara Efek suara bisa membuat suatu adegan atau aksi pada sebuah video menjadi lebih kuat dalam penyampaiannya. Contohnya ketika ada adegan sedih, digunakan pula efek suara yang bertema sedih, maka akan menambah kekuatan adegan dalam penyampaian adegan tersebut. Efek suara bisa ditambahkan dengan melakukan drag-drop pada bagian voice track atau music track.

Gambar 4.8 Tampilan Menambahkan Suara f. Menambahkan Animasi Dalam editing video, bisa juga menambahkan animasi sederhana. Berikut setiap langkahnya:

### 1) Pilih Graphic.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 55 -->

2) Pastikan di opsi memilih Flash Animation. 3) Drag-drop file animasi ke awal atau akhir video, file animasi bisa juga kreasi sendiri.

Gambar 4.9 Tampilan Menambahkan Animasi g. Menambahkan Filter Ada juga penambahan filter pada video. Langkah penambahan filter adalah:

1) Pilih Filter. 2) Drag-drop filter yang diinginkan ke video.

Gambar 4.10 Tampilan Menambahkan Filter 2. Produksi Video Jika kita telah selesai dalam peng-edit-an video dengan menambahkan file-file tertentu, langkah selanjutnya adalah menyatukan semua file tersebut menjadi satu kesatuan(rendering). Langkahnya adalah sebagai berikut:

### 1). Pilih tab Share.

Gambar 4.11 Tampilan Menu Share 2). Pilih format video yang diinginkan.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 56 -->

Gambar 4.12 Tampilan Pilihan Format Video 3). Tentukan lokasi penyimpanan kemudian pilih Save. 4.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Lakukan produksi multimedia untuk menghasilkan video dengan tema Sustainable Development Goals atau video terkait company profile dari aset aktivitas praktikum pada pertemuan 2! | 100 |

### 4.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 57 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 58 -->

## PRAKTIKUM 5: KOMPRESI DAN STREAMING VIDEO

Pertemuan ke : 5 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsipprinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan komputasi yang kompleks. |
| --- | --- |
| CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |

5.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu: 1. Menjelaskan bitrate, codec, protokol RTMP/SRT dan penyebab buffering. 2. Menyiarkan video P4 via OBS ke YouTube Live (unlisted) atau RTMP lokal + merekam lokal. 3. Menganalisis stats (dropped frames, bitrate) dan memilih profil kompresi.

5.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual khususnya dalam kompresi dan streaming video |
| --- | --- | --- |

Video digital merupakan kumpulan frame yang ditampilkan secara berurutan sehingga menghasilkan persepsi gerak. Karena setiap frame dapat mengandung informasi dalam jumlah besar, video membutuhkan kapasitas penyimpanan dan bandwidth yang relatif tinggi. Kompresi video digunakan untuk mengurangi jumlah data tersebut dengan tetap mempertahankan kualitas visual pada tingkat yang dapat diterima. Dalam konteks multimedia, kompresi menjadi bagian penting baik untuk penyimpanan video (Video on Demand/VOD) maupun untuk distribusi video secara langsung (live streaming). Standar H.264/AVC dan H.265/HEVC merupakan teknologi pengodean video yang dirancang untuk meningkatkan efisiensi representasi video

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 59 -->

dan mendukung berbagai kebutuhan komunikasi, penyimpanan, penyiaran, serta Internet streaming (ITU-T, 2026a; ITU-T, 2026b).

1. Codec H.264 dan H.265

Codec (coder-decoder) merupakan teknologi yang digunakan untuk melakukan proses pengodean dan penguraian kembali data multimedia. H.264/AVC merupakan salah satu standar pengodean video yang banyak digunakan karena menyediakan keseimbangan antara kualitas, ukuran data, dan kompatibilitas perangkat. Sementara itu, H.265/HEVC dikembangkan sebagai evolusi teknologi pengodean sebelumnya dengan tujuan meningkatkan efisiensi kompresi sehingga video dengan kualitas tertentu dapat direpresentasikan dengan kebutuhan bitrate yang lebih rendah pada kondisi tertentu. Perbedaan efisiensi tersebut membuat pemilihan codec perlu mempertimbangkan kualitas yang diinginkan, kemampuan perangkat, beban proses encoding, serta dukungan platform tujuan (ITU-T, 2026a; ITU-T, 2026b).

2. Bitrate dan Kualitas Video

Bitrate menunjukkan jumlah data yang dialokasikan untuk merepresentasikan video dalam satuan waktu, umumnya dinyatakan dalam kbps atau Mbps. Bitrate merupakan salah satu parameter utama yang memengaruhi kualitas visual sekaligus kebutuhan bandwidth. Semakin tinggi bitrate, semakin besar data yang dapat digunakan untuk mempertahankan detail gambar, tetapi kebutuhan bandwidth dan ukuran file juga meningkat. Sebaliknya, bitrate yang terlalu rendah dapat menyebabkan artefak kompresi seperti blocking, hilangnya detail, dan gambar yang tampak kurang tajam. Dalam praktik live streaming, YouTube memberikan rentang bitrate berdasarkan resolusi, frame rate, dan codec; misalnya untuk 720p30 dan 1080p30, rekomendasi H.264 masing-masing berada pada sekitar 3–8 Mbps dan 5–14 Mbps. Dengan demikian, nilai 2.500–6.000 kbps dapat digunakan sebagai rentang praktikum untuk mengamati hubungan antara bitrate dan kualitas, tetapi bukan angka universal untuk semua platform dan kondisi streaming.

3. Konsep Live Streaming Video

Live streaming adalah proses pengiriman data audio-video secara terus-menerus sehingga pengguna dapat menyaksikan konten ketika proses produksi dan distribusi masih berlangsung. Secara konseptual, alur streaming dapat digambarkan sebagai sumber video → encoding → pengiriman melalui protokol streaming → server/CDN → penonton. Pada sisi pengirim, aplikasi seperti OBS Studio melakukan capture dan encoding terhadap sumber video, kemudian mengirimkan stream menuju layanan streaming. Platform seperti YouTube selanjutnya dapat melakukan transcoding untuk menghasilkan beberapa kualitas video yang sesuai dengan kemampuan perangkat dan koneksi penonton.

4. RTMP, SRT, dan Distribusi melalui CDN

Protokol komunikasi merupakan bagian penting dalam proses pengiriman video dari encoder menuju server streaming. RTMP/RTMPS merupakan salah satu protokol yang digunakan dalam proses video ingestion ke platform streaming. YouTube, misalnya, menyediakan RTMP/RTMPS sebagai protokol untuk menerima live stream dari encoder. Setelah stream diterima, platform dapat melakukan transcoding sehingga satu sumber video dapat disediakan dalam berbagai resolusi dan bitrate untuk menyesuaikan kondisi jaringan penonton. Dalam arsitektur distribusi berskala besar, CDN (Content Delivery Network) berfungsi membantu mendistribusikan konten dari infrastruktur server menuju pengguna melalui lokasi distribusi

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 60 -->

yang lebih dekat dengan pengguna. Dengan demikian, streaming tidak hanya berkaitan dengan proses encoding, tetapi juga dengan efisiensi pengiriman dan distribusi data kepada banyak penonton.

5. Hubungan Kompresi dan Streaming

Berdasarkan konsep tersebut, kompresi dan streaming video merupakan dua proses yang saling berkaitan. Encoding H.264/H.265 menentukan bagaimana video direpresentasikan dalam bentuk data yang lebih efisien, sedangkan bitrate menentukan besarnya data yang harus ditransmisikan setiap detik. Data hasil encoding kemudian dikirim melalui protokol seperti RTMP/RTMPS menuju layanan streaming dan selanjutnya didistribusikan kepada penonton. Dalam proses tersebut, mahasiswa perlu memahami bahwa peningkatan kualitas tidak selalu berarti meningkatkan bitrate setinggi mungkin, karena bitrate harus disesuaikan dengan resolusi, frame rate, codec, kemampuan jaringan, serta target latensi dan stabilitas. Oleh karena itu, praktikum kompresi dan streaming video pada dasarnya merupakan latihan untuk menemukan konfigurasi yang memberikan keseimbangan antara kualitas visual, efisiensi data, dan keberlangsungan transmisi.

6. Arsitektur Streaming

Sebelum memulai praktikum, mahasiswa memahami alur berikut:

Kamera/Video → OBS Studio → Encoding H.264 → RTMP/RTMPS → YouTube → CDN → Penonton

Pada sisi OBS, video dan audio ditangkap kemudian dikompresi (encoding). Data hasil encoding dikirim ke server YouTube menggunakan protokol streaming. YouTube selanjutnya memproses dan mendistribusikan video kepada penonton.

5.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Laptop/PC 2. Webcam atau kamera 3. Mikrofon/headset 4. Koneksi internet yang stabil 5. Disarankan menggunakan koneksi dengan upload speed minimal 5–10 Mbps untuk eksperimen

720p–1080p. 6. OBS Studio 30 7. Akun Google/YouTube 8. HandBrake — digunakan pada praktikum kompresi/VOD

5.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Bitrate vs resolusi vs kualitas, berapa untuk 1080p30? 2. Bedakan RTMP dan SRT! 3. 3 penyebab buffering dan solusinya! | 35 30 35 |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 61 -->

### 5.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

### Langkah 1 — Login ke YouTube

1. Buka YouTube. 2. Login menggunakan akun Google. 3. Buka YouTube Studio. 4. Pilih Create → Go live. Jika akun belum dapat melakukan live streaming, YouTube dapat meminta proses verifikasi atau aktivasi fitur terlebih dahulu. Aktivasi ini sebaiknya dilakukan sebelum hari praktikum. Langkah 2 — Buat Live Stream Pada YouTube Studio:

1. Pilih Go Live. 2. Pilih metode streaming menggunakan Encoder. 3. Buat jadwal atau gunakan opsi untuk melakukan streaming sekarang. 4. Catat informasi:

o Stream URL/server o Stream Key PERINGATAN: Stream Key bersifat rahasia. Jangan memasukkannya ke laporan, screenshot, atau membagikannya kepada orang lain. Langkah 3 — Membuka OBS

1. Jalankan OBS Studio. 2. Jika muncul Auto-Configuration Wizard, pilih konfigurasi untuk streaming. 3. Pilih resolusi dasar sesuai kemampuan komputer. Untuk praktikum, gunakan:

Parameter Nilai awal

Resolution 1280 × 720

FPS 30 fps

Video Codec H.264

Audio Codec AAC

Audio Bitrate 128 kbps

Keyframe Interval 2 detik

Langkah 4 — Membuat Scene Pada bagian Scenes:

1. Klik +.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 62 -->

2. Beri nama: Streaming Praktikum Langkah 5 — Menambahkan Kamera Pada bagian Sources:

1. Klik +. 2. Pilih Video Capture Device. 3. Pilih webcam/kamera. 4. Atur resolusi kamera menjadi: 1280 × 720, 30 FPS 5. Klik OK.

Langkah 6 — Menambahkan Mikrofon Pada Audio Mixer:

1. Pastikan mikrofon terdeteksi. 2. Periksa indikator level audio. 3. Lakukan pengujian suara. Pastikan level audio tidak terus-menerus berada pada kondisi clipping. Langkah 7 – Pengaturan Output

Settings → Output Pilih:

Output Mode: Advanced Kemudian pilih tab Streaming. Gunakan konfigurasi awal:

Parameter Nilai

Encoder H.264

Rate Control CBR

Bitrate 4.000 kbps

Keyframe Interval 2 s

Audio Bitrate 128 kbps

Untuk eksperimen berikutnya, bitrate dapat diubah menjadi:

• 2.500 kbps • 4.000 kbps • 6.000 kbps Langkah 8 -- Pengaturan Video

Settings → Video Atur:

Parameter Nilai

Base (Canvas) Resolution 1280 × 720

Output (Scaled) Resolution 1280 × 720

Common FPS Values 30

Kemudian klik Apply → OK. Langkah 9 — Memasukkan Stream Key

Pada OBS:

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 63 -->

Settings → Stream Pilih: Service → YouTube Kemudian:

1. Login dengan akun YouTube jika tersedia. 2. Atau gunakan Stream Key dari YouTube Studio. 3. Masukkan stream key. 4. Klik Apply. Pastikan server streaming yang digunakan sesuai dengan konfigurasi YouTube. Langkah 10 — Memulai Streaming

Sebelum melakukan live:

1. Pastikan kamera aktif. 2. Pastikan mikrofon aktif. 3. Pastikan scene sudah benar. 4. Pastikan bitrate sudah sesuai. 5. Pastikan koneksi internet stabil. 6. Periksa kembali bahwa Stream Key tidak terlihat oleh orang lain. Kemudian pada OBS: Start Streaming Tunggu beberapa saat sampai YouTube menerima stream. Pada YouTube Studio akan muncul preview video. Lakukan beberapa seting berbeda untuk resolusi, bitrate, dan FBS. Lalau amati perbedaan kualitas videonya. 5.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Siaran 2 menit + file VOD terkompresi + analisis 1 paragraf kenapa setting dipilih. | 100 |

### 5.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 64 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 65 -->

## PRAKTIKUM 6: PEMODELAN KARAKTER 2D

Pertemuan ke : 6 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 |  | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsip- |  |
| --- | --- | --- | --- |
|  |  | prinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan |  |
|  |  | komputasi yang kompleks. |  |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

6.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Menjelaskan urgensi implementasi pemodelan karakter 2 Dimensi. 2. Merancang dan mengimplementasi pemodelan karakter 2 Dimensi.

6.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menerapkan pemodelan karakter 2D |
| --- | --- | --- |

### 6.3. TEORI PENDUKUNG

Salah satu tahapan dalam desain dan pengembangan film animasi yaitu pemodelan karakter. Pemodelan karakter merupakan rancangan karakter film animasi mulai dari menentukan jenis peno- kohan, obyek pendukung, penggambaran karakter(sketsa), desain karakter, dan pewarnaan. Pemo- delan karakter telah menjadi komponen utama dari karya fiksi dalam dunia animasi.

Pembuatan karakter harus sesuai dengan sifat dan peran dari tokoh pada sebuah film. Sebagai contoh, seorang tokoh utama dalam suatu film, adalan si Arman, maka tokoh si Arman dideskripsikan secara detail sebagai berikut:

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 66 -->

7. Tabel 1.1. Data Karakter

| Nama | Arman |
| --- | --- |
| Usia | 10 tahun |
| Sifat | Sopan, baik, cerdas, periang, sedikit nakal |
| Kulit | Sawo matang |
| Rambut | Hitam, lurus |
| Mata | Coklat |

Bisa juga ditambahkan data keterangan mengenai siapa sebenarnya si tokoh yang dibuat da-lam suatu film. Berikut adalah contoh pemodelan karakter:

Gambar 6.1 Perancangan Model 2 Dimensi

6.4 HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Drawing pad 3. Adobe photoshop 4. Gimp 5. Inkscape 6.5 PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan teminologi dari animasi! 2. Sebutkan 5 jenis animasi! 3. Sebutkan 12 prinsip dasar animasi! | 15 25 60 |

### 6.6 LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 67 -->

### Langkah-Langkah Praktikum:

### 1. Jenis Karakter Pada Film.

Secara umum jenis penokohan dalam cerita bisa dibagi menjadi 3, tokoh protagonis, antagonis, dan tokoh abu-abu. Secara singkat protagonis bisa diartikan sebagai tokoh utama yang menjadi "pahlawan" atau tokoh utama yang baik, kemudian antagonis adalah tokoh jahat, dan tokoh abu-abu yang tidak jelas apakah dia protagonis atau antagonis, kecenderungan penokohan pada film animasi saat ini adalah penempatan tokoh-tokoh “gray” sebagai tokoh utama karena bisa mengembangkan cerita secara lebih dalam tanpa harus keluar dari cerita yang sudah ada atau cerita buat.

2. Pemodelan Karakter. Dalam membuat suatu karakter, ada beberapa hal yang perlu dilakukan, yaitu: perancangan karakter => pemodelan => pewarnaan. Perancangan karakter dilakukan dengan membubuhkan ide pada media perancangan berupa kertas atau dengan kata lain membuat sketsa. Pemodelan karakter menjadi file digital yang dilakukan pada software pengeditan image seperti photoshop, GIMP, dan sejenisnya. Perwarnaan merupakan dimana file digital karakter diberi warna. Namun di era modern sekarang ini, untuk membuat pemodelan karakter bisa menggunakan Drwaing Pad sehingga file yang dihasilkan sudah dalam bentuk digital. Pada praktikum ini, lakukanlah tugas berikut :

a. Carilah minimal satu perancangan karakter mulai dari sketsa sampai pewarnaan di internet, unduhlah gambarnya. b. Lakukan analisis pada langkah-langkah pembuatan karakter tersebut. c. Tulislah hasil analisis anda. 6.7 POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Buatlah satu rancanglah pemodelan karakter mulai dari sketsa, pemodelan, dan pewarnaan! Tambahkan pula data karakternya! 2. Buatlah sketsa gambar kunci (key) berjalan pose-topose dari karakter yang telah dibangun (poin 1)! | 50 50 |

### 6.8 HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 68 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 69 -->

## PRAKTIKUM 7: TEKNIK ANIMASI 2D INTERAKTIF

Pertemuan ke : 7 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 |  | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsip- |  |
| --- | --- | --- | --- |
|  |  | prinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan |  |
|  |  | komputasi yang kompleks. |  |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

7.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu menerapkan teknik animasi dalam desain dan pengembangan film animasi 7.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dapat menerapkan teknik animasi |
| --- | --- | --- |

### 7.3. TEORI PENDUKUNG

Teknik Animasi 2D Terdapat tiga teknik dasar pembuatan animasi, yaitu: Frame by frame, Tweening dan Script. Masing-masing teknik dapat dieksplorasi untuk membuat berbagai tampilan animasi. Selain itu terda-pat teknik tambahan untuk memperkaya tampilan animasi, seperti: Motion Guide dan Masking. 1. Frame by Frame

Teknik frame by frame merupakan teknik merangkai urutan gambar yang diletakkan pada se- jumlah frame. Pada dasarnya pembuatan animasi frame by frame memerlukan minimal dua fra-

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 70 -->

me. Jika pada frame 1 diletakkan objek lingkaran warna merah, pada frame 2 diletakkan objek lingkaran warna kuning, maka pada saat movie dimainkan akan tampil animasi warna kelip merah dan kuning. 2. Shape Tweening

Teknik shape tweening digunakan untuk menganimasi objek shape(kurva), seperti lingkaran, persegiempat, poligon atau bentuk bebas. Teknik pembuatannya adalah: 1) Membuat objek shape pertama pada frame awal. 2) Membuat objek shape kedua pada frame akhir. 3) Memberikan tweening shape diantara frame awal dan frame akhir. 3. Motion Tweening

Teknik tweening tipe motion atau motion tweening digunakan untuk menganimasi objek-objek seperti teks, group objek, dan simbol. Teknik pembuatannya adalah: 1) Mengatur objek pada frame awal. 2) Mengatur objek pada frame akhir. 3) Memberikan tweening motion diantara frame awal dan frame akhir.

7.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Aplikasi Krita 7.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Sebutkan minimal 3 portal/website yang menyediakan aset animasi 2/3 dimensi secara berbayar dan gratis! 2. Jelaskan 3 teknik dalam proses produksi film animasi 2 dimensi! 3. Jelaskan perbedaan antara pengembangan animasi tradisional dengan animasi digital! | 30 30 40 |

### 7.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

1. Buka apliaksi krita 2. File > New 1280x1024 72dpi nama walk-cycle > tab background canvas-color (Image > Image

### Properties bila perlu) > Create > Window > Workspace > Animation.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 71 -->

Gambar 7.1. Tampilan Aplikasi Krita 3. Buat 2 layer transparan (+/Ins): bawah environment, atas walkcycle. Di environment pakai

Straight Line Tool garis horizon.

Gambar 7.2. Layer stack environment + walkcycle. 4. Gambar garis tanah

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 72 -->

Gambar 7.3. Garis Tanah 5. Di walkcycle gambar kepala + torso stick figure.

Gambar 7.4. Kepala Awal 6. klik kanan frame 0 Timeline > Create Duplicate Frame (JANGAN Blank agar tidak hilang). Ikon onion muncul = animasi. Duplikat ke frame 1, Move Tool (T) + Shift+Panah Atas. Nyalakan onion off jadi on.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 73 -->

Gambar 7.5. Duplikate Frame dan Onion On 7. lakukan pembyatan gambar ulang

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 74 -->

### Gambar 7.6 Frame lalu merah (hitam + siluet merah).

Gambar 7.7. Frame depan hijau. 8. Gambar 2 ekstrem: kaki terbuka maksimal vs satu lurus satu tekuk. Manfaatkan onion menumpuk. Perhatian: Krita anggap putih sebagai warna, pastikan layer transparan (bila terlanjur putih pakai filter Color to Alpha, tapi cegah dari awal).

### Gambar 7.8. Dua ekstrem, kaki semi-transparan untuk salin.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 75 -->

9. Copy: klik kanan frame > Copy Keyframes > klik posisi > Paste Keyframes. Copy 0 ke 2, 1 ke 3.

Hapus garis transparan agar jelas depan/belakang. Animation Settings framerate 12 (praktikum; manual contoh 4). Drag seleksi semua > Play. File > Incremental Backup tiap milestone.

### Gambar 7.9. Bersihkan kaki depan/belakang.

### Gambar 7.10. Set framerate.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 76 -->

### Gambar 7.11. Seleksi semua lalu Play.

Gambar 7.12. Hasil loop 4 frame kasar (GIF manual, ganti render sendiri). 10. Seleksi semua > klik kanan > Hold frames > Insert Hold Frame. Gambar inbetween mulai tumit > kaki > lutut. Label warna: ekstrem biru, inbetween hijau/kuning. Onion Skin Docker atur jumlah + transparansi (cukup prev/next).

### Gambar 7.13 Hold Frame dan ruang inbetween.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 77 -->

### Gambar 7.14 Contoh inbetween tumit dulu.

Gambar 7.15. Atur Onion Skin Docker. 11. Tangan layer baru hands: bila hilang dari Timeline, pin via ikon pin di Layer Docker (Krita 4.3+ auto-pin). Ayun berlawanan kaki.

### Gambar 7.16. Layer hands hilang, perlu pin.

Gambar 7.17. Pin layer yang sedang dianimasikan. 12. Jalan maju opsional: group hands+walkcycle > kanan Add > Transform mask. Buka Settings >

Dockers > Animation Curves, frame pertama Adds keyframe scalar (diamond), Transform Tool geser start tekan Enter, frame akhir geser end, Zoom fit. Ulangi walk 3-4x lalu pindah scalar ke akhir. Sinkron kaki napak: tandai guide vertikal tiap kaki napak, Transform per frame agar kaki diam selama napak (lihat kurva).

Gambar 7.18. Scalar tween jalan maju (perlu sinkron guide). 13. Export: File > Render Animation > instal FFmpeg dan arahkan di Settings > export PNG sequence + MP4 H.264. Kumpulkan folder NIM_P7A: walk-cycle.kra, MP4, GIF, 4 screenshot Timeline + setting export. Cara SS: Win+Shift+S min 1280px PNG + caption.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 78 -->

### Gambar 7.19 Walk cycle halus final (acuan, ganti milik sendiri).

### 7.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Buat animasi burung terbang | 100 |

### 7.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 79 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 80 -->

## PRAKTIKUM 8: PEMODELAN KARAKTER 3D

Pertemuan ke : 8 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsipprinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan komputasi yang kompleks. |  |  |
| --- | --- | --- | --- |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

8.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Menjelaskan urgensi dari pengembangan karakter 3 Dimensi dalam produksi film animasi 2. Merancang dan menghasilkan karakter 3 Dimensi 8.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menerapkan pemodelan karakter 3D |
| --- | --- | --- |

### 8.3. TEORI PENDUKUNG

Mengembangkan konsep seni untuk semua elemen dalam produksi film animasi. Melakukan pembuatan desain-desain yang biasanya mencakup karakter, properti, lingkungan, dan setiap aset yang perlu dibuat selama tahap produksi film animasi.

Dalam membuat karakter atau tokoh dalam film animasi, perlu dipersiapkan desain visual dari karakter yang akan dibuat (blueprint). Umumnya blueprint untuk karakter dibuat dengan mengambil sudut dari arah depan dan samping karakter.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 81 -->

8.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Blender 3. Blueprint karakter 3D 8.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan perbedaan antara animasi 2 dimensi dengan 3 dimensi! 2. Jelaskan tahapan dalam proses pengembangan karakter 3 dimensi! 3. Sebutkan kakas (perangkat hardware & software) yang digunakan dalam proses pengembangan animasi 3 dimensi! | 30 40 30 |

### 8.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

1. Buka terlebih dahulu aplikasi Blender 3 Dimensi yang sudah Kita install sebelumnya. Lalu akan muncul tampilan awal berupa kubus. Kubus tersebut jangan dihapus, karena akan digunakan sebagai objek untuk membuat karakter.

Gambar 8.1 Tampilan Awal Blender

2. Masuk ke dalam edit mode untuk melakukan perubahan atau peng-edit-an pada objek dengan menekan tombol tab.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 82 -->

3. Jika sudah, Kita akan lakukan pembagian kubus menjadi beberapa bagian yang lebih kecil lagi dengan menggunakan perintah subdivide. Proses untuk menggunakan perintah subdivide dilaku-kan dengan edit mode dan tekan tombol W lalu pilih subdivide.

Gambar 8.2 Tampilan Hasil Subdivide

4. Kubus yang sudah dibagi tersebut digunakan sebagai bentuk kepala pada karakter yang akan dibuat. Proses membuatnya bisa menggunakan tombol Alt + Shift + S untuk merubah bentuk dari sebuah kubus menjadi bentuk yang menyerupai lingkaran. Tetapi bentuk lingkaran yang terbentuk masih belum rapih dan masih memiliki sudut-sudut seperti bentuk kubus. Maka harus dirapihkan lagi sehingga menjadi bentuk di bawah ini.

Gambar 8.3 Tampilan Pembentukan Kepala

5. Kemudian Kita akan membuat bagian tubuh atau badan. Pertama kita hapus face select(titik pada bagian sisi objek) bagian bawah dari kepala yang tadi, lalu kita extrude dan size dengan menggunakan tombol E + S. Hasilnya akan terbentuk lubang kecil untuk membentuk bagian lehernya. Kemudian pada bagian leher tersebut Kita extrude ke bawah untuk membuat bagian badan dari objek. Karena bagian tersebut mengikuti ukuran dari leher, maka perlu membesar-kan ukurannya dengan perintah size/tekan tombol S, sehingga menjadi sebuah bentuk badan.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 83 -->

Gambar 8.4 Tampilan Bentuk Badan

6. Ketika badan tersebut sudah terbentuk, untuk mempemudah membuatnya Kita akan memakai modifier “Mirror” sehingga ketika merubah bagian kanannya makanya pada bagian kirinya akan mengikuti perubahan tersebut. Proses tersebut dilakukan dengan menghapus setengah bagian dari kepala hingga badan tersebut, lalu pilih modifier di sebelah kanan jendela blender dan pilih “Mirror”.

Gambar 8.5 Tampilan Proses Miror

Gambar 8.6 Tampilan Modifier Mirror

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 84 -->

7. Selanjutnya jika bagian badan sudah terbentuk maka kita akan membuat kaki dan tangan.

Disini Kita menggunakan teknik extrude untuk memanjangkan bagian yang nantinya akan dibentuk menjadi bagian tangan dan kaki.

Gambar 8.7 Tampilan Membuat Kaki

Gambar 8.8 Tampilan Membuat Tangan

8. Terakhir, proses pewarnaan untuk karakter tersebut dengan menggunakan modifier materi- al, di sini Kita memiliki beberapa warna untuk setiap bagian.

Gambar 8.9 Tampilan Pewarnaan Karakter

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 85 -->

Gambar 8.10 Tampilan Modifier Material

Keterangan jenis warna yang digunakan :

• Coklat : digunakan sebagai warna dasar

• Merah : untuk warna baju

• Biru gelap : untuk warna calana

• Putih : untuk warna hiasan sepatu

• Hitam : untuk warna sepatu

### 8.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Lakukan perancangan blueprint yang menggambarkan karakter 3 dimensi berdasarkan sudut pandang depan, samping, dan atas. 2. Lakukan pengembangan karakter 3 dimensi berdasarkan blueprint yang telah dibuat (poin 1) | 50 50 |

### 8.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 86 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 87 -->

## PRAKTIKUM 9: TEKNIK ANIMASI 3D (SHADING, RIGGING, SKINING)

Pertemuan ke : 9 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 |  | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsip- |  |
| --- | --- | --- | --- |
|  |  | prinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan |  |
|  |  | komputasi yang kompleks. |  |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

9.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Menjelaskan teknik rigging dan animating pada objek virtual 3 dimensi 2. Melakukan penyatuan terhadap objek virtual 3 dimensi 3. Melakukan pergerakan terhadap objek virtual 3 dimensi 9.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam merekam dan mengoptimalkan kualitas audio untuk diintegrasikan ke dalam film animasi |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 88 -->

Gambar 9.1 Tampilan Proses Rigging

9.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Blender 3. Autodesk Maya (student version) 4. Blueprint karakter 3D 5. Aset karakter 3D 9.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan terminologi dari rigging dalam produksi animasi 3D! 2. Jelaskan terminologi dari animating dalam produksi animasi 3D! 3. Jelaskan terminologi dari Concept Artist! 4. Jelaskan terminologi dari Compositor! 5. Jelaskan terminologi dari 3D Effect Artist! | 20 20 20 20 20 |

### 9.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

### Langkah-Langkah Praktikum:

1. Membuat Sistem Gerak Tubuh (Rigging)

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 89 -->

Setelah pada praktikum sebelumnya melakukan pembuatan karakter 3 Dimensi, pada praktik-um ini akan memberikan sistem gerak tubuh dengan menambahkan kerangka tubuh. Gunakan file karakter 3 Dimensi “Kakashi.blend” yang akan diberikan oleh asisten untuk membuat rigging. Bentuk karakternya sepereti gambar berikut:

Gambar 9.2 Bentuk Model 3 Dimensi Proses pertama setelah membuka karakter pada blender adalah memasukkan metarig-nya terhadap karakter kakashi ini dengan cara:

a. SHIFT + S pilih kursor to center b. SHIFT + A pilih ARMATURE lalu pilih HUMAN METARIG c. Tekan S lalu tarik mouse sampai metarig ini sama dengan karakter Kakashinya d. CTRL + A lalu pilih SCALE untuk membuat properties dari metarig ini tidak mengecil pada saat di- generated e. Pilih edit mode dan 3D cursor f. Pada menu kiri silahkan pilih OPTION lalu centang pada X AXIS MIROR dalam proses menyama- kan metarig di sebelah kiri maka di sebelah kanan juga ikut menyesuaikan g. Silahkan sesuaikan metarig-nya dengan karakter yang dibuat mulai dari kaki sampai tangan dan jari h. Setelah selesai lalu klik generated pada menu armature-nya

Gambar 9.3 Tampilan Setting Rig Layer Sampai tahap di atas karakter bisa digerakan dengan cara memilih layer pada gambar di atas dan proses lebih lanjut pilih mode kursor di Transformation(lengkung curve) untuk sesuaikan mode Glo-bal atau Gimbal.

i. Pada 3D VIEW ubah Object Mode menjadi Pose Mode j. Posisikan karakter sesuai pada fose saat mau berjalan bisa dilihat pada gambar di bawah:

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 90 -->

Gambar 9.4 Tampilan 3D View Blender k. Ubah mode deault pada kotak di atas ke mode animasi l. Pada CURRENT EDITOR TYPE AREA silahkan ganti dope sheet ke action editor m. Pada TIMELINE silahkan klik tombol merah/record n. Tekan A untuk seleksi semua o. Tekan I lalu pilih LOCROT Membuat Karakter Berjalan

1. Pada menu 3D view silahkan klik icon panah ke atas/COPY 2. Geser timeline pada frame 21 lalu pada menu 3D view klik icon panah ke bawah arah kiri/PASTE 3. Lalu geser timeline-nya atau klik icon PLAY, sampai di sini karakter yang dibuat sudah dapat ber- jalan tetapi dengan gerakan yang masih kaku

Gambar 9.5 Tampilan Proses Rigging Keterangan:  (1) icon recor (2) timeline (3) icon copy (4) icon paste 4. Periksa frame 11 untuk memposisikan karakter agar nyaman dilihat saat berjalan, dimana pada layer 11 terdapat perpindahan antara kaki tangan kiri ke kaki tangan kanan 5. Setelah selesai memposisikan, silahkan tekan A lalu tekan I dan pilih LOCROT 6. Tekan icon panah ke atas/copy 7. Geser layer pada timeline ke layer 31 lalu klik icon panah ke bawah/paste 8. Setting timeline end pada layer 31 9. Lakukan play, sampai di sini karakter sudah memiliki bentuk gerakan yang halus tetapi masih berjalan di tempat 10. Ubah mode current type off ke mode NLA EDITOR 11. Klik panah dua ke bawah sampai muncul garis kuning dan tekan N untuk menampilkan proper-ties lalu pilih repeat playback setting dari 1000 ke 2000 12. Tekan SHIFT + A, pilih mess  dan pilih plane untuk menampilkan landasan berjalannya karakter

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 91 -->

13. Geser karakter ke posisi kanan layar lalu pastikan frame pada layer 1 lalu tekan I dan pilih LOCROT, kemudian geser karakter ke paling kanan layar dan pastikan frame pada layer 61 lalu tekan I dan pilih LOCROT 14. Pada NLA EDITOR klik tanda panah dua ke bawah 15. Lakukan play, maka karakter yang dibuat sudah bisa berjalan maju pada landasan

Gambar 9.6 Tampilan Menggerakan Karakter 9.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Lakukan pemberian rigging dan animating terhadap hasil penyusunan karakter 3D pada pertemuan 6! | 100 |

### 9.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 92 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 93 -->

## PRAKTIKUM 10: INTEGRASI MULTIMEDIA PADA AR/VR

Pertemuan ke : 10 Total Alokasi Waktu : 90 menit • Materi : 15 menit • Pre-Test : 15 menit • Praktikum : 45 menit • Post-Test : 15 menit Total Bobot Penilaian : 100% • Pre-Test : 20 % • Praktik : 30 % • Post-Test : 50 % Pemenuhan CPL dan CPMK:

| CPL 05P01 |  | Pengetahuan - Kemampuan memahami konsep teoritis dan mengaplikasikan prinsip- |  |
| --- | --- | --- | --- |
|  |  | prinsip komputasi dan disiplin ilmu relevan lainnya untuk menyelesaikan persoalan |  |
|  |  | komputasi yang kompleks. |  |
| CPMK 5.4 |  | Kemampuan menerapkan prinsip dasar animasi serta konsep teknologi virtual |  |

10.1. DESKRIPSI CAPAIAN PEMBELAJARAN Setelah mengikuti praktikum ini mahasiswa diharapkan mampu:

1. Mengerti layar kerja dari salah suata software untuk membuat augmented reality 2. Menerapkan teknologi augmented reality menjadi suatu produk multimedia 10.2. INDIKATOR KETERCAPAIAN PEMBELAJARAN Indikator ketercapaian diukur dengan:

| CPL 05P01 | CPMK 5.4 | Kemampuan mahasiswa dalam menerapkan objek virtual 3 dimensi ke dalam teknologi augmented reality |
| --- | --- | --- |

Metode Augmented Reality Metode yang dikembangkan pada Augmented Reality terbagi menjadi dua, yaitu Marker Based Tracking dan Markless Augmented Reality.

### a. Marker Augmented Reality (Marker Based Tracking)

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 94 -->

Marker biasanya merupakan ilustrasi hitam dan putih persegi dengan batas hitam tebal dan latar belakang putih. Komputer akan mengenali posisi dan orientasi marker dan men-ciptakan dunia virtual 3D yaitu titik (0,0,0) dan tiga sumbu yaitu X, Y, dan Z. Marker Based Tracking ini sudah lama dikembangkan sejak 1980-an dan pada awal 1990-an mulai dikem-bangkan untuk penggunaan Augmented Reality.

b. Markerless Augmented Reality Salah satu metode Augmented Reality yang saat ini sedang berkembang adalah metode “Markerless Augmented Reality”, dengan metode ini pengguna tidak perlu lagi menggunakan sebuah marker untuk menampilkan elemen digital, dengan tool yang disediakan Qualcomm untuk pengembangan Augmented Reality berbasis mobile device, dapat mempermudah pe-ngembang untuk membuat aplikasi yang markerless (Qualcomm, 2012). Seperti yang saat ini dikembangkan oleh perusahaan Augmented Reality terbesar di dunia Total Immersion dan Qualcomm, mereka telah membuat berbagai macam teknik Mar-kerless Tracking sebagai sebuah teknologi handal, seperti Face Tracking, 3D Object Tracking dan Motion Tracking.

1) Face Tracking Algoritma pada komputer terus dikembangkan, hal ini membuat komputer dapat meng-enali wajah manusia secara umum dengan cara mengenali mata, hidung dan mulut ma-nusia dan mengabaikan objek lain di sekitarnya. Teknik ini pernah digunakan pada kegia-tan Indonesia pada Pekan Raya Jakarta 2010 dan Toy Story 3 Event (Widiansyah, Firman, 2014).

2) 3D Object Tracking Berbeda dengan Face Tracking yang hanya mengenali wajah manusia secara umum, tek-nik 3D Object Tracking dapat mengenali semua bentuk benda yang ada disekitar, seperti mobil, meja, televisi, dan lain-lain.

3) Motion Tracking Komputer dapat menangkap gerakan, motion tracking telah digunakan secara ekstensif untuk memproduksi film-film yang mensimulasikan gerakan.

4) GPS Based Tracking Teknik GPS Based Tracking saat ini mulai populer dan banyak dikembangkan pada apli-kasi smartphone (iPhone dan Android), dengan memanfaatkan fitur GPS dan kompas di dalam smartphone, aplikasi akan mengambil data dari GPS dan kompas untuk kemudian menampilkannya dalam bentuk arah yang kita inginkan secara real-time, bahkan ada beberapa aplikasi menampikannya dalam bentuk 3 Dimensi. 10.4. HARDWARE DAN SOFTWARE Hardware dan software yang digunakan dalam praktikum ini yaitu:

1. Komputer 2. Unity 3D 3. Vuforia SDK 4. Smartphone / Tablet 5. Asset multimedia (gambar dan objek virtual 3D) 10.5. PRE-TEST Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | 1. Jelaskan setiap tahapan dalam mengembangkan produk mulitmedia dengan teknologi augmented reality! 2. Jelaskan 3 keunggulan dan kekurangan dari fiducial marker dengan markerless! | 40 40 |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 95 -->

|  |  |  | 3. Sebutkan minimal 3 tren teknologi augmented reality pada masa mendatang! | 20 |
| --- | --- | --- | --- | --- |

### 10.6. LANGKAH PRAKTIKUM

### Aturan Penilaian (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Dokumen Pendukung | Skor |
| --- | --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Selesaikan semua langkah praktikum | Hasil praktikum | 100 |

Langkah-Langkah Praktikum: Langkah 1 : Buka Unity dan buat project baru

• Buka Unity klik File >> New Project >> Tentukan lokasi penyimpanan project.

Gambar 10.1 Tampilan Awal Unity3D • Setelah itu pilih File >> Build Settings >> pilih platform Android dan klik Switch Platform.

Gambar 10.2 Tampilan Aksi Switch Platform Android

Langkah 2: Konfigurasi Proyek

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 96 -->

• Pada menu Build Setting >> klik Player Setting.

Gambar 10.3 Tampilan Aksi Player Settings • Lihat bagian Inspector >> Lihat bagian Resolution & Presentation >> Ubah menjadi default orientation ke 'Landscape Left' . • Lihat bagian Other Setting >> Isikan Bundle Identifier dengan nama package. (contoh : com.duniadigit.arexample) >> Ubah minimum API Level Android 2.2 (Froyo)

Gambar 10.4 Tampilan Menu Inspector Langkah 3: Integrasi Vuforia dengan Unity3D

• Setelah project baru dibuat langkah selanjutnya adalah memasukkan Vuforia SDK ke dalam project Unity 3D. Caranya: double klik Vuforia SDK yang baru saja di-download.

Gambar 8.5 Tampilan Konfigurasi Vuforia

• Setelah di-double klik maka akan muncul konfirmasi import pada Unity3D. Pilih semua elemen dan klik Import.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 97 -->

Gambar 10.6 Tampilan package Vuforia SDK • Setelah berhasil di-import maka akan muncul isi dari package Vuforia SDK pada window project.

Gambar 10.7 Tampilan Window Project Langkah 4: Konfigurasi AR dan Membuat Image Target

• Drag & drop prefab ARCamera dan ImageTarget dari window project ke window scene.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 98 -->

Gambar 10.8 Tampilan Window Project • Klik object ImageTarget pada window scene dan pada inspector klik press here for target....'

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 99 -->

Gambar 10.9 Tampilan Konfigurasi Image Target • Gunakan gambar di bawah sebagai Image Target.

Gambar 10 10 Contoh Gambar Image Target. • Pada website Vuforia buat database baru dan beri nama dengan “AR_Tutorial”

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 100 -->

Gambar 10.11 Tampilan Membuat Database Vuforia • Image Target yang dibuat akan ditampilkan kosong. Klik pada Image Target tersebut untuk menambahkan gambar sebagai marker.

Gambar 8.12 Tampilan Database Vuforia

• Klik Add Target untuk menambahkan gambar untuk digunakan sebagai Image Target.

Gambar 10.13 Tampilan Menambah Image Target • Setelah itu akan ditampilkan form upload marker. • Lengkapi ketentuan pada form dan klik Add.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 101 -->

Gambar 10.14 Tampilan Upload Marker • Setelah marker berhasil di-upload ke dalam Vuforia akan muncul kualitas marker yang di- tentukan berdasarkan bentuk tekstur dan kontras warna. Semakin tinggi kualitas marker akan mempengaruhi pada proses pendeteksian dan pelacakan marker.

Gambar 10.15 Tampilan Kualitas Marker • Download marker yang telah terdaftar pada Vuforia untuk di-upload ke dalam Unity3D.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 102 -->

Gambar 10.16 Tampilan Download Marker • Pilih format file marker untuk digunakan pada Unity3D Editor.

Gambar 10.17 Tampilan Memilih Ekstensi Unity Editor Langkah 5: Import Marker ke dalam Project

• Setelah download file marker dari website Vuforia, double klik file tersebut untuk mulai import ke dalam project Unity.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 103 -->

Gambar 10.18 Tampilan Import File Marker • Selanjutnya lihat pada bagian bagian Inspector dari Image Target dan lakukan konfigurasi seperti pada gambar di bawah:

Gambar 10.19 Tampilan Konfigurasi Inspector Image Target • Hasil dari proses konfigurasi adalah tampilan preview Image Target yang semula berwarna putih mejadi tekstur gambar marker. • Terakhir, lihat pada bagian bagian Inspector dari ARCamera dan lakukan konfigurasi seperti pada gambar di bawah

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 104 -->

Gambar 10.20 Tampilan Konfigurasi Inspector ARCamera Langkah 6: Uji coba proyek

• Buat objek cube di atas marker dengan cara: Klik Game Object >> Create Other >> Cube. • Selanjutnya posisikan cube sedemikian rupa di atas marker.

Gambar 10.21 Tampilan Membuat Objek Virtual

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 105 -->

• Kamudian simpan scene dengan cara: klik File >> Save Scenes. • Pada project ini, scene disimpan ke direktori Scenes >> Main Scenes. • Proses meng-compile project harus dilakukan proses include scene ke dalam build settings dengan cara: Klik File >> Build Settings >> Drag & drop scene ke Build Settings

Gambar 10.22 Tampilan Konfigurasi Compile Project • Klik Build And Run, tunggu proses selesai dan perhatikan tampilan aplikasinya. • Arahkan kamera ke marker yang telah di-import ke dalam project.

Gambar 10.23 Tampilan Hasil Pendeteksian Marker • Proses berikutnya adalah meambahkan texture dan penerangan directional light

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 106 -->

Gambar 10.24 Tampilan Menambahkan Tekstur • Hasil project setelah ditambahkan tekstur

Gambar 10.25 Hasil Project Setelah Ditambahkan Tekstur

### 10.7. POST TEST

### Jawablah pertanyaan berikut (Total Skor: 100):

| No | CPL | CPMK | Pertanyaan | Skor |
| --- | --- | --- | --- | --- |
| 1. | CPL 05P01 | CPMK 5.4 | Gunakan hasil praktikum P8 untuk membuat aplikasi VR | 100 |

### 10.8. HASIL CAPAIAN PRAKTIKUM

Diisi oleh asisten setelah semua assessment dinilai.

| No | Bentuk Assessment | CPL | CPMK | Bobot | Skor (0-100) | Nilai Akhir (Bobot x Skor) |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | Pre-Test | CPL 05-P01 | CPMK 5.4 | 20% |  |  |
| 2. | Praktik | CPL 05-P01 | CPMK 5.4 | 30% |  |  |
| 3. | Post-Test | CPL 05-P01 | CPMK 5.4 | 50% |  |  |
| Total Nilai |  |  |  |  |  |  |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 107 -->

### LEMBAR JAWABAN PRE-TEST DAN POST-TEST PRAKTIKUM

| Nama : NIM : | Asisten: Paraf Asisten: | Tanggal: Nilai: |
| --- | --- | --- |

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 108 -->

### DAFTAR PUSTAKA 
 
 
[1] 
M. Muliansyah and Z. Maizi, “ANIMASI PENGENALAN ALAT TRADISONAL PENUMBUK PADI ( TOP

JEUNGKI) MENGGUNAKAN APLIKASI BLENDER,” J. Informatics Comput. Sci., vol. 5, no. 1, pp. 40–

41, 2019.

[2] M. S. Kurniawan, “PRODUK MULTIMEDIA SEBAGAI MEDIA BELAJAR BAHASA PERANCIS UNTUK

SMA/MA POKOK BAHASAN FUTUR PROCHE,” Universitas Negeri Yogyakarta, 2016.

[3] IDS, “ARTI FOTOGRAFI MENURUT PARA AHLI,” International Design School, 2018. [Online].

Available: https://idseducation.com/articles/fotografi-menurut-para-ahli/. [Accessed: 20-Feb-

2020].

[4] F. L. MAHFUZH, “DEVELOPING AN INTERACTIVE MAP BASED TECHNOLOGY OF AUGMENTED

REALITY(CASE STUDY THE TOURISM REGION OF BAWEAN ISLAND),” Institut Teknologi Sepuluh

Nopember, 2017.

Praktikum Teknologi Multimedia-Informatika-2026

---

<!-- Halaman 109 -->

Praktikum Teknologi Multimedia-Informatika-2026