import flask

from controller.controller import TestingtonController

app = flask.Flask(__name__)
app.debug = True
controller = TestingtonController()


@app.route("/api/test", methods=['GET', 'POST'])
def test():
    if flask.request.method == 'GET':
        print(controller.get_rows())
        return flask.jsonify(controller.get_rows())
    elif flask.request.method == 'POST':
        request_json = flask.request.data
        request_json = flask.json.loads(request_json)
        print(request_json)
        if 'email' not in request_json:
            return 'Email was not provided!'
        message = request_json['message'] if 'message' in request_json else ''
        return controller.insert_row(message=message, email=request_json['email'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
