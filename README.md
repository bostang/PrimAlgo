# PrimAlgo
Presentasi terakhir mata kuliah EL2003 Struktur Diskret tentang pencarian minimum spanning tree menggunakan algoritma Prim.

####   Perintah :
> - Kembangkan program untuk algoritma Prim<br>
> - Design skenario untuk mengetes algoritma Prim

### Anggota kelompok :
- Farhan Hakim Iskandar (13220007)
- Bintang Moralino Cerdasa (13220017)
- Senggani Fatah Sedayu (13220035)
- Dion Timotius Daeli (13220045)
- Bostang Palaguna (13220055)
***
### Skenario yang digunakan :

 misalkan kita ingin membangun infrastuktur _fiber optic_ yang menghubungkan 11 kota di Indonesia:
  1. Medan
  2. Palembang
  3. Jakarta
  4. Bandung
  5. Pontianak
  6. Balikpapan
  7. Bali
  8. Gorontalo
  9. Makassar
  10. Kupang
  11. Papua Barat

![peta 11 kota yang mau dicari MST-nya](https://github.com/bostang/PrimAlgo/blob/main/stepBystep_primIndonesia/step00.png)

kita ingin mencari sebuah `tree` sehingga total `jarak euclidean` antar kota pada peta minimum (_total weight_ dari graf.
Jarak yang minimum akan memberikan cost yang minimum pula dalam pembangunan infrastruktur _fiber optic_.

Untuk mencari jarak antar kota, kita bisa menggunakan fitur _measure distance_ pada `google map` sehingga kita peroleh `adjacency matrix` :
![jarak antar kota](https://github.com/bostang/PrimAlgo/blob/main/dataJarak_kotaIndonesia.png)

dengan menerapkan algoritma prim pada `adjacency matrix` tersebut, kita akan peroleh:

![Minimum spanning tree](https://github.com/bostang/PrimAlgo/blob/main/stepBystep_primIndonesia/step10.png)
