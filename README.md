# Server Monitoring API

## How to use:

- At the DB machine, copy `docker-compose.yml` located at `src/db/`, edit the file to change the credentials and the database, and run `docker-compose run db`. You can also change the port of the database (host side port).
- At the server machine, copy the content of the directory `opt/` to the server filesystem `/opt/` and install the requirements using `pip install -r /opt/requirements.txt`, then copy `docker-compose.yml` located at `src/server/`, edit the file to change the database information (host, port, username, password, database, collection), and run `docker-compose run server`. You can also change the port of the API (host side port).
