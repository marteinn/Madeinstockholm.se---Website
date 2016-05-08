'use strict'

// Disable annoying terminal notice
process.env.DISABLE_NOTIFIER = true;

var elixir = require('laravel-elixir');

elixir(function(mix) {
    var publicPath = elixir.config.publicPath;

    // Add trailing slash
    publicPath += publicPath.endsWith("/") ? "" : "/";

    mix.less("less/main.less")
        .copy('fonts', publicPath+'css/fonts')
        .copy("less/lib/normalize/normalize.css",
            publicPath+"css/normalize.css");

    mix.browserify("js/main.js", publicPath+"js/main.js");
    mix.copy('js/lib', publicPath+'js/lib');

    mix.copy('img', publicPath+'img');
});
