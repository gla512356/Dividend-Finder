# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/11(수) 06:00", 
            "ex_date": "2/11(수)",
            "pay_date": "2/12(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5293, 'rate': 45.61, 'sec': 0.00, 'roc': 34.54, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2323, 'rate': 59.42, 'sec': 88.90, 'roc': 48.79, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.1595, 'rate': 32.66, 'sec': 49.07, 'roc': 48.37, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2328, 'rate': 30.18, 'sec': 0.00, 'roc': 0.00, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2170, 'rate': 50.45, 'sec': 0.00, 'roc': 0.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.3163, 'rate': 39.00, 'sec': 0.00, 'roc': 0.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.3464, 'rate': 44.20, 'sec': 0.00, 'roc': 0.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.2650, 'rate': 31.20, 'sec': 0.00, 'roc': 0.00, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3660, 'rate': 65.23, 'sec': 2.62, 'roc': 94.01, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.4505, 'rate': 65.30, 'sec': 0.00, 'roc': 0.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.1149, 'rate': 44.25, 'sec': 62.04, 'roc': 78.72, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0743, 'rate': 43.50, 'sec': 97.68, 'roc': 59.48, 'name': 'Universe Fund'},
        }
    }
