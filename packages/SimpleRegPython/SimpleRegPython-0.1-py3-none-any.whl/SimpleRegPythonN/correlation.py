
def mysxy(x, y):
    x_dev = x - x.mean()
    y_dev = y - y.mean()
    temp = x_dev * y_dev
    return temp.sum()

def mysx(x):
    x_dev = x - x.mean()
    temp = x_dev**2
    return temp.sum()

def mycorr(x, y):
    temp1 = mysxy(x, y)
    temp2 = mysx(x)
    temp3 = mysx(y)
    return temp1 / (temp2 * temp3)**0.5
