# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 테마 (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "12/31(수) 06:00", 
            "ex_date": "1/2(금)",
            "pay_date": "1/5(월)"
        },

        "tickers": {
            'ABNY': {'div': 0.3313, 'rate': 36.12, 'sec': 2.92, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1725, 'rate': 50.71, 'sec': 3.08, 'roc': 0.00, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3796, 'rate': 51.64, 'sec': 1.15, 'roc': 95.55, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0651, 'rate': 25.34, 'sec': 2.97, 'roc': 89.57, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0532, 'rate': 20.69, 'sec': 2.32, 'roc': 89.19, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.0915, 'rate': 35.90, 'sec': 2.37, 'roc': 91.54, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1368, 'rate': 15.71, 'sec': 2.55, 'roc': 11.88, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.4342, 'rate': 56.15, 'sec': 3.91, 'roc': 41.34, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.4012, 'rate': 85.68, 'sec': 4.59, 'roc': 95.86, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2406, 'rate': 48.88, 'sec': 2.60, 'roc': 0.00, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.3320, 'rate': 45.83, 'sec': 2.51, 'roc': 4.85, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3945, 'rate': 40.07, 'sec': 2.75, 'roc': 87.54, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0899, 'rate': 38.28, 'sec': 3.41, 'roc': 58.43, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.3011, 'rate': 50.23, 'sec': 2.84, 'roc': 42.06, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0612, 'rate': 25.03, 'sec': 2.97, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.4126, 'rate': 77.71, 'sec': 2.63, 'roc': 97.58, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1593, 'rate': 51.24, 'sec': 2.64, 'roc': 95.40, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3829, 'rate': 55.11, 'sec': 2.90, 'roc': 5.78, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.0846, 'rate': 30.01, 'sec': 2.37, 'roc': 91.70, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.3145, 'rate': 65.42, 'sec': 4.00, 'roc': 25.20, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.5728, 'rate': 61.44, 'sec': 1.68, 'roc': 26.92, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0812, 'rate': 26.38, 'sec': 1.96, 'roc': 92.54, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.1285, 'rate': 85.29, 'sec': 4.66, 'roc': 92.54, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.1601, 'rate': 55.18, 'sec': 2.85, 'roc': 0.00, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0620, 'rate': 20.75, 'sec': 3.05, 'roc': 85.48, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.4091, 'rate': 70.36, 'sec': 2.73, 'roc': 94.34, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0729, 'rate': 31.54, 'sec': 3.21, 'roc': 87.18, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.1435, 'rate': 50.87, 'sec': 2.58, 'roc': 94.92, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2191, 'rate': 30.88, 'sec': 2.76, 'roc': 0.00, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.5130, 'rate': 50.78, 'sec': 3.06, 'roc': 94.88, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2833, 'rate': 35.61, 'sec': 3.73, 'roc': 97.61, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2572, 'rate': 45.49, 'sec': 3.92, 'roc': 0.00, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.4836, 'rate': 65.98, 'sec': 2.81, 'roc': 0.00, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.0947, 'rate': 60.07, 'sec': 3.90, 'roc': 19.12, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.1081, 'rate': 45.38, 'sec': 2.51, 'roc': 37.95, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3658, 'rate': 50.21, 'sec': 2.77, 'roc': 0.00, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.0906, 'rate': 30.59, 'sec': 2.45, 'roc': 91.35, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.6812, 'rate': 90.88, 'sec': 1.56, 'roc': 83.32, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.0456, 'rate': 20.20, 'sec': 3.28, 'roc': 86.47, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.3337, 'rate': 50.75, 'sec': 3.60, 'roc': 29.32, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2846, 'rate': 43.73, 'sec': 2.45, 'roc': 92.66, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0423, 'rate': 18.18, 'sec': 2.77, 'roc': 0.00, 'name': 'Short N100 Strategy'},
        }
    }