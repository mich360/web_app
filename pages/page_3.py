import streamlit as st
import pandas as pd   
#import matplotlib.pyplot as plt  
#データデータ分析関連
df = pd.read_csv('./data/平均気温.csv', index_col='月')
st.line_chart(df)
st.bar_chart(df['2021年'])
# st.dataframe(df)
# st.table(df)
# Matplotlibは、Pythonのデータ可視化ライブラリの1つ
# fig, ax = plt.subplots()
# ax.plot(df.index, df['2021年'])
# ax.set_title('matplotlib graph')
# st.pyplot(fig)
