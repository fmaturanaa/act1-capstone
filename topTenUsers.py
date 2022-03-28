import pandas as pd
from pandas.io.json import json_normalize

def topTenUsers(dataFrame):
    users = json_normalize(dataFrame['user'])
    users = pd.DataFrame(users)
    users.drop_duplicates(subset=['id'], inplace=True)
    users = users.sort_values('statusesCount', ascending=False)
    users = users[:10]
    users = users[['username', 'statusesCount']]
    return users