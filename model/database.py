
from repo import Repo
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##### Models #####

class Repo(db.Model):
    id = database.Column(db.Integer, primary_key=True)
    name = database.Column(db.String)
    url = database.Column(db.String)
    site_url = database.Column(db.String)

    def __init__(self):
        self.name = ""
        self.url = ""
        self.site_url = ""

##### Public Methods #####

def add_repo(repo):
    db.session.add(repo)
    commit_changes()


def create_tables():
    db.create_all()


def delete_repo(id):
    repo = get_repo(id)
    db.session.delete(repo)
    commit_changes()


def get_all_repos():
    repos = Repo.query.all()
    repos = sorted(repos, key=lambda repo: repo.name)
    return repos


def get_repo(id):
    repo = Repo.query.filter_by(id = id).first()
    return repo


def repo_exists(name):
    repos = get_all_repos()

    for repo in repos:
        if repo.name == name:
            return True

    return False

##### Private Methods #####

def commit_changes():
    db.session.commit()
