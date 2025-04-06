from flask import Flask, url_for, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    with open('templates/choice_design.html') as html_stream:
        html = html_stream.read()
    html = html.replace("{{ planet_name }}", planet_name)
    return html


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    print(nickname, level, rating)
    with open('templates/results_design.html') as html_stream:
        html = html_stream.read()
    html = html.replace("{{ nickname }}", nickname)
    html = html.replace("{{ level }}", str(level))
    html = html.replace("{{ rating }}", str(rating))
    return html


@app.route("/load_photo", methods=["GET", "POST"])
def load_photo():
    photo_url = None
    if request.method == "POST":
        if "photo" in request.files:
            photo = request.files["photo"]
            if photo.filename != "":
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
                photo.save(file_path)
                photo_url = url_for('static', filename=f'img/{photo.filename}')
    return render_template("load_photo.html", photo_url=photo_url)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8090)
