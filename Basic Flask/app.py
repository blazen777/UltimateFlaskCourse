from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)
# tut 1.12 - Configuration
app.config['DEBUG']=True
# tut 1.13 - Sessions
app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route('/users/',methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/users/<string:name>',methods=['POST','GET'])
def name(name):
    return f"<h1>Hello from Flask, {name}!!</h1>"

# tut 1.13
@app.route('/home/',methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>',methods=['POST','GET'])
def home(name):
    session['name'] = name
    return f"<h1>Hello from Flask, {name}!!</h1>"

@app.route('/')
def index():
    # 1.13
    session.pop('name',None)
    ###
    return '<h2> You are at the homepage</h2>'

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1,2,3,4,5]})

# tut 1.13
@app.route('/jsonname')
def json_name():
    if 'name' in session:
        name = session['name']
    else:
        name = 'Default'
    return jsonify({'key': 'value', 'key2': [1,2,3,4,5], 'name':name})

@app.route('/query')
def query():
    # Pass arg to url: 127.0.0.1:5000/query?name=Sergey&location=Rovenki
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h2>Hello {name} from {location} <h2>'

# tut 1.8
# @app.route('/theform')
# def theform():
#     return """
#             <form method='POST' action='/theform'>
#                 <input type='text' name='name'>
#                 <input type='text' name='location'>
#                 <input type='submit' value='submit'>
#             </form>"""

# @app.route('/theform', methods=['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return f'<h2>Hello {name} from {location} '


# tut 1.9
@app.route('/processjson', methods=['POST'])
def process_json():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlists']

    return jsonify({'result': 'Success', 'name': name, 'location': location, 'list': randomlist})

# tut 1.10
'''
@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return """
                <form method='POST' action='/theform'>
                    <input type='text' name='name'>
                    <input type='text' name='location'>
                    <input type='submit' value='submit'>
                </form>"""
    else:
        name = request.form['name']
        location = request.form['location']
        return f'<h2>Hello {name} from {location} '
'''

# tut1.11

@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return """
                <form method='POST' action='/theform'>
                    <input type='text' name='name'>
                    <input type='text' name='location'>
                    <input type='submit' value='submit'>
                </form>"""
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('name', name=name,location=location))


if __name__ == "__main__":
    app.run()