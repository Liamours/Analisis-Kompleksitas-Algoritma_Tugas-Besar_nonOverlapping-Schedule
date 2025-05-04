# 🗓️ nonOverlapping\_Schedul

Oleh:
- M. Rifqi Dzaky Azhad - 103012330009
- Fathan Arya Maulana - 103012300083

## 📚 Tugas Besar Analisis Kompleksitas Algoritma

Proyek ini membandingkan dua pendekatan algoritma—**rekursif** dan **iteratif**—untuk menyelesaikan masalah *activity selection* (penjadwalan aktivitas non-overlapping) berdasarkan kompleksitas waktu dan performa eksekusi.

---

## ⚙️ Deskripsi Eksperimen

* Kedua algoritma diuji menggunakan **list aktivitas yang dihasilkan secara acak**.
* Evaluasi dilakukan berdasarkan **waktu eksekusi** dan **kompleksitas waktu teoretis**.
* Walaupun aktivitas di-*generate* secara acak, hasil pengujian menunjukkan pola yang konsisten antara **jumlah aktivitas** dan **waktu eksekusi**.

---

## 📈 Hasil & Analisis

* Kompleksitas waktu untuk kedua algoritma adalah:
  🧮 **O(n log n)** (dengan asumsi *n* adalah jumlah aktivitas dan *log n* dari proses sorting).
* Dari pengamatan pada **Fig. 8**, terlihat bahwa:

  * Keduanya memiliki performa eksekusi yang hampir serupa untuk input kecil hingga menengah.
  * Namun, seiring bertambahnya jumlah input, **algoritma iteratif menunjukkan efisiensi yang lebih baik** dibandingkan dengan algoritma rekursif.

---

## 📊 Kesimpulan

✅ **Iteratif lebih unggul** dalam hal efisiensi waktu saat skala input meningkat.
✅ **Keduanya setara** dalam kompleksitas teoritis, namun **praktik menunjukkan keunggulan iteratif** dalam efisiensi eksekusi.
