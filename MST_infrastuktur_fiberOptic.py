# Program MST_infrastrukturFiberOptic
	# implementasi algoritma prim dalam menemukan minimum spanning tree dari
	# beberapa kota di indonesia

	# kota yang dilingkupi : 
		# indeks 		KOTA
		# 0.  		  Medan
		# 1.  		  Palembang
		# 2.  		  Jakarta
		# 3.  		  Bandung
		# 4.  		  Bali
		# 5.  		  Pontianak
		# 6.  		  Makassar
		# 7.  		  Balikpapan
		# 8.  		  Gorontalo
		# 9.  		  Kupang
		# 10. 		  Papua Barat

	# referensi : https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
# KAMUS 
	# Variabel
		# V : integer { jumlah vertex, dalam hal ini jumlah kota }
		# INT_MAX : integer { infinity }
		# kota : array of string { list kota yang ingin dihubungkan }
		# distance : array of array of integer { graph yang ingin kita cari MST-nya  }
	# Fungsi / Prosedur
		# function isValidEdge(int u, int v, bool inMST) -> boolean
			# mengembalikan True jika edge u-v adalah edge yang valid untuk di-tambahkan ke MST ( minimum spanning tree ).
			# sebuah edge valid jika satu vertex telah ada di MST dan vertex lain belum ada di MST
		# procedure primMST(input : array of array of integer distance)
			# prosedur untuk menghitung MST dari sebuah graph yang direpresentasikan dengan adjacencey matrix distance
# ALGORITMA UTAMA

from sys import maxsize
INT_MAX = maxsize
V = 11
kota = ["Medan","Palembang","Jakarta","Bandung","Bali","Pontianak","Makassar","Balikpapan", "Gorontalo", "Kupang", "Papua Barat"]

# REALISASI FUNGSI/PROSEDUR

def isValidEdge(u, v, inMST):
	# KAMUS LOKAL
		# inMST : array of bool { array yang menyatakan apakah suatu vertex telah di-include ke MST atau belum } 
	# ALGORITMA
	if u == v:
		return False
	if inMST[u] == False and inMST[v] == False:
		return False
	elif inMST[u] == True and inMST[v] == True:
		return False
	return True # jika salah satu dari u dan v yang bernilai true, maka edge valid

def primMST(distance):
	# KAMUS LOKAL
		# Variabel
			# edge_count : integer { jumlah edge yang telah ditambahkan ke MST }
			# mindistance : integer { total minimum distance dari keseluruhan MST }
			# minn : integer { distance dari suatu edge yang sedang diuji saat traversing edge }
			# i,j : integer { variabel untuk melakukan looping dalam traversing edge pada MST }
			# a, b : integer { nomor vertex yang termasuk dalam edge }
		
	# ALGORITMA 
	inMST = [False] * V

	# menambahkan initial vertex pada MST
	inMST[0] = True

	# menambahkan sejumlah V - 2  edge ke dalam MST. 
		# mengapa V - 2 dan bukan V - 1 ? karena initial vertex sudah ditambahkan sebelumnya
	edge_count = 0
	mindistance = 0
	while edge_count < V - 1:

		# mencari bobot edge minimum ( yang valid )
		minn = INT_MAX
		a = -1
		b = -1
		for i in range(V):
			for j in range(V):
				if distance[i][j] < minn:
					if isValidEdge(i, j, inMST):
						minn = distance[i][j]
						a = i
						b = j

		if a != -1 and b != -1:
			print("Edge %d: (%s, %s) distance: %d Km" %
				(edge_count,kota[a], kota[b], minn))
			print(mindistance)
			edge_count += 1
			mindistance += minn
			inMST[b] = inMST[a] = True # jika vertex a dan b telah ditambahkan ke MST, maka akan dibuat true
	
	print("Minimum Total distance = %d Km" % mindistance)

# Driver Code
if __name__ == "__main__":

	distance = [
			[0, 998.05 , 1424.86 , 1550.57 ,2263.58 ,1245.29 ,2523.42 ,2100.66 ,2729.29 ,3167.22 ,4329.10],
			[998.05 ,0, 439.72 , 539.38 , 1299.94 , 601.81 , 1644.20 , 1360.04 , 2067.53 , 2227.29 , 3567.15],
			[1424.86, 439.72, 0,112.88, 952.01 , 751.01 , 1392.09 , 1249.41 , 1941.94 , 1891.32 , 3320.52],
			[1550.57 ,539.38 ,112.88 ,0, 859.03 , 783.93 , 1310.50 , 1201.93 , 1891.00 , 1793.69 , 3241.85],
			[2263.58 , 1299.94 , 952.01 , 859.03, 0 , 1139.73 , 590.35 , 833.54 , 1317.38 , 946.98 , 2442.53],
			[1245.29 , 601.81 , 751.01 , 783.93 , 1139.73, 0 , 1267.83 , 830.48 , 1529.81 , 1942.42 , 3109.70],
			[2523.42 , 1644.20 , 1392.09 , 1310.50 , 590.35 , 1267.83,0 , 546.27 , 738.68 , 729.56 , 1941.99],
			[2100.66 , 1360.04 ,1249.41 ,1201.93 ,833.54 ,830.48 ,546.27,0 ,718.53 ,1244.59 ,2251.69],
			[2729.29 , 2067.53 , 1941.94 ,1891.00 ,1317.38 ,1529.81 ,738.68 ,718.53 ,0,1183.55 ,1589.30],
			[3167.22 ,2227.29 ,1891.32 ,1793.69 ,946.98 ,1942.42 ,729.56 ,1244.59 ,1183.55 ,0,1609.45],
			[4329.10 ,3567.15 ,3320.52 ,3241.85 ,2442.53 ,3109.70 ,1941.99 ,2251.69 ,1589.30 ,1609.45 ,0]
			]

	# mencetak minimum distance
	primMST(distance)
