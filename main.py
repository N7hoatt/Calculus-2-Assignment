import streamlit as st

from topic1 import get_fig_t1_cau1, get_fig_t1_cau2, get_fig_t1_cau3, get_fig_t1_cau4
from topic2 import get_fig_t2_cau1, get_fig_t2_cau2, get_fig_t2_cau3, get_fig_t2_cau4
from topic3 import get_fig_t3_cau1, get_fig_t3_cau2, get_fig_t3_cau3, get_fig_t3_cau4

st.set_page_config(page_title="Đồ án Giải tích", layout="wide")

# --- MENU BÊN TRÁI ---
st.sidebar.title("📚 Menu Tùy Chọn")

topic_selection = st.sidebar.selectbox("1. Chọn Đề Tài:", ["Đề Tài 1", "Đề Tài 2", "Đề Tài 3"])
question_selection = st.sidebar.radio("2. Chọn Câu Hỏi:", ["Câu 1", "Câu 2", "Câu 3", "Câu 4"])

# --- GIAO DIỆN CHÍNH ---
st.title(f"Project Đồ họa Toán học - {topic_selection}")
st.markdown("---")

# KIỂM TRA ĐỀ TÀI VÀ CÂU HỎI ĐỂ RENDER ĐÚNG ĐỒ THỊ
if topic_selection == "Đề Tài 1":
    if question_selection == "Câu 1":
        st.plotly_chart(get_fig_t1_cau1(), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(get_fig_t1_cau2(), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(get_fig_t1_cau3(), use_container_width=True)
    elif question_selection == "Câu 4":
        st.plotly_chart(get_fig_t1_cau4(), use_container_width=True)

elif topic_selection == "Đề Tài 2":
    if question_selection == "Câu 1":
        st.plotly_chart(get_fig_t2_cau1(), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(get_fig_t2_cau2(), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(get_fig_t2_cau3(), use_container_width=True)
    elif question_selection == "Câu 4":
        st.plotly_chart(get_fig_t2_cau4(), use_container_width=True)

elif topic_selection == "Đề Tài 3":
    if question_selection == "Câu 1":
        st.markdown("Vật thể giới hạn bởi mặt cầu $x^2+y^2+z^2 \le 4z$ và nón $3z \ge \sqrt{x^2+y^2}$, cắt bởi $x \ge y$.")
        st.plotly_chart(get_fig_t3_cau1(), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(get_fig_t3_cau2(), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(get_fig_t3_cau3(), use_container_width=True)
    elif question_selection == "Câu 4":
        st.markdown("Mặt trụ cong $y = 1 - x^2$ bị vát chéo bởi mặt phẳng $y+z=1$.")
        st.plotly_chart(get_fig_t3_cau4(), use_container_width=True)