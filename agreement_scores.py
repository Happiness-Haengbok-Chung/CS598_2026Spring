import pandas as pd
import numpy as np
from scipy.stats import kendalltau

# 1. 데이터 생성
data = {
    # Grok 계열 데이터
    '4.1-fast-reasoning': [390, 43, 6, 58, 15, 8, 583],
    '4-fast-reasoning': [438, 49, 4, 91, 17, 16, 488],
    '3': [388, 37, 15, 58, 71, 77, 457],
    
    # Gemini 계열 데이터
    '3-Pro-Preview': [106, 14, 0, 5, 7, 4, 967],
    '3-flash': [103, 14, 0, 5, 7, 4, 970],
    '2.5-flash': [319, 48, 63, 25, 9, 26, 613]
}
df = pd.DataFrame(data)

# 2. Cronbach's Alpha 계산
# 직접 계산하는 함수 (표준 공식 적용)
def cronbach_alpha(df):
    item_vars = df.var(axis=0, ddof=1)
    t_var = df.sum(axis=1).var(ddof=1)
    n_items = df.shape[1]
    return (n_items / (n_items - 1)) * (1 - (item_vars.sum() / t_var))

alpha = cronbach_alpha(df)

# 3. Kendall's W 계산
def kendall_w(df):
    dims = df.shape
    m = dims[1]  # 평가자 수 (3)
    n = dims[0]  # 샘플 수 (7)
    
    # 순위로 변환
    ranks = df.rank(axis=0, ascending=False)
    # 각 샘플의 순위 합
    r_sum = ranks.sum(axis=1)
    s = np.sum((r_sum - np.mean(r_sum))**2)
    
    w = (12 * s) / (m**2 * (n**3 - n))
    return w

w_score = kendall_w(df)

print(f"Cronbach's Alpha: {alpha:.4f}")
print(f"Kendall's W: {w_score:.4f}")