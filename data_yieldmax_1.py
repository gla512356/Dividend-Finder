# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/28(수) 06:00", 
            "ex_date": "1/28(수)",
            "pay_date": "1/29(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.4826, 'rate': 42.15, 'sec': 0.00, 'roc': 100.00, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2173, 'rate': 46.75, 'sec': 79.10, 'roc': 83.34, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.1588, 'rate': 27.36, 'sec': 42.30, 'roc': 83.26, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2831, 'rate': 35.02, 'sec': 0.00, 'roc': 100.00, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2741, 'rate': 55.88, 'sec': 3.47, 'roc': 100.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.2525, 'rate': 30.20, 'sec': 0.23, 'roc': 0.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.2654, 'rate': 33.87, 'sec': 1.48, 'roc': 0.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.2063, 'rate': 23.99, 'sec': 0.03, 'roc': 55.99, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3467, 'rate': 60.27, 'sec': 1.81, 'roc': 95.49, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.5021, 'rate': 70.36, 'sec': 0.00, 'roc': 100.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0754, 'rate': 27.96, 'sec': 64.33, 'roc': 54.37, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0830, 'rate': 43.67, 'sec': 94.58, 'roc': 64.35, 'name': 'Universe Fund'},
        }
    }
