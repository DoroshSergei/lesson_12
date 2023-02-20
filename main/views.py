from flask import render_template, Blueprint, request
import json
from functions import load_files

PATH = 'posts.json'

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def page_search_post():
    files = load_files(PATH)
    s = request.args['s']
    return render_template('post_list.html', s=s, files=files)




