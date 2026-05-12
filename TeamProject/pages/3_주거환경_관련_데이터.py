import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_all, sidebar_filters

st.set_page_config(layout="wide")
power, daily, sector, supply = load_all()
reg_sel, h_rng, d_rng = sidebar_filters(power, daily)

start, end = pd.to_datetime(d_rng[0]), pd.to_datetime(d_rng[1])
all_hr = power[(power["시간"].between(*h_rng)) & (power["거래일자"].between(start, end))]
all_dy = daily[daily["date"].between(start, end)]

reg_tot = all_hr.groupby("지역")["전력거래량(MWh)"].sum().reset_index().sort_values("전력거래량(MWh)", ascending=False)
reg_tot = reg_tot.merge(sector[["지역", "지역유형"]], on="지역", how="left")

st.title("주거 환경 및 도시 유형 분석")
st.subheader("🏭 전체 지역별 총 전력거래량 비교")
st.plotly_chart(px.bar(reg_tot, x="지역", y="전력거래량(MWh)", color="지역유형", title="지역별 총 전력거래량").update_layout(height=650), use_container_width=True)

st.divider()
st.subheader("🏠 도시 유형별 비교 분석")
city_comp = all_dy.merge(sector[["지역", "지역유형"]], on="지역")
c1, c2 = st.columns(2)
c1.plotly_chart(px.bar(city_comp.groupby("지역유형")["power_usage"].mean().reset_index(), x="지역유형", y="power_usage", title="유형별 일평균 전력량").update_layout(height=500), use_container_width=True)
c2.plotly_chart(px.scatter(city_comp, x="temp", y="power_usage", color="지역유형", trendline="ols", title="유형별 기온-전력 상관관계").update_layout(height=500), use_container_width=True)