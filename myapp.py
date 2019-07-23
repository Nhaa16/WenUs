
from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route('/')
def index():
<<<<<<< HEAD
    return render_templates('home.html')

@app. route('/whereami')
def whereami():
    return 'HTU, Ghana, Global Code!!!'  
=======
    return render_template('log.html')

'''@app. route('/whereami')
def whereami():
    return 'HTU, Ghana, Global Code!!!'  '''
>>>>>>> 3f1c9398b3c99257b0fd268ddca2d2bdfe736a24

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
