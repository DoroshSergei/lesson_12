from flask import render_template, Blueprint, request

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/index.html')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def page_search_post():
    s = request.args['s']
    return render_template('post_list.html', s=s)




