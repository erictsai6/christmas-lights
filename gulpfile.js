// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var shell = require('gulp-shell')

// Lint Task
gulp.task('lint', function() {
    return gulp.src('static/app/**/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Compile Our Sass
gulp.task('sass', function() {
    return gulp.src('static/scss/**/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('static/css'));
});

gulp.task('build', ['sass'], shell.task([
    './node_modules/.bin/webpack -d'
]));

gulp.task('server', shell.task([
  'python server.py'
]));

gulp.task('redis-server', shell.task([
    'redis-3.2.6/src/redis-server'
]))

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('static/jsx/**/*.jsx', ['build']);
    gulp.watch('server.py', ['server']);
    gulp.watch('server/**/*.py', ['server']);
    gulp.watch('static/scss/**/*.scss', ['sass']);
});

// Default Task
gulp.task('default', ['lint', 'build', 'server', 'redis-server', 'watch']);