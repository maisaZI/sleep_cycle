
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="حاسبة دورة النوم", page_icon="😴")
st.title("حاسبة وقت الاستيقاظ حسب دورة النوم")

st.markdown("""
احسب وقت الاستيقاظ المثالي بناءً على عدد دورات النوم (كل دورة 93 دقيقة).
""")

sleep_time_input = st.time_input("متى تنام؟", value=datetime.now().time())
cycles = st.slider("اختر عدد دورات النوم:", min_value=1, max_value=6, value=5)

today = datetime.today()
sleep_time = datetime.combine(today, sleep_time_input)
wake_time = sleep_time + timedelta(minutes=93 * cycles)
wake_time_str = wake_time.strftime("%I:%M %p")

st.subheader("النتيجة:")
st.write(f"إذا نمت الساعة {sleep_time.strftime('%I:%M %p')} واخترت {cycles} دورة،")
st.write(f"أنسب وقت تقوم فيه هو: **{wake_time_str}**")

st.markdown("---")
st.markdown("### تم إنشاء هذا التطبيق بواسطة: **اسمك هنا**")
