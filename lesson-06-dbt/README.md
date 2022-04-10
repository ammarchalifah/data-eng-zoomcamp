# Learning Notes

OS: Windows 11

## Step-by-step
1. Run the following commands
```
docker-compose build
```
```
docker-compose run dbt-catalog init
```
   - Input the required values to initialize dbt project (including the desired project name).
2. To test connection, execute
```
docker-compose run --workdir="//usr/app/dbt/{PROJECT_NAME}" dbt-catalog debug
```
3. This repo contains an initiated DBT project. So, build all the seeds and models by running
```
docker-compose run --workdir="//usr/app/dbt/{PROJECT_NAME}" dbt-catalog build
```
This command combines `dbt seed`, `dbt run`, and `dbt test` at once.
4. To generate documentation, run 
```
docker-compose run --workdir="//usr/app/dbt/{PROJECT_NAME}" dbt-catalog docs generate
```
5. Serve the docs by running
```
docker-compose run --workdir="//usr/app/dbt/{PROJECT_NAME}" dbt-catalog docs serve
```

***

## DBT
1. For complete guide, access: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/docker_setup/README.md 
2. DBT uses Jinja template and Macros (function in Jinja template). This templating framework can make SQL a bit more programmatic.
3. DBT properties can be set up with any file names, as long as it ends with `.yml` and put inside `/models` directory.