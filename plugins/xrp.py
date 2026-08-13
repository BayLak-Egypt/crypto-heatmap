class Plugin:
    def __init__(self, base_class):
        self.instance = base_class(name="Ripple", icon_path="assets/xrp.png")
        self.symbol = "XRP-USD"
        self.group_id = 1
    def calculate_status(self, price):
        return self.instance.calculate_status(price)