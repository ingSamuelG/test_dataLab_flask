from flask import render_template, jsonify
from . import main
from .helpers import userResToDic,projectResToDic
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/proyecto/<name>')
def project(name):
    proyects_res = db.getProjectByName(name)
    users_res = db.getUsers()

    response = {
        "projects": list(map(projectResToDic, proyects_res)),
        "users": list(map(userResToDic,users_res))
        }
    return jsonify(response)
# user, user role association