from flask import render_template, request, Blueprint


loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/post', methods=['GET', 'POST'])
def add_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post_uploaded', methods=['POST'])
def page_uploaded():
    pass






