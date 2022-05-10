from flask import Flask, url_for, request
from PIL import Image

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/photos/download.png')
        # with Image.open('static/photos/download.png', 'rgb') as d:
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                        href={url_for('static', filename='css/formstyle.css')}>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                        <h1 align="center">Загрузка фотографии</h1>
                        <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src={url_for('static', filename='photos/download.png')} width=400>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                </head>
                <body>
                <h1>Пейзажи Марса</h1>
                <div class="container">
                  <br>
                  <div id="myCarousel" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                      <li data-target="#myCarousel" data-slide-to="1" class="active"></li>
                      <li data-target="#myCarousel" data-slide-to="2"></li>
                      <li data-target="#myCarousel" data-slide-to="3"></li>
                    </ol>
                    <div class="carousel-inner" role="listbox">
                      <div class="item active">
                        <img src="{url_for('static', filename='photos/landscape1.jpg')}" alt="First slide">
                            <div class="carousel-caption d-none d-md-block">
                            </div>
                      </div>
                      <div class="item">
                        <img src="{url_for('static', filename='photos/landscape2.jpg')}" alt="Second slide">
                            <div class="carousel-caption d-none d-md-block">
                            </div>
                      </div>
                      <div class="item">
                        <img class="d-block w-100" src="{url_for('static', filename='photos/landscape3.jpg')}" alt="Third slide">
                        <div class="carousel-caption d-none d-md-block">
                        </div>
                      </div>
                    </div>
                    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                      <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                      <span class="sr-only">Next</span>
                    </a>
                  </div>
                </div>
                </body>
                </html>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
