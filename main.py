import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# <---------------------- Akses File ---------------------->

def readFileCsv(fileName):
    items = []
    try:
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 4:
                    items.append(Item(row[0], row[1], int(row[2]), int(row[3])))
    except FileNotFoundError:
        # Handle the case where the file does not exist
        pass
    return items

# <---------------------- Algoritma Sorting ---------------------->

def mergeSort(arr, parameter):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid], parameter)
    right = mergeSort(arr[mid:], parameter)
    
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

class Gudang:
    next_id = 1

    def __init__(self):
        self.items = readFileCsv("items.csv")
        if self.items:
            Gudang.next_id = len(self.items) + 1

    def getAllproduct(self):
        return [item.to_list() for item in self.items]
    
    def getNameItem(self, id):
        item = self.SearchItemById(id)
        return item.name if item else None
    
    def getPriceItem(self, id):
        item = self.SearchItemById(id)
        return item.price if item else None

    def getQuantityItem(self, id):
        item = self.SearchItemById(id)
        return item.quantity if item else None

    def setNameItem(self, id, name):
        item = self.SearchItemById(id)
        if item:
            item.name = name
            self.updateFileCsv()

    def setPriceItem(self, id, price):
        item = self.SearchItemById(id)
        if item:
            item.price = price
            self.updateFileCsv()

    def setQuantityItem(self, id, quantity):
        item = self.SearchItemById(id)
        if item:
            item.quantity = quantity
            self.updateFileCsv()

    def addItem(self, name, quantity, price):
        self.next_id += 1
        self.items.append(Item(str(self.next_id), name, quantity, price))
        self.updateFileCsv()
        
    def removeItemByName(self, name):
        self.items = [item for item in self.items if item.name != name]
        self.next_id += 1
        self.updateFileCsv()
    
    def removeItemById(self, id):
        self.items = [item for item in self.items if item.id != id]
        self.next_id += 1
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
    
    def SearchItemById(self, id):
        self.sortById()
        index = binarySearch(self.items, id)
        if index != -1:
            return self.items[index]
        return None
    
    def searchByName(self, name):
        return [item for item in self.items if item.name.lower() == name.lower()]
    
    def displayAllproduct(self):
        for item in self.items:
            print(item.to_list())

class GudangApp(tk.Tk):
    def __init__(self, gudang):
        super().__init__()
        
        self.gudang = gudang
        self.title("Gudang Inventory Management")
        self.geometry("800x600")
        
        self.create_widgets()

    def create_widgets(self):
        # <----------------- GENERATE NAV FRAME ----------------->
        self.nav_frame = tk.Frame(self, height=40, bg="red")
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        # <----------------- GENERATE CONTENT FRAME ----------------->
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # <----------------- GENERATE NAV CONTENT ----------------->
        self.btn_display_all = tk.Button(self.nav_frame, text="Display All", command=self.display_all)
        self.btn_display_all.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_add_item = tk.Button(self.nav_frame, text="Add Item", command=self.add_item)
        self.btn_add_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_remove_item = tk.Button(self.nav_frame, text="Remove Item", command=self.remove_item)
        self.btn_remove_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_search_item = tk.Button(self.nav_frame, text="Search Item", command=self.search_item)
        self.btn_search_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_sort_price = tk.Button(self.nav_frame, text="Sort by Price", command=self.sort_by_price)
        self.btn_sort_price.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.btn_sort_quantity = tk.Button(self.nav_frame, text="Sort by Quantity", command=self.sort_by_quantity)
        self.btn_sort_quantity.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.btn_sort_id = tk.Button(self.nav_frame, text="Sort by ID", command=self.sort_by_id)
        self.btn_sort_id.pack(side=tk.RIGHT, padx=5, pady=5)
        
        # <----------------- GENERATE CONTENT ----------------->
        self.content_text = tk.Text(self.content_frame)
        self.content_text.pack(fill=tk.BOTH, expand=True)
        
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def display_all(self):
        self.clear_content_frame()
        self.content_text = tk.Text(self.content_frame)
        self.content_text.pack(fill=tk.BOTH, expand=True)
        self.content_text.delete(1.0, tk.END)
        products = self.gudang.getAllproduct()
        for product in products:
            self.content_text.insert(tk.END, f"{product}\n")

    def add_item(self):
        self.clear_content_frame()
        label_name_entry = tk.Label(self.content_frame, text="Name")
        label_name_entry.pack(padx=10, pady=10)
        
        name_entry = tk.Entry(self.content_frame)
        name_entry.pack(padx=10, pady=10)
        
        label_quantity_entry = tk.Label(self.content_frame, text="Quantity")
        label_quantity_entry.pack(padx=10, pady=10)
        
        quantity_entry = tk.Entry(self.content_frame)
        quantity_entry.pack(padx=10, pady=10)
        
        label_price_entry = tk.Label(self.content_frame, text="Price")
        label_price_entry.pack(padx=10, pady=10)
        
        price_entry = tk.Entry(self.content_frame)
        price_entry.pack(padx=10, pady=10)
        
        def add_item_to_gudang():
            name = name_entry.get()
            quantity_str = quantity_entry.get()
            price_str = price_entry.get()
            
            if name and quantity_str.isdigit() and price_str.isdigit():
                quantity = int(quantity_str)
                price = int(price_str)
                self.gudang.addItem(name, quantity, price)
                messagebox.showinfo("Sukses", "Data Berhasil Ditambahkan")
                self.display_all()
            else:
                messagebox.showerror("Input Error", "Please enter valid name, quantity, and price.")
        
        add_button = tk.Button(self.content_frame, text="Add", command=add_item_to_gudang)
        add_button.pack(padx=10, pady=10)

    def remove_item(self):
        self.clear_content_frame()
        
        label_name = tk.Label(self.content_frame, text="Masukan Nama Yang Ingin di Hapus!")
        label_name.pack(padx=10, pady=10)
        
        name_entry = tk.Entry(self.content_frame)
        name_entry.pack(padx=10, pady=10)
        
        def remove_item_in_gudang():
            name = name_entry.get()  # Get the name when the button is clicked
            if self.gudang.searchByName(name):
                self.gudang.removeItemByName(name)
                messagebox.showwarning("Sukses", "Data Berhasil Dihapus")
                self.display_all()
            else:
                messagebox.showerror("Error", "Nama tidak ditemukan")
        
        delete_button = tk.Button(self.content_frame, text="Delete", command=remove_item_in_gudang)
        delete_button.pack(padx=10, pady=10)

    def search_item(self):
        id = simpledialog.askstring("Input", "Enter item ID to search:")
        if id:
            item = self.gudang.SearchItemById(id)
            self.clear_content_frame()
            self.content_text = tk.Text(self.content_frame)
            self.content_text.pack(fill=tk.BOTH, expand=True)
            self.content_text.delete(1.0, tk.END)
            if item:
                self.content_text.insert(tk.END, f"Item found: {item.to_list()}\n")
            else:
                self.content_text.insert(tk.END, "Item not found.\n")

    def sort_by_price(self):
        self.gudang.sortByPrice()
        self.display_all()
        
    def sort_by_quantity(self):
        self.gudang.sortByQuantity()
        self.display_all()
        
    def sort_by_id(self):
        self.gudang.sortById()
        self.display_all()

# <---------------------- Main program ---------------------->
if __name__ == "__main__":
    gudang = Gudang()
    app = GudangApp(gudang)
    app.mainloop()
# <---------------------- End Main program ---------------------->

