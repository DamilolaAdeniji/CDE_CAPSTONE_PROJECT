{{ config(schema='public') }}

select
    country_name, 
    independence, 
    united_nation_members, 
    startofweek,
    official_country_name, 
    common_native_name, 
    currency_code,
    currency_name, 
    currency_symbol, 
    country_code_idd, 
    capital,
    region, 
    subregion, 
    languages, 
    continents
from
    {{ ref('staging') }} as staging