a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a)) #ソフトマックス関数の計算

c = np.max(a) # 1010
a - c

np.exp(a - c) / np.sum(np.exp(a -c))
# e^0 / (e^0 + e^-10 + e^-20) ,
# e^-10 / (e^0 + e^-10 + e^-20),
# e^-20 / (e^0 + e^-10 + e^-20)
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
