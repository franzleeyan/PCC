import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot


#读取数据，进行处理
dta = [3800643.817,3195356.756,2905928.449,2819945.452,2176637.815,1793570.332,1699566.33,1497019.272,2413549.908,1979961.395,2008415.536,1452536.613,1430134.26,1637599.235,2758991.637,1554319.822,1285427.321,1297343.364,937880.752,932622.8508]
dta = np.array(dta,dtype=np.float)
dta = pd.Series(dta)

#对数据进行绘图，观测是否是平稳时间序列
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('201812','202007'))
# dta.plot(figsize=(12,8))
# plt.show()

# fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(111)
# diff1 = dta.diff(1)
# diff1.plot(ax=ax1)
# plt.show()

#选择合适的p,q
diff1 = dta.diff(1)
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax2)
# plt.show()

#获取最佳模型
arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit()
print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
arma_mod30 = sm.tsa.ARMA(dta,(0,1)).fit()
print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)

#模型检验
resid = arma_mod80.resid
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax2)
plt.show()

print(sm.stats.durbin_watson(arma_mod80.resid.values))

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid,line='q',ax=ax,fit=True)
plt.show()

r,q,p = sm.tsa.acf(resid.values.squeeze(),qstat=True)
data = np.c_[range(1,41),r[1:],q,p]
table = pd.DataFrame(data,columns=['lag','AC','Q','Prob(>Q)'])
print(table.set_index('lag'))

#模型预测
predict_sunspots = arma_mod80.predict('2016','2026',dynamic=True)
print(predict_sunspots)
fig,ax = plt.subplots(figsize=(12,8))
ax = dta.ix['1927':].plot(ax=ax)
fig = arma_mod80.plot_predict('2016','2026',dynamic=True,ax=ax,plot_insample=False)
plt.show()

