# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/12(목) 06:00", 
            "ex_date": "2/12(목)",
            "pay_date": "2/13(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2284, 'rate': 28.86, 'sec': 2.68, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1495, 'rate': 55.64, 'sec': 3.58, 'roc': 0.00, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3498, 'rate': 54.65, 'sec': 2.62, 'roc': 0.00, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0783, 'rate': 35.57, 'sec': 2.73, 'roc': 0.00, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.1774, 'rate': 70.75, 'sec': 2.23, 'roc': 94.79, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.1138, 'rate': 42.87, 'sec': 2.49, 'roc': 0.00, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1489, 'rate': 17.45, 'sec': 2.78, 'roc': 83.18, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.2556, 'rate': 49.08, 'sec': 3.88, 'roc': 92.72, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.2306, 'rate': 68.38, 'sec': 4.39, 'roc': 100.00, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.3023, 'rate': 61.22, 'sec': 2.52, 'roc': 95.63, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.2861, 'rate': 46.03, 'sec': 2.67, 'roc': 58.13, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3568, 'rate': 37.41, 'sec': 2.47, 'roc': 93.31, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0715, 'rate': 32.24, 'sec': 2.76, 'roc': 13.12, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2242, 'rate': 49.60, 'sec': 2.71, 'roc': 87.90, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0776, 'rate': 33.21, 'sec': 2.49, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.6287, 'rate': 100.44, 'sec': 1.61, 'roc': 98.77, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1629, 'rate': 49.83, 'sec': 2.29, 'roc': 95.27, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3892, 'rate': 53.75, 'sec': 2.47, 'roc': 96.11, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.0958, 'rate': 34.66, 'sec': 2.40, 'roc': 0.00, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.1543, 'rate': 61.41, 'sec': 5.84, 'roc': 0.00, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.3423, 'rate': 51.89, 'sec': 2.55, 'roc': 92.49, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0620, 'rate': 21.11, 'sec': 2.83, 'roc': 87.92, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.0909, 'rate': 80.48, 'sec': 4.27, 'roc': 94.52, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.3473, 'rate': 100.71, 'sec': 1.50, 'roc': 12.52, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0693, 'rate': 27.47, 'sec': 3.00, 'roc': 88.32, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.2980, 'rate': 64.53, 'sec': 1.57, 'roc': 98.59, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0611, 'rate': 30.19, 'sec': 3.33, 'roc': 0.00, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.1057, 'rate': 38.73, 'sec': 2.36, 'roc': 2.53, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2043, 'rate': 32.35, 'sec': 2.80, 'roc': 89.89, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.3845, 'rate': 50.64, 'sec': 3.42, 'roc': 0.00, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.1954, 'rate': 35.24, 'sec': 3.74, 'roc': 93.73, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.3174, 'rate': 68.55, 'sec': 6.55, 'roc': 35.60, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.2981, 'rate': 65.51, 'sec': 2.75, 'roc': 0.00, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.1322, 'rate': 82.33, 'sec': 3.41, 'roc': 96.73, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0770, 'rate': 41.54, 'sec': 3.24, 'roc': 90.09, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3307, 'rate': 50.01, 'sec': 2.84, 'roc': 34.18, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1342, 'rate': 41.10, 'sec': 2.34, 'roc': 94.11, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.4544, 'rate': 64.18, 'sec': 0.76, 'roc': 97.61, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.1934, 'rate': 75.11, 'sec': 2.41, 'roc': 98.65, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.2619, 'rate': 48.47, 'sec': 3.63, 'roc': 98.16, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2193, 'rate': 45.64, 'sec': 3.04, 'roc': 88.31, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0630, 'rate': 26.82, 'sec': 2.47, 'roc': 90.47, 'name': 'Short N100 Strategy'},
        }
    }
