# Increase the number of of max files open with nginx to handle multiple requests

exec { 'increase-max-files':
  command  => 'sed -i s/15/4096/g /etc/default/nginx',
  provider => shell,
}

exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
