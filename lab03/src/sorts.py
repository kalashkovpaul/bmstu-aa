def pancakeSort(data, size):
    if size > 1:
        for currentSize in range(size, 1, -1):
            # Позиция максимума в неотсортированной части
            maxIndex = max(range(currentSize), key = data.__getitem__)
            if maxIndex + 1 != currentSize:
                # Если максимум не слова, то нужно развернуть
                if maxIndex != 0:
                    # Переворачиваем так, чтобы максимум оказался слева
                    data[:maxIndex + 1] = reversed(data[:maxIndex + 1])
                # Переворачиваем неотсортированную часть массива,
                # максимум становится на своё место
                data[:currentSize] = reversed(data[:currentSize])
    return data

def countingSort(array, size, place):
    output = [0] * size
    count = [0] * 10

    # Считаем количество каждых значений
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(data, size):
    maxElement = max(data)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while maxElement // place > 0:
        countingSort(data, size, place)
        place *= 10
    return data

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "U"

    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key <= node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.right is not None:
            self.right.inorder()

    def toString(self):
        leftStr = self.left.toString() if self.left else ""
        rightStr = self.right.toString() if self.right else ""
        selfStr = str(self.key) if self.key else ""
        return leftStr + selfStr + ", " + rightStr


class BSTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        rootStr = self.root.toString()[:-2]
        return "[" + rootStr + "]"

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def add(self, key):
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

def bstSort(data, n):
    bstree = BSTree()
    for x in data:
        bstree.add(x)
    return bstree
