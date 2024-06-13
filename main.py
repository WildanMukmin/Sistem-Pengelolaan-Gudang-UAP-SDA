import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
# <---------------------- Akses File ---------------------->

def readFileCsv(fileName):
    items = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 4:
                items.append(Item(row[0], row[1], row[2], row[3]))
    return items

# <---------------------- Algoritma Sorting ---------------------->

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

# <---------------------- Algoritma Search ---------------------->

def binarySearch(arr, target_id):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        current_id = arr[mid].id
        
        # # Debug: Tampilkan nilai left, right, dan mid
        # print(f"left: {left}, right: {right}, mid: {mid}, current_id: {current_id}")
        
        if current_id == target_id:
            return mid
        elif current_id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# <---------------------- Class Item dan Gudang ---------------------->

class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = int(quantity)
        self.price = int(price)
    
    def to_list(self):
        return [self.id, self.name, self.quantity, self.price]

    # def __str__(self):
    #     return f"Item(id={self.id}, name={self.name}, quantity={self.quantity}, price={self.price})"




class Gudang:
    next_id = 1
    # <---------------------- Constructor ---------------------->
    
    def __init__(self):
        self.items = readFileCsv("items.csv")
        if self.items:
            Gudang.next_id = len(self.items) + 1
        
    # <---------------------- Setter Getter ---------------------->
    
    def getAllproduct(self):
        arr = []
        for item in self.items:
            arr.append(item.to_list())
        return arr
    
    def getNameItem(self, id):
            item = self.SeacrhItemById(id)
            return item.name if item else None
        
    def getPriceItem(self, id):
        item = self.SeacrhItemById(id)
        return item.price if item else None

    def getQuantityItem(self, id):
        item = self.SeacrhItemById(id)
        return item.quantity if item else None

    def setNameItem(self, id, name):
        item = self.SeacrhItemById(id)
        if item:
            item.name = name
            self.updateFileCsv()

    def setPriceItem(self, id, price):
        item = self.SeacrhItemById(id)
        if item:
            item.price = price
            self.updateFileCsv()

    def setQuantityItem(self, id, quantity):
        item = self.SeacrhItemById(id)
        if item:
            item.quantity = quantity
            self.updateFileCsv()
   
    # <---------------------- Method CRUD ---------------------->

    def addItem(self, name, quantity, price):
        item_id = Gudang.next_id
        Gudang.next_id += 1
        self.items.append(Item(str(item_id), name, quantity, price))
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

    # <---------------------- Method Tambahan ---------------------->

    def sortByPrice(self):
        self.items = mergeSort(self.items, 'price')
        self.updateFileCsv()

    def sortByQuantity(self):
        self.items = mergeSort(self.items, 'quantity')
        self.updateFileCsv()

    def sortById(self):
        self.items = mergeSort(self.items, 'id')
        self.updateFileCsv()
    
    def SeacrhItemById(self, id):
        self.sortById()
        index = binarySearch(self.items, id)
        if index != -1:
            return self.items[index]
        return None
    
    def displayAllproduct(self):
        for item in self.items:
            print(item.to_list())
    



# <---------------------- Main program ---------------------->

# Testing the Gudang class
listBarang = Gudang()

# <---------------------- End Main program ---------------------->
