import pandas as pd
import numpy as np
from pathlib import Path


data_path = Path('../data_analysis/datasets/bike_rentals/bike_rentals.csv')
df = pd.read_csv(data_path)
df.iloc[2, 3] = np.nan # 결측치를 임의로 만들기 위해 추가
df.head(10)

# iloc을 이용한 행 선택 (인덱스로 선택)
df.iloc[2:5, 3:6]

# loc을 이용한 행 선택 (이름으로 선택)
df.loc[2:4, 'workingday':'temp']
df.loc[2:4, ['workingday','temp','casual']]

# season 열의 값이 2인 행들만 선택
df.loc[df['season'] == 2]

# season이 2인 행들 중에 casual, resistered, count 열만 선택
df.loc[df['season'] == 2, 'casual':]

#season이 1이 아니면서 동시에 weather가 2가 아닌 모든 행 선택
df.loc[(df['season'] != 1) & (df['weather'] != 2)]

#season이 1이 아니면서 동시에 weather가 2가 아닌 모든 행 선택, ~ 사용
df.loc[~(df['season'] == 1) & ~(df['weather'] == 2)]