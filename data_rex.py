# data_rex.py

def get_data():
    return {
        "title": "REX Shares - Growth & Income",
        # REX 테마 컬러 (Dark Navy & Blue)
        "theme_color": ["#021B79", "#0575E6"], 

        "schedule": {
            "buy_limit": "2/17(화) 06:00", 
            "ex_date": "2/17(화)",
            "pay_date": "2/18(수)" 
        },

        "tickers": {
            'NVII': {'div': 0.3143, 'rate': 61.79, 'sec': 4.05, 'roc': 100.00, 'name': 'NVDA Growth & Income'},
            'TSII': {'div': 0.2780, 'rate': 65.73, 'sec': 4.76, 'roc': 100.00, 'name': 'TSLA Growth & Income'},
            'MSII': {'div': 0.0739, 'rate': 61.58, 'sec': 4.89, 'roc': 100.00, 'name': 'MSTR Growth & Income'},
            'COII': {'div': 0.0921, 'rate': 51.91, 'sec': 5.55, 'roc': 100.00, 'name': 'COIN Growth & Income'},
            'HOII': {'div': 0.0988, 'rate': 46.44, 'sec': 3.90, 'roc': 100.00, 'name': 'HOOD Growth & Income'},
            'LLII': {'div': 0.2473, 'rate': 50.18, 'sec': 2.52, 'roc': 100.00, 'name': 'LLY Growth & Income'},
            'CWII': {'div': 0.1344, 'rate': 50.18, 'sec': 3.21, 'roc': 100.00, 'name': 'CRWV Growth & Income'},
            'PLTI': {'div': 0.0992, 'rate': 35.50, 'sec': 3.54, 'roc': 100.00, 'name': 'PLTR Growth & Income'},
            'WMTI': {'div': 0.1958, 'rate': 35.06, 'sec': 2.75, 'roc': 100.00, 'name': 'WMT Growth & Income'},
        }
    }
