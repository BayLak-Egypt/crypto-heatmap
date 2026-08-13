class Plugin:
    def __init__(self, base_class):
        self.instance = base_class(name="TRON", icon_path="assets/trx.png")
        self.symbol = "TRX-USD"
        self.group_id = 1
    def calculate_status(self, price):
        return self.instance.calculate_status(price)