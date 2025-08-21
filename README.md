# 🧾 Invoice Calculator (CLI)

A simple **Command Line Invoice Calculator** with a clean and colorful interface.  
This project is implemented in **Python**, using:

- [rich](https://github.com/Textualize/rich) → for colorful & styled CLI output  
- [tabulate](https://github.com/astanin/python-tabulate) → for displaying tables in a neat format  

---

## ✨ Features
- Add products with price, quantity, and discount.  
- Automatic calculation of total and final price.  
- Display results in a **colorful, user-friendly CLI**.  
- Modular design:  
  - **Core logic** in one file  
  - **User interface** (CLI) in another file  

---

## 📂 Project Structure

.
├── core.py # Business logic (invoice calculations uses tabulate package)
├── cli.py # CLI interface (uses rich package)
└── README.md # Documentation

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MohammadReza-py/Invoice_Calculator.git
   cd invoice-calculator

## ▶️ Usage
Run the CLI interface:
  python cli.py

You can use the core.py as package for your project

## 🛠️ Requirements
- python programming language
- rich package
- tabulate package
pip install -r requirements.txt

📌 Notes
- Keep your core logic separate for reusability.
- You can extend the project by adding features like:
  - Saving invoices to a file (CSV, JSON, or PDF).
  - Loading past invoices.
  - Multi-language support.

📜 License

This project is released under the MIT License.
