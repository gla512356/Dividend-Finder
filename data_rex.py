# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "1/13(화) 06:00", 
            "ex_date": "1/13(화)",
            "pay_date": "1/14(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.2036, 'rate': 37.87, 'sec': 4.18, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.2461, 'rate': 50.82, 'sec': 4.26, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0381, 'rate': 23.44, 'sec': 5.31, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0619, 'rate': 20.88, 'sec': 4.98, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0885, 'rate': 24.78, 'sec': 3.94, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.1371, 'rate': 24.90, 'sec': 2.49, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.0985, 'rate': 33.03, 'sec': 4.96, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0775, 'rate': 19.80, 'sec': 3.10, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.0966, 'rate': 17.86, 'sec': 2.46, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
