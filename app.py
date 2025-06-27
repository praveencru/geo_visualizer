from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Form for file upload

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    try:
        df = pd.read_csv(file, encoding='utf-8')  # Try UTF-8
    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding='latin1')  # Fallback if utf-8 fails

    print(df.head())  # You can test if the file was loaded properly
    return df.head().to_html()  # Show the data in the browser

if __name__ == '__main__':
    app.run(debug=True)


