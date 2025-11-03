from flask import Flask, render_template, request, jsonify
from converter import convert_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    legacy_code = request.form['legacy_code']
    target_language = request.form['language']
    converted_code = convert_code(legacy_code, target_language)
    return jsonify({'converted_code': converted_code})

if __name__ == '__main__':
    app.run(debug=True)