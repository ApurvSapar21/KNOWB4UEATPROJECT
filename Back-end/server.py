import openfoodfacts

from flask import Flask
import requests
import json
from flask import Flask,render_template, request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template ("home-v2.html")

@app.route('/Food_sub',endpoint='Food_sub')
def get_food_sub():
    return render_template("Food_sub.html")

@app.route('/childeducation',endpoint='childeducation')
def get_food_sub():
    return render_template("childeducation.html")

@app.route('/wheat',endpoint='wheat')
def get_wheat():
    return render_template("wheat.html")

@app.route('/dairy',endpoint='dairy')
def get_dairy():
    return render_template("dairy.html")

@app.route('/egg',endpoint='egg')
def get_egg():
    return render_template("egg.html")

@app.route('/shellfish',endpoint='shellfish')
def get_shellfish():
    return render_template("shellfish.html")

@app.route('/soy',endpoint='soy')
def get_soy():
    return render_template("soy.html")

@app.route('/sesame',endpoint='sesame')
def get_sesame():
    return render_template("sesame.html")

@app.route('/treenut',endpoint='treenut')
def get_treenut():
    return render_template("treenut.html")

@app.route('/peanut',endpoint='peanut')
def get_peanut():
    return render_template("peanut.html")

@app.route('/static_information',endpoint='static_information')
def get_static_information():
    return render_template("static_infomation.html")

@app.route('/form',methods=['GET'],endpoint='form')
def form():
    code = '5000396015935'
    temp_url = "https://world.openfoodfacts.org/api/v0/product.json"
    url = '/'.join([temp_url, code])
    myResponse = requests.get(url, verify=True)
    # print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if (myResponse.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        print(jData)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
   # pro = openfoodfacts.products.get_product('5000396015935')
   # print(type(pro['product']['ingredients_hierarchy']))
    #return str(pro['product']['ingredients_hierarchy'])
    return jData

@app.route('/barcode_post', methods=['POST','GET'],endpoint='barcode_post')
def form():
    code = '5000396015935'
    temp_url = "https://world.openfoodfacts.org/api/v0/product.json"
    url = '/'.join([temp_url, code])
    myResponse = requests.get(url, verify=True)
    # print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if (myResponse.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        print(jData)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
   # pro = openfoodfacts.products.get_product('5000396015935')
   # print(type(pro['product']['ingredients_hierarchy']))
    #return str(pro['product']['ingredients_hierarchy'])
    return jData['product']

if (__name__ == '__main__'):
    app.run()