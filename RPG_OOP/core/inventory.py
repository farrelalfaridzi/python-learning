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
        else:
            return False

    def show_inventory(self):
        nomor = 0
        print("=== INVENTORY ===")
        for item in self.items:
            nomor += 1
            print(f"{nomor}. {item.nama} ({item.__class__.__name__})")
        print("=================")

    def choose_item(self, index):
        index -= 1
        if index >= len(self.items) or index <0:
            return None
        else:
            return self.items[index]