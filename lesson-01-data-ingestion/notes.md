# Learning Notes

OS: Windows 11

## Step-by-step
1. Download the NY yellow taxi data from this page (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Just download one of the yellow taxi CSV.
2. Run the docker container by executing this command: ```docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi"
 -v ${pwd}\ny_taxi_data:/var/lib/postgresql/data -p 5432:5432 postgres:13```
 3. Start the ingestion by executing this command from the host computer (outside of the container): ```python ingestion.py --user root --password root --host localhost --port 5432 --db ny_taxi --table_name {table-name-to-create} --csv_name {CSV-filename}1.csv```
 4. To inspect the ingested table, install `pgcli` by using pip (`pip install pgcli`), then connect to the postgres table by executing this command on the host computer: ```pgcli -h localhost -p 5432 -u root -d ny_taxi```. Inside the Postgres client, execute `\dt` to check all available tables in the database, and query anything using SQL to explore the ingested data.

## Docker
1. We can run a docker container while specifying the environment variables through flags.

## Database
1. A Pandas dataframe schema can be inferred by using `pd.io.sql.get_scheme(df, name = name)`.
2. The Pandas' schema are defined in DDL (data definition language), a standard language for creating, modifying, and removing objects in database environments.
3. Pandas uses SQLAlchemy to create a connection with databases.
4. To avoid OOM (out-of-memory), load CSV file into Pandas DataFrame using an iterator (with predefined chunksize).