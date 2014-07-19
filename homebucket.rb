require 'sinatra'

configure :production do
  require 'newrelic_rpm'
end

get '/' do
	@options = {
		'title' => "Homebucket",
		'active_page' => 0
	}

	@links = [
		{
			'name' => "Linkbucket",
			'tagline' => "Grab links for later.",
			'prerelease' => false
		},
		{
			'name' => "Songbucket",
			'tagline' => "Listen to YouTube.",
			'prerelease' => true
		},
		{
			'name' => "Workbucket",
			'tagline' => "Stylish timesheets.",
			'prerelease' => true
		}
	]

	erb :index
end
