from flask import Flask, render_template, jsonify, json, request
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name='PyCOMO'):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404 


##########################
# Our API
##########################
users = list()

@app.route('/api/users', methods=['GET','POST'])
def handle_users():
    if request.method == 'GET':
        return jsonify(users)
    else:
        print(dir(request.json))
        users.append(request.json)
        return jsonify(message="User %s added!" % request.json.name)
        

if __name__ == '__main__':
    app.run(debug=True)
