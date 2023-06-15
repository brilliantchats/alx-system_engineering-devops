# Change OS configuration to allow holberton user to login without any error

exec { 'change-hard':
  command  => 'sed -i s/5$/1024/g /etc/security/limits.conf',
  provider => shell,
}

exec { 'change-soft':
  command  => 'sed -i s/4$/1024/g /etc/security/limits.conf',
  provider => shell,
}
