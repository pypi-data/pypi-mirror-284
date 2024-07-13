import pandas as pd
import os

def usaggregate(data, level, agg_numeric='mean', agg_character='first'):
    if not isinstance(data, list) or len(data) < 1:
        raise ValueError("Data must be a list of one or more pandas DataFrames.")
    
    supported_levels = ['zip', 'city', 'county', 'state']
    if level not in supported_levels:
        raise ValueError(f"Level must be one of {supported_levels}.")
    
    zipcodes_path = os.path.join(os.path.dirname(__file__), 'data', 'zipcodes.csv')
    zip_relations = pd.read_csv(zipcodes_path)
    
    level_hierarchy = {'zip': 0, 'city': 1, 'county': 2, 'state': 3}

    def detect_geo_columns(df):
        geo_columns = {}
        for col in df.columns:
            if 'zip' in col.lower():
                geo_columns['zip'] = col
            if 'city' in col.lower():
                geo_columns['city'] = col
            if 'state' in col.lower():
                geo_columns['state'] = col
            if 'county' in col.lower():
                geo_columns['county'] = col
        return geo_columns

    def get_geo_id(row, level, geo_columns, zip_relations):
        if level == 'city':
            city_state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]][['city', 'ST']].iloc[0]
            return f"{city_state['city']}, {city_state['ST']}"
        elif level == 'county':
            county_state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]][['county', 'ST']].iloc[0]
            return f"{county_state['county']}, {county_state['ST']}"
        elif level == 'state':
            state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]]['ST'].iloc[0]
            return state

    def aggregate_dataframe(df, level):
        geo_columns = detect_geo_columns(df)
        highest_granularity = min(geo_columns.keys(), key=lambda k: level_hierarchy[k])
        
        if level_hierarchy[highest_granularity] > level_hierarchy[level]:
            raise ValueError(f"Cannot aggregate from {highest_granularity} to {level}. Please choose a higher level of aggregation.")
        
        if level_hierarchy[highest_granularity] <= level_hierarchy[level]:
            geo_id_col = 'GEO_ID'
            
            if highest_granularity != level:
                df[geo_id_col] = df.apply(lambda x: get_geo_id(x, level, geo_columns, zip_relations), axis=1)
                df.drop(columns=[geo_columns[highest_granularity]], inplace=True)
            else:
                df[geo_id_col] = df[geo_columns[highest_granularity]]
                df.drop(columns=[geo_columns[highest_granularity]], inplace=True)

            numeric_cols = df.select_dtypes(include=['number']).columns
            char_cols = df.select_dtypes(include=['object']).columns.difference(['GEO_ID', 'year'])
            
            if agg_numeric == 'mean':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].mean()
            elif agg_numeric == 'median':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].median()
            elif agg_numeric == 'mode':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].agg(lambda x: x.mode()[0])
            elif agg_numeric == 'sum':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].sum()
            elif agg_numeric == 'first':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].first()
            elif agg_numeric == 'last':
                numeric_agg = df.groupby([geo_id_col, 'year'], dropna=True)[numeric_cols].last()
            else:
                raise ValueError("agg_numeric must be 'mean', 'median', 'mode', 'sum', 'first', or 'last'.")
            
            if agg_character == 'first':
                char_agg = df.groupby([geo_id_col, 'year'], dropna=True)[char_cols].first()
            elif agg_character == 'last':
                char_agg = df.groupby([geo_id_col, 'year'], dropna=True)[char_cols].last()
            elif agg_character == 'mode':
                char_agg = df.groupby([geo_id_col, 'year'], dropna=True)[char_cols].agg(lambda x: x.mode()[0])
            else:
                raise ValueError("agg_character must be 'first', 'last', or 'mode'.")
            
            return numeric_agg.join(char_agg).reset_index()
        else:
            return df

    aggregated_data = [aggregate_dataframe(df, level) for df in data]
    
    if len(aggregated_data) > 1:
        result = aggregated_data[0]
        for df in aggregated_data[1:]:
            result = result.merge(df, on=['GEO_ID', 'year'], how='outer', suffixes=('', '_dup'))
            # Remove duplicate columns after merge
            result = result.loc[:, ~result.columns.duplicated()]
        return result
    else:
        return aggregated_data[0]