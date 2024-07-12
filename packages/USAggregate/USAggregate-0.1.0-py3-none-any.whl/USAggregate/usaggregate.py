import pandas as pd
from uszipcode import SearchEngine
from us import states

def usaggregate(data, level, merge_numeric='mean', merge_character='first'):
    """
    Aggregate and merge multiple pandas DataFrames based on a specified geographic level and year.

    Parameters:
    data (list of pd.DataFrame): List of pandas DataFrames to aggregate and merge.
    level (str): Geographic level for aggregation ('zip', 'city', 'county', 'state').
    merge_numeric (str): Method to aggregate numeric data ('mean', 'median', 'mode').
    merge_character (str): Method to aggregate character data ('first', 'last', 'mode').

    Returns:
    pd.DataFrame: Aggregated and merged DataFrame.
    """

    if not isinstance(data, list) or len(data) < 1:
        raise ValueError("Data must be a list of one or more pandas DataFrames.")
    
    # Define supported geographic levels and their hierarchy
    supported_levels = ['zip', 'city', 'county', 'state']
    if level not in supported_levels:
        raise ValueError(f"Level must be one of {supported_levels}.")
    
    # Define level hierarchy for validation
    level_hierarchy = {'zip': 0, 'city': 1, 'county': 2, 'state': 3}

    def detect_geo_columns(df):
        """
        Detect geographic columns in the DataFrame.

        Parameters:
        df (pd.DataFrame): DataFrame to detect geographic columns in.

        Returns:
        dict: Mapping of geographic levels to detected column names.
        """
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
    
    def get_geo_id(row, level, geo_columns):
        """
        Generate a geographic identifier based on the specified level.

        Parameters:
        row (pd.Series): A row of the DataFrame.
        level (str): Geographic level for the identifier.
        geo_columns (dict): Mapping of geographic levels to column names.

        Returns:
        str: Geographic identifier.
        """
        if level == 'zip':
            return row[geo_columns['zip']]
        elif level == 'city':
            return f"{row[geo_columns['city']]}, {row[geo_columns['state']]}"
        elif level == 'county':
            return f"{row[geo_columns['county']]}, {row[geo_columns['state']]}"
        elif level == 'state':
            return row[geo_columns['state']]
    
    def aggregate_dataframe(df, level):
        """
        Aggregate a single DataFrame based on the specified geographic level.

        Parameters:
        df (pd.DataFrame): DataFrame to aggregate.
        level (str): Geographic level for aggregation.

        Returns:
        pd.DataFrame: Aggregated DataFrame.
        """
        geo_columns = detect_geo_columns(df)
        if level not in geo_columns:
            raise ValueError(f"The specified level '{level}' is not present in the DataFrame columns.")
        
        geo_id_col = 'GEO_ID'
        
        # Create GEO_ID column based on the specified level
        df[geo_id_col] = df.apply(lambda x: get_geo_id(x, level, geo_columns), axis=1)
        
        # Select numeric and character columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        char_cols = df.select_dtypes(include=['object']).columns.difference(['GEO_ID', 'year'])
        
        # Aggregate numeric columns
        if merge_numeric == 'mean':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].mean()
        elif merge_numeric == 'median':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].median()
        elif merge_numeric == 'mode':
            numeric_agg = df.groupby([geo_id_col, 'year'])[numeric_cols].agg(lambda x: x.mode()[0])
        else:
            raise ValueError("merge_numeric must be 'mean', 'median', or 'mode'.")
        
        # Aggregate character columns
        if merge_character == 'first':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].first()
        elif merge_character == 'last':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].last()
        elif merge_character == 'mode':
            char_agg = df.groupby([geo_id_col, 'year'])[char_cols].agg(lambda x: x.mode()[0])
        else:
            raise ValueError("merge_character must be 'first', 'last', or 'mode'.")
        
        # Join numeric and character aggregations and reset index
        return numeric_agg.join(char_agg).reset_index()
    
    # Validate that all dataframes can be aggregated to the specified level
    for df in data:
        geo_columns = detect_geo_columns(df)
        most_granular_level = min(geo_columns.keys(), key=lambda k: level_hierarchy[k])
        if level_hierarchy[most_granular_level] > level_hierarchy[level]:
            raise ValueError(f"Cannot aggregate from {most_granular_level} to {level}. Please choose a higher level of aggregation.")
    
    # Aggregate each DataFrame in the list
    aggregated_data = [aggregate_dataframe(df, level) for df in data]
    
    # Merge all aggregated DataFrames on GEO_ID and year
    if len(aggregated_data) > 1:
        result = aggregated_data[0]
        for df in aggregated_data[1:]:
            result = result.merge(df, on=['GEO_ID', 'year'], how='outer')
        return result
    else:
        return aggregated_data[0]