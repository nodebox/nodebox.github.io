task :default => [:rebuild]

desc 'Remove old _site and rebuild'
task :rebuild do
  sh 'rm -rf _site'
  sh 'time jekyll'
end

desc 'Deploy to the live server'
task :deploy => [:rebuild] do
  sh 'rsync -rtz --omit-dir-times --delete _site/ emrg@nodebox.net:/www/nodebox.net/public_html/'
end

desc 'Run Jekyll in server mode'
task :server do
  sh 'jekyll --auto --server'
end
