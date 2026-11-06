1. Mengapa pada dashboard.php hash dibandingkan dengan “===” dan bukan “==”? Jelaskan risikonya jika memakai “==”

\=== membandingkan hasil dan tipe data

“6” \=== 6 —-\> FALSE

\== membandingkan hasilnya saja

“6” \== 6 —-\> TRUE

&nbsp;

&nbsp;

2. pada dashboard.php terdapat baris berikut

```
if (strtolower($calculated_hash) === strtolower($verifikasi_hash)) {
```

&nbsp;

jika tidak menggunakan strlower maka operator akan memberikan hasil yang FALSE ketika ada satu saja karakter yang hurufnya besar

&nbsp;

3. pada dashboard terdapat baris:

&nbsp;

```
$verifikasi_hash = trim($_POST['verifikasi_hash']);
```

&nbsp;

fungsi trim digunakan untuk menghapus whitespace pada string. ketika fungsi ini tidak dipakai maka perbandingan akan salah ketika verifikasi\_hash sama persis tapi ada whitespace yang tersembunyi