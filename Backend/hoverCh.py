from flask import Flask, render_template_string
import plotly.graph_objects as go
import plotly.colors as pc

app = Flask(__name__)

@app.route('/piechart2')
def generate_pie_chart():
    # Crop Names
    crops = ['rice', 'coconut', 'jute', 'coffee', 'pigeonpeas', 'papaya', 'apple', 'orange',
             'pomegranate', 'kidneybeans', 'banana', 'mango', 'maize', 'cotton', 'chickpea',
             'grapes', 'blackgram', 'mothbeans', 'watermelon', 'mungbean', 'lentil', 'muskmelon']

    # Corresponding Average Rainfall Percentages
    rainfall = [10.4, 7.7, 7.7, 6.9, 6.6, 6.3, 4.9, 4.9, 4.7, 4.7, 4.6, 4.2, 3.7, 3.5, 3.5, 
                3.1, 3.0, 2.9, 2.3, 2.2, 2.1, 1.1]

    # Use Plotly's predefined color scale
    colors = pc.qualitative.Set3

    # Create interactive Pie Chart using Plotly
    fig = go.Figure(data=[
        go.Pie(
            labels=crops,
            values=rainfall,
            hoverinfo='label+percent',
            textinfo='label',
            marker=dict(colors=colors),
          
        )
    ])

    fig.update_layout(
        title_text='Crops Distribution by Average Rainfall',
        hovermode='x unified',
        showlegend=False
    )

    chart_html = fig.to_html(full_html=False)

    return render_template_string("""
    <html>
      <head>
        <title>Interactive Pie Chart</title>
      </head>
      <body>
        <h1>Hover to Highlight Crop</h1>
        {{ chart_html|safe }}
      </body>
    </html>
    """, chart_html=chart_html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)