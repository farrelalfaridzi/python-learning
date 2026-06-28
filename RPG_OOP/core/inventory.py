class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def has_item(self, item):
        if item in self.items:
            return True

    def show_inventory(self):
        nomor = 0
        print("=== INVENTORY ===")
        for item in self.items:
            nomor += 1
            print(nomor, item.nama)
        print("=================")