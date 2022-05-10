from flask import Flask, url_for, request
from PIL import Image

app = Flask(__name__)


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
