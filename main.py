import streamlit as st
import plotly.graph_objects as go

from Topic1 import get_fig_t1_cau1, get_fig_t1_cau2, get_fig_t1_cau3, get_fig_t1_cau4
from Topic2 import get_fig_t2_cau1, get_fig_t2_cau2, get_fig_t2_cau3, get_fig_t2_cau4
from Topic3 import get_fig_t3_cau1, get_fig_t3_cau2, get_fig_t3_cau3, get_fig_t3_cau4

st.set_page_config(page_title="Bài tập lớn Giải tích 2", layout="wide")

# --- Hàm chung tô đậm trục Ox, Oy, Oz ---
def bold_axes(fig):
    is_3d = any(trace.type in ['surface', 'scatter3d'] for trace in fig.data)
    
    if is_3d:
        fig.update_scenes(
            xaxis=dict(zeroline=False),
            yaxis=dict(zeroline=False),
            zaxis=dict(zeroline=False)
        )
        
        L = 4 
        
        fig.add_trace(go.Scatter3d(x=[-L, L], y=[0, 0], z=[0, 0],
                                   mode='lines', line=dict(color='red', width=5),
                                   name='Trục Ox', showlegend=False, hoverinfo='skip'))
        fig.add_trace(go.Scatter3d(x=[0, 0], y=[-L, L], z=[0, 0],
                                   mode='lines', line=dict(color='green', width=5),
                                   name='Trục Oy', showlegend=False, hoverinfo='skip'))
        fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-L, L],
                                   mode='lines', line=dict(color='blue', width=5),
                                   name='Trục Oz', showlegend=False, hoverinfo='skip'))
        
        fig.add_trace(go.Cone(x=[L], y=[0], z=[0], u=[1], v=[0], w=[0], sizemode="absolute", sizeref=0.4, anchor="tip", showscale=False, colorscale=[[0, 'red'], [1, 'red']], hoverinfo='skip'))

        fig.add_trace(go.Cone(x=[0], y=[L], z=[0], u=[0], v=[1], w=[0], sizemode="absolute", sizeref=0.4, anchor="tip", showscale=False, colorscale=[[0, 'green'], [1, 'green']], hoverinfo='skip'))

        fig.add_trace(go.Cone(x=[0], y=[0], z=[L], u=[0], v=[0], w=[1], sizemode="absolute", sizeref=0.4, anchor="tip", showscale=False, colorscale=[[0, 'blue'], [1, 'blue']], hoverinfo='skip'))

        fig.add_trace(go.Scatter3d(x=[L+0.3, 0, 0], y=[0, L+0.3, 0], z=[0, 0, L+0.3], mode='text', text=['X', 'Y', 'Z'], textfont=dict(size=16), showlegend=False, hoverinfo='skip'))
    else:
        fig.update_xaxes(zeroline=True, zerolinewidth=3, zerolinecolor='red')
        fig.update_yaxes(zeroline=True, zerolinewidth=3, zerolinecolor='green')
        
    return fig

# --- MENU BÊN TRÁI ---
st.sidebar.title("📚 Menu Tùy Chọn")

topic_selection = st.sidebar.selectbox("1. Chọn Đề Tài:", ["Đề Tài 1", "Đề Tài 2", "Đề Tài 3"])
question_selection = st.sidebar.radio("2. Chọn Câu Hỏi:", ["Câu 1", "Câu 2", "Câu 3", "Câu 4"])

# --- GIAO DIỆN CHÍNH ---
st.title(f"Project Minh họa Tích phân trong Không gian - {topic_selection}")
st.markdown("---")

# KIỂM TRA ĐỀ TÀI VÀ CÂU HỎI ĐỂ RENDER ĐÚNG ĐỒ THỊ
if topic_selection == "Đề Tài 1":
    if question_selection == "Câu 1":
        st.plotly_chart(bold_axes(get_fig_t1_cau1()), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(bold_axes(get_fig_t1_cau2()), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(bold_axes(get_fig_t1_cau3()), use_container_width=True)
    elif question_selection == "Câu 4":
        st.plotly_chart(bold_axes(get_fig_t1_cau4()), use_container_width=True)

elif topic_selection == "Đề Tài 2":
    if question_selection == "Câu 1":
        st.plotly_chart(bold_axes(get_fig_t2_cau1()), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(bold_axes(get_fig_t2_cau2()), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(bold_axes(get_fig_t2_cau3()), use_container_width=True)
    elif question_selection == "Câu 4":
        st.plotly_chart(bold_axes(get_fig_t2_cau4()), use_container_width=True)

elif topic_selection == "Đề Tài 3":
    if question_selection == "Câu 1":
        st.markdown("Vật thể giới hạn bởi mặt cầu $x^2+y^2+z^2 \le 4z$ và nón $3z \ge \sqrt{x^2+y^2}$, cắt bởi $x \ge y$.")
        st.plotly_chart(bold_axes(get_fig_t3_cau1()), use_container_width=True)
    elif question_selection == "Câu 2":
        st.plotly_chart(bold_axes(get_fig_t3_cau2()), use_container_width=True)
    elif question_selection == "Câu 3":
        st.plotly_chart(bold_axes(get_fig_t3_cau3()), use_container_width=True)
    elif question_selection == "Câu 4":
        st.markdown("Mặt trụ cong $y = 1 - x^2$ bị vát chéo bởi mặt phẳng $y+z=1$.")
        st.plotly_chart(bold_axes(get_fig_t3_cau4()), use_container_width=True)