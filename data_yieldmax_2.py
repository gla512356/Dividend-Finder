# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 테마 (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/15(목) 06:00", 
            "ex_date": "1/15(목)",
            "pay_date": "1/16(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2873, 'rate': 31.32, 'sec': 4.07, 'roc': 91.36, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1850, 'rate': 56.05, 'sec': 2.88, 'roc': 94.31, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3206, 'rate': 44.04, 'sec': 0.91, 'roc': 89.42, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0959, 'rate': 36.81, 'sec': 3.03, 'roc': 92.37, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0415, 'rate': 16.92, 'sec': 2.03, 'roc': 0.00, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.0864, 'rate': 31.26, 'sec': 3.44, 'roc': 90.90, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1260, 'rate': 14.74, 'sec': 2.62, 'roc': 79.68, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.3965, 'rate': 48.74, 'sec': 3.49, 'roc': 93.48, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.3418, 'rate': 71.25, 'sec': 4.35, 'roc': 99.72, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2422, 'rate': 49.36, 'sec': 2.79, 'roc': 94.35, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.3134, 'rate': 41.09, 'sec': 2.16, 'roc': 0.00, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3628, 'rate': 36.64, 'sec': 2.57, 'roc': 0.00, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0521, 'rate': 22.67, 'sec': 2.80, 'roc': 0.00, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.1772, 'rate': 30.73, 'sec': 2.20, 'roc': 0.00, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0583, 'rate': 25.18, 'sec': 2.59, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.2449, 'rate': 50.88, 'sec': 1.90, 'roc': 0.00, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1281, 'rate': 39.14, 'sec': 2.53, 'roc': 94.33, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3306, 'rate': 48.38, 'sec': 2.90, 'roc': 94.43, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.0981, 'rate': 33.51, 'sec': 2.55, 'roc': 0.00, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.2416, 'rate': 52.57, 'sec': 5.17, 'roc': 100.00, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.5501, 'rate': 58.40, 'sec': 1.93, 'roc': 85.49, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0768, 'rate': 26.11, 'sec': 1.82, 'roc': 0.00, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.1188, 'rate': 73.49, 'sec': 7.97, 'roc': 92.21, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.2477, 'rate': 70.32, 'sec': 2.39, 'roc': 0.00, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0593, 'rate': 20.63, 'sec': 2.85, 'roc': 85.31, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.4137, 'rate': 67.05, 'sec': 1.45, 'roc': 93.90, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0645, 'rate': 29.14, 'sec': 3.41, 'roc': 92.41, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.0950, 'rate': 34.24, 'sec': 2.65, 'roc': 87.38, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2490, 'rate': 33.99, 'sec': 2.75, 'roc': 91.68, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.4130, 'rate': 42.23, 'sec': 2.73, 'roc': 93.43, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2419, 'rate': 31.84, 'sec': 1.97, 'roc': 88.78, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2547, 'rate': 45.26, 'sec': 4.42, 'roc': 93.50, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.6558, 'rate': 88.85, 'sec': 2.23, 'roc': 0.00, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.0860, 'rate': 56.69, 'sec': 4.36, 'roc': 40.68, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0674, 'rate': 30.76, 'sec': 2.92, 'roc': 89.89, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3495, 'rate': 49.45, 'sec': 2.67, 'roc': 100.00, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1387, 'rate': 43.79, 'sec': 2.46, 'roc': 0.00, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.5767, 'rate': 81.40, 'sec': 0.89, 'roc': 29.22, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.0669, 'rate': 28.90, 'sec': 2.64, 'roc': 0.00, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.3775, 'rate': 57.38, 'sec': 3.37, 'roc': 0.00, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.2358, 'rate': 35.06, 'sec': 2.73, 'roc': 91.81, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0373, 'rate': 16.23, 'sec': 2.50, 'roc': 0.00, 'name': 'Short N100 Strategy'},
        }
    }
