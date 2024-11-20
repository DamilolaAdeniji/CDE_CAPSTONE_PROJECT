import pandas as pd

def extract_value(d, key,islist=False):
    try:
        value = d.get(key)
        if islist:
            return value[0]
        else:
            return value
    except:
        return None
    

def get_nested_values(d,return_type='val'):
    try:
        for key, value in d.items():
            if value is not None:
                if return_type == 'code':
                    return key
                elif return_type == 'name':
                    return value['name']
                elif return_type == 'symbol':
                    return value['symbol']
                else:
                    return value
        return None
    except:
        return None
    

def dataframe_transformer(df):
    df['country_name'] = df['name'].apply(lambda d: extract_value(d, 'common'))

    df['independence'] = df['independent']

    df['united_nation_members'] = df['unMember']

    df['startofweek'] = df['startOfWeek']

    df['official_country_name'] = df['name'].apply(lambda d: extract_value(d, 'official'))

    df['common_native_name'] = df['name'].apply(lambda d: extract_value(d, 'official'))

    df['currency_code'] = df['currencies'].apply(lambda d: get_nested_values(d, 'code'))

    df['currency_name'] = df['currencies'].apply(lambda d: get_nested_values(d, 'name'))

    df['currency_symbol'] = df['currencies'].apply(lambda d: get_nested_values(d, 'symbol'))

    df['country_code_root'] = df['idd'].apply(lambda d: extract_value(d, 'root'))

    df['country_code_suffixes'] = df['idd'].apply(lambda d: extract_value(d, 'suffixes'))

    df['country_code_suffixes'] = df.country_code_suffixes.apply(lambda x : x[0] if x is not None else x)

    df['country_code_idd'] = df['country_code_root'] + df.country_code_suffixes 

    df['capital'] = df.capital.apply(lambda x : x[0] if x is not None else x)

    df['languages'] = df['languages'].apply(lambda d: get_nested_values(d))

    df['continents'] = df.continents.apply(lambda x : x[0] if x is not None else x)

    new_cols = [
    'country_name','independence','united_nation_members','startofweek','official_country_name','common_native_name','currency_code',
    'currency_name','currency_symbol','country_code_idd','capital','region','subregion','languages','continents'
    ]

    return df[new_cols]

