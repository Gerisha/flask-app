from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'contact':u'8765432451',
        'name':u'Jennie',
        'done':False
    },

    {
        'id':2,
        'contact' : u'6543352677',
        'name' : u'lisa',
        'done':False
    }
]
   



@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data",methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data'
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })



@app.route("/get-data")
def get_data():
    return jsonify({
        'data':tasks
    })


if (__name__ == "__main__"):
    app.run(debug=True)

    






