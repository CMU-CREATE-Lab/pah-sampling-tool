"""Gunicorn configuration for Apache's spectroexplorer Unix-socket proxy."""

# Apache's ProxyPass directives connect to this exact socket.
bind = "unix:/projects/spectroexplorer.createlab.org/spectroexplorer.sock"

# Resolve app.py and its relative data/ paths from the deployed project.
chdir = "/projects/spectroexplorer.createlab.org/pah-sampling-tool"
wsgi_app = "app:server"

# Keep the loaded Excel data shared by forked workers where possible.
preload_app = True
workers = 2
worker_class = "gthread"
threads = 4
timeout = 120
graceful_timeout = 30

# Let Apache's www-data group connect when the systemd unit sets that group.
umask = 0o007

accesslog = "-"
errorlog = "-"
loglevel = "info"
capture_output = True
