def pancakeSort(data, n):
    if n > 1:
        for size in range(n, 1, -1):
            # Позиция максимума в неотсортированной части
            maxindex = max(range(size), key = data.__getitem__)
            if maxindex + 1 != size:
                # Если максимум не слова, то нужно развернуть
                if maxindex != 0:
                    # Переворачиваем так, чтобы максимум оказался слева
                    data[:maxindex + 1] = reversed(data[:maxindex + 1])
                # Переворачиваем неотсортированную часть массива,
                # максимум становится на своё место
                data[:size] = reversed(data[:size])
    return data

# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
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
def radixSort(data, n):
    # Get maximum element
    max_element = max(data)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(data, place)
        place *= 10
    return data


def shaker_sort(arr, n):

    left = 0
    right = n - 1

    swapped = True

    while(swapped):
        swapped = False

        for i in range(left, right):
            if (arr[i] > arr[i + 1]):
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

                swapped = True

        if (swapped == False):
            break

        swapped = False
        right -= 1

        for i in range(right - 1, left - 1, -1):
            if (arr[i] > arr[i + 1]):
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp

                swapped = True

        left += 1

    return arr

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
        # print(self.key, end=' ')
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
    bstree.inorder()
    return bstree
