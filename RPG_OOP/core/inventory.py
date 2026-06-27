class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        nomor = 0
        print("=== INVENTORY ===")
        for item in self.items:
            nomor += 1
            print(nomor, item.nama)
        print("=================")