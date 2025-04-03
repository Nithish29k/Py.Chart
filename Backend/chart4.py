from flask import Flask, render_template_string
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/chart4')
def generate_chart():
    # Sample Data
    x = [1, 2, 3, 4, 5, 6]
    y = [2, 4, 1, 5, 2, 6]

    # Create interactive chart using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        line=dict(color='green', dash='dash', width=3),
        marker=dict(color='blue', size=12),
        name='Custom Line',
        hovertemplate='<b>X:</b> %{x}<br><b>Y:</b> %{y}<extra></extra>'
    ))

    # Customize layout
    fig.update_layout(
        title='Interactive Chart with Hover',
        xaxis_title='x - axis',
        yaxis_title='y - axis',
        xaxis=dict(range=[1, 8]),
        yaxis=dict(range=[1, 8]),
        hovermode='x unified',  # Enable hover on x-axis
    )

    # Convert chart to HTML (removing download & plot link options)
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn', config={"displayModeBar": False})

    # Return HTML with embedded chart
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Interactive Chart</title>
      </head>
      <body>
        <h1>Interactive Chart with Hover</h1>
        {{ chart_html|safe }}
      </body>
    </html>
    """, chart_html=chart_html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
