var gulp = require('gulp'),
    browserSync = require('browser-sync').create();

gulp.task('watch', function() {
  browserSync.init({
    server: './'
  });
  gulp.watch('index.html').on('change', browserSync.reload);
  gulp.watch('pages/*.html').on('change', browserSync.reload);
  gulp.watch('js/*.js').on('change', browserSync.reload);
  gulp.watch('css/*.css').on('change', browserSync.reload);

});
