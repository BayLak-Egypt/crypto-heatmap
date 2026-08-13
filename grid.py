import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import squarify
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
class BoxItem:
    def __init__(self, ax, data, rect, icon_path=None):
        self.ax = ax
        self.rect = rect
        self.patch = plt.Rectangle((rect['x'], rect['y']), rect['dx'], rect['dy'],
                                   facecolor='#ff4d4d', edgecolor='black', linewidth=1.5)
        self.ax.add_patch(self.patch)
        self.text_info = self.ax.text(0, 0, "", ha='center', va='center', color='white',
                                      fontweight='bold')
        self.text_change = self.ax.text(0, 0, "", ha='center', va='center',
                                        fontweight='bold')
        self.ab = None
        self.update_content(data, icon_path)
    def update_content(self, data, icon_path=None):
        center_x = self.rect['x'] + self.rect['dx'] / 2
        center_y = (self.rect['y'] + self.rect['dy'] / 2) - (self.rect['dy'] * 0.05)
        self.text_info.set_position((center_x, center_y + self.rect['dy'] * 0.05))
        self.text_info.set_text(f"{data['name']}\n{data['price']:.2f}$")
        self.text_info.set_fontsize(max(8, min(self.rect['dx'], self.rect['dy']) * 0.3))
        change_val = float(data['change'])
        color = '#2ecc71' if change_val >= 0 else '#3498db'
        arrow = "▲" if change_val >= 0 else "▼"
        self.text_change.set_position((center_x, center_y - self.rect['dy'] * 0.25))
        self.text_change.set_text(f"{arrow} {change_val}%")
        self.text_change.set_color(color)
        self.text_change.set_fontsize(max(7, min(self.rect['dx'], self.rect['dy']) * 0.25))
        if icon_path and os.path.exists(icon_path):
            try:
                if self.ab:
                    self.ab.remove()
                img = mpimg.imread(icon_path)
                zoom = min(self.rect['dx'], self.rect['dy']) / 500
                imagebox = OffsetImage(img, zoom=zoom)
                self.ab = AnnotationBbox(imagebox, (center_x, center_y + self.rect['dy'] * 0.35), frameon=False)
                self.ax.add_artist(self.ab)
            except Exception:
                pass
class TreeMapGrid:
    def __init__(self, master):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.fig.patch.set_facecolor('#1a1a1a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.boxes = {}
    def draw(self, data_list, plugins):
        sorted_data = sorted(data_list, key=lambda x: x['name'])
        if not self.boxes:
            sizes = [abs(float(d['change'])) + 5 for d in sorted_data]
            normed = squarify.normalize_sizes(sizes, 100, 100)
            rects = squarify.squarify(normed, 0, 0, 100, 100)
            for i, rect in enumerate(rects):
                data = sorted_data[i]
                name = data['name']
                plugin = next((p for p in plugins if p.instance.name == name), None)
                icon_path = plugin.instance.icon_path if plugin else None
                self.boxes[name] = BoxItem(self.ax, data, rect, icon_path)
        else:
            for data in sorted_data:
                name = data['name']
                if name in self.boxes:
                    plugin = next((p for p in plugins if p.instance.name == name), None)
                    icon_path = plugin.instance.icon_path if plugin else None
                    self.boxes[name].update_content(data, icon_path)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.axis('off')
        self.canvas.draw_idle()