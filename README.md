# 💱 Currency Exchange Rate Converter

A modern, user-friendly desktop application for converting currencies with real-time exchange rates. Built with Python and featuring a sleek, dark-themed interface.

## ✨ Features

- **Real-time Exchange Rates** - Get live currency exchange rates from reliable APIs
- **24 Popular Currencies** - Support for USD, EUR, GBP, JPY, PHP, and 20+ more currencies
- **Modern UI** - Beautiful, dark-themed interface with CustomTkinter (falls back to standard Tkinter)
- **Currency Swap** - Quick swap button to instantly reverse currency pairs
- **Auto-updates** - Exchange rate automatically updates when you change currency selections
- **Smart Formatting** - Numbers are formatted with thousand separators for easy reading
- **Error Handling** - Graceful error handling with user-friendly messages
- **Dual API Support** - Automatic fallback to backup API if primary API fails

## 📋 Requirements

- Python 3.7 or higher
- `requests` library (for API calls)
- `customtkinter` library (optional, for modern UI - falls back to tkinter if not installed)

## 🚀 Installation

1. **Clone or download this repository**

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install requests customtkinter
   ```

   > **Note:** If `customtkinter` is not installed, the app will still work using standard Tkinter, but the UI will be less modern.

## 💻 Usage

1. **Run the application:**

   ```bash
   python currency_converter.py
   ```

2. **Using the converter:**

   - Enter the amount you want to convert in the amount field
   - Select the source currency from the "From" dropdown
   - Select the target currency from the "To" dropdown
   - Click the "Convert" button or wait for automatic rate updates
   - View the converted amount and current exchange rate

3. **Quick Swap:**

   - Click the ⇄ button to instantly swap the "From" and "To" currencies

## 🎨 Supported Currencies

The application supports 24 major currencies:

- **Americas:** USD, CAD, MXN, BRL
- **Europe:** EUR, GBP, CHF, RUB
- **Asia-Pacific:** JPY, CNY, INR, PHP, SGD, HKD, THB, MYR, IDR, KRW, VND, AED
- **Oceania:** AUD, NZD
- **Africa:** ZAR
- **Middle East:** TRY

## 🔌 API Information

The application uses two free currency exchange rate APIs with automatic fallback:

1. **Primary API:** [exchangerate.host](https://exchangerate.host/)
2. **Backup API:** [ExchangeRate-API](https://www.exchangerate-api.com/)

Both APIs provide free access to real-time exchange rates without requiring API keys.

## 📁 Project Structure

```
Exchange Currency Rate/
│
├── currency_converter.py    # Main application file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ How It Works

1. **CurrencyConverter Class**: Main application class that handles the UI and business logic
2. **Dual UI Support**: Automatically uses CustomTkinter if available, otherwise falls back to standard Tkinter
3. **Real-time Updates**: Fetches and displays exchange rates when currencies are changed
4. **Error Handling**: Handles network errors and invalid inputs gracefully

## 🎯 Key Functions

- `get_rate()` - Fetches exchange rate from API with fallback support
- `convert_currency()` - Performs currency conversion and updates display
- `swap_currencies()` - Swaps the from/to currency pair
- `on_currency_change()` - Automatically updates exchange rate when currencies change
- `update_rate_display()` - Updates the UI with current exchange rate

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.7+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`

### Exchange rates not loading
- Check your internet connection
- The APIs might be temporarily unavailable (the app will try backup APIs)

### Import errors
- Make sure all dependencies are installed: `pip install requests customtkinter`
- If CustomTkinter is not available, the app will use standard Tkinter

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to submit a pull request.

## 📧 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Made with ❤️ for easy currency conversion**

