from multiprocessing import Lock,Process,Queue,current_process
import time
import queue
import multiprocessing
def cekirdek():
    print("İslemci Cekirdek Sayiniz: ",multiprocessing.cpu_count())

def gorevler(yapilacak_gorevler,yapilmis_gorevler):
    while True:
        try:
            gorev=yapilacak_gorevler.get_nowait()
        except queue.Empty:
            break
        else:
            print(gorev)
            yapilmis_gorevler.put(gorev + ' ' 'Tarafından yapıldı' ' ' + current_process().name)
            time.sleep(5)
    return True
def ana_gorev():
    gorev_num=10
    islemci_num=4
    yapilacak_gorevler=Queue()
    yapilmis_gorevler=Queue()
    islemciler=[]

    for i in range(gorev_num):
        yapilacak_gorevler.put("Görev No : " + str(i))

    #işlemci oluşturalım
    for w in range (islemci_num):
        p=Process(target=gorevler,args=(yapilacak_gorevler,yapilmis_gorevler))
        islemciler.append(p)
        p.start()
    #işlemciyi tamamla
    for p in islemciler:
        p.join()
    #çıktıları bastıralım
    while not yapilmis_gorevler.empty():
        print(yapilmis_gorevler.get())
    return True
if __name__=="__main__":
    cekirdek()
    ana_gorev()



