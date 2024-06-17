from flask import Flask, render_template, request
from math import sin, tan, cos, pi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Trig_funk():

    result = {}
    selected_functions = []

    if request.method == 'POST':

        grad = float(request.form['grad'])
        precision = int(request.form['precision'])
        units = request.form['units']
        selected_functions = request.form.getlist('functions')

        if units == 'degrees':
            degrees = grad * pi / 180

            if 'sin' in selected_functions:
                result['sin'] = round(sin(degrees), precision)
            if 'cos' in selected_functions:
                result['cos'] = round(cos(degrees), precision)
            if 'tg' in selected_functions:
                result['tg'] = round(tan(degrees), precision)
            if 'ctg' in selected_functions:
                result['ctg'] = round(1 / tan(degrees), precision)

            return render_template("index.html", result=result, selected_functions=selected_functions)

        if units == 'radians':

            if 'sin' in selected_functions:
                result['sin'] = round(sin(grad), precision)
            if 'cos' in selected_functions:
                result['cos'] = round(cos(grad), precision)
            if 'tg' in selected_functions:
                result['tg'] = round(tan(grad), precision)
            if 'ctg' in selected_functions:
                result['ctg'] = round(1 / tan(grad), precision)

            return render_template("index.html", result=result, selected_functions=selected_functions)

    return render_template("index.html", selected_functions=selected_functions)

if __name__ == "__main__":
    app.run(debug=True)