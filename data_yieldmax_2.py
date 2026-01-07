# data_yieldmax_2.py

def get_data():
    return {
        "title": "YieldMax Option Income (Group 2)",
        # YieldMax Group 2 테마 (Deep Night: Navy & Cyan)
        "theme_color": ["#1a2980", "#26d0ce"], 

        "schedule": {
            "buy_limit": "1/8(목) 06:00", 
            "ex_date": "1/8(목)",
            "pay_date": "1/9(금)"
        },

        "tickers": {
            'ABNY': {'div': 0.2688, 'rate': 29.70, 'sec': 4.07, 'roc': 0.00, 'name': 'ABNB Option Strategy'},
            'AIYY': {'div': 0.1894, 'rate': 55.43, 'sec': 2.88, 'roc': 39.33, 'name': 'AI Option Strategy'},
            'AMDY': {'div': 0.3984, 'rate': 55.04, 'sec': 0.91, 'roc': 89.62, 'name': 'AMD Option Strategy'},
            'AMZY': {'div': 0.0655, 'rate': 25.13, 'sec': 3.03, 'roc': 0.00, 'name': 'AMZN Option Strategy'},
            'APLY': {'div': 0.0481, 'rate': 19.42, 'sec': 2.03, 'roc': 0.00, 'name': 'AAPL Option Strategy'},
            'BABO': {'div': 0.1166, 'rate': 45.08, 'sec': 3.44, 'roc': 93.22, 'name': 'BABA Option Strategy'},
            'BRKC': {'div': 0.1005, 'rate': 11.66, 'sec': 2.62, 'roc': 64.42, 'name': 'BRKB Option Strategy'},
            'CONY': {'div': 0.4091, 'rate': 50.53, 'sec': 3.49, 'roc': 74.22, 'name': 'COIN Option Strategy'},
            'CRCO': {'div': 0.3702, 'rate': 76.38, 'sec': 4.35, 'roc': 15.24, 'name': 'CRCL Option Strategy'},
            'CRSH': {'div': 0.2334, 'rate': 46.15, 'sec': 2.79, 'roc': 94.00, 'name': 'Short TSLA Strategy'},
            'CVNY': {'div': 0.3112, 'rate': 42.63, 'sec': 2.16, 'roc': 8.04, 'name': 'CVNA Option Strategy'},
            'DIPS': {'div': 0.3758, 'rate': 38.23, 'sec': 2.57, 'roc': 11.89, 'name': 'Short NVDA Strategy'},
            'DISO': {'div': 0.0448, 'rate': 19.23, 'sec': 2.80, 'roc': 0.00, 'name': 'DIS Option Strategy'},
            'DRAY': {'div': 0.2900, 'rate': 49.33, 'sec': 2.20, 'roc': 0.00, 'name': 'DKNG Option Strategy'},
            'FBY': {'div': 0.0642, 'rate': 26.50, 'sec': 2.59, 'roc': 0.00, 'name': 'META Option Strategy'},
            'FIAT': {'div': 0.2700, 'rate': 55.34, 'sec': 1.90, 'roc': 77.34, 'name': 'Short COIN Strategy'},
            'GDXY': {'div': 0.1280, 'rate': 39.91, 'sec': 2.53, 'roc': 94.08, 'name': 'Gold Miners Strategy'},
            'GMEY': {'div': 0.3220, 'rate': 46.72, 'sec': 2.90, 'roc': 31.58, 'name': 'GME Option Strategy'},
            'GOOY': {'div': 0.0799, 'rate': 28.51, 'sec': 2.55, 'roc': 59.99, 'name': 'GOOGL Option Strategy'},
            'HIYY': {'div': 0.2949, 'rate': 58.79, 'sec': 5.17, 'roc': 2.19, 'name': 'HIMS Option Strategy'},
            'HOOY': {'div': 0.5526, 'rate': 57.83, 'sec': 1.93, 'roc': 39.76, 'name': 'HOOD Option Strategy'},
            'JPMO': {'div': 0.0542, 'rate': 17.17, 'sec': 1.82, 'roc': 0.00, 'name': 'JPM Option Strategy'},
            'MARO': {'div': 0.1318, 'rate': 83.86, 'sec': 7.97, 'roc': 17.88, 'name': 'MARA Option Strategy'},
            'MRNY': {'div': 0.1765, 'rate': 55.56, 'sec': 2.39, 'roc': 10.47, 'name': 'MRNA Option Strategy'},
            'MSFO': {'div': 0.0532, 'rate': 18.18, 'sec': 2.85, 'roc': 84.13, 'name': 'MSFT Option Strategy'},
            'MSTY': {'div': 0.3741, 'rate': 64.23, 'sec': 1.45, 'roc': 91.90, 'name': 'MSTR Option Strategy'},
            'NFLY': {'div': 0.0722, 'rate': 32.32, 'sec': 3.41, 'roc': 71.14, 'name': 'NFLX Option Strategy'},
            'NVDY': {'div': 0.1054, 'rate': 37.57, 'sec': 2.65, 'roc': 21.81, 'name': 'NVDA Option Strategy'},
            'OARK': {'div': 0.2382, 'rate': 32.67, 'sec': 2.75, 'roc': 16.95, 'name': 'Innovation Strategy'},
            'PLTY': {'div': 0.4508, 'rate': 45.50, 'sec': 2.73, 'roc': 0.00, 'name': 'PLTR Option Strategy'},
            'PYPY': {'div': 0.2429, 'rate': 30.57, 'sec': 1.97, 'roc': 85.12, 'name': 'PYPL Option Strategy'},
            'RBLY': {'div': 0.2457, 'rate': 46.78, 'sec': 4.42, 'roc': 13.23, 'name': 'RBLX Option Strategy'},
            'RDYY': {'div': 0.4737, 'rate': 61.08, 'sec': 2.23, 'roc': 100.00, 'name': 'RDDT Option Strategy'},
            'SMCY': {'div': 0.0728, 'rate': 45.41, 'sec': 4.36, 'roc': 90.09, 'name': 'SMCI Option Strategy'},
            'SNOY': {'div': 0.0868, 'rate': 35.41, 'sec': 2.92, 'roc': 0.00, 'name': 'SNOW Option Strategy'},
            'TSLY': {'div': 0.3183, 'rate': 45.95, 'sec': 2.67, 'roc': 0.00, 'name': 'TSLA Option Strategy'},
            'TSMY': {'div': 0.1104, 'rate': 35.16, 'sec': 2.46, 'roc': 93.05, 'name': 'TSM Option Strategy'},
            'WNTR': {'div': 0.5276, 'rate': 72.09, 'sec': 0.89, 'roc': 0.00, 'name': 'Short MSTR Strategy'},
            'XOMO': {'div': 0.0524, 'rate': 23.38, 'sec': 2.64, 'roc': 92.17, 'name': 'XOM Option Strategy'},
            'XYZY': {'div': 0.3452, 'rate': 50.21, 'sec': 3.37, 'roc': 32.26, 'name': 'XYZ Option Strategy'},
            'YBIT': {'div': 0.3054, 'rate': 45.52, 'sec': 2.73, 'roc': 90.40, 'name': 'Bitcoin Option Strategy'},
            'YQQQ': {'div': 0.0530, 'rate': 22.96, 'sec': 2.50, 'roc': 88.16, 'name': 'Short N100 Strategy'},
        }
    }
