from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True)