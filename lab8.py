from flask import Blueprint, render_template, request, jsonify


lab8=Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')