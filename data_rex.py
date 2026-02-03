# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "2/3(화) 06:00", 
            "ex_date": "2/3(화)",
            "pay_date": "2/4(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.2321, 'rate': 43.60, 'sec': 4.05, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.3820, 'rate': 85.47, 'sec': 4.76, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0373, 'rate': 26.84, 'sec': 4.89, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0491, 'rate': 22.25, 'sec': 5.55, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0651, 'rate': 22.81, 'sec': 3.90, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.1963, 'rate': 38.45, 'sec': 2.52, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1023, 'rate': 34.44, 'sec': 3.21, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0644, 'rate': 20.53, 'sec': 3.54, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.0928, 'rate': 16.85, 'sec': 2.75, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
