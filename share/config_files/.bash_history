kill -USR2 `cat /var/run/anaconda.pid`
kill -HUP `cat /var/run/anaconda.pid`
udevadm info --export-db | less
tail -f /tmp/storage.log
echo b > /proc/sysrq-trigger
dmsetup table
multipath -d
HOME=/root chroot /mnt/sysimage bash -l -i
