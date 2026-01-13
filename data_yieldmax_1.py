# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/14(수) 06:00", 
            "ex_date": "1/14(수)",
            "pay_date": "1/15(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5196, 'rate': 45.24, 'sec': 0.00, 'roc': 100.00, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2494, 'rate': 51.50, 'sec': 79.10, 'roc': 61.86, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.1765, 'rate': 29.55, 'sec': 42.30, 'roc': 61.71, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.3365, 'rate': 40.50, 'sec': 0.00, 'roc': 72.24, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2835, 'rate': 55.95, 'sec': 3.47, 'roc': 89.24, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.2416, 'rate': 28.62, 'sec': 0.23, 'roc': 100.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.2741, 'rate': 35.10, 'sec': 1.48, 'roc': 100.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.1805, 'rate': 20.80, 'sec': 0.03, 'roc': 81.60, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3580, 'rate': 60.56, 'sec': 1.81, 'roc': 95.63, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.5186, 'rate': 70.83, 'sec': 0.00, 'roc': 100.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0634, 'rate': 23.25, 'sec': 64.33, 'roc': 0.30, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0816, 'rate': 41.82, 'sec': 94.58, 'roc': 41.70, 'name': 'Universe Fund'},
        }
    }
