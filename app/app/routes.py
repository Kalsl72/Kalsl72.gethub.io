from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/household_survey', methods=['GET', 'POST'])
def household_survey():
    if request.method == 'POST':
        # Handle form submission
        pass
    return render_template('household_survey.html')

@main.route('/donor_dashboard')
def donor_dashboard():
    return render_template('donor_dashboard.html')

@main.route('/admin_panel')
def admin_panel():
    return render_template('admin_panel.html')
