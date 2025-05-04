# 🗓️ nonOverlapping\_Schedul

## 📚 Tugas Besar Analisis Kompleksitas Algoritma

Proyek ini membandingkan dua pendekatan algoritma—**rekursif** dan **iteratif**—untuk menyelesaikan masalah *activity selection* (penjadwalan aktivitas non-overlapping) berdasarkan kompleksitas waktu dan performa eksekusi.

---

## ⚙️ Deskripsi Eksperimen

* Kedua algoritma diuji menggunakan **list aktivitas yang dihasilkan secara acak**.
* Evaluasi dilakukan berdasarkan **waktu eksekusi** dan **kompleksitas waktu teoretis**.
* Walaupun aktivitas di-*generate* secara acak, hasil pengujian menunjukkan pola yang konsisten antara **jumlah aktivitas** dan **waktu eksekusi**.

---

## 📈 Hasil & Analisis Eksperimen

* Kompleksitas waktu untuk kedua algoritma secara umum adalah:
  🧮 **O(n log n)** (dengan asumsi *n* adalah jumlah aktivitas dan *log n* dari proses sorting).
* Dari pengamatan pada **Fig. 8**, terlihat bahwa:

  * Keduanya memiliki performa eksekusi yang hampir serupa untuk input kecil hingga menengah.
  * Namun, seiring bertambahnya jumlah input, **algoritma iteratif menunjukkan efisiensi yang lebih baik** dibandingkan algoritma rekursif.

---

## 🧠 Analisis Kompleksitas Teoretis

### 🔁 Algoritma Rekursif: `nonOverlappingSchedule_Rekursif`

#### Best Case

* Kondisi:

  * Semua aktivitas terjadi di hari yang sama (`AktL.Hari == AktJ.Hari`) dan **overlap**.
* Kompleksitas:

  $$
  T_{\text{best}}(nL) = nL \in \Theta(nL)
  $$

  Berkategori **linier**.

#### Worst Case

* Kondisi:

  * Aktivitas saling tidak overlap tetapi tetap dibandingkan semua.
* Kompleksitas:

  $$
  T_{\text{worst}}(nL) = nL \cdot nJ \in \Theta(nL \cdot nJ)
  $$

  Berkategori **kuadratik**.

#### Average Case

* Kompleksitas:

  $$
  T_{\text{avg}}(n) = \frac{nL \cdot nJ + 1}{2} \in \Theta(nL \cdot nJ)
  $$

---

### 🔄 Algoritma Iteratif: `nonOverlappingSchedule_Iteratif`

#### Best Case

* Kondisi:

  * Semua aktivitas di hari yang sama dan tidak overlap.
* Kompleksitas:

  $$
  T_{\text{best}}(n) = nL \in \Theta(nL)
  $$

#### Worst Case

* Kondisi:

  * Semua aktivitas perlu dibandingkan dengan semua yang lain.
* Kompleksitas:

  $$
  T_{\text{worst}}(n) = nL \cdot nJ \in \Theta(nL \cdot nJ)
  $$

#### Average Case

* Kompleksitas:

  $$
  T_{\text{avg}}(n) = \frac{nL \cdot nJ + 1}{2} \in \Theta(nL \cdot nJ)
  $$

---

## 📊 Kesimpulan

✅ **Iteratif lebih unggul** dalam hal efisiensi waktu saat skala input meningkat.
✅ **Keduanya setara** dalam kompleksitas teoritis, namun **praktik menunjukkan keunggulan iteratif** dalam efisiensi eksekusi.
✅ Analisis kompleksitas mendukung hasil eksperimen: iteratif lebih stabil dan scalable.
