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
   - Input the required values to initialize dbt project.
2. To test connection, execute
```
docker-compose run --workdir="//usr/app/dbt/{PROJECT_NAME}" dbt-catalog debug
```

***

## DBT
1. lala