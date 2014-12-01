$(function() {
    getReposFromGithub();
});

function addNewRepo(name, description, siteURL) {
    var html = '<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">' +
                    '<div id="repo-{{ repo.id }}" class="repo">' +
                        '<a target="_blank" href="' + siteURL + ' ">' +
                            '<div class="logo">' +
                                '<img src="' + siteURL + '/static/apple-touch-icon.png" />' +
                            '</div>' +
                            '<p class="name">' + capitaliseFirstLetter(name) + '</p>' +
                            '<p class="description">' + description + '</p>' +
                        '</a>' +
                    '</div>' +
                '</div>';

    $('.row').append(html);
}

function capitaliseFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function getReposFromGithub() {
    $.ajax({
        url: '/api/github'
    }).done(function(data) {
        if (data['success']) {
            for (var i = 0; i < data['repos'].length; i++) {
                var repo = data['repos'][i];
                addNewRepo(repo['name'], repo['description'], repo['site_url']);
            }
        }
    });
}
