from flask import Flask, render_template

app = Flask(__name__)


@app.route('/promotion')
def promotion():
    promo = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promo)


@app.route('/image_mars')
def img():
    return """<!doctype html>
                <html>
                  <head>
                    <meta charset="UTF-8">
                      <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="static/img.png">
                        <figcaption>
                        Вот она какая, красная планета
                        </figcaption>
                    </figure>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return f'''<!doctype html>
                <html>
                  <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <title>Варианты выбора</title>
                      <link rel="stylesheet"
                                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                   crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h2>Эта планета ближже к Земле;<h2>
                    <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning" role="alert">
                      На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>'''


@app.route('/')
@app.route('/index/<title>')
def page(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')