#!/bin/sh

# temp file to deal with the crontab
temp_file=~/temp.$(date "+%Y.%m.%d-%H.%M.%S")

# dump the crontab to the temp file
crontab -l > $temp_file

# add the stats_collector job
sed -i "/^.*stats_collector.py$/d" $temp_file
echo "0 * * * * python /usr/src/app/stats_collector.py" >> $temp_file

# reload the crontab with the edited temp file
crontab $temp_file

# remove the tempfile
rm -f $temp_file

# start the crontab
/usr/sbin/crond  &

# start the flask application
python /usr/src/app/api.py
