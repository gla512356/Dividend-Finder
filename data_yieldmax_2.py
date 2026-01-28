# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/29(목) 06:00", 
            "ex_date": "1/29(목)",
            "pay_date": "1/30(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2495, 'rate': 28.76, 'sec': 4.07, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1399, 'rate': 45.65, 'sec': 2.88, 'roc': 0.00, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.5465, 'rate': 70.90, 'sec': 0.91, 'roc': 96.38, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0650, 'rate': 25.30, 'sec': 3.03, 'roc': 89.00, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0494, 'rate': 20.47, 'sec': 2.03, 'roc': 87.78, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.1695, 'rate': 60.51, 'sec': 3.44, 'roc': 95.68, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1239, 'rate': 14.88, 'sec': 2.62, 'roc': 49.60, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.3089, 'rate': 45.31, 'sec': 3.49, 'roc': 0.00, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.2660, 'rate': 65.10, 'sec': 4.35, 'roc': 0.00, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2252, 'rate': 45.21, 'sec': 2.79, 'roc': 94.31, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.4630, 'rate': 60.35, 'sec': 2.16, 'roc': 69.19, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3787, 'rate': 38.73, 'sec': 2.57, 'roc': 52.45, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0500, 'rate': 22.27, 'sec': 2.80, 'roc': 1.56, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2435, 'rate': 47.58, 'sec': 2.20, 'roc': 9.59, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0627, 'rate': 25.97, 'sec': 2.59, 'roc': 89.80, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.3263, 'rate': 60.47, 'sec': 1.90, 'roc': 97.63, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.2837, 'rate': 80.58, 'sec': 2.53, 'roc': 97.28, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3639, 'rate': 50.16, 'sec': 2.90, 'roc': 95.19, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.1032, 'rate': 35.58, 'sec': 2.55, 'roc': 0.00, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.2341, 'rate': 55.37, 'sec': 5.17, 'roc': 0.00, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.4542, 'rate': 54.55, 'sec': 1.93, 'roc': 95.11, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0585, 'rate': 20.68, 'sec': 1.82, 'roc': 0.00, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.1265, 'rate': 83.82, 'sec': 7.97, 'roc': 58.93, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.4791, 'rate': 125.60, 'sec': 2.39, 'roc': 97.87, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0641, 'rate': 22.05, 'sec': 2.85, 'roc': 86.92, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.3725, 'rate': 65.29, 'sec': 1.45, 'roc': 9.29, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0846, 'rate': 40.08, 'sec': 3.41, 'roc': 0.00, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.1076, 'rate': 38.66, 'sec': 2.65, 'roc': 0.00, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2154, 'rate': 30.47, 'sec': 2.75, 'roc': 0.00, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.3688, 'rate': 40.75, 'sec': 2.73, 'roc': 0.00, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2202, 'rate': 29.58, 'sec': 1.97, 'roc': 89.54, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2169, 'rate': 45.51, 'sec': 4.42, 'roc': 91.15, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.3545, 'rate': 59.43, 'sec': 2.23, 'roc': 0.00, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.0958, 'rate': 61.15, 'sec': 4.36, 'roc': 95.37, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0778, 'rate': 35.20, 'sec': 2.92, 'roc': 47.86, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3244, 'rate': 47.56, 'sec': 2.67, 'roc': 0.00, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1266, 'rate': 40.40, 'sec': 2.46, 'roc': 93.59, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.4392, 'rate': 65.70, 'sec': 0.89, 'roc': 98.50, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.0931, 'rate': 38.25, 'sec': 2.64, 'roc': 93.42, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.2718, 'rate': 43.87, 'sec': 3.37, 'roc': 92.68, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2514, 'rate': 40.18, 'sec': 2.73, 'roc': 92.69, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0352, 'rate': 15.38, 'sec': 2.50, 'roc': 0.00, 'name': 'Short N100 Strategy'},
        }
    }
