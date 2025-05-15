from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('obligation.dashboard'))
    return render_template('login.html')
