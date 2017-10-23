from multiprocessing import Queue

renkler=['kırmızı',"beyaz","bordo","mavi","siyah"]
say=1
#Kuyruk örneği oluşturalım
Kuyruk=Queue()
print("Öğeleri Sıraya Sokuyoruz")
for renk in renkler:
    print('Nesne No: ', say,'',renk )
    Kuyruk.put(renk)
    say +=1
print("\nKuyruğa atılan öğeler")
say=0
while not Kuyruk.empty():
    print('Nesne No: ',say,'',Kuyruk.get())
    say+=1
