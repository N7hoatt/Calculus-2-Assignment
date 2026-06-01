import plotly.graph_objects as go

def get_fig_cau3():
    # Tọa độ các đỉnh (đỉnh cuối lặp lại để khép kín hình)
    x = [1, 0, -1, 0, 1]
    y = [0, 1, 0, -1, 0]

    fig = go.Figure()
    
    # Vẽ miền D và Biên C
    fig.add_trace(go.Scatter(x=x, y=y, fill='toself', fillcolor='rgba(173, 216, 230, 0.5)', 
                             line=dict(color='blue', width=2), name='Miền D / Biên C'))
    
    # Đánh dấu các đỉnh
    fig.add_trace(go.Scatter(x=[1, 0, -1, 0], y=[0, 1, 0, -1], mode='markers+text',
                             text=['A(1,0)', 'B(0,1)', 'C(-1,0)', 'D(0,-1)'], textposition='top center',
                             marker=dict(size=10, color='red'), name='Các đỉnh'))

    fig.update_layout(
        title="Câu 3: Hình vuông ABCD", 
        xaxis=dict(scaleanchor="y", scaleratio=1, title='Trục X'), # Tỉ lệ 1:1
        yaxis=dict(scaleanchor="x", scaleratio=1, title='Trục Y'),
        showlegend=True
    )
    return fig