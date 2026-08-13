import customtkinter as ctk
import yfinance as yf
import threading
import webbrowser
import os
from PIL import Image
from plugin_manager import discover_plugins
from grid import TreeMapGrid
from about import AboutWindow
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Crypto Heatmap")
        self.geometry("1000x700")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, "assets")
        try:
            self.yt_icon_image = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_dir, "youtube_icon.png")),
                dark_image=Image.open(os.path.join(assets_dir, "youtube_icon.png")),
                size=(20, 20)
            )
            self.gh_icon_image = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_dir, "github_icon.png")),
                dark_image=Image.open(os.path.join(assets_dir, "github_icon.png")),
                size=(20, 20)
            )
        except FileNotFoundError:
            print("تحذير: لم يتم العثور على مجلد 'assets' أو ملفات الصور. يرجى التأكد من المسارات.")
            self.yt_icon_image = None
            self.gh_icon_image = None
        self.plugins = discover_plugins()
        self.create_top_bar()
        self.grid = TreeMapGrid(self)
        self.initial_draw_done = False
        self.update_chart()
    def create_top_bar(self):
        top_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        top_frame.pack(side="top", fill="x")
        container = ctk.CTkFrame(top_frame, fg_color="transparent")
        container.pack(fill="x", padx=15, pady=8)
        social_frame = ctk.CTkFrame(container, fg_color="transparent")
        social_frame.pack(side="left")
        gh_btn = ctk.CTkButton(
            social_frame,
            text="",
            image=self.gh_icon_image,
            width=35,
            height=35,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray85", "gray20"),
            command=lambda: webbrowser.open("https://github.com/BayLak-Egypt")
        )
        gh_btn.pack(side="left", padx=(0, 5))
        yt_btn = ctk.CTkButton(
            social_frame,
            text="",
            image=self.yt_icon_image,
            width=35,
            height=35,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray85", "gray20"),
            command=lambda: webbrowser.open("https://www.youtube.com/@baylak-egypt")
        )
        yt_btn.pack(side="left")
        right_frame = ctk.CTkFrame(container, fg_color="transparent")
        right_frame.pack(side="right")
        coins_count = len(self.plugins)
        self.coins_label = ctk.CTkLabel(
            right_frame,
            text=f"Coins: {coins_count}",
            font=("Segoe UI", 12, "bold"),
            text_color=("gray40", "gray60")
        )
        self.coins_label.pack(side="left", padx=15)
        about_btn = ctk.CTkButton(
            right_frame,
            text="ℹ About",
            font=("Segoe UI", 12),
            width=90,
            height=30,
            fg_color=("gray80", "gray20"),
            text_color=("black", "white"),
            hover_color=("gray70", "gray30"),
            command=self.open_about_window
        )
        about_btn.pack(side="left")
    def open_about_window(self):
        if not hasattr(self, "about_win") or not self.about_win.winfo_exists():
            self.about_win = AboutWindow(self)
        else:
            self.about_win.focus()
    def update_chart(self):
        threading.Thread(target=self.fetch_and_update, daemon=True).start()
        self.after(10000, self.update_chart)
    def fetch_and_update(self):
        data_list = []
        for p in self.plugins:
            try:
                ticker = yf.Ticker(p.symbol)
                hist = ticker.history(period="1d", interval="1m")
                if not hist.empty:
                    price = hist['Close'].iloc[-1]
                    change, _ = p.calculate_status(price)
                    data_list.append({
                        "name": p.instance.name,
                        "price": price,
                        "change": float(str(change).replace("%", "").replace("+", "")),
                        "group": p.group_id
                    })
            except Exception as e:
                print(f"Error fetching {p.symbol}: {e}")
        if data_list:
            self.after(0, lambda: self.apply_update(data_list))
    def apply_update(self, data_list):
        sorted_data = sorted(data_list, key=lambda x: x['name'])
        if not self.initial_draw_done:
            self.grid.draw(sorted_data, self.plugins)
            self.initial_draw_done = True
        else:
            for data in sorted_data:
                name = data['name']
                if name in self.grid.boxes:
                    plugin = next((p for p in self.plugins if p.instance.name == name), None)
                    icon = plugin.instance.icon_path if plugin else None
                    self.grid.boxes[name].update_content(data, icon)
            self.grid.canvas.draw_idle()
if __name__ == "__main__":
    app = App()
    app.mainloop()