class BasePlugin:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path
        self.last_price = None
    def calculate_status(self, current_price):
        icon = "⚪"
        change_pct = 0.0
        if self.last_price is not None:
            change_pct = ((current_price - self.last_price) / self.last_price) * 100
            icon = "▲" if change_pct >= 0 else "▼"
        self.last_price = current_price
        return f"{change_pct:+.2f}%", icon