# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "1/6(화) 06:00", 
            "ex_date": "1/6(화)",
            "pay_date": "1/7(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.1500, 'rate': 27.44, 'sec': 4.18, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.2650, 'rate': 53.75, 'sec': 4.26, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0400, 'rate': 24.19, 'sec': 5.31, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0640, 'rate': 20.86, 'sec': 4.98, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0900, 'rate': 24.60, 'sec': 3.94, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.0800, 'rate': 15.11, 'sec': 2.49, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.0920, 'rate': 35.91, 'sec': 4.96, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0750, 'rate': 19.71, 'sec': 3.10, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.0860, 'rate': 16.57, 'sec': 2.46, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
