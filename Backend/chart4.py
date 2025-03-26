from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/chart4')
def generate_chart():
    # Sample Data
    x = [1, 2, 3, 4, 5, 6]
    y = [2, 4, 1, 5, 2, 6]

    # Create a figure
    plt.figure(figsize=(6,4))
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    
    plt.ylim(1, 8)
    plt.xlim(1, 8)
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Some cool customizations!')

    # Save the image to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


    
