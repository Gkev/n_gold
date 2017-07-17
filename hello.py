from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "my_key"


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/process_money', methods=['POST'])
def survey():
	print request.form['name']
	session['name'] = request.form
	return redirect('/success')



@app.route('/success')
def success():
	return render_template('success.html')	
	

app.run(debug=True)	