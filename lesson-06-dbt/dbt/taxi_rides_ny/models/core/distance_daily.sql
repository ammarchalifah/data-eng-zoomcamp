{{ config(materialized='table') }}

SELECT
    date_trunc(tpep_pickup_datetime, DAY) AS date_id,
    sum(trip_distance) distance 
FROM {{ source('trips_data_all', 'yellow_tripdata') }}
GROUP BY 1