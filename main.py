from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)                     
app.secret_key = 'ThisIsSecret'


@app.route('/')                                                                    
def index():
    # Initialise the counter, or increment it
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/add2', methods=['post'])                                                                    
def add2():
    session['counter'] = session['counter'] + 2
    return render_template('index.html')

@app.route('/reset_count', methods=['post'])                                                                    
def reset():
    session['counter'] = 0
    return redirect('/')
           
app.run(debug=True)