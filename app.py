from flask import Flask, render_template, request, jsonify
from services.openai_checker import check_openai_balance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    key = request.form.get('api_key')
    platform = request.form.get('platform')

    if platform == 'openai':
        success, result = check_openai_balance(key)
    else:
        success, result = False, 'Platform not supported'

    return jsonify({'success': success, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
