// https://github.com/gruntjs/grunt/issues/225

module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),

        less: {
            index: {
                src: "mis/static/less/main.less",
                dest: "mis/static/css/main.css",
                options: {
                    compress: true
                }
            }
        },

        watch: {
            files: ["mis/static/less/**/*.less", "mis/static/js/main.js",
                "mis/static/css/main.css"],
            tasks: ["less", "uglify", "cmq"]
        },

        uglify: {
            site: {
                files: {
                    "mis/static/js/mis.min.js": [
                        "mis/static/js/main.js",
                        "mis/static/js/plugins.js",
                        "mis/static/lib/js/retina.js-js/retina.js"
                    ],

                    "mis/static/lib/js/modernizr/modernizr.min.js" :
                        "mis/static/lib/js/modernizr/modernizr.js"
                }
            }
        },

        bower: {
            install: {
                //just run "grunt bower:install" and you"ll see files from your Bower packages in lib directory
                options: {
                    targetDir: "mis/static/lib",
                    // layout: "byType",
                    cleanTargetDir: true,
                    layout: function(type, component) {
                        var renamedType = type;
                        return type+"/"+component;
                    }
                }
            }
        },

        cmq: {
            options: {
                log: false
            },
            site: {
                files: {
                    "mis/static/css/": ["mis/static/css/main.css"]
                }
            }
        }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks("grunt-contrib-less");
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-bower-task");
    grunt.loadNpmTasks("grunt-contrib-uglify");
    grunt.loadNpmTasks("grunt-combine-media-queries");

    // Default task(s).
    grunt.registerTask("default", ["less", "watch", "uglify", "bower", "cmq"]);
};
