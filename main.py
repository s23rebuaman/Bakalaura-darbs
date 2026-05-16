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
import pymysql.cursors

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

connection = pymysql.connect(
    user='root',  
    password='rootAdmin.2004', 
    host='localhost',
    database='ventspils_reiss',
    cursorclass=pymysql.cursors.DictCursor  
)


@app.route('/query_result', methods=['POST'])
def get_results():
    year = request.form.get('years')
    month = request.form.get('months')
    #day = request.form.get('days')
    date = request.form.get('dates')
    start = request.form.get('beginning_hours')
    end = request.form.get('ending_hours')

    with connection:

        with connection.cursor() as cursor:
            query = """
            select Marsruta_nr, Reisa_nosaukums, Datums_un_laiks, Bilesu_sk
            from info
            where year(Datums_un_laiks) = %s
            and month(Datums_un_laiks) = %s
            and day(Datums_un_laiks) = %s
            and (time(Datums_un_laiks) > %s and time(Datums_un_laiks) < %s)
            order by Bilesu_sk desc
            """
            #query = "SELECT `Marsruta_nr`, count(Bilesu_sk) FROM `info` WHERE year(Datums_un_laiks) = %s"
            cursor.execute(query, (int(year), int(month), int(date), start, end))
            #cursor.execute(query, year)
            result = cursor.fetchall()
            #print("year: " + year + ", " + "month: " + month + ", " + "date: " + date)
            #return result
            return result

        connection.commit()

if __name__ == '__main__':
    app.run(debug=True)