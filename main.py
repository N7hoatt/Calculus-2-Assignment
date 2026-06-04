import streamlit as st

# Import các hàm vẽ đồ thị từ các file con
from Topic1 import get_fig_cau1
from Topic1 import get_fig_cau2
from Topic1 import get_fig_cau3
from Topic1 import get_fig_cau4

# Cấu hình trang web
st.set_page_config(page_title="Đồ án Giải tích - Vẽ Hình", layout="wide")

# Tạo Sidebar menu bên trái
st.sidebar.title("📚 Menu Chọn Bài")
st.sidebar.markdown("Vui lòng chọn bài cần hiển thị:")
selection = st.sidebar.radio("Danh sách:", 
                             ["Câu 1: Giao tuyến Nón & Cầu", 
                              "Câu 2: Giao tuyến Paraboloid & Trụ", 
                              "Câu 3: Hình vuông ABCD", 
                              "Câu 4: Mặt trụ parabol"])

# Tiêu đề chính
st.title("Project Đồ họa Toán học (Giải tích 2)")
st.markdown("Sử dụng **Streamlit** và **Plotly** để mô phỏng tương tác 3D/2D.")
st.markdown("---")

# Render đồ thị tương ứng dựa vào menu
if "Câu 1" in selection:
    st.subheader("📌 Câu 1: Vật thể giới hạn bởi mặt cầu và mặt nón")
    st.markdown("Kéo chuột để xoay hình học 3D. Vật thể được cắt bởi mặt phẳng $y \\ge 0$.")
    fig1 = get_fig_cau1()
    st.plotly_chart(fig1, use_container_width=True)

elif "Câu 2" in selection:
    st.subheader("📌 Câu 2: Đường cong C nối từ A(0,1,0) đến B(1,0,1)")
    st.markdown("Giao tuyến của mặt paraboloid $z = 2 - x^2 - 2y^2$ và mặt trụ $z = x^2$.")
    fig2 = get_fig_cau2()
    st.plotly_chart(fig2, use_container_width=True)

elif "Câu 3" in selection:
    st.subheader("📌 Câu 3: Tính tích phân đường trên biên hình vuông")
    st.markdown("Biên $C$ của hình vuông có các đỉnh $A(1,0); B(0,1); C(-1,0); D(0,-1)$.")
    fig3 = get_fig_cau3()
    st.plotly_chart(fig3, use_container_width=True)

elif "Câu 4" in selection:
    st.subheader("📌 Câu 4: Mặt cong S")
    st.markdown("Mặt trụ $x = y^2$ bị chắn bởi các mặt $x = 1, z = 1, z = 0$.")
    fig4 = get_fig_cau4()
    st.plotly_chart(fig4, use_container_width=True)