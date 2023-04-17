class Kasir:
    def __init__(self):
        self.queue = []
    
    def _len_(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def enqueue(self, pelanggan):
        self.queue.append(pelanggan)
        
    def printAll(self):
        print("=== Kasir ===")
        for i in range(len(self.queue)):
            print(f"{i+1}. {self.queue[i]}")

# Inisialisasi kasir
kasir = Kasir()

# Menambah pelanggan kedalam antrian kasir
kasir.enqueue("Haniif")
kasir.enqueue("Sindu")
kasir.enqueue("Dedi")

# Mencetak isi antrian kasir
kasir.printAll()

# Pelanggan pertama selesai membayar
print("Pelanggan Haniif Selesai Membayar")
kasir.dequeue()

# Melakukan resize 
print("* Melakukan Resize *")
kasir.enqueue("Beatrix")
kasir.enqueue("Kosong")
kasir.enqueue("Kosong")

# Mencetak isi antrian kasir setelah resize
kasir.printAll()

# Pelanggan kedua selesai membayar
print("Pelanggan Sindu Selesai Membayar")
kasir.dequeue()

# Mencetak isi antrian kasir setelah pelanggan selesai membayar
kasir.printAll()

# Menambah pelanggan baru kedalam antrian setelah resize
kasir.enqueue("Shalon")

# Mencetak isi antrian kasir setelah menambahkan pelanggan baru
kasir.printAll()