from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login
        return redirect(url_for('main_routes.result'))
    return render_template('login.html')

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process registration
        return redirect(url_for('auth.login'))
    return render_template('register.html')
