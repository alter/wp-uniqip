/bin/mv /var/log/apache2/domain.name_log /var/log/apache2/domain.name_log.old
/usr/sbin/apache2ctl graceful
/bin/sleep 6
/bin/gzip /var/log/apache2/domain.name_log.old

