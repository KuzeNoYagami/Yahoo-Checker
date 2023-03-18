# Yahoo-Checker

Pertama-tama, kita membaca daftar akun email dari file `list.txt`. Setiap baris di file tersebut berisi email dan password yang dipisahkan oleh karakter `|`. Selanjutnya, untuk setiap akun email, kita akan membuat session dan csrf token secara acak, dan juga melakukan bypass captcha menggunakan API dari Anti Captcha. Kemudian, kita melakukan request ke halaman login Yahoo dengan menggunakan headers dan data yang sesuai, dan memeriksa apakah login berhasil atau tidak berdasarkan url halaman setelah login. Jika login berhasil, email dan password akan ditulis ke file `live.txt`, sedangkan jika gagal, akan ditulis ke file `dead.txt`. Sebelum mencoba akun berikutnya, kita menunggu sebentar dengan jangka waktu random antara 5-15 detik.

Demikianlah script untuk akses Yahoo email dengan menggunakan Python 3. Semoga bermanfaat!
#DISCLAIMER
#just_learn_it
