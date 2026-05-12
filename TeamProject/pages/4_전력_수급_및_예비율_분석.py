import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_all, sidebar_filters

st.set_page_config(layout="wide")
power, daily, sector, supply = load_all()
reg_sel, h_rng, d_rng = sidebar_filters(power, daily)

start, end = pd.to_datetime(d_rng[0]), pd.to_datetime(d_rng[1])
f_sup = supply[supply["date"].between(start, end)]

st.title("국가 전력 수급 및 예비율 분석")
st.subheader("⚡ 날짜별 공급예비율 추이")

fig_s = px.line(f_sup, x="date", y="공급예비율(%)", title="일별 공급예비율 추이")
fig_s.add_hline(y=10, line_dash="dash", line_color="red", annotation_text="안전 한계선 (10%)")
st.plotly_chart(fig_s.update_layout(height=550), use_container_width=True)

low_day = f_sup.loc[f_sup["공급예비율(%)"].idxmin()]
st.info(f"최저 예비율 발생일: **{low_day['date'].date()}** (예비율: {low_day['공급예비율(%)']:.2f}%)")

peak_hr = power[power["거래일자"]==low_day["date"]].groupby("시간")["전력거래량(MWh)"].sum().reset_index()
st.plotly_chart(px.area(peak_hr, x="시간", y="전력거래량(MWh)", title=f"{low_day['date'].date()} 전국 전력 사용 패턴", color_discrete_sequence=['#FF4B4B']).update_layout(height=550), use_container_width=True)