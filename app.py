from flask import Flask, request, render_template

app = Flask(__name__)


def bmi_calculate(bmi_index):
    answer = 'Severe Thinness'
    bmi_index_value = {
        16: 'Moderate Thinness',
        17: 'Mild Thinness',
        18.5: 'Normal',
        25: 'Overweight',
        30: 'Obese'
    }
    for i in bmi_index_value:
        if i > bmi_index:
            return f"You have {answer} BMI:{bmi_index}"
        else:
            answer = bmi_index_value[i]

    return f"You have {answer} BMI:{bmi_index}"


@app.route('/', methods=['GET', 'POST'])
def index():
    var_name = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        user_weight = float(request.form.get('weight'))
        user_height_sqr = (float(request.form.get('height')) / 100) ** 2
        var_name = bmi_calculate(round(user_weight / user_height_sqr, 1))

    return render_template('index.html',
                           name=var_name)


print(bmi_calculate(15))
print(bmi_calculate(16.1))
print(bmi_calculate(17.2))
print(bmi_calculate(18.6))
print(bmi_calculate(25))
print(bmi_calculate(25.1))
print(bmi_calculate(30))
print(bmi_calculate(31))
if __name__ == '__main__':


    app.run()
