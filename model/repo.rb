class Repo
	attr_accessor :name, :tagline, :ext_url, :github_url

	def initialize(name, tagline, ext_url, github_url)
		@name = name
		@tagline = tagline
		@ext_url = ext_url
		@github_url = github_url
	end
end
