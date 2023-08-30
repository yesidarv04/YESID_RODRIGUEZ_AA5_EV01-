from flask import Flask, render_template
from app.routes import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    return render_template('inicio_sesion.html')

if __name__ == '__main__':
    app.run()
