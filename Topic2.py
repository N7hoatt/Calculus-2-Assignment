import plotly.graph_objects as go
import numpy as np

def get_fig_t2_cau1():
    fig = go.Figure()

    x = np.linspace(-2, 2, 50)
    t = np.linspace(0, 1, 50)
    X, T = np.meshgrid(x, t)

    Z1 = 4 - X**2
    Y1 = T * (X**2 / 2) 
    fig.add_trace(go.Surface(x=X, y=Y1, z=Z1, colorscale='Blues', opacity=0.8, name='Mặt trụ parabol'))

    Z2 = T * (4 - X**2)
    Y2 = 2 - Z2 / 2
    fig.add_trace(go.Surface(x=X, y=Y2, z=Z2, colorscale='Reds', opacity=0.8, name='Mặt phẳng 2y+z=4'))

    fig.update_layout(
        title="Đề 2 - Câu 1: Vật thể Ω",
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t2_cau2():
    fig = go.Figure()
    
    t = np.linspace(0, 2*np.pi, 100)
    X, Y = np.cos(t), np.sin(t)
    Z = 1 - X
    
    fig.add_trace(go.Scatter3d(x=X, y=Y, z=Z, mode='lines', 
                               line=dict(color='red', width=8), name='Đường cong C'))
    
    z_cyl = np.linspace(0, 2, 20)
    T, Z_cyl = np.meshgrid(t, z_cyl)
    X_cyl, Y_cyl = np.cos(T), np.sin(T)
    fig.add_trace(go.Surface(x=X_cyl, y=Y_cyl, z=Z_cyl, colorscale='Greys', opacity=0.3, showscale=False))

    fig.update_layout(
        title="Đề 2 - Câu 2: Đường cong C", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t2_cau3():
    x = [1, 0, -1, 0, 1]
    y = [0, 1, 0, -1, 0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, fill='toself', fillcolor='rgba(255, 165, 0, 0.5)', 
                             line=dict(color='orangered', width=3), name='Miền D'))
    fig.add_trace(go.Scatter(x=[1, 0, -1, 0], y=[0, 1, 0, -1], mode='markers+text',
                             text=['(1,0)', '(0,1)', '(-1,0)', '(0,-1)'], textposition='top center',
                             marker=dict(size=10, color='black'), name='Các đỉnh'))

    fig.update_layout(
        title="Đề 2 - Câu 3: Miền D", 
        xaxis=dict(scaleanchor="y", scaleratio=1), yaxis=dict(scaleanchor="x", scaleratio=1)
    )
    return fig

def get_fig_t2_cau4():
    r = np.linspace(0, np.sqrt(3), 50)
    theta = np.linspace(0, 2*np.pi, 50)
    R, Theta = np.meshgrid(r, theta)
    
    Y = R * np.cos(Theta)
    Z = R * np.sin(Theta)
    X = np.sqrt(3) * R

    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.9, name='Mặt nón S'))

    fig.update_layout(
        title="Đề 2 - Câu 4: Mặt nón S", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig