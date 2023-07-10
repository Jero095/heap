class minheap:
    def __init__(self, ray) :
        self.heap = []
        if type(ray) is list:
            self.heap =ray.copy()
            for i in range(len(self.heap))[::-1]:
                self.float_down(i)
    def float_up(self, i):
        padre_i =(i-1)//2
        while i!=0 and self.heap[i]>self.heap[padre_i]:
            temp =self.heap[i]
            self.heap[i]= self.heap[padre_i]
            self.heap[padre_i] = temp
            i = padre_i
            padre_i = (i-1)//2
    def float_down(self,i):
        hijo_izq_i = (2*i)+1
        hijo_der_i = (2*i)+2
        
        while (hijo_izq_i < len(self.heap) and self.heap[i] > self.heap[hijo_izq_i]) or (hijo_der_i < len(self.heap) and self.heap[i] > self.heap[hijo_der_i]):
            smallest = hijo_izq_i if (hijo_der_i >= len(self.heap) or self.heap[hijo_izq_i] < self.heap[hijo_der_i]) else hijo_der_i
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            hijo_izq_i = 2*i + 1
            hijo_der_i = 2*i + 2
    def añadir(self, valor):
        
        self.heap.append(valor)
        self.float_up(len(self.heap)-1)
    def preorden(self,i=0):
        if(i<len(self.heap)):
            
            print(self.heap[i])
            
            self.preorden((2*i)+1)
            self.preorden((2*i)+2)
    def por_niveles(self):
        for n in self.heap:
            print(n)





class Nodo:
        def __init__(self, valor):
            self.valor = valor

heap = minheap([5, 10, 9, 7, 4, 3])
heap.por_niveles() 
print("__________")
heap.preorden()
