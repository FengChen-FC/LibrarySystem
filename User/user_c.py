from flask import Blueprint, request, session, redirect, url_for, render_template

user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    print(session.get('user_login'))
    if request.method == 'GET':
        if session.get('user_login'):
            db_user = User.query.filter_by(username=session['user_login']).first()
            if db_user is not None:
                return redirect(url_for('user.user_info', id=db_user.id))

        return render_template('user/login.html')
