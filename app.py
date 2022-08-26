app = Flask(__name__)
@app.route('/demo1')
def index():
    return jsonify({'name': 'akbar',
                    'email': 'akbar@outlook.com'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
app.run()
