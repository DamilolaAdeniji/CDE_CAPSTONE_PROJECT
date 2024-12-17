truncate stage.raw_countries;

COPY INTO stage.raw_countries
FROM @public.s3_countries
FILE_FORMAT = (TYPE = 'PARQUET');