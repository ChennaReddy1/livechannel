from flask import Flask
app = Flask(__name__)

@app.route('/sakshi')
def channel1():
    return """
    <h1>sakshi!</h1>

    <iframe src="http://livetvchannelsfree.com/sakshitv.html" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
    """
@app.route('/tv9')
def channel2():
    return """
    <h1>tv9!</h1>

    <iframe src="http://livetvchannelsfree.com/tv9.html" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
    """
@app.route('/abn')
def channel3():
    return """
    <h1>abn!</h1>

    <iframe src="http://livetvchannelsfree.com/abnandrajyothi.html" width="100%" height="100" frameborder="0" allowfullscreen></iframe>
    """
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
