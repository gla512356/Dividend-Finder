# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "1/27(화) 06:00", 
            "ex_date": "1/27(화)",
            "pay_date": "1/28(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.1752, 'rate': 32.41, 'sec': 4.18, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.1837, 'rate': 38.27, 'sec': 4.26, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0405, 'rate': 24.73, 'sec': 5.31, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0545, 'rate': 20.85, 'sec': 4.98, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0765, 'rate': 24.01, 'sec': 3.94, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.1680, 'rate': 31.56, 'sec': 2.49, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1192, 'rate': 41.14, 'sec': 4.96, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0748, 'rate': 20.57, 'sec': 3.10, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.1067, 'rate': 20.12, 'sec': 2.46, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
