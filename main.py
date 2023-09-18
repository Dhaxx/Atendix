from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route('/main', methods=['GET','POST'])
def main():
    return render_template('main.html')
