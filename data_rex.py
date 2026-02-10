# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "2/10(화) 06:00", 
            "ex_date": "2/10(화)",
            "pay_date": "2/11(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.2422, 'rate': 47.24, 'sec': 4.05, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.2586, 'rate': 60.68, 'sec': 4.76, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0749, 'rate': 59.89, 'sec': 4.89, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0707, 'rate': 42.02, 'sec': 5.55, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0985, 'rate': 42.36, 'sec': 3.90, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.4747, 'rate': 93.95, 'sec': 2.52, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1411, 'rate': 51.32, 'sec': 3.21, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.1013, 'rate': 35.28, 'sec': 3.54, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.0966, 'rate': 17.27, 'sec': 2.75, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
