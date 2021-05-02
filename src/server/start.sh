#!/bin/sh

# enable crond and start it
systemctl3 enable crond
systemctl3 start crond

# temp file to deal with the crontab
temp_file=~/temp.$(date "+%Y.%m.%d-%H.%M.%S")

# dump the crontab to the temp file
crontab -l > $temp_file

# add the stats_collector job
sed -i "/^.*stats_collector.py$/d" $temp_file
echo "0 * * * * python3 /usr/src/app/stats_collector.py" >> $temp_file

# reload the crontab with the edited temp file
crontab $temp_file

# remove the tempfile
rm -f $temp_file

# restart crond
systemctl3 restart crond

# start the flask application
python3 /usr/src/app/api.py
