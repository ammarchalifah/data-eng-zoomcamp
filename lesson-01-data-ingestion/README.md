# Learning Notes

OS: Windows 11

## Step-by-step
1. Change the working directory to inside of `lesson-01-data-ingestion`.
2. Download the NY yellow taxi data from this page (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Just download one of the yellow taxi CSV.
3. Run the docker container by executing this command: 
```
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi"
 -v ${pwd}\ny_taxi_data:/var/lib/postgresql/data -p 5432:5432 postgres:13
 ```
4. Start the ingestion by executing this command from the host computer (outside of the container): 
```
python ingestion.py --user root --password root --host localhost --port 5432 --db ny_taxi --table_name {table-name-to-create} --csv_name {CSV-filename}.csv
```
 1. To inspect the ingested table, install `pgcli` by using pip (`pip install pgcli`), then connect to the postgres table by executing this command on the host computer: ```pgcli -h localhost -p 5432 -u root -d ny_taxi```. Inside the Postgres client, execute `\dt` to check all available tables in the database, and query anything using SQL to explore the ingested data.


### Connecting Postgres container to PgAdmin
1. Create a docker network to allow cross-container communication by executing `docker network create {NETWORK-NAME}` in host machine. In my case, I used 
   ```
   docker network create pg-network
   ```
2. Rerun the docker container for Postgres by adding `--network={NETWORK-NAME} --name {CONTAINER-NAME}` flag. In my case, I used `pg-network` as the network name and `pg-database` as the container name.
3. To make database administration easier, we can use PgAdmin (a GUI for Postgres) by running another Docker container. Execute this command from host machine: 
```
docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.org" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network={NETWORK-NAME} --name pgadmin dpage/pgadmin4
```
4. Open the GUI on `https://localhost:8080`. Sign in using the credentials (admin@admin.org and root, in this case).
5. Add new server. Connect to `pg-database` host on port 5432.

***

## Docker
1. We can run a docker container while specifying the environment variables through flags.

## Database
1. A Pandas dataframe schema can be inferred by using `pd.io.sql.get_scheme(df, name = name)`.
2. The Pandas' schema are defined in DDL (data definition language), a standard language for creating, modifying, and removing objects in database environments.
3. Pandas uses SQLAlchemy to create a connection with databases.
4. To avoid OOM (out-of-memory), load CSV file into Pandas DataFrame using an iterator (with predefined chunksize).