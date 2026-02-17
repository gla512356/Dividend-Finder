# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/18(수) 06:00", 
            "ex_date": "2/18(수)",
            "pay_date": "2/19(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5259, 'rate': 45.16, 'sec': 0.00, 'roc': 100.00, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2314, 'rate': 61.89, 'sec': 88.90, 'roc': 3.93, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.1731, 'rate': 36.95, 'sec': 49.07, 'roc': 0.02, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2619, 'rate': 35.16, 'sec': 0.00, 'roc': 43.62, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2294, 'rate': 55.83, 'sec': 0.00, 'roc': 0.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.3057, 'rate': 39.00, 'sec': 0.00, 'roc': 100.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.3392, 'rate': 44.20, 'sec': 0.00, 'roc': 100.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.2327, 'rate': 28.10, 'sec': 0.00, 'roc': 100.00, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3696, 'rate': 65.46, 'sec': 2.62, 'roc': 12.51, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.4360, 'rate': 65.66, 'sec': 0.00, 'roc': 99.87, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.1076, 'rate': 43.47, 'sec': 62.04, 'roc': 77.03, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0778, 'rate': 47.85, 'sec': 97.68, 'roc': 58.54, 'name': 'Universe Fund'},
        }
    }
