from multiprocessing import Pool
import time
calisma=(["A", 5], ["B", 2], ["C", 1], ["D", 3])
def calisma_kayit(calisma_veriler):
    print("İşlemci %s bekliyor %s saniye"%(calisma_veriler[0],calisma_veriler[1]))
    time.sleep(int(calisma_veriler[1]))
    print("İşlemci %s İşlemini Tamamladı."% calisma_veriler[0])

def havuz():
    p=Pool(2)
    p.map(calisma_kayit,calisma)
if __name__ == "__main__":
    havuz()
