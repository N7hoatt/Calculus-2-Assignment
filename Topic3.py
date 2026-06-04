import plotly.graph_objects as go
import numpy as np

def get_fig_t3_cau1():
    fig = go.Figure()
    
    theta = np.linspace(-3*np.pi/4, np.pi/4, 50)
    phi_cone = np.arctan(3)
    phi = np.linspace(0, phi_cone, 50)
    Phi, Theta = np.meshgrid(phi, theta)
    
    Rho_sphere = 4 * np.cos(Phi)
    X_s = Rho_sphere * np.sin(Phi) * np.cos(Theta)
    Y_s = Rho_sphere * np.sin(Phi) * np.sin(Theta)
    Z_s = Rho_sphere * np.cos(Phi)
    fig.add_trace(go.Surface(x=X_s, y=Y_s, z=Z_s, colorscale='Reds', opacity=0.9, name='Mặt cầu'))

    rho_c = np.linspace(0, 4*np.cos(phi_cone), 50)
    Rho_c, Theta_c = np.meshgrid(rho_c, theta)
    X_c = Rho_c * np.sin(phi_cone) * np.cos(Theta_c)
    Y_c = Rho_c * np.sin(phi_cone) * np.sin(Theta_c)
    Z_c = Rho_c * np.cos(phi_cone)
    fig.add_trace(go.Surface(x=X_c, y=Y_c, z=Z_c, colorscale='Blues', opacity=0.8, name='Mặt nón'))

    fig.update_layout(
        title="Đề 3 - Câu 1: Vật thể Ω (Cắt bởi x ≥ y)",
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t3_cau2():
    fig = go.Figure()
    
    x = [1, 0, -1, 0, 1]
    y = [0, 1, 0, -1, 0]
    z = [yi / 2 for yi in y]

    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines+markers', 
                               marker=dict(size=5, color='black'),
                               line=dict(color='red', width=8), name='Đường cong C'))
    
    for i in range(4):
        X_cyl = [[x[i], x[i+1]], [x[i], x[i+1]]]
        Y_cyl = [[y[i], y[i+1]], [y[i], y[i+1]]]
        Z_cyl = [[-1, -1], [1, 1]]
        fig.add_trace(go.Surface(x=X_cyl, y=Y_cyl, z=Z_cyl, colorscale='Greys', opacity=0.2, showscale=False))

    fig.update_layout(
        title="Đề 3 - Câu 2: Đường cong C (|x|+|y|=1 và y=2z)", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def get_fig_t3_cau3():
    fig = go.Figure()
    
    y = np.linspace(0, 1, 100)
    x_left = 1 - np.sqrt(1 - y**2) # Cung tròn
    x_right = 2 - y                # Đường thẳng

    x_bound = np.concatenate([x_left, x_right[::-1]])
    y_bound = np.concatenate([y, y[::-1]])

    fig.add_trace(go.Scatter(x=x_bound, y=y_bound, fill='toself', fillcolor='rgba(255, 165, 0, 0.5)', 
                             line=dict(color='orangered', width=3), name='Miền D'))
    
    # Đánh dấu đỉnh
    fig.add_trace(go.Scatter(x=[0, 1, 2], y=[0, 1, 0], mode='markers+text',
                             text=['(0,0)', '(1,1)', '(2,0)'], textposition='top center',
                             marker=dict(size=10, color='black'), name='Các đỉnh'))

    fig.update_layout(
        title="Đề 3 - Câu 3: Miền D", 
        xaxis=dict(scaleanchor="y", scaleratio=1), yaxis=dict(scaleanchor="x", scaleratio=1)
    )
    return fig

def get_fig_t3_cau4():
    fig = go.Figure()
    
    x = np.linspace(-1, 1, 50)
    t = np.linspace(0, 1, 50) 
    X, T = np.meshgrid(x, t)
    
    Y = 1 - X**2
    Z = T * (1 - Y)

    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.9, name='Mặt S'))

    fig.update_layout(
        title="Đề 3 - Câu 4: Mặt trụ S (y=1-x²) bị cắt bởi z=0 và y+z=1", 
        scene=dict(aspectmode='data', xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig