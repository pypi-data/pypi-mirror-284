def var(data):
    # 计算平均值
    mean = sum(data) / len(data)
    # 计算方差
    var = sum([(i - mean) ** 2 for i in data]) / len(data)
    # 计算标准差
    std = var ** 0.5
    return var

def std(data):
    mean = sum(data) / len(data)
    var = sum([(i - mean) ** 2 for i in data]) / len(data)
    std = var ** 0.5
    return std


