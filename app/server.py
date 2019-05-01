from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/debug')
def debug():
	import rpdb; rpdb.set_trace("0.0.0.0")
	return 'debug'

if __name__ == '__main__':
	app.run()
