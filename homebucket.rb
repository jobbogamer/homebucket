require 'sinatra'

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
		}
	]

	erb :index
end
