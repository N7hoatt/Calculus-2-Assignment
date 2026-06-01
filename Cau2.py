import plotly.graph_objects as go
import numpy as np

def get_fig_cau2():
    fig = go.Figure()
    
    # Tham số hóa đường cong C: x^2 + y^2 = 1 và z = x^2
    t = np.linspace(0, 2*np.pi, 100)
    x_c = np.cos(t)
    y_c = np.sin(t)
    z_c = x_c**2
    
    # Vẽ toàn bộ đường cong C (nét mỏng)
    fig.add_trace(go.Scatter3d(x=x_c, y=y_c, z=z_c, mode='lines', 
                               line=dict(color='lightblue', width=4), name='Đường cong C'))
    
    # Đoạn AB tương ứng t chạy từ pi/2 (điểm A) về 0 (điểm B)
    t_seg = np.linspace(0, np.pi/2, 50)
    x_seg = np.cos(t_seg)
    y_seg = np.sin(t_seg)
    z_seg = x_seg**2
    
    # Tô đậm đoạn AB (nét dày)
    fig.add_trace(go.Scatter3d(x=x_seg, y=y_seg, z=z_seg, mode='lines', 
                               line=dict(color='red', width=8), name='Đoạn AB (Tô đậm)'))

    # Đánh dấu các đỉnh A và B
    fig.add_trace(go.Scatter3d(x=[0, 1], y=[1, 0], z=[0, 1], mode='markers+text', 
                               text=['A(0,1,0)', 'B(1,0,1)'], textposition='top center',
                               marker=dict(size=6, color='black'), name='Đỉnh'))

    fig.update_layout(
        title="Câu 2: Đường cong C và đoạn nối A với B", 
        scene=dict(aspectmode='cube',
                   xaxis_title='Trục X', yaxis_title='Trục Y', zaxis_title='Trục Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig