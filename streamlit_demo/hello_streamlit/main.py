import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門やで')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)



left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')

# condition = st.slider('あなたの今の調子は?', 0, 100, 50)
# 'あなたの趣味は、', text, 'です'
# 'あなたの調子は、', condition, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('/mnt/e/dir/act/real/じゅじゅ/img/twitter/D7ngGlgUEAAbOR7.jpg')
#     st.image(img, caption='かわいい', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)
