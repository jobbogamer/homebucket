require 'sequel'
require './model/repo'

def add_repo(repo)
	@repos.insert(:name => repo.name, :tagline => repo.tagline,
	              :ext_url => repo.ext_url, :github_url => repo.github_url)
end

def all_repos()
	repo_objects = []
	@repos.all.each do |repo|
		repo_objects.push(Repo.new(repo[:name], repo[:tagline],
		                           repo[:ext_url], repo[:github_url]))
	end
	return repo_objects
end


if ENV['DATABASE_URL']
	db_url = ENV['DATABASE_URL']
else
	db_url = "postgres://localhost:5432"
end

DB = Sequel.connect(db_url)

DB.create_table? :repos do
		primary_key :id
		String :name
		String :tagline
		String :ext_url
		String :github_url
end

@repos = DB[:repos]
