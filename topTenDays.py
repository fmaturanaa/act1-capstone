import pandas as pd

def topTenDays(dataFrame):
    dataFrame['day'] = pd.to_datetime(dataFrame['date']).dt.date
    top_ten_days = dataFrame['day'].value_counts()
    top_ten_days = top_ten_days[:10]
    return top_ten_days