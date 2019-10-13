from flask import Flask,jsonify,request
app=Flask(__name__)
lang = [{'name':'js'},{'name':'java'},{'name':'aws'}]
@app.route('/',methods=['GET'])
def temp():
    return jsonify({'lang':lang})
if(__name__=='__main__'):
    app.run(host="0.0.0.0")
