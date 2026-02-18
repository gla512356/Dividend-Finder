# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "2/19(목) 06:00", 
            "ex_date": "2/19(목)",
            "pay_date": "2/20(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.3195, 'rate': 39.09, 'sec': 2.68, 'roc': 86.22, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1501, 'rate': 59.36, 'sec': 3.58, 'roc': 94.67, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.2793, 'rate': 45.93, 'sec': 2.62, 'roc': 93.22, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0875, 'rate': 40.82, 'sec': 2.73, 'roc': 16.63, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0498, 'rate': 20.87, 'sec': 2.23, 'roc': 87.08, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.0965, 'rate': 38.67, 'sec': 2.49, 'roc': 92.47, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1479, 'rate': 17.30, 'sec': 2.78, 'roc': 63.34, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.2994, 'rate': 57.54, 'sec': 3.88, 'roc': 94.12, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.2302, 'rate': 67.55, 'sec': 4.39, 'roc': 95.77, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2644, 'rate': 52.47, 'sec': 2.52, 'roc': 0.00, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.2744, 'rate': 49.01, 'sec': 2.67, 'roc': 93.46, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3791, 'rate': 39.51, 'sec': 2.47, 'roc': 0.00, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0759, 'rate': 35.71, 'sec': 2.76, 'roc': 41.31, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2270, 'rate': 59.19, 'sec': 2.71, 'roc': 92.67, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0812, 'rate': 36.40, 'sec': 2.49, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.6050, 'rate': 100.49, 'sec': 1.61, 'roc': 98.21, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1938, 'rate': 60.96, 'sec': 2.29, 'roc': 96.14, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3711, 'rate': 54.36, 'sec': 2.47, 'roc': 0.00, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.1017, 'rate': 38.79, 'sec': 2.40, 'roc': 0.00, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.1706, 'rate': 71.78, 'sec': 5.84, 'roc': 96.29, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.3306, 'rate': 55.96, 'sec': 2.55, 'roc': 93.85, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0571, 'rate': 20.15, 'sec': 2.83, 'roc': 0.00, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.0927, 'rate': 84.14, 'sec': 4.27, 'roc': 94.90, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.3174, 'rate': 90.39, 'sec': 1.50, 'roc': 96.60, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0739, 'rate': 30.32, 'sec': 3.00, 'roc': 88.31, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.3607, 'rate': 80.83, 'sec': 1.57, 'roc': 97.91, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0634, 'rate': 33.40, 'sec': 3.33, 'roc': 0.00, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.0944, 'rate': 35.38, 'sec': 2.36, 'roc': 92.62, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2281, 'rate': 36.89, 'sec': 2.80, 'roc': 75.08, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.3865, 'rate': 53.18, 'sec': 3.42, 'roc': 95.65, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2137, 'rate': 39.34, 'sec': 3.74, 'roc': 87.50, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.3169, 'rate': 75.26, 'sec': 6.55, 'roc': 100.00, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.2938, 'rate': 69.54, 'sec': 2.75, 'roc': 94.30, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.1221, 'rate': 83.43, 'sec': 3.41, 'roc': 0.00, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0919, 'rate': 51.24, 'sec': 3.24, 'roc': 92.19, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3213, 'rate': 50.15, 'sec': 2.84, 'roc': 94.08, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1427, 'rate': 43.74, 'sec': 2.34, 'roc': 0.00, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.7318, 'rate': 100.54, 'sec': 0.76, 'roc': 97.50, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.1126, 'rate': 45.84, 'sec': 2.41, 'roc': 0.00, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.2469, 'rate': 51.48, 'sec': 3.63, 'roc': 0.00, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2396, 'rate': 50.68, 'sec': 3.04, 'roc': 0.00, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0681, 'rate': 28.62, 'sec': 2.47, 'roc': 31.95, 'name': 'Short N100 Strategy'},
        }
    }
