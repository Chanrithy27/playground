from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def start_playground():
    return render_template("index.html", x=3, color= "#9fc5f8")

@app.route('/play/<int:x>')
def display_boxes(x):
    return render_template("index.html", x = x, color= "#9fc5f8")

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=8000)