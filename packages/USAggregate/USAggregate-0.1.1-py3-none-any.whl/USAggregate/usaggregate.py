import csv
import os

def read_zipcodes_csv(filepath):
    zip_dict = {}
    with open(filepath, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            zip_dict[row['zipcode']] = {
                'city': row['city'],
                'county': row['county'],
                'state': row['ST']
            }
    return zip_dict

def detect_geo_columns(data):
    geo_columns = {}
    for i, df in enumerate(data):
        for col in df[0].keys():
            if 'zip' in col.lower():
                geo_columns[i] = 'zip'
            if 'city' in col.lower():
                geo_columns[i] = 'city'
            if 'state' in col.lower():
                geo_columns[i] = 'state'
            if 'county' in col.lower():
                geo_columns[i] = 'county'
    return geo_columns

def aggregate_to_level(data, geo_columns, level, zip_dict, agg_numeric='mean', agg_character='first'):
    level_hierarchy = {'zip': 0, 'city': 1, 'county': 2, 'state': 3}
    
    def aggregate(data, geo_col, level):
        aggregated_data = {}
        for row in data:
            geo_id = row[geo_col]
            if geo_col == 'zip' and level == 'city':
                geo_id = f"{zip_dict[geo_id]['city']}, {zip_dict[geo_id]['state']}"
            elif geo_col == 'zip' and level == 'county':
                geo_id = f"{zip_dict[geo_id]['county']}, {zip_dict[geo_id]['state']}"
            elif geo_col == 'zip' and level == 'state':
                geo_id = zip_dict[geo_id]['state']
            elif geo_col == 'city' and level == 'state':
                geo_id = row['state']
            elif geo_col == 'county' and level == 'state':
                geo_id = row['state']
            else:
                geo_id = row[geo_col]

            if geo_id not in aggregated_data:
                aggregated_data[geo_id] = {}
                for key in row:
                    if key not in [geo_col, 'year']:
                        if key not in aggregated_data[geo_id]:
                            aggregated_data[geo_id][key] = [row[key]]
                        else:
                            aggregated_data[geo_id][key].append(row[key])
                aggregated_data[geo_id]['year'] = row['year']
            else:
                for key in row:
                    if key not in [geo_col, 'year']:
                        aggregated_data[geo_id][key].append(row[key])

        for geo_id in aggregated_data:
            for key in aggregated_data[geo_id]:
                if key != 'year':
                    if isinstance(aggregated_data[geo_id][key][0], (int, float)):
                        if agg_numeric == 'mean':
                            aggregated_data[geo_id][key] = sum(aggregated_data[geo_id][key]) / len(aggregated_data[geo_id][key])
                        elif agg_numeric == 'sum':
                            aggregated_data[geo_id][key] = sum(aggregated_data[geo_id][key])
                        elif agg_numeric == 'first':
                            aggregated_data[geo_id][key] = aggregated_data[geo_id][key][0]
                        elif agg_numeric == 'last':
                            aggregated_data[geo_id][key] = aggregated_data[geo_id][key][-1]
                    else:
                        if agg_character == 'first':
                            aggregated_data[geo_id][key] = aggregated_data[geo_id][key][0]
                        elif agg_character == 'last':
                            aggregated_data[geo_id][key] = aggregated_data[geo_id][key][-1]

        return aggregated_data

    aggregated_data_frames = []
    for i, df in enumerate(data):
        geo_col = geo_columns[i]
        if level_hierarchy[geo_col] <= level_hierarchy[level]:
            aggregated_data = aggregate(df, geo_col, level)
            aggregated_data_frames.append(aggregated_data)
        else:
            raise ValueError(f"Cannot aggregate from {geo_col} to {level}. Please choose a higher level of aggregation.")
    
    return aggregated_data_frames

def merge_aggregated_data(data_frames):
    merged_data = {}
    for data in data_frames:
        for geo_id, values in data.items():
            if geo_id not in merged_data:
                merged_data[geo_id] = values
            else:
                for key, value in values.items():
                    if key in merged_data[geo_id] and key != 'year':
                        merged_data[geo_id][key + '_dup'] = value
                    else:
                        merged_data[geo_id][key] = value
    return merged_data

def usaggregate(data, level, agg_numeric='mean', agg_character='first'):
    zipcodes_path = os.path.join(os.path.dirname(__file__), 'data', 'zipcodes.csv')
    zip_dict = read_zipcodes_csv(zipcodes_path)
    geo_columns = detect_geo_columns(data)
    aggregated_data_frames = aggregate_to_level(data, geo_columns, level, zip_dict, agg_numeric, agg_character)
    merged_data = merge_aggregated_data(aggregated_data_frames)
    return merged_data