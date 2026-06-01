import plotly.graph_objects as go
import numpy as np

def get_fig_cau4():
    # Lưới điểm y và z theo giới hạn đề bài
    y = np.linspace(-1, 1, 50)
    z = np.linspace(0, 1, 50)
    Y, Z = np.meshgrid(y, z)
    
    # Mặt parabol trụ x = y^2
    X = Y**2

    fig = go.Figure()
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.9, name='Mặt cong S'))

    fig.update_layout(
        title="Câu 4: Mặt trụ parabol S (x = y^2)", 
        scene=dict(aspectmode='data',
                   xaxis_title='Trục X', yaxis_title='Trục Y', zaxis_title='Trục Z'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig