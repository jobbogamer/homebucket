require 'sinatra'

get '/' do
	@options = {
		'title' => "Homebucket",
		'active_page' => 0
	}

	@links = [
		{
			'name' => "Linkbucket",
			'tagline' => "Grab links for later."
		}
	]

	erb :index
end
