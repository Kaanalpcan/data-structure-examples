from multiprocessing import Process
import multiprocessing
def cekirdek():
    print("İşlemcinizin Çekirdek Sayısı: ",multiprocessing.cpu_count())
def yazma_fonsiyonu(kıta='Avrupa'):
    print("Bulunduğunuz Kıtanın İsmi: ",kıta)
if __name__ == "__main__":
    cekirdek()
    kıtalar=['America', 'Asya', 'Afrika']
    islem=[]
    surec= Process(target=yazma_fonsiyonu) #Argüman vermeden süreci başlattık
    islem.append(surec)
    surec.start()

    #Argüman vererek süreci başlatalım
    for i in kıtalar:
        #print(i)
        surec= Process(target=yazma_fonsiyonu,args=(i,))
        islem.append(surec)
        surec.start()
    #Süreci tamamlayalım
    for surec in islem:
        surec.join()