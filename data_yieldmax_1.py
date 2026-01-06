# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 테마 (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/7(수) 06:00", 
            "ex_date": "1/7(수)",
            "pay_date": "1/8(목)" 
        },

        "tickers": {
            'CHPY': {'div': 0.5040, 'rate': 45.27, 'sec': 0.00, 'roc': 86.94, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.2609, 'rate': 52.97, 'sec': 79.10, 'roc': 56.15, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.2077, 'rate': 34.31, 'sec': 42.30, 'roc': 59.45, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2915, 'rate': 35.22, 'sec': 0.00, 'roc': 0.00, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2885, 'rate': 55.93, 'sec': 3.47, 'roc': 26.23, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.1749, 'rate': 20.85, 'sec': 0.23, 'roc': 11.43, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.1575, 'rate': 20.30, 'sec': 1.48, 'roc': 4.38, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.1344, 'rate': 15.60, 'sec': 0.03, 'roc': 10.43, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.4097, 'rate': 65.78, 'sec': 1.81, 'roc': 55.59, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.4705, 'rate': 65.05, 'sec': 0.00, 'roc': 0.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0503, 'rate': 18.42, 'sec': 64.33, 'roc': 33.75, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.0880, 'rate': 44.62, 'sec': 94.58, 'roc': 50.79, 'name': 'Universe Fund'},
        }
    }
