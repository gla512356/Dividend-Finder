# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/5(목) 06:00", 
            "ex_date": "2/5(목)",
            "pay_date": "2/6(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2213, 'rate': 27.54, 'sec': 2.68, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1331, 'rate': 50.42, 'sec': 3.58, 'roc': 92.19, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3466, 'rate': 47.06, 'sec': 2.62, 'roc': 0.00, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0752, 'rate': 29.87, 'sec': 2.73, 'roc': 90.93, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0584, 'rate': 23.60, 'sec': 2.23, 'roc': 89.58, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.1190, 'rate': 44.87, 'sec': 2.49, 'roc': 0.00, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1318, 'rate': 15.62, 'sec': 2.78, 'roc': 65.12, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.2838, 'rate': 46.77, 'sec': 3.88, 'roc': 91.30, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.2284, 'rate': 69.92, 'sec': 4.39, 'roc': 94.15, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2517, 'rate': 49.85, 'sec': 2.52, 'roc': 94.66, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.2835, 'rate': 43.14, 'sec': 2.67, 'roc': 0.00, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3543, 'rate': 35.35, 'sec': 2.47, 'roc': 0.00, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0532, 'rate': 24.99, 'sec': 2.76, 'roc': 35.52, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2128, 'rate': 46.71, 'sec': 2.71, 'roc': 4.03, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.2473, 'rate': 100.92, 'sec': 2.49, 'roc': 97.23, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.4817, 'rate': 80.76, 'sec': 1.61, 'roc': 0.00, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1525, 'rate': 47.82, 'sec': 2.29, 'roc': 95.21, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.4113, 'rate': 56.37, 'sec': 2.47, 'roc': 96.20, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.1124, 'rate': 38.50, 'sec': 2.40, 'roc': 93.68, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.2067, 'rate': 56.20, 'sec': 5.84, 'roc': 94.36, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.3554, 'rate': 51.60, 'sec': 2.55, 'roc': 92.93, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0746, 'rate': 25.45, 'sec': 2.83, 'roc': 86.71, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.0990, 'rate': 75.34, 'sec': 4.27, 'roc': 95.88, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.2662, 'rate': 75.99, 'sec': 1.50, 'roc': 0.00, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0565, 'rate': 22.34, 'sec': 3.00, 'roc': 85.69, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.3083, 'rate': 65.25, 'sec': 1.57, 'roc': 93.12, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0593, 'rate': 29.92, 'sec': 3.33, 'roc': 24.36, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.0939, 'rate': 35.23, 'sec': 2.36, 'roc': 92.80, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2035, 'rate': 31.33, 'sec': 2.80, 'roc': 0.00, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.3591, 'rate': 41.99, 'sec': 3.42, 'roc': 92.82, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.1660, 'rate': 29.43, 'sec': 3.74, 'roc': 85.97, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2001, 'rate': 46.79, 'sec': 6.55, 'roc': 92.14, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.2884, 'rate': 57.16, 'sec': 2.75, 'roc': 88.78, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.0910, 'rate': 61.06, 'sec': 3.41, 'roc': 0.00, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0666, 'rate': 36.50, 'sec': 3.24, 'roc': 0.00, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3302, 'rate': 49.32, 'sec': 2.84, 'roc': 0.00, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1049, 'rate': 33.84, 'sec': 2.34, 'roc': 92.63, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.4920, 'rate': 65.61, 'sec': 0.76, 'roc': 0.00, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.1262, 'rate': 50.22, 'sec': 2.41, 'roc': 95.49, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.2503, 'rate': 45.94, 'sec': 3.63, 'roc': 92.15, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2381, 'rate': 44.25, 'sec': 3.04, 'roc': 0.00, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0393, 'rate': 16.83, 'sec': 2.47, 'roc': 0.00, 'name': 'Short N100 Strategy'},
        }
    }
