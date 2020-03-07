import json
from flask import Flask, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)



@app.route('/msg_api', methods=['GET','POST'])
def items():
    if request.method == "POST":
        postdata = request.form['replys']
        data = json.loads(postdata)
        print(data)
        if data.get("content"):
            return '请求数据成功'
        return '请求数据失败'

    if request.method == "GET":
        return 'hello 123'


if __name__ == '__main__':
    app.config["JSON_AS_ASCII"] = False
    #app.run(debug=True,host= '0.0.0.0',port=5000)
    WSGIServer(('0.0.0.0', 5001), app).serve_forever()
