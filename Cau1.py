import plotly.graph_objects as go
import numpy as np

def get_fig_cau1():
    # Tạo lưới tọa độ cực (chỉ lấy y >= 0 nên góc theta từ 0 đến pi)
    r = np.linspace(0, 1, 50)
    theta = np.linspace(0, np.pi, 50)
    R, Theta = np.meshgrid(r, theta)

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    # Mặt nón: z = -1 + r
    Z_cone = -1 + R
    
    # Mặt cầu: z = sqrt(1 - r^2)
    Z_sphere = np.sqrt(1 - R**2)

    fig = go.Figure()
    
    # Vẽ mặt nón
    fig.add_trace(go.Surface(x=X, y=Y, z=Z_cone, colorscale='Blues', opacity=0.8, name='Mặt nón'))
    
    # Vẽ mặt cầu
    fig.add_trace(go.Surface(x=X, y=Y, z=Z_sphere, colorscale='Reds', opacity=0.8, name='Mặt cầu'))

    fig.update_layout(
        title="Câu 1: Vật thể giới hạn bởi Mặt nón và Mặt cầu (y ≥ 0)", 
        scene=dict(aspectmode='data', 
                   xaxis_title='Trục X', yaxis_title='Trục Y', zaxis_title='Trục Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig