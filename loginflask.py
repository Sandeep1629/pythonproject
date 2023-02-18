from flask import *
import pymongo

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')
@app.route('/l',methods=['POST'])
def hl():
    ename = request.form.get("username")
    epass = request.form.get("password")

    client = pymongo.MongoClient(
        'mongodb+srv://2100032245:2100032245@cluster0.iejagan.mongodb.net/?retryWrites=true&w=majority')

    db = client["sdp"]
    collection = db["sdp4"]
    user = {"username": ename, "password": epass}
    result = collection.find_one(user)

    if result != None:
        return  render_template("index.html")
    else:
        return "<h1><center>fail</center></h1>"
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/lr',methods=['POST','GET'])
def hlr():
    ename = request.form.get("username")
    epass = request.form.get("password")
    cpass = request.form.get("cpassword")
    # Connect to MongoDB
    client = pymongo.MongoClient(
        'mongodb+srv://2100032245:2100032245@cluster0.iejagan.mongodb.net/?retryWrites=true&w=majority')

    db = client["sdp"]
    collection = db["sdp4"]
    user = {"username": ename, "password": epass, "confirm-password": cpass}
    result = collection.insert_one(user)
    if result != None:
        return "<h1><center>HOLA!! U CREATED U ACCOUNT PLEASE LOGIN</center></h1>"
    else:
        return "<h1><center>invalid</center></h1>"


if __name__ =="__main__":
    app.run(debug=False,host='0.0.0.0')
