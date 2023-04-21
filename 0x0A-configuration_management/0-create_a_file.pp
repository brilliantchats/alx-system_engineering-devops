# Puppet manifest that creates a directory and then creates a file in directory
file { '/tmp/school':
  ensure  => 'present',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
