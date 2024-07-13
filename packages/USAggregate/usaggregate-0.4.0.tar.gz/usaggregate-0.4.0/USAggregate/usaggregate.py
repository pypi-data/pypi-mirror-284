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
            if df[col].dtype == 'object' and ',' in df[col].iloc[0]:  
                geo_columns['combined'] = col
        return geo_columns

    def split_combined_column(df, combined_col):
        new_cols = df[combined_col].str.split(', ', expand=True)
        if 'county' in combined_col.lower():
            df['county'] = new_cols[0]
            df['state'] = new_cols[1]
        elif 'city' in combined_col.lower():
            df['city'] = new_cols[0]
            df['state'] = new_cols[1]
        return df

    def get_geo_id(row, level, geo_columns, zip_relations):
        if level == 'zip':
            return row[geo_columns['zip']]
        elif level == 'city':
            if 'zip' in geo_columns:
                city_state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]][['city', 'ST']].iloc[0]
                return f"{city_state['city']}, {city_state['ST']}"
            else:
                return f"{row[geo_columns['city']]}, {row[geo_columns['state']]}"
        elif level == 'county':
            if 'zip' in geo_columns:
                county_state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]][['county', 'ST']].iloc[0]
                return f"{county_state['county']}, {county_state['ST']}"
            else:
                return f"{row[geo_columns['county']]}, {row[geo_columns['state']]}"
        elif level == 'state':
            if 'zip' in geo_columns:
                state = zip_relations[zip_relations['zipcode'] == row[geo_columns['zip']]]['ST'].iloc[0]
                return state
            else:
                return row[geo_columns['state']]

    def aggregate_dataframe(df, level):
        geo_columns = detect_geo_columns(df)
        if 'combined' in geo_columns:
            df = split_combined_column(df, geo_columns['combined'])
            geo_columns = detect_geo_columns(df)

        if level not in geo_columns and 'zip' not in geo_columns:
            raise ValueError(f"The specified level '{level}' or 'zip' is not present in the DataFrame columns.")
        
        geo_id_col = 'GEO_ID'
        
        df[geo_id_col] = df.apply(lambda x: get_geo_id(x, level, geo_columns, zip_relations), axis=1)
        
        numeric_cols = df.select_dtypes(include=['number']).columns
        char_cols = df.select_dtypes(include=['object']).columns.difference(['GEO_ID', 'year'])
        
        if agg_numeric == 'mean':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].mean()
        elif agg_numeric == 'median':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].median()
        elif agg_numeric == 'mode':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].agg(lambda x: x.mode()[0])
        elif agg_numeric == 'sum':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].sum()
        elif agg_numeric == 'first':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].first()
        elif agg_numeric == 'last':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].last()
        else:
            raise ValueError("agg_numeric must be 'mean', 'median', 'mode', 'sum', 'first', or 'last'.")
        
        if agg_character == 'first':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].first()
        elif agg_character == 'last':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].last()
        elif agg_character == 'mode':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].agg(lambda x: x.mode()[0])
        else:
            raise ValueError("agg_character must be 'first', 'last', or 'mode'.")
        
        return numeric_agg.join(char_agg).reset_index()

    for df in data:
        geo_columns = detect_geo_columns(df)
        if 'combined' in geo_columns:
            df = split_combined_column(df, geo_columns['combined'])
            geo_columns = detect_geo_columns(df)
        most_granular_level = min(geo_columns.keys(), key=lambda k: level_hierarchy[k])
        if level_hierarchy[most_granular_level] > level_hierarchy[level]:
            raise ValueError(f"Cannot aggregate from {most_granular_level} to {level}. Please choose a higher level of aggregation.")
    
    aggregated_data = [aggregate_dataframe(df, level) for df in data]
    
    if len(aggregated_data) > 1:
        result = aggregated_data[0]
        for df in aggregated_data[1:]:
            result = result.merge(df, on=['GEO_ID', 'year'], how='outer', suffixes=('', '_dup'))
            # Remove duplicate columns
            for col in result.columns:
                if col.endswith('_dup'):
                    result.drop(col, axis=1, inplace=True)
        return result
    else:
        return aggregated_data[0]