# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "12/30(화) 06:00", 
            "ex_date": "12/30(화)",
            "pay_date": "12/31(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.1724, 'rate': 31.36, 'sec': 4.56, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.3084, 'rate': 60.70, 'sec': 4.38, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0400, 'rate': 25.29, 'sec': 7.13, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0600, 'rate': 20.60, 'sec': 5.55, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0896, 'rate': 0.00,  'sec': 0.00, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.1665, 'rate': 0.00,  'sec': 0.00, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1256, 'rate': 0.00,  'sec': 0.00, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0800, 'rate': 0.00,  'sec': 0.00, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.0870, 'rate': 0.00,  'sec': 0.00, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }