def topTenHashtags(dataFrame):
    counts = dataFrame['content'].str.findall(r'(#\w+)').explode().value_counts()
    return counts[:10]