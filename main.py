import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    def __init__(self):
        self.items = readFileCsv("items.csv")

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
        self.sortById()
        self.next_id = int(self.items[-1].to_list()[0]) + 1
        self.items.append(Item(str(self.next_id), name, quantity, price))
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
        self.resizable(False, False)
        
        self.create_widgets()

    def create_widgets(self):
        # <----------------- GENERATE NAV FRAME ----------------->
        self.nav_frame = tk.Frame(self, height=40, bg="#175227")
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        # <----------------- GENERATE CONTENT FRAME ----------------->
        self.content_frame = tk.Frame(self, bg="#7d807e")
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # <----------------- GENERATE NAV CONTENT ----------------->
        style_button_nav = ttk.Style()
        style_button_nav.configure('TButton', font=('Helvetica', 8), padding=6, relief='flat', background='#000000', foreground='black')

        self.btn_display_all = ttk.Button(self.nav_frame, text="Display All", command=self.display_all, style='TButton')
        self.btn_display_all.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_add_item = ttk.Button(self.nav_frame, text="Add Item", command=self.add_item, style='TButton')
        self.btn_add_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_remove_item = ttk.Button(self.nav_frame, text="Remove Item", command=self.remove_item, style='TButton')
        self.btn_remove_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_search_item = ttk.Button(self.nav_frame, text="Search Item", command=self.search_item, style='TButton')
        self.btn_search_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_update_item = ttk.Button(self.nav_frame, text="Update Item", command=self.update_item, style='TButton')
        self.btn_update_item.pack(side=tk.LEFT, padx=5, pady=5)
        
        
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def display_all(self):
        self.clear_content_frame()
        
        # <----------------- GENERATE NAV SORT ----------------->
        self.nav_frame_sort = tk.Frame(self.content_frame, height=40, bg="#175227")
        self.nav_frame_sort.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.btn_sort_price = ttk.Button(self.nav_frame_sort, text="Sort by Price", command=self.sort_by_price, style='TButton')
        self.btn_sort_price.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.btn_sort_quantity = ttk.Button(self.nav_frame_sort, text="Sort by Quantity", command=self.sort_by_quantity, style='TButton')
        self.btn_sort_quantity.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.btn_sort_id = ttk.Button(self.nav_frame_sort, text="Sort by ID", command=self.sort_by_id, style='TButton')
        self.btn_sort_id.pack(side=tk.RIGHT, padx=5, pady=5)      
        
        self.canvas_content_frame = tk.Canvas(self.content_frame, bg="#7d807e")
        self.canvas_content_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=40, pady=5)
        
        self.canvas_content_frame_scrolbar = ttk.Scrollbar(self.content_frame, orient=tk.VERTICAL, command=self.canvas_content_frame.yview)
        self.canvas_content_frame_scrolbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas_content_frame.configure(yscrollcommand=self.canvas_content_frame_scrolbar.set)
        self.canvas_content_frame.bind("<Configure>", lambda e : self.canvas_content_frame.configure(scrollregion=self.canvas_content_frame.bbox("all")))
        
        self.box_detail_item = tk.Frame(self.canvas_content_frame, height=30, bg="#7d807e")
        
        self.canvas_content_frame.create_window((0,0), window=self.box_detail_item, anchor=tk.NW)
        
        products = self.gudang.getAllproduct()
        
        for product in products:
            self.box_info = ttk.Label(self.box_detail_item, text=f"Id Barang : {product[0]},\t\t Nama Barang : {product[1]},\t\t Jumlah Barang : {product[2]},\t\t Harga Barang : {product[3]}").pack(side=tk.TOP, padx=10, pady=5, fill="x", expand=True)
        
        
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
        
        add_button = tk.Button(self.content_frame, text="ADD", command=add_item_to_gudang)
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
        
        delete_button = tk.Button(self.content_frame, text="DELETE", command=remove_item_in_gudang)
        delete_button.pack(padx=10, pady=10)

    def search_item(self):
        self.clear_content_frame()
        
        label_name = tk.Label(self.content_frame, text="Masukan Nama Yang Ingin Anda Cari!")
        label_name.pack(padx=10, pady=10)
        
        name_entry = tk.Entry(self.content_frame)
        name_entry.pack(padx=10, pady=10)

        def display_item_in_gudang():
            name = name_entry.get().strip()  # Get the name when the button is clicked
            items = self.gudang.searchByName(name)
            
            if items:
                self.content_text = tk.Text(self.content_frame)
                self.content_text.pack(fill=tk.BOTH, expand=True)
                self.content_text.delete(1.0, tk.END)
                messagebox.showinfo("Sukses", "Data ditemukan")
                
                for item in items:
                    self.content_text.insert(tk.END, f"ID: {item.id}\n")
                    self.content_text.insert(tk.END, f"Nama: {item.name}\n")
                    self.content_text.insert(tk.END, f"Jumlah: {item.quantity}\n")
                    self.content_text.insert(tk.END, f"Harga: {item.price}\n")
                    self.content_text.insert(tk.END, "\n")
            else:
                messagebox.showerror("Error", "Nama tidak ditemukan")
        
        search_button = tk.Button(self.content_frame, text="FIND", command=display_item_in_gudang)
        search_button.pack(padx=10, pady=10)
        
    def update_item(self):
        self.clear_content_frame()

        # Entry for item ID
        label_id = tk.Label(self.content_frame, text="Masukkan ID yang ingin diperbarui:")
        label_id.pack(padx=10, pady=10)

        id_entry = tk.Entry(self.content_frame)
        id_entry.pack(padx=10, pady=10)

        # Entry for new name
        label_new_name = tk.Label(self.content_frame, text="Nama baru (kosongkan jika tidak ingin mengubah):")
        label_new_name.pack(padx=10, pady=10)

        new_name_entry = tk.Entry(self.content_frame)
        new_name_entry.pack(padx=10, pady=10)

        # Entry for new quantity
        label_new_quantity = tk.Label(self.content_frame, text="Jumlah baru (kosongkan jika tidak ingin mengubah):")
        label_new_quantity.pack(padx=10, pady=10)

        new_quantity_entry = tk.Entry(self.content_frame)
        new_quantity_entry.pack(padx=10, pady=10)

        # Entry for new price
        label_new_price = tk.Label(self.content_frame, text="Harga baru (kosongkan jika tidak ingin mengubah):")
        label_new_price.pack(padx=10, pady=10)

        new_price_entry = tk.Entry(self.content_frame)
        new_price_entry.pack(padx=10, pady=10)

        def update_item_in_gudang():
            item_id = id_entry.get().strip()
            new_name = new_name_entry.get().strip()
            new_quantity_str = new_quantity_entry.get().strip()
            new_price_str = new_price_entry.get().strip()

            item = self.gudang.SearchItemById(item_id)
            if item:
                if new_name:
                    self.gudang.setNameItem(item_id, new_name)
                if new_quantity_str.isdigit():
                    new_quantity = int(new_quantity_str)
                    self.gudang.setQuantityItem(item_id, new_quantity)
                if new_price_str.isdigit():
                    new_price = int(new_price_str)
                    self.gudang.setPriceItem(item_id, new_price)
                messagebox.showinfo("Sukses", "Data berhasil diperbarui")
                self.display_all()
            else:
                messagebox.showerror("Error", "ID tidak ditemukan")

        update_button = tk.Button(self.content_frame, text="UPDATE", command=update_item_in_gudang)
        update_button.pack(padx=10, pady=10)

    def sort_by_price(self):
        self.clear_content_frame()
        self.gudang.sortByPrice()
        self.display_all()
        
    def sort_by_quantity(self):
        self.clear_content_frame()
        self.gudang.sortByQuantity()
        self.display_all()
        
    def sort_by_id(self):
        self.clear_content_frame()
        self.gudang.sortById()
        self.display_all()

# <---------------------- Main program ---------------------->
if __name__ == "__main__":
    gudang = Gudang()
    app = GudangApp(gudang)
    app.mainloop()
# <---------------------- End Main program ---------------------->

