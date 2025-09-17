import numpy as np
import plotly.graph_objects as go

def f(x):
    # return x**3 + 200
    return np.exp(2*x) - 3

x = np.linspace(-10, 10, 200)
y = f(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x) = e^(2x) - 3'))

fig.update_layout(
    # title="Grafik f(x) = x^3 + 200",
    xaxis_title="x",
    yaxis_title="f(x)",
    hovermode="x unified"
)

fig.show()
