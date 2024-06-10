import csv

def readFileCsv(fileName):
    items = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 4:
                items.append(Item(row[0], row[1], row[2], row[3]))
    return items

def mergeSort(arr, parameter):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left, parameter)
    right = mergeSort(right, parameter)
    
    return merge(left, right, parameter)

def merge(left, right, parameter):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if getattr(left[i], parameter) < getattr(right[j], parameter):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = int(quantity)
        self.price = int(price)
    
    def to_list(self):
        return [self.id, self.name, self.quantity, self.price]

class Gudang:
    def __init__(self):
        self.items = readFileCsv("items.csv")
        
    def addItem(self, id, name, quantity, price):
        self.items.append(Item(id, name, quantity, price))
        self.updateFileCsv()
        
    def removeItemByName(self, name):
        self.items = [item for item in self.items if item.name != name]
        self.updateFileCsv()
    
    def removeItemById(self, id):
        self.items = [item for item in self.items if item.id != id]
        self.updateFileCsv()
    
    def updateFileCsv(self):
        with open("items.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'quantity', 'price'])  # Add header row
            for item in self.items:
                writer.writerow(item.to_list())
                
    def sortByPrice(self):
        self.items = mergeSort(self.items, 'price')
        self.updateFileCsv()

    def sortByQuantity(self):
        self.items = mergeSort(self.items, 'quantity')
        self.updateFileCsv()

    def sortById(self):
        self.items = mergeSort(self.items, 'id')
        self.updateFileCsv()




# Testing the Gudang class
listBarang = Gudang()

# Uncomment to add items
# listBarang.addItem("p001", "pisang", 100, 10120)
# listBarang.addItem("p002", "anu", 0, 10340)
# listBarang.addItem("p003", "asak", 1010, 10210)
# listBarang.addItem("p004", "aslja", 40, 101210)
# listBarang.addItem("p005", "adjad", 1, 150)

# listBarang.sortByQuantity()
# listBarang.sortByPrice()
listBarang.sortById()
listBarang.addItem("p101", "Item101", 100, 20000)
listBarang.removeItemById("p101")
# Uncomment to remove an item
# listBarang.removeItem("anu")
