import plotly.graph_objects as go
import numpy as np

def get_fig_t1_cau1():
    r = np.linspace(0, 1, 50)
    theta = np.linspace(0, np.pi, 50)
    R, Theta = np.meshgrid(r, theta)

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    Z_cone = -1 + R
    Z_sphere = np.sqrt(1 - R**2)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z_cone, colorscale='Blues', opacity=0.8, name='Mặt nón'))
    fig.add_trace(go.Surface(x=X, y=Y, z=Z_sphere, colorscale='Reds', opacity=0.8, name='Mặt cầu'))

    fig.update_layout(
        title="Đề 1 - Câu 1: Giao tuyến Mặt nón và Mặt cầu (y ≥ 0)", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t1_cau2():
    fig = go.Figure()
    
    t = np.linspace(0, 2*np.pi, 100)
    x_c, y_c = np.cos(t), np.sin(t)
    z_c = x_c**2
    fig.add_trace(go.Scatter3d(x=x_c, y=y_c, z=z_c, mode='lines', 
                               line=dict(color='lightblue', width=4), name='Đường cong C'))
    
    t_seg = np.linspace(0, np.pi/2, 50)
    x_seg, y_seg = np.cos(t_seg), np.sin(t_seg)
    z_seg = x_seg**2
    fig.add_trace(go.Scatter3d(x=x_seg, y=y_seg, z=z_seg, mode='lines', 
                               line=dict(color='red', width=8), name='Đoạn AB'))

    fig.add_trace(go.Scatter3d(x=[0, 1], y=[1, 0], z=[0, 1], mode='markers+text', 
                               text=['A(0,1,0)', 'B(1,0,1)'], textposition='top center',
                               marker=dict(size=6, color='black'), name='Đỉnh'))

    fig.update_layout(
        title="Đề 1 - Câu 2: Đường cong C và đoạn nối A với B", 
        scene=dict(aspectmode='cube', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t1_cau3():
    x = [1, 0, -1, 0, 1]
    y = [0, 1, 0, -1, 0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, fill='toself', fillcolor='rgba(173, 216, 230, 0.5)', 
                             line=dict(color='blue', width=2), name='Miền D'))
    fig.add_trace(go.Scatter(x=[1, 0, -1, 0], y=[0, 1, 0, -1], mode='markers+text',
                             text=['A(1,0)', 'B(0,1)', 'C(-1,0)', 'D(0,-1)'], textposition='top center',
                             marker=dict(size=10, color='red'), name='Các đỉnh'))

    fig.update_layout(
        title="Đề 1 - Câu 3: Hình vuông ABCD", 
        xaxis=dict(scaleanchor="y", scaleratio=1), yaxis=dict(scaleanchor="x", scaleratio=1)
    )
    return fig

def get_fig_t1_cau4():
    y = np.linspace(-1, 1, 50)
    z = np.linspace(0, 1, 50)
    Y, Z = np.meshgrid(y, z)
    X = Y**2

    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.9, name='Mặt S'))

    fig.update_layout(
        title="Đề 1 - Câu 4: Mặt trụ parabol S", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig