import openfoodfacts.products
from flask import Flask,render_template, request,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_bootstrap import Bootstrap
#from PIL import Image
#from pytesseract import pytesseract
import mysql.connector
import requests
import json
import base64
import io
import pyodbc
app = Flask(__name__,template_folder='templates',static_folder='static')
CORS(app)
Bootstrap(app)



# Obtain connection string information from the portal
cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=tcp:knowb4ueatserver.database.windows.net,1433;"
            "Database=knowb4ueatdb;"
            "UID=akshaya_sai;"
            "PWD=#admin123;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
            )

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testdemo'

mysql = MySQL(app)

selected_allergens = []
product_barcode = []

@app.route('/')
def HomePagev():
    opening_slogan = 'Shopping Has Never been Easier for \nParents of Children with Food Allergies'
    button_txt="Click to start scanning for Allergens"
    return render_template('home-v2.html',result = opening_slogan,
                           btn_txt = button_txt)


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")

@app.route('/Food_sub',endpoint='Food_sub')
def get_food_sub():
    return render_template("Food_sub.html")

@app.route('/childeducation',endpoint='childeducation')
def get_food_sub():
    return render_template("childeducation.html")


@app.route('/static_information',endpoint='static_information')
def get_static_information():
    return render_template("static_infomation.html")



@app.route('/getstudentdetails', methods=['GET'],endpoint='getStudentDetails')
def getStudentDetails():
    if request.method == 'GET':
        print("hello world")
        allergens = []
        cnxn = pyodbc.connect(cnxn_str)
        cursor = cnxn.cursor()
        """ list = []
        #dict = {"name": "jane doe", "salary": 9000, "email": "JaneDoe@pynative.com"}
        select_sql = "SELECT * FROM student"
        res = cursor.execute(select_sql)
        print(type(res))
        for ele in res:
            list.append(ele[1])
        print(cursor.fetchall())
        """
        demo = ["dairy", "wheat"]
      

        execu = cursor.execute(
            """
            Select 
             allergen_name,
             alternative_name
            From
                alternative_allergen_name
            where
             allergen_name in ({})
            """.format(','.join("?" * len(demo))), demo)

        myallergens = cursor.fetchall()

        for x, y in myallergens:
            allergens.append(y)
        #dict['name'] = list
        response = jsonify({
            "result": allergens
        })
        return response


@app.route('/form',methods=['GET'],endpoint='form')
def form():
    code = '5000396015935'
    temp_url = "https://world.openfoodfacts.org/api/v0/product.json"
    url = '/'.join([temp_url, code])
    myResponse = requests.get(url, verify=True)
    # print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if (myResponse.ok):
       
        jData = json.loads(myResponse.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        print(jData)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    pro = openfoodfacts.products.get_product('5000396015935')
    print(type(pro['product']['ingredients_hierarchy']))
    return str(pro['product']['ingredients_hierarchy'])
