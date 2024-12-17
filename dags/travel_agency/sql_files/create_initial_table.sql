use role dbt_role;

use database cde_db;

create schema stage;


create transient table stage.raw_countries (
country_name varchar, 
independence varchar, 
united_nation_members varchar, 
startofweek varchar,
official_country_name varchar, 
common_native_name varchar, 
currency_code varchar,
currency_name varchar, 
currency_symbol varchar, 
country_code_idd varchar, 
capital varchar,
region varchar, 
subregion varchar, 
languages varchar, 
continents varchar
)