n=int(input("Masukkan Nilai N: "))              ## Memperkenalkan variable sebagai integer, kemudian menginputkan nilai

from random import random                       ## Mengimport fungsi random
a=random()                                      ## Memperkenalkan variable a sebagai random

jumlah=n+1                                      ## Jumlah = variable n + 1
start=1                                         ## Dimulai dari angka 1
stop=jumlah                                     ## Berhenti ketika variable jumlah sudah sesuai
step=1                                          ## Step angka 1

for i in range(start,stop,step):                ## Perulangan i dengan nilai awal variable start, nilai akhir variable s
    print("data ke : ",i,"=",(a))               ## Mencetak hasil
print("\nDone")