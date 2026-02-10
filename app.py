from flask import Flask, request, render_template, url_for, flash
from database import db_session, Usuario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = 'senaisp'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    user = select(Usuario).where(Usuario.id == int(user_id))
    result = db_session.execute(user).scalar_one_or_none()
    return result

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)