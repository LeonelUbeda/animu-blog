const gulp = require('gulp');
const sass = require('gulp-sass');
const del = require('del');
const autoprefixer = require('gulp-autoprefixer')

var path = {
    distCSS: './anime/anime/static/dist/css/'
}



gulp.task('styles', () => {
    return gulp.src('./anime/anime/static/scss/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({cascade: false, grid: 'autoplace'}))
        .pipe(gulp.dest(path.distCSS));
});


gulp.task('watch', () => {
    gulp.watch('./anime/anime/static/**/*.scss', (done) => {
        gulp.series(['clean', 'styles'])(done);
    });
});

gulp.task('clean', () => {
    return del([
        'css/main.css',
    ]);
});

gulp.task('default', gulp.series(['clean', 'styles']));