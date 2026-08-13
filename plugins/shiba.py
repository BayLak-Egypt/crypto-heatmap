class Plugin:
    def __init__(self, base_class):
        self.instance = base_class(name="Shiba Inu", icon_path="assets/shib.png")
        self.symbol = "SHIB-USD"
        self.group_id = 1
    def calculate_status(self, price):
        return self.instance.calculate_status(price)