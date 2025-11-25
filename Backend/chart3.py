from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/chart3')
def generate_chart():
    # Line 1 points
    x1 = [1, 2, 3]
    y1 = [2, 4, 1]
    plt.plot(x1, y1, label="Line 1")

    # Line 2 points
    x2 = [1, 2, 3]
    y2 = [4, 1, 3]
    plt.plot(x2, y2, label="Line 2")

    # Naming axes and title
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Two Lines on Same Graph')

    # Add legend
    plt.legend()

    # Save the image 
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    
    plt.clf()

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
