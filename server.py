from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_motto():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promo_text = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем о  битаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return '<br>'.join(promo_text)


@app.route('/image_mars')
def image_mars():
    return f'''
    <h1>Жди нас, Марс!<h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
    alt="здесь должна была быть картинка, но не нашлась" width="400">'''


@app.route('/promotion_image')
def promotion_image():
    with open('templates/promotion_design.html') as html_stream:
        html = html_stream.read()

    html = html.replace("{{ url }}", f"{url_for('static', filename='img/mars.jpg')}")
    return html


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == "GET":
        with open('templates/astronaut_selection_design.html') as html_stream:
            html = html_stream.read()
    elif request.method == "POST":
        data = request.form
        print(data)
        return "Форма успешно отправлена!"
    return html


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8090)
