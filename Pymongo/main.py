from flask import Flask,jsonify,request,render_template,make_response
from pymongo import MongoClient

app = Flask(__name__)

URI='mongodb+srv://admin:1234567890@database1.ucnto.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(URI)

db = client.jsn
data = db.student

@app.route('/', methods = ["GET"])
def get_data():
    res = data.find_one({"name":'joy'})
    return "CMD"

@app.route('/', methods = ['POST'])
def post_data():
    store = request.get_json()
    idd = data.insert_one(store).inserted_id
    return 'ADD OR NOT !'+str(idd)

@app.route('/', methods = ["PUT"])
def put_data():
    res = data.update({'name' : 'abc'},{'$set':{'name':'john'}})
    return 'name changed'

@app.route('/', methods = ['DELETE'])
def delete_data():
    res = data.delete_one({'name':'abc'})
    print(res)

@app.route('/all',methods=['GET'])
def gettt():
    res=data.find()
    ans=[]
    for i in res:  
        dic = {}
        dic['name']= i['name']
        ans.append(dic)   
    print(ans)
    return jsonify({'store':ans})       

if __name__ == '__main__':
    app.run(debug=True)    
