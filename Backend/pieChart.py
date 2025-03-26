from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/pieChart')
def generate_pie_chart():
    # Defining labels
    activities = ['Eat', 'Sleep', 'Work', 'Play']
    
    # Portion covered by each label
    slices = [3, 7, 8, 6]
    
    # Colors for each label
    colors = ['r', 'y', 'g', 'b']
    
    # Plotting the pie chart
    plt.figure(figsize=(6, 6))  # Adjust figure size
    plt.pie(slices, labels=activities, colors=colors, 
            startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
            radius=1.2, autopct='%1.1f%%')
    
    # Adding legend
    plt.legend()
    
    # Save the image to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    
    # Clear the plot to avoid overlapping on multiple requests
    plt.clf()
    
    return send_file(img, mimetype='image/png')
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
