import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from utils import load_all, sidebar_filters

# 0. 설정 및 데이터 로드
st.set_page_config(layout="wide")
power, daily, sector, supply = load_all()
reg_sel, h_rng, d_rng = sidebar_filters(power, daily)

# 데이터 필터링
start, end = pd.to_datetime(d_rng[0]), pd.to_datetime(d_rng[1])
f_dy = daily[(daily["지역"] == reg_sel) & (daily["date"].between(start, end))]
all_dy = daily[daily["date"].between(start, end)]

st.title("기온 및 기상 요소 분석")
st.markdown("---")

# 1. 날짜별 혼합 차트 (전력량 + 기상 요소)
st.subheader("🌡️ 날짜별 전력 사용량과 기상 데이터 비교")
w_opt = st.selectbox("비교 기상 요소 선택", ["temp", "강수량", "습도"], 
                     format_func=lambda x: {"temp":"기온","강수량":"강수량","습도":"습도"}[x])

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Bar(x=f_dy["date"], y=f_dy["power_usage"], name="일별 전력 사용량", opacity=0.6), secondary_y=False)
fig.add_trace(go.Scatter(x=f_dy["date"], y=f_dy["rolling_mean_7"], name="7일 이동평균"), secondary_y=False)
fig.add_trace(go.Scatter(x=f_dy["date"], y=f_dy[w_opt], name=w_opt, mode="lines+markers"), secondary_y=True)
st.plotly_chart(fig.update_layout(height=600, hovermode="x unified"), use_container_width=True)

# 2. 기상 요소별 산점도 (반복문으로 최적화)
st.divider()
st.subheader("📈 기상 요소별 전력 사용량 관계 (추세선 포함)")
cols = st.columns(3)
for i, col_name in enumerate(["temp", "강수량", "습도"]):
    fig_sc = px.scatter(f_dy, x=col_name, y="power_usage", color="월", trendline="ols", 
                        trendline_scope="overall", trendline_color_override="red",
                        title=f"{col_name} vs 전력 사용량")
    cols[i].plotly_chart(fig_sc.update_layout(height=450), use_container_width=True)

# 3. 지역별 기온 민감도 랭킹 (리스트 컴프리헨션 활용)
st.divider()
st.subheader("🌡️ 지역별 기온 민감도 랭킹")
# 상관계수 계산 로직 최적화
corr_data = [{"지역": r, 
              "기온상관계수": (tmp := all_dy[all_dy["지역"]==r])["power_usage"].corr(tmp["temp"]),
              "지역유형": sector.set_index("지역").at[r, "지역유형"] if r in sector["지역"].values else "N/A"
             } for r in all_dy["지역"].unique() if len(all_dy[all_dy["지역"]==r]) > 5]

corr_df = pd.DataFrame(corr_data).sort_values("기온상관계수", key=abs, ascending=False)
st.plotly_chart(px.bar(corr_df, x="기온상관계수", y="지역", color="지역유형", orientation="h", 
                       title="지역별 기온-전력 상관계수 (절대값 기준 정렬)").update_layout(height=800), use_container_width=True)
st.dataframe(corr_df, use_container_width=True)

# 4. 냉난방 부하 분석 (CDD & HDD)
st.divider()
st.subheader("❄️ 냉난방 부하 분석 (CDD & HDD)")
st.caption("CDD(냉방도일): 기온-24℃ / HDD(난방도일): 18℃-기온")
l_col, r_col = st.columns(2)
# CDD/HDD 시각화 루프화 가능하나 가독성을 위해 개별 유지
l_col.plotly_chart(px.scatter(f_dy[f_dy["CDD"]>0], x="CDD", y="power_usage", trendline="ols", 
                               trendline_color_override="red", title="냉방 부하 (CDD) 상관관계").update_layout(height=500), use_container_width=True)
r_col.plotly_chart(px.scatter(f_dy[f_dy["HDD"]>0], x="HDD", y="power_usage", trendline="ols", 
                               trendline_color_override="blue", title="난방 부하 (HDD) 상관관계").update_layout(height=500), use_container_width=True)