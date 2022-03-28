def topTenRetweeted (dataFrame):
    top_ten_retweeted = dataFrame.sort_values('retweetCount', ascending=False)
    top_ten_retweeted = top_ten_retweeted[:10]
    top_ten_retweeted = top_ten_retweeted[['content', 'retweetCount']]
    return top_ten_retweeted
