
from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('log.html')

'''@app. route('/whereami')
def whereami():
    return 'HTU, Ghana, Global Code!!!'  '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
