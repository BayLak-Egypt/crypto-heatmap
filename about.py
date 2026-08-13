import customtkinter as ctk
import re
import urllib.request
import threading
import webbrowser
class AboutWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("About")
        self.geometry("450x600")
        self.resizable(False, False)
        self.setup_ui()
        self.update_idletasks()
        self.transient(master)
        try:
            self.grab_set()
        except Exception as e:
            print(f"Grab warning: {e}")
    def setup_ui(self):
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        ctk.CTkLabel(main_frame, text="Crypto & Investment Hub 🚀",
                     font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        desc_text = (
            "A professional application for tracking financial markets, "
            "crypto assets, and investment trends. Developed by BayLak Egypt "
            "to empower your financial growth through smart analytics."
        )
        ctk.CTkLabel(main_frame, text=desc_text, wraplength=380, justify="center").pack(pady=10)
        ctk.CTkFrame(main_frame, height=2, fg_color=("gray70", "gray30")).pack(fill="x", pady=10)
        ctk.CTkLabel(main_frame, text="🌐 Connect With Us:", font=ctk.CTkFont(weight="bold")).pack(pady=5)
        self.social_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.social_frame.pack(fill="x", pady=10)
        self.status_label = ctk.CTkLabel(self.social_frame, text="Loading links...", text_color="gray")
        self.status_label.pack()
        threading.Thread(target=self.fetch_social_links, daemon=True).start()
    def fetch_social_links(self):
        url = "https://raw.githubusercontent.com/BayLak-Egypt/baylak-egypt.github.io/refs/heads/main/mysocial.txt"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                content = response.read().decode("utf-8").strip()
            matches = re.findall(r"(\w+)\s*=\s*(\S+)", content)
            self.after(0, lambda: self.status_label.destroy())
            for platform, link in matches:
                full_link = link if link.startswith("http") else f"https://{link}"
                btn = ctk.CTkButton(
                    self.social_frame,
                    text=platform.capitalize(),
                    command=lambda l=full_link: webbrowser.open(l),
                    fg_color="black",
                    hover_color="gray20",
                    text_color="white",
                    height=32
                )
                btn.pack(fill="x", pady=3)
        except Exception:
            self.after(0, lambda: self.status_label.configure(text="⚠️ Failed to load links.", text_color="red"))