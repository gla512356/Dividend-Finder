# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/4(수) 06:00", 
            "ex_date": "2/4(수)",
            "pay_date": "2/5(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5253, 'rate': 45.02, 'sec': 0.00, 'roc': 0.00, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2924, 'rate': 68.27, 'sec': 88.90, 'roc': 56.50, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.2429, 'rate': 45.40, 'sec': 49.07, 'roc': 56.37, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2384, 'rate': 30.09, 'sec': 0.00, 'roc': 100.00, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2353, 'rate': 51.54, 'sec': 0.00, 'roc': 100.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.2577, 'rate': 30.89, 'sec': 0.00, 'roc': 100.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.2599, 'rate': 33.38, 'sec': 0.00, 'roc': 100.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.2218, 'rate': 25.76, 'sec': 0.00, 'roc': 100.00, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3745, 'rate': 65.25, 'sec': 2.62, 'roc': 83.48, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.4541, 'rate': 65.90, 'sec': 0.00, 'roc': 100.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0829, 'rate': 30.80, 'sec': 62.04, 'roc': 38.60, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0821, 'rate': 45.99, 'sec': 97.68, 'roc': 54.42, 'name': 'Universe Fund'},
        }
    }
