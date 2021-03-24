# Server Monitoring API
## How to use:
  * At the DB machine, download the `docker-compose.yml` located at `src/db/`, edit the file to change the credintials and the database, and run `docker-compose up`. You can also change the port of the database (host side port).
  * At the server machine, download the `docker-compose.yml` located at `src/server/`, edit the file to change the database information (host, port, username, password, database, collection), and run `docker-compose up`. You can also change the port of the API (host side port).
