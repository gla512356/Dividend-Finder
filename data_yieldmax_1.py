# data_yieldmax_1.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 1)",
        # YieldMax Group 1 테마 (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "12/31(수) 06:00", 
            "ex_date": "12/31(수)",
            "pay_date": "1/2(금)" 
        },

        "tickers": {
            'CHPY': {'div': 0.4401, 'rate': 40.59, 'sec': 0.00, 'roc': 99.47, 'name': 'Semiconductor Portfolio'},
            'FEAT': {'div': 0.3415, 'rate': 69.07, 'sec': 69.57, 'roc': 60.49, 'name': 'Dorsey Wright Featured 5'},
            'FIVY': {'div': 0.2507, 'rate': 41.55, 'sec': 37.98, 'roc': 60.37, 'name': 'Dorsey Wright Hybrid 5'},
            'GPTY': {'div': 0.2565, 'rate': 30.99, 'sec': 0.00, 'roc': 0.00, 'name': 'AI & Tech Portfolio'},
            'LFGY': {'div': 0.2481, 'rate': 50.04, 'sec': 0.00, 'roc': 0.00, 'name': 'Crypto Industry & Tech'},
            'QDTY': {'div': 0.1494, 'rate': 17.70, 'sec': 0.20, 'roc': 0.00, 'name': 'Nasdaq 100 0DTE'},
            'RDTY': {'div': 0.2049, 'rate': 26.63, 'sec': 1.15, 'roc': 0.00, 'name': 'R2000 0DTE'},
            'SDTY': {'div': 0.1240, 'rate': 14.37, 'sec': 0.13, 'roc': 0.00, 'name': 'S&P 500 0DTE'},
            'SLTY': {'div': 0.3947, 'rate': 60.13, 'sec': 2.05, 'roc': 95.76, 'name': 'Ultra Short Option'},
            'ULTY': {'div': 0.4866, 'rate': 65.97, 'sec': 0.00, 'roc': 0.00, 'name': 'Ultra Option Strategy'},
            'YMAG': {'div': 0.0992, 'rate': 35.86, 'sec': 59.29, 'roc': 59.48, 'name': 'Magnificent 7 Fund'},
            'YMAX': {'div': 0.1060, 'rate': 53.95, 'sec': 85.99, 'roc': 59.11, 'name': 'Universe Fund'},
        }
    }