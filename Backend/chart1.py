from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# First Chart 
@app.route('/chart1')
def generate_chart1():
    x = [1, 2, 3, 4, 5, 6]
    y = [2, 4, 1, 5, 2, 6]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    plt.ylim(1, 8)
    plt.xlim(1, 8)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Chart 1: Custom Line Plot')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.clf()  # Clear plot to avoid overlapping
    return send_file(img, mimetype='image/png')

# Second Chart 
@app.route('/chart2')
def generate_chart2():
    x1, y1 = [1, 2, 3], [2, 4, 1]
    x2, y2 = [1, 2, 3], [4, 1, 3]

    plt.figure(figsize=(6, 4))
    plt.plot(x1, y1, label="Line 1", color='red')
    plt.plot(x2, y2, label="Line 2", color='blue')

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Chart 2: Two Lines on Same Graph')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.clf()  # Clear plot
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
