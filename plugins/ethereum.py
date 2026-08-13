class Plugin:
    def __init__(self, base_class):
        self.instance = base_class(name="Ethereum", icon_path="assets/eth.png")
        self.symbol = "ETH-USD"
        self.group_id = 1
    def calculate_status(self, price):
        return self.instance.calculate_status(price)