# Kills a process
exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow'
}
