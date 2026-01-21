# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 Theme (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/22(목) 06:00", 
            "ex_date": "1/22(목)",
            "pay_date": "1/23(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2259, 'rate': 26.29, 'sec': 4.07, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1635, 'rate': 53.42, 'sec': 2.88, 'roc': 3.88, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3542, 'rate': 47.95, 'sec': 0.91, 'roc': 93.33, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0606, 'rate': 24.42, 'sec': 3.03, 'roc': 0.00, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0473, 'rate': 20.36, 'sec': 2.03, 'roc': 0.00, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.1277, 'rate': 47.68, 'sec': 3.44, 'roc': 53.36, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1228, 'rate': 14.67, 'sec': 2.62, 'roc': 5.93, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.2219, 'rate': 30.23, 'sec': 3.49, 'roc': 88.56, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.2991, 'rate': 70.96, 'sec': 4.35, 'roc': 76.75, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.3117, 'rate': 61.09, 'sec': 2.79, 'roc': 0.00, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.2362, 'rate': 32.56, 'sec': 2.16, 'roc': 92.70, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3516, 'rate': 34.86, 'sec': 2.57, 'roc': 0.00, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0511, 'rate': 22.76, 'sec': 2.80, 'roc': 8.24, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2576, 'rate': 47.19, 'sec': 2.20, 'roc': 52.16, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0467, 'rate': 21.06, 'sec': 2.59, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.2607, 'rate': 50.33, 'sec': 1.90, 'roc': 38.73, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1677, 'rate': 49.05, 'sec': 2.53, 'roc': 95.90, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.2020, 'rate': 29.67, 'sec': 2.90, 'roc': 63.67, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.1052, 'rate': 37.29, 'sec': 2.55, 'roc': 93.80, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.2433, 'rate': 55.68, 'sec': 5.17, 'roc': 0.74, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.4636, 'rate': 55.20, 'sec': 1.93, 'roc': 67.29, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0567, 'rate': 19.84, 'sec': 1.82, 'roc': 0.00, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.1387, 'rate': 91.66, 'sec': 7.97, 'roc': 96.51, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.3737, 'rate': 102.53, 'sec': 2.39, 'roc': 98.42, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0582, 'rate': 20.95, 'sec': 2.85, 'roc': 85.86, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.4300, 'rate': 75.12, 'sec': 1.45, 'roc': 94.69, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0605, 'rate': 28.21, 'sec': 3.41, 'roc': 26.89, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.0848, 'rate': 31.71, 'sec': 2.65, 'roc': 72.87, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2191, 'rate': 31.24, 'sec': 2.75, 'roc': 90.99, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.3791, 'rate': 41.11, 'sec': 2.73, 'roc': 76.48, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2283, 'rate': 30.86, 'sec': 1.97, 'roc': 89.39, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2938, 'rate': 56.47, 'sec': 4.42, 'roc': 93.15, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.3929, 'rate': 58.15, 'sec': 2.23, 'roc': 86.91, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.1184, 'rate': 74.04, 'sec': 4.36, 'roc': 95.85, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0743, 'rate': 34.46, 'sec': 2.92, 'roc': 0.00, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.2865, 'rate': 42.85, 'sec': 2.67, 'roc': 74.15, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1890, 'rate': 61.45, 'sec': 2.46, 'roc': 96.16, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.4452, 'rate': 65.36, 'sec': 0.89, 'roc': 98.30, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.0878, 'rate': 36.84, 'sec': 2.64, 'roc': 92.77, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.2602, 'rate': 42.66, 'sec': 3.37, 'roc': 10.81, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.3355, 'rate': 49.92, 'sec': 2.73, 'roc': 94.41, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0387, 'rate': 16.54, 'sec': 2.50, 'roc': 0.00, 'name': 'Short N100 Strategy'},
        }
    }
