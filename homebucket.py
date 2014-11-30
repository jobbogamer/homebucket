
# Standard library
import os

# 3rd party
from flask import Flask, url_for, render_template, request, jsonify
import newrelic.agent

# Local
from model import database
from model.options import Options
from external_apis import github

##### Config #####

newrelic.agent.initialize('newrelic.ini')

app = Flask(__name__)
app.config["SECRET_KEY"] = "d47d2b74ff64e5a6ae5aedd4edebeaf1"

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except KeyError as error:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost:5432"

database.db.init_app(app)

options = Options()

##### Routes #####

@app.route('/')
def index():
    database.create_tables()

    options.title = "Homebucket"
    options.active_page = 0

    #repos = database.get_all_repos()

    repos = github.get_repos_for_user("jobbogamer")
    repos = [r for r in repos if r.name.endswith('bucket') and \
                not r.name == "homebucket"]

    return render_template('index.html', options=options, repos=repos)

##### API Routes #####



##### Template Filters #####



##### Main #####

if (__name__ == "__main__"):
    app.run(debug=True)
