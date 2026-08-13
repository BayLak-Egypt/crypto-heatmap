class Plugin:
    def __init__(self, base_class):
        self.instance = base_class(name="Solana", icon_path="assets/sol.png")
        self.symbol = "SOL-USD"
        self.group_id = 1
    def calculate_status(self, price):
        return self.instance.calculate_status(price)