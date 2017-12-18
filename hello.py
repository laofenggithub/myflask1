from flask import Flask
app = Flask(__name__)

# @app.route('/<id>/')# http://192.168.99.100:5000/5/
# def hello_world(id):
#     return 'Hello World!'+id
@app.route('/<id>/')#<converter:variable_name>
def hello_world(id):
    return 'Hello World!+{}'.format(id)

@app.route('/')
def hello_world2():
    return 'Hello World!-'

# @app.route('/<any(a,b):/')
def hello_world1():
    return 'Hello World!+'


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

