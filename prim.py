# Program prim
	# implementasi algoritma prim dalam menemukan spanning tree dari suatu graph tak berarah
	# dengan menggunakan adjacency matrix

	# referensi : https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
# KAMUS 
	# Variabel
		# V : integer { jumlah vertex }
		# INT_MAX : integer { infinity }
	# Fungsi / Prosedur
		# function isValidEdge(int u, int v, bool inMST) -> boolean
			# mengembalikan True jika edge u-v adalah edge yang valid untuk di-tambahkan ke MST ( minimum spanning tree ).
			# sebuah edge valid jika satu vertex telah ada di MST dan vertex lain belum ada di MST
		# procedure primMST(input : array of array of integer cost)
			# prosedur untuk menghitung MST dari sebuah graph yang direpresentasikan dengan adjacencey matrix cost
# ALGORITMA UTAMA

from sys import maxsize
INT_MAX = maxsize
V = 5

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

def primMST(cost):
	# KAMUS LOKAL
		# Variabel
			# edge_count : integer { jumlah edge yang telah ditambahkan ke MST }
			# mincost : integer { total minimum cost dari keseluruhan MST }
			# minn : integer { cost dari suatu edge yang sedang diuji saat traversing edge }
			# i,j : integer { variabel untuk melakukan looping dalam traversing edge pada MST }
			# a, b : integer { nomor vertex yang termasuk dalam edge }
		
	# ALGORITMA 
	
	# menginisasi semua vertex belum ditambahkan ke MST
	inMST = [False] * V

	# menambahkan initial vertex pada MST
	inMST[0] = True

	# menambahkan sejumlah V - 1  edge ke dalam MST. 
	edge_count = 0
	mincost = 0
	while edge_count < V - 1:

		# mencari bobot edge minimum ( yang valid )
		minn = INT_MAX
		a = -1
		b = -1
		for i in range(V):
			for j in range(V):
				if cost[i][j] < minn:
					if isValidEdge(i, j, inMST):
						minn = cost[i][j]
						a = i
						b = j

		if a != -1 and b != -1:
			print("Edge %d: (%d, %d) cost: %d" %
				(edge_count, a, b, minn))
			edge_count += 1
			mincost += minn
			inMST[b] = inMST[a] = True # jika vertex a dan b telah ditambahkan ke MST, maka akan dibuat true
	
	print("Minimum cost = %d" % mincost)

# Driver Code
if __name__ == "__main__":

	cost = [[INT_MAX, 2, INT_MAX, 6, INT_MAX],
			[2, INT_MAX, 3, 8, 5],
			[INT_MAX, 3, INT_MAX, INT_MAX, 7],
			[6, 8, INT_MAX, INT_MAX, 9],
			[INT_MAX, 5, 7, 9, INT_MAX]]

	# mencetak minimum cost
	primMST(cost)
