import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

# Try to import customtkinter for modern UI, fallback to tkinter
try:
    import customtkinter as ctk
    USE_CUSTOMTKINTER = True
except ImportError:
    USE_CUSTOMTKINTER = False

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("💱 Currency Exchange Rate Converter")
        
        # Configure window
        if USE_CUSTOMTKINTER:
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.root.geometry("600x700")
        else:
            self.root.geometry("600x700")
            self.root.config(bg="#1a1a2e")
        
        # Supported currencies (expanded list)
        self.currencies = [
            "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY",
            "INR", "PHP", "SGD", "HKD", "NZD", "KRW", "MXN", "BRL",
            "ZAR", "RUB", "TRY", "AED", "THB", "MYR", "IDR", "VND"
        ]
        
        self.from_currency = tk.StringVar(value="USD")
        self.to_currency = tk.StringVar(value="PHP")
        self.amount = tk.StringVar(value="1.00")
        self.exchange_rate = tk.StringVar(value="")
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the modern UI"""
        if USE_CUSTOMTKINTER:
            self.setup_customtkinter_ui()
        else:
            self.setup_tkinter_ui()
    
    def setup_customtkinter_ui(self):
        """Modern UI using CustomTkinter"""
        # Header
        header = ctk.CTkLabel(
            self.root,
            text="Currency Converter",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#4A90E2"
        )
        header.pack(pady=(30, 10))
        
        subtitle = ctk.CTkLabel(
            self.root,
            text="Real-time Exchange Rates",
            font=ctk.CTkFont(size=14),
            text_color="#888"
        )
        subtitle.pack(pady=(0, 30))
        
        # Main container
        container = ctk.CTkFrame(self.root, corner_radius=20)
        container.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Amount input section
        amount_label = ctk.CTkLabel(
            container,
            text="Amount",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        amount_label.pack(pady=(20, 10))
        
        self.amount_entry = ctk.CTkEntry(
            container,
            textvariable=self.amount,
            font=ctk.CTkFont(size=24),
            height=50,
            width=400
        )
        self.amount_entry.pack(pady=10)
        
        # Currency selection section
        currency_frame = ctk.CTkFrame(container)
        currency_frame.pack(pady=20, padx=20, fill="x")
        
        # From currency
        from_label = ctk.CTkLabel(
            currency_frame,
            text="From",
            font=ctk.CTkFont(size=12),
            text_color="#888"
        )
        from_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        
        self.from_combobox = ctk.CTkComboBox(
            currency_frame,
            values=self.currencies,
            variable=self.from_currency,
            width=200,
            font=ctk.CTkFont(size=16),
            command=self.on_currency_change
        )
        self.from_combobox.grid(row=1, column=0, padx=20, pady=(0, 20))
        
        # Swap button
        swap_btn = ctk.CTkButton(
            currency_frame,
            text="⇄",
            width=50,
            height=50,
            font=ctk.CTkFont(size=20),
            command=self.swap_currencies,
            fg_color="#4A90E2",
            hover_color="#357ABD"
        )
        swap_btn.grid(row=1, column=1, padx=10, pady=(0, 20))
        
        # To currency
        to_label = ctk.CTkLabel(
            currency_frame,
            text="To",
            font=ctk.CTkFont(size=12),
            text_color="#888"
        )
        to_label.grid(row=0, column=2, padx=20, pady=(20, 5))
        
        self.to_combobox = ctk.CTkComboBox(
            currency_frame,
            values=self.currencies,
            variable=self.to_currency,
            width=200,
            font=ctk.CTkFont(size=16),
            command=self.on_currency_change
        )
        self.to_combobox.grid(row=1, column=2, padx=20, pady=(0, 20))
        
        # Exchange rate display
        self.rate_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=12),
            text_color="#666"
        )
        self.rate_label.pack(pady=10)
        
        # Convert button
        self.convert_btn = ctk.CTkButton(
            container,
            text="Convert",
            command=self.convert_currency,
            font=ctk.CTkFont(size=18, weight="bold"),
            height=50,
            width=400,
            fg_color="#4A90E2",
            hover_color="#357ABD"
        )
        self.convert_btn.pack(pady=20)
        
        # Result display
        result_frame = ctk.CTkFrame(container, corner_radius=15)
        result_frame.pack(pady=20, padx=20, fill="x")
        
        self.result_label = ctk.CTkLabel(
            result_frame,
            text="",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#4A90E2"
        )
        self.result_label.pack(pady=30)
        
        # Footer with timestamp
        self.footer_label = ctk.CTkLabel(
            container,
            text="",
            font=ctk.CTkFont(size=10),
            text_color="#555"
        )
        self.footer_label.pack(pady=(0, 20))
        
        # Load initial rate
        self.on_currency_change()
    
    def setup_tkinter_ui(self):
        """Fallback UI using standard Tkinter with modern styling"""
        # Header
        header = tk.Label(
            self.root,
            text="Currency Converter",
            font=("Segoe UI", 32, "bold"),
            bg="#1a1a2e",
            fg="#4A90E2"
        )
        header.pack(pady=(30, 10))
        
        subtitle = tk.Label(
            self.root,
            text="Real-time Exchange Rates",
            font=("Segoe UI", 14),
            bg="#1a1a2e",
            fg="#888"
        )
        subtitle.pack(pady=(0, 30))
        
        # Main container
        container = tk.Frame(self.root, bg="#16213e", relief=tk.FLAT, bd=0)
        container.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Amount input
        amount_label = tk.Label(
            container,
            text="Amount",
            font=("Segoe UI", 14, "bold"),
            bg="#16213e",
            fg="#fff"
        )
        amount_label.pack(pady=(20, 10))
        
        self.amount_entry = tk.Entry(
            container,
            textvariable=self.amount,
            font=("Segoe UI", 24),
            bg="#0f3460",
            fg="#fff",
            insertbackground="#fff",
            relief=tk.FLAT,
            bd=10,
            width=20,
            justify=tk.CENTER
        )
        self.amount_entry.pack(pady=10)
        
        # Currency selection
        currency_frame = tk.Frame(container, bg="#16213e")
        currency_frame.pack(pady=20, padx=20, fill="x")
        
        # From currency
        from_label = tk.Label(
            currency_frame,
            text="From",
            font=("Segoe UI", 12),
            bg="#16213e",
            fg="#888"
        )
        from_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        
        self.from_combobox = ttk.Combobox(
            currency_frame,
            values=self.currencies,
            textvariable=self.from_currency,
            width=18,
            font=("Segoe UI", 16),
            state="readonly"
        )
        self.from_combobox.grid(row=1, column=0, padx=20, pady=(0, 20))
        self.from_combobox.bind("<<ComboboxSelected>>", lambda e: self.on_currency_change())
        
        # Swap button
        swap_btn = tk.Button(
            currency_frame,
            text="⇄",
            font=("Segoe UI", 20),
            bg="#4A90E2",
            fg="#fff",
            activebackground="#357ABD",
            activeforeground="#fff",
            relief=tk.FLAT,
            width=3,
            height=1,
            command=self.swap_currencies,
            cursor="hand2"
        )
        swap_btn.grid(row=1, column=1, padx=10, pady=(0, 20))
        
        # To currency
        to_label = tk.Label(
            currency_frame,
            text="To",
            font=("Segoe UI", 12),
            bg="#16213e",
            fg="#888"
        )
        to_label.grid(row=0, column=2, padx=20, pady=(20, 5))
        
        self.to_combobox = ttk.Combobox(
            currency_frame,
            values=self.currencies,
            textvariable=self.to_currency,
            width=18,
            font=("Segoe UI", 16),
            state="readonly"
        )
        self.to_combobox.grid(row=1, column=2, padx=20, pady=(0, 20))
        self.to_combobox.bind("<<ComboboxSelected>>", lambda e: self.on_currency_change())
        
        # Exchange rate display
        self.rate_label = tk.Label(
            container,
            text="",
            font=("Segoe UI", 12),
            bg="#16213e",
            fg="#666"
        )
        self.rate_label.pack(pady=10)
        
        # Convert button
        self.convert_btn = tk.Button(
            container,
            text="Convert",
            command=self.convert_currency,
            font=("Segoe UI", 18, "bold"),
            bg="#4A90E2",
            fg="#fff",
            activebackground="#357ABD",
            activeforeground="#fff",
            relief=tk.FLAT,
            width=25,
            height=2,
            cursor="hand2"
        )
        self.convert_btn.pack(pady=20)
        
        # Result display
        result_frame = tk.Frame(container, bg="#0f3460", relief=tk.FLAT)
        result_frame.pack(pady=20, padx=20, fill="x")
        
        self.result_label = tk.Label(
            result_frame,
            text="",
            font=("Segoe UI", 28, "bold"),
            bg="#0f3460",
            fg="#4A90E2"
        )
        self.result_label.pack(pady=30)
        
        # Footer
        self.footer_label = tk.Label(
            container,
            text="",
            font=("Segoe UI", 10),
            bg="#16213e",
            fg="#555"
        )
        self.footer_label.pack(pady=(0, 20))
        
        # Load initial rate
        self.on_currency_change()
    
    def get_rate(self, from_currency, to_currency):
        """Fetch exchange rate from API"""
        try:
            # Primary API
            url = f"https://api.exchangerate.host/latest?base={from_currency}"
            response = requests.get(url, timeout=5)
            data = response.json()

            if "rates" in data and to_currency in data["rates"]:
                return data["rates"][to_currency]
            
            # Backup API
            backup_url = f"https://open.er-api.com/v6/latest/{from_currency}"
            backup_response = requests.get(backup_url, timeout=5)
            backup_data = backup_response.json()

            if "rates" in backup_data and to_currency in backup_data["rates"]:
                return backup_data["rates"][to_currency]
            
            raise ValueError("No valid rate found from either API.")
            
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Connection Error", f"Failed to fetch exchange rate.\nPlease check your internet connection.\n\n{e}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch exchange rate.\n{e}")
            return None

    def on_currency_change(self, *args):
        """Update exchange rate when currency selection changes"""
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        if from_curr == to_curr:
            if USE_CUSTOMTKINTER:
                self.rate_label.configure(text=f"1 {from_curr} = 1.0000 {to_curr}")
            else:
                self.rate_label.config(text=f"1 {from_curr} = 1.0000 {to_curr}")
        return

        # Update button text
        if USE_CUSTOMTKINTER:
            self.convert_btn.configure(text="Loading...", state="disabled")
        else:
            self.convert_btn.config(text="Loading...", state="disabled")
        
        # Fetch rate in background
        self.root.after(100, lambda: self.update_rate_display(from_curr, to_curr))
    
    def update_rate_display(self, from_curr, to_curr):
        """Update the exchange rate display"""
        rate = self.get_rate(from_curr, to_curr)
        
        if rate:
            rate_text = f"1 {from_curr} = {rate:.4f} {to_curr}"
            if USE_CUSTOMTKINTER:
                self.rate_label.configure(text=rate_text)
                self.convert_btn.configure(text="Convert", state="normal")
            else:
                self.rate_label.config(text=rate_text)
                self.convert_btn.config(text="Convert", state="normal")
        else:
            if USE_CUSTOMTKINTER:
                self.convert_btn.configure(text="Convert", state="normal")
            else:
                self.convert_btn.config(text="Convert", state="normal")
    
    def swap_currencies(self):
        """Swap the from and to currencies"""
        from_val = self.from_currency.get()
        to_val = self.to_currency.get()
        
        self.from_currency.set(to_val)
        self.to_currency.set(from_val)
        
        # Trigger conversion with new values
        self.on_currency_change()
        self.convert_currency()
    
    def convert_currency(self):
        """Convert the currency"""
        try:
            amount = float(self.amount.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return
        
        if amount < 0:
            messagebox.showwarning("Invalid Input", "Amount cannot be negative!")
            return
        
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        if from_curr == to_curr:
            result_text = f"{amount:,.2f} {from_curr}"
        else:
            rate = self.get_rate(from_curr, to_curr)
            
            if rate:
                result = amount * rate
                result_text = f"{amount:,.2f} {from_curr} = {result:,.2f} {to_curr}"
                
                # Update footer with timestamp
                timestamp = datetime.now().strftime("Last updated: %Y-%m-%d %H:%M:%S")
                if USE_CUSTOMTKINTER:
                    self.footer_label.configure(text=timestamp)
                else:
                    self.footer_label.config(text=timestamp)
            else:
                result_text = "Error fetching exchange rate"
        
        if USE_CUSTOMTKINTER:
            self.result_label.configure(text=result_text)
        else:
            self.result_label.config(text=result_text)

def main():
    root = tk.Tk() if not USE_CUSTOMTKINTER else ctk.CTk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
