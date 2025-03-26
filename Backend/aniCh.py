from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

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

    # Create Pie Chart
    fig, ax = plt.subplots(figsize=(10, 10))
    wedges, texts, autotexts = ax.pie(rainfall, labels=crops, autopct='%1.1f%%',
                                      startangle=140, colors=plt.cm.Blues(range(50, 250, 10)))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title('Crops Distribution by Average Rainfall')

    # Save chart to memory
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches="tight")
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
