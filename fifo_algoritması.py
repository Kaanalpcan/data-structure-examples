import queue
class fifom:
    def __init__(self):
        self.items=[]
    def ekle(self,item):
        self.items.append(item)
    def sil(self):
        itemiSil=self.items[0]
        del self.items[0]
        return itemiSil
    def uzunluk(self):
        return len(self.items)
    def raporla (self):
        return self.items
def TestFifo():
    fifo=fifom()
    fifo.ekle("Kaan")
    fifo.ekle("Alp")
    fifo.ekle("Can")
    fifo.ekle("RTEÜ BÖTE")
    fifo.ekle("3.SINIF")
    print(fifo.uzunluk())
    print(fifo.raporla())
    print(fifo.sil())
    print(fifo.raporla())

TestFifo()
