require 'json'
require 'open-uri'
require './model/repo'


def get_repos(user)
	url = "https://api.github.com/users/#{user}/repos"
	repos = []
	open(url) { |data|
		json = data.read
		json_repos = JSON.parse(json)
		json_repos.each { |repo|
			repos.push(Repo.new(repo["name"], repo["description"],
			                	repo["homepage"], repo["html_url"]))
		}
	}
	return repos
end
