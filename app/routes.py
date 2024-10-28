from flask import Blueprint, render_template
from .data_analysis import analyze_sales_data

main_routes = Blueprint('main', __name__)

@main_routes.route('/result')
def result():
    summary = analyze_sales_data()
    return render_template('result.html', summary=summary)
