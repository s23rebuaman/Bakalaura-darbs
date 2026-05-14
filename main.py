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

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('data_filter.html')

app.run()