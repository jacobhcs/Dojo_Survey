from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdfjkl'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/info', methods=['POST'])
def displayinfo():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['language'] = request.form['language']
  session['comment'] = request.form['comment']
  return render_template('display.html', name=session['name'])

@app.route('/reset', methods=['POST'])
def goback():
  session.clear()
  return redirect('/')

if __name__=="__main__":
  app.run(debug=True)