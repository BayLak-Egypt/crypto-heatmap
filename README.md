# 🚀 Crypto Heatmap

> **Real-Time Cryptocurrency Market Visualization for Desktop**


<img width="1012" height="741" alt="Screenshot from 2026-08-13 20-14-08" src="https://github.com/user-attachments/assets/cc83d684-a843-4560-9173-efb3f46860d8" />


Crypto Heatmap is a lightweight, modular, and modern desktop application built with **Python** and **CustomTkinter**. It provides a real-time visual overview of cryptocurrency market performance through an interactive **TreeMap grid**, making it easy to identify market movements at a glance.

The application is designed with a modular plugin architecture, allowing cryptocurrencies and other supported assets to be added, removed, or managed independently.

---

## ✨ Features

### 📊 Real-Time Market Data

* Fetches live cryptocurrency market information using **Yahoo Finance** through `yfinance`.
* Continuously updates market performance.
* Uses background threading to prevent the interface from freezing during data requests.

### 🗺️ Interactive TreeMap

* Displays cryptocurrencies inside a dynamic grid.
* Each asset is represented by an interactive visual box.
* Market performance is represented using percentage changes.
* Makes positive and negative movements easy to identify visually.

### 🧩 Modular Plugin System

Crypto Heatmap uses a dedicated plugin architecture for managing assets.

* Easily add new cryptocurrencies.
* Remove or modify existing assets.
* Automatically discover available plugins.
* Keep individual asset configurations separated from the main application.

### 🎨 Modern Desktop Interface

Built with **CustomTkinter** for a modern Python desktop experience.

* Clean and lightweight interface.
* Light and Dark appearance support.
* Responsive UI.
* Modern widgets and layouts.

### 🔗 Quick Access

The application provides quick access to developer resources, including:

* GitHub repository
* YouTube channel
* Developer updates and project resources

---

## 🛠️ Technology Stack

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| 🐍 **Python 3.x**     | Core programming language           |
| 🖥️ **CustomTkinter** | Modern desktop GUI                  |
| 📈 **yfinance**       | Yahoo Finance market data           |
| 🖼️ **Pillow (PIL)**  | Image processing and asset handling |

---

## 📂 Project Structure

```text
Crypto-Heatmap/
│
├── assets/
│   └── Icons, images, and media resources
│
├── plugins/
│   └── Cryptocurrency and asset plugins
│
├── about.py
│   └── About window and developer information
│
├── base.py
│   └── Base classes and plugin definitions
│
├── deadcited-server.py
│   └── Optional server / utility component
│
├── grid.py
│   └── TreeMap grid layout and asset boxes
│
├── plugin_manager.py
│   └── Plugin discovery and loading system
│
├── app.py
│   └── Application controller and UI logic
│
└── main.py
    └── Main application entry point
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BayLak-Egypt/Crypto-Heatmap.git
```

### 2. Enter the Project Directory

```bash
cd Crypto-Heatmap
```

### 3. Install Dependencies

```bash
pip install customtkinter yfinance pillow
```

Or install them individually:

```bash
pip install customtkinter
pip install yfinance
pip install pillow
```

---

## ▶️ Running the Application

Start Crypto Heatmap using:

```bash
python main.py
```

The application will launch the desktop interface and begin retrieving market information.

---

## 🧩 Plugin Architecture

One of the main goals of Crypto Heatmap is to keep asset management separate from the core application.

Plugins are stored inside:

```text
plugins/
```

This allows the project to scale without requiring major changes to the main application.

A typical workflow is:

```text
Plugin
   │
   ▼
Plugin Manager
   │
   ▼
Market Data
   │
   ▼
TreeMap Grid
   │
   ▼
Visual Market Overview
```

This modular approach makes it easier to maintain, extend, and customize the application.

---

## 📈 How It Works

Crypto Heatmap follows a simple data visualization pipeline:

```text
Yahoo Finance
      │
      ▼
   yfinance
      │
      ▼
Background Data Fetching
      │
      ▼
Plugin / Asset Management
      │
      ▼
TreeMap Grid
      │
      ▼
Real-Time Market Visualization
```

The use of background processing helps keep the graphical interface responsive while market data is being retrieved.

---

## 🎯 Project Goals

Crypto Heatmap is designed to provide:

* ⚡ Fast market overview
* 📊 Easy-to-understand visualizations
* 🧩 Extensible asset management
* 🎨 Modern desktop UI
* 🛠️ Simple project structure
* 🔄 Continuously updated market information

Instead of relying only on traditional tables and numbers, the TreeMap approach allows users to understand overall market movement visually.

---

## ⚠️ Disclaimer

Crypto Heatmap is a **market visualization and educational software project**.

The information displayed by the application is retrieved from external market-data providers and may be delayed, incomplete, inaccurate, or unavailable.

**Crypto Heatmap does not provide financial, investment, or trading advice.**

Do not use the application as the sole basis for financial or investment decisions.

---

## 🤝 Contributing

Contributions are welcome!

You can help improve the project by:

* 🐛 Reporting bugs
* 💡 Suggesting new features
* 🧩 Creating new plugins
* 🛠️ Improving existing components
* 📚 Improving documentation
* 🔧 Submitting pull requests

For major changes, please open an issue first to discuss the proposed modification.

---

## 🐛 Issues & Feature Requests

Found a bug or have an idea?

Open an issue in the project's GitHub repository and provide as much useful information as possible, including:

* Description of the issue
* Steps to reproduce it
* Expected behavior
* Actual behavior
* Relevant error messages

---

## 🔗 Connect with BayLak

### 💻 GitHub

**BayLak-Egypt**

https://github.com/BayLak-Egypt

### ▶️ YouTube

**@baylak-egypt**

Follow the channel for project updates, development content, and new releases.

---

## ⭐ Support the Project

If you find **Crypto Heatmap** useful:

⭐ Star the repository
🐛 Report bugs
💡 Suggest improvements
🔧 Contribute code
📢 Share the project

Every contribution helps improve the project.

---

## 🛡️ License

This project is open-source and available for educational and developmental purposes.


---
<div align="center">

### 🚀 Crypto Heatmap


**Visualize the Crypto Market. Understand the Movement.**

**Made with ❤️ by BayLak (Egypt <img src="https://github.com/user-attachments/assets/637a365d-98e8-4a47-814c-11965370d212" width="35" height="15" alt="Egypt flag"/>)**

</div>

