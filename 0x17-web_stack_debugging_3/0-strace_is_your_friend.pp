# Correct a typo in a wordpress config file

exec { 'fix-typo':
  command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  provider => shell,
}
