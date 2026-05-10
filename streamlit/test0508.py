import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(page_title="Heart Failure 데이터 시각화",layout="wide")

# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
df_a = pd.read_json(r"streamlit\heart_failure_a.json")
df_b = pd.read_json(r"streamlit\heart_failure_b.json")

# person_id 기준으로 병합
df = pd.merge(df_a, df_b, on="person_id", how="inner")

# 병합하면서 사라진 데이터 개수
dropped_num = len(df_a) + len(df_b) - len(df) * 2

# --------------------------------------------------
# 제목
# --------------------------------------------------
st.title("Heart Failure 데이터 시각화-이한이")
st.write("심부전 데이터를 이용하여 사망 여부, 나이, 심박출률, 혈소판, 흡연 여부를 시각화합니다.")

st.divider()

# --------------------------------------------------
# 데이터 요약
# --------------------------------------------------
st.header("데이터 요약")

col1, col2, col3, col4 = st.columns(4)

col1.metric("df_a 데이터 수", len(df_a))
col2.metric("df_b 데이터 수", len(df_b))
col3.metric("병합 후 데이터 수", len(df))
col4.metric("제외된 데이터 수", dropped_num)

st.divider()

# --------------------------------------------------
# 요구사항 1: ejection_fraction과 age 관계
# 박출계수와 나이의 상관관계를 위해 jointplot 그래프를 그리세요.
#           - seaborn의 jontplot을 활용
#           - x축 : ejection_fraction
#           - y축 : age
#           - 색상(hue) : DEATH_EVENT
# --------------------------------------------------
st.header("1. 심박출률과 나이의 관계")

st.write("ejection_fraction과 age의 관계-> DEATH_EVENT 기준으로 표시")

a= sns.jointplot(data=df, x="ejection_fraction", y="age", hue="DEATH_EVENT", height=6)
st.pyplot(a.figure)
st.divider()

# --------------------------------------------------
# 요구사항 2: 흡연 여부 선택
# 죽음과 당뇨, 흡연의 상관관계를 보기 위한 그래프를 그리세요.
#          - seaborn의 violinplot을 이용
#          - X축 : DEATH_EVENT
#          - Y축 : platelets
#          - hue : smoking
#          - split : True
# --------------------------------------------------
st.header("2. 흡연 여부에 따른 혈소판 분포")
 
smoking_status= st.radio(
    "흡연 여부를 선택하세요.",
    ["전체", "흡연", "비흡연"]
)

if smoking_status== "흡연":
    smoking_df = df[df["smoking"] == 1]
    st.write("흡연자 데이터만 표시합니다.")

elif smoking_status== "비흡연":
    smoking_df= df[df["smoking"] == 0]
    st.write("비흡연자 데이터만 표시합니다.")

else:
    smoking_df= df
    st.write("전체 데이터를 표시합니다.")

fig, ax= plt.subplots(figsize=(10, 5))

sns.violinplot(data=smoking_df, x="DEATH_EVENT", y="platelets", hue="smoking", ax=ax, split=True)

ax.set_title("DEATH_EVENT와 platelets 관계")
ax.set_xlabel("DEATH_EVENT")
ax.set_ylabel("platelets")

st.pyplot(fig)
st.divider()

# --------------------------------------------------
# 그래프 3: ejection_fraction 범위 선택
# time칼럼을 알아보기 위해 해당 칼럼의 histogram을 작성합니다. 
# seaborn의 histplot 함수를 이용하세요.
#       - x축 : time
#       - bins : 20
#       - 색상(hue) : DEATH_EVENT
# --------------------------------------------------
st.header("3. ejection_fraction 범위별 time 분포")

ran = st.slider(
    "ejection_fraction 범위를 선택하세요.",
    0.0,
    80.0,
    (0.0, 80.0)
)

df_filtered = df[(df["ejection_fraction"] >= ran[0]) &(df["ejection_fraction"] <= ran[1])]

st.write("선택한 ejection_fraction 범위:", ran[0], "~", ran[1])

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(data=df_filtered, x="time",bins=20, hue="DEATH_EVENT", kde=True, ax=ax)

ax.set_title("ejection_fraction 범위별 time 분포")
ax.set_xlabel("time")
ax.set_ylabel("count")

st.pyplot(fig)
st.divider()
