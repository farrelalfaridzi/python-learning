class Shop:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        nomor = 0
        print("===== SHOP =====")
        for item in self.items:
            nomor += 1
            print(f"{nomor}. {item.nama} | {item.harga} gold")
        print("================")

    def choose_item(self, index):
        index -= 1
        if index >= len(self.items) or index <0:
            return None
        else:
            return self.items[index]

    def open(self, player):
        while True:
            self.show_items()
            print(f"Gold : {player.gold}")
            print("#pilih 0 untuk keluar")
            input_nomor = int(input("pilih nomor: "))
            if input_nomor == 0:
                print("keluar shop...")
                break
            else:
                item = self.choose_item(input_nomor)
                if item is None:
                    print("pilihan tidak valid")
                    continue
                player.buy(item)