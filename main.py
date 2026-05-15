# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def main():
#     myfile = open('route.geojson')
#     txt = myfile.read()
#     return(txt)


# app.run()

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/returnjson', methods=['GET'])
# def return_json():
#     if request.method == 'GET':
#         myfile = open('route.geojson')
#         txt = myfile.read()
#         return jsonify(txt)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('data_filter.html')

# @app.route('/data_result', methods=['POST'])
# def data_result():
    # # if request.method == 'POST':
    # #     return render_template('data_result.php')
    # year = request.form.get('years')
    # month = request.form.get('months')
    # day = request.form.get('days')
    # date = request.form.get('dates')

    # return render_template('data_result.html', year=year, month=month, day=day, date=date)

db_credentials = {
    'user': 'root',  
    'password': 'rootAdmin.2004', 
    'host': '127.0.0.1',
    'name': 'ventspils_reiss'  
}
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://\
{db_credentials['user']}:{db_credentials['password']}@{db_credentials['host']}/\
{db_credentials['name']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INITIALIZE DATABASE AFTER CONFIGURATION
db = SQLAlchemy(app)

# APP ROUTE TO GET RESULTS FOR SELECT QUERY
@app.route('/query_result', methods=['POST'])
def get_results():
    year = request.form.get('years')
    month = request.form.get('months')
    day = request.form.get('days')
    date = request.form.get('dates')
    print(year, month, day, date)

    result = db.engine.execute('select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, count(Bilesu_sk) from info where year(Datums_un_laiks) = 2023 and month(Datums_un_laiks) = 2 and day(Datums_un_laiks) = 2 and Bilesu_sk=(select max(Bilesu_sk))')
    response = {f'Record {i}': list(each) for i, each in enumerate(result, start=1)}
    return response


app.run()