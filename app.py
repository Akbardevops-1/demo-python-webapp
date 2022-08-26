app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'akbar',
                    'email': 'akbar@outlook.com'})
@app.rout('/health')
def index():
    return jsonify(
          status="UP")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
app.run()
