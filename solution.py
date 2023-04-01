import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    
    n = len(x)
    s2=np.var(x, ddof=1)
    q1 = chi2.ppf(p/2, df = n -1)
    q2 = chi2.ppf(alpha/2, df = n-1)
    left = np.sqrt((n-1)*s2/q2)/np.sqrt(48)
    right =  np.sqrt((n-1)*s2/q1)/np.sqrt(48)
    
    return (left, right)


