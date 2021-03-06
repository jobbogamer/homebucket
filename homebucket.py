
# Standard library
import os

# 3rd party
from flask import Flask, url_for, render_template, request, jsonify
import newrelic.agent

# Local
from model import database
from model.options import Options
from external_apis import github
from external_apis import notifications

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

    repos = database.get_all_repos()
    for repo in repos:
        notifications.check_for_notifications(repo)

    return render_template('index.html', options=options, repos=repos)

##### API Routes #####

@app.route('/api/github')
def api_github():
    repos = database.get_all_repos()
    remote_repos = github.get_repos_for_user("jobbogamer")
    new_repos = []

    if repos is None:
        result = {
            "success": False,
            "repos": []
        }
    else:
        for repo in remote_repos:
            if repo.name.endswith('bucket') and not repo.name == "homebucket":
                already_known = False
                for local_repo in repos:
                    if local_repo.name == repo.name:
                        already_known = True

                if not already_known:
                    new_repos.append({
                        'name': repo.name,
                        'description': repo.description,
                        'site_url': repo.site_url
                    })
                    database.add_repo(repo)

        for repo in repos:
            still_exists = False
            for remote_repo in remote_repos:
                if remote_repo.name == repo.name:
                    still_exists = True
                    repo.description = remote_repo.description
                    repo.site_url = remote_repo.site_url

            if not still_exists:
                database.delete_repo(repo)

        database.commit_changes()

        result = {
            "success": True,
            "repos": new_repos
        }

    return jsonify(result)


##### Template Filters #####



##### Main #####

if (__name__ == "__main__"):
    app.run(debug=True)
