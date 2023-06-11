# Postmortem - Web app Outage

## Issue Summary
Duration of outage 1200hrs — 1230hrs CAT. Web app was down and not serving any web pages. Root cause was a typo in one of the wordpress configuration files, wp-settings.php in which the file class-wp-locale.php was incorrectly typed in as class-wp-locale.phpp.

## Timeline
1200hrs- Issue detected. Detected by the engineer on trying to launch the app.
1210hrs- strace tool was used to dig through a curl of the site
1215hrs — Noticed several ENOENT errors in the stack trace. At the bottom of the stack was a reference to no such file or directory named class-wp-locale.phpp in one of wordpress configuration files.
1220hrs- Navigated to /var/www/html directory. Opened the file wp-settings.php and saw the typo in which class-wp-locale.phpp had an extra p.
1225hrs- Corrected the typo using a puppet manifest.
1230hrs- Web app back up and all services working.

## Root Cause and Resolution
The issue was essentially caused by a typo in one of the Wordpress configuration files. There are two wordpress config files namely wp-config.php and wp-settings.php. On the strace there was an error of no such file or directory of the file class-wp-locale.phpp. Research of the wordpress docs showed that class-wp-locale.php is one of a number of files used to load the L10n library which is essential in building the frontend. The file is a php file and in our web app the extension was incorrectly typed in as phpp insted of php. The issue was solved by editing the wp-settings.php file by using the streamline editor, sed. The code for this was put in a puppet manifest and voila the issue was resolved.

## Corrective and Preventative measures
Corrective measures were to write an exec resource in a puppet manifest in which sed was used to change in place every occurence of class-wp-locale.phpp to class-wp-locale.php in the file /var/www/html/wp-settings.php.

Preventative measures are to always look up the configuration files of a site especially that of a service using wordpress before starting the service to avoid unexpected errors.
