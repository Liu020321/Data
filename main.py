# 数据导入
import matplotlib as matplotlib
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# 可视化显示在界面
% matplotlib
inline
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

import seaborn as sns

sns.set(color_codes=True)
# 学习seaborn参考：https://www.jianshu.com/p/c26bc5ccf604

import json
import warnings

warnings.filterwarnings('ignore')
from wordcloud import WordCloud, STOPWORDS

movies = pd.read_csv('F:\\tmdb-movie-metadata\\tmdb_5000_movies.csv', encoding='utf_8')
credits = pd.read_csv('F:\\tmdb-movie-metadata\\tmdb_5000_credits.csv', encoding='utf_8')
movies.info()  # 查看信息
credits.info()