# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "1/21(수) 06:00", 
            "ex_date": "1/21(수)",
            "pay_date": "1/22(목)" 
        },

        "tickers": {
            'NVII': {'div': 0.2075, 'rate': 40.47, 'sec': 4.18, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.2160, 'rate': 48.29, 'sec': 4.26, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0464, 'rate': 28.83, 'sec': 5.31, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0591, 'rate': 21.34, 'sec': 4.98, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0773, 'rate': 24.14, 'sec': 3.94, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.1798, 'rate': 34.20, 'sec': 2.49, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1106, 'rate': 37.10, 'sec': 4.96, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0795, 'rate': 21.46, 'sec': 3.10, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.1428, 'rate': 26.56, 'sec': 2.46, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
