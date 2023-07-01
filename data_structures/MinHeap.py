class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        """
        Inserisce l'elemento nell'heap.
        """
        self.heap.append(item)
        self._upheap(len(self.heap) - 1)

    def extract_min(self):
        """
        Estrae l'elemento minimo dall'heap.
        Solleva IndexError se l'heap è vuoto.
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_item
            self._downheap(0)
        return min_item

    def _upheap(self, i):
        """
        Esegue l'operazione up-heapify per mantenere la proprietà di min heap.
        """
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _downheap(self, i):
        """
        Esegue l'operazione down-heapify per mantenere la proprietà di min heap.
        """
        while self.left_child(i) < len(self.heap):
            left = self.left_child(i)
            right = self.right_child(i)
            smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[i] <= self.heap[smallest]:
                break
            self.swap(i, smallest)
            i = smallest

    def count_values_below_root(self):
        """
        Restituisce il numero di valori nell'heap che sono minori o uguali al valore della radice.
        """
        root_value = self.heap[0]
        count = 0

        for value in self.heap:
            if value <= root_value:
                count += 1

        return count
