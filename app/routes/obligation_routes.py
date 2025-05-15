from flask import Blueprint, render_template, request, redirect, url_for
from app.models.models import db, Obligation
from datetime import datetime

obligation_bp = Blueprint('obligation', __name__, template_folder='../templates')

@obligation_bp.route('/dashboard')
def dashboard():
    obligations = Obligation.query.all()
    return render_template('dashboard.html', obligations=obligations)

@obligation_bp.route('/add', methods=['GET', 'POST'])
def add_obligation():
    if request.method == 'POST':
        due_date_str = request.form['due_date']

        if due_date_str:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        else:
            # Handle missing due_date
            due_date = None
         
        obligation = Obligation(
            title=request.form['title'],
            type=request.form['type'],
            due_date=datetime.strptime(request.form['due_date'], '%Y-%m-%d'),
            assigned_to=request.form['assigned_to'],
            status=request.form['status']
        )
        db.session.add(obligation)
        db.session.commit()
        return redirect(url_for('obligation.dashboard'))
    return render_template('obligation_form.html')
