# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/21(수) 06:00", 
            "ex_date": "1/21(수)",
            "pay_date": "1/22(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5267, 'rate': 45.51, 'sec': 0.00, 'roc': 100.00, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.3016, 'rate': 63.89, 'sec': 79.10, 'roc': 46.75, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.1895, 'rate': 32.38, 'sec': 42.30, 'roc': 64.35, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2915, 'rate': 35.58, 'sec': 0.00, 'roc': 23.70, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2822, 'rate': 54.19, 'sec': 3.47, 'roc': 0.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.2605, 'rate': 31.19, 'sec': 0.23, 'roc': 63.75, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.2594, 'rate': 32.80, 'sec': 1.48, 'roc': 77.09, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.2014, 'rate': 23.40, 'sec': 0.03, 'roc': 80.96, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3528, 'rate': 60.71, 'sec': 1.81, 'roc': 70.44, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.5054, 'rate': 70.05, 'sec': 0.00, 'roc': 100.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0857, 'rate': 32.01, 'sec': 64.33, 'roc': 59.40, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0824, 'rate': 42.65, 'sec': 94.58, 'roc': 61.09, 'name': 'Universe Fund'},
        }
    }
