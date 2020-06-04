from datetime import datetime

def time_con(dd):
    a = datetime.fromisoformat(dd)
    return a.strftime('%Y-%m-%d')