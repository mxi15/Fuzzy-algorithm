#初始化
t = temperature = [56,28,18,80,70]  #输入的温度
hy = humidity = [33,20,40,50,10]    #输入的湿度
tl = temperatureLow = [0,0,0,0,0]            #温度低的隶属度
tm = temperatureMid = [0,0,0,0,0]           #温度中的隶属度
thr = temperatureHighter = [0,0,0,0,0]        #温度较高的隶属度
tht = temperatureHightest = [0,0,0,0,0]        #温度较高的隶属度
hl = humidityLow = [0,0,0,0,0]              #湿度低的隶属度
hm = humidityMid = [0,0,0,0,0]             #湿度中的隶属度
hh = humidityHight = [0,0,0,0,0]        #湿度高的隶属度
til = timeLow = [0,0,0,0,0]
tim = timeMid = [0,0,0,0,0]
tih = timeHight = [0,0,0,0,0]
time = [0,0,0,0,0]                         #最终时间

#温度隶属度函数(三角)
def temperLow(x):
    if 0 < x < 25:
        return -x/25 + 1
    else: return 0
def temperMid(x):
    if 0 < x < 25:
        return x/25
    elif 25 < x < 50:
        return -x/25 + 2
    else: return 0
def temperHigher(x):
    if 25 < x < 50:
        return x/25 - 1
    elif 50 < x < 75:
        return -x/25 + 3
    else: return 0
def temprtHighest(x):
    if 50 < x < 75:
        return x/25 - 2
    elif 75 < x < 100:
        return -x/25 + 4
    else: return 0

#湿度隶属度函数(三角)
def humLow(x):
    if 0 < x < 25:
        return -x/25 + 1
    else: return 0
def humMid(x):
    if 15 < x < 30:
        return x/15 - 1
    elif 30 < x <45:
        return -x/15 + 3
    else: return 0
def humHight(x):
    if 35 < x < 60:
        return x/25 - 7/5
    else: return 0

#运行
for i in range(len(t)):
    tl[i] = temperLow(t[i])
    tm[i] = temperMid(t[i])
    thr[i] = temperHigher(t[i])
    tht[i] = temprtHighest(t[i])
    hl[i] = humLow(hy[i])
    hm[i] = humMid(hy[i])
    hh[i] = humHight(hy[i])
    til[i] = max(min(hm[i],tl[i]),min(hm[i],tm[i]),min(hm[i],thr[i]),min(hh[i],tm[i]))
    tim[i] = max(min(hl[i],tl[i]),min(hl[i],tm[i]),\
            min(hm[i],tht[i]),min(hh[i],thr[i]),min(hh[i],tht[i]))
    tih[i] = max(min(hl[i],thr[i]),min(hl[i],tht[i]),min(hh[i],tl[i]))  
    time[i] = (100*til[i]+500*tim[i]+1000*tih[i])/(til[i]+tim[i]+tih[i])
    print('温度:{:.2f},湿度:{:.2f},运转时间:{:.2f}'.format(t[i],hy[i],time[i]))