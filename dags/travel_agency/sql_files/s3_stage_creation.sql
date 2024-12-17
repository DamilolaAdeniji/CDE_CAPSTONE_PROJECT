CREATE or replace FILE FORMAT public.my_parquet_format
  TYPE = 'PARQUET';

CREATE OR REPLACE STAGE public.s3_countries
  URL='s3://dami-cde-bucket/stage/'
  CREDENTIALS=(AWS_KEY_ID=key_id AWS_SECRET_KEY=secret_key_id)
  ENCRYPTION=(TYPE='AWS_SSE_KMS' KMS_KEY_ID = 'aws/key')
FILE_FORMAT = my_parquet_format;