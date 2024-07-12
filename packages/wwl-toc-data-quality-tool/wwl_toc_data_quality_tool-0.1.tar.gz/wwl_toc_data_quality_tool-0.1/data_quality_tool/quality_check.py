import os, re
import pandas as pd
import time
from datetime import datetime, timezone

def get_current_date_indicator():
    current_time_ns = time.time_ns()
    current_time_s = current_time_ns / 1_000_000_000
    current_datetime = datetime.fromtimestamp(current_time_s, tz=timezone.utc)
    return current_datetime.strftime('%Y-%m-%d')

# Function to add or update an entry in the log
def add_log_entry(log_df, variable, MISSING='/', DTYPE_WRONG='/', data_type='/', 
                  type_standards='/', VALUE_WRONG='/', values='/', value_standards='/'):
    if variable in log_df['variable'].values:
        idx = log_df.index[log_df['variable'] == variable].tolist()[0]
        log_df.at[idx, 'MISSING'] = MISSING if MISSING != '/' else log_df.at[idx, 'MISSING']
        log_df.at[idx, 'DTYPE_WRONG'] = DTYPE_WRONG if DTYPE_WRONG != '/' else log_df.at[idx, 'DTYPE_WRONG']
        log_df.at[idx, 'data_type'] = data_type if data_type != '/' else log_df.at[idx, 'data_type']
        log_df.at[idx, 'type_standards'] = type_standards if type_standards != '/' else log_df.at[idx, 'type_standards']
        log_df.at[idx, 'VALUE_WRONG'] = VALUE_WRONG if VALUE_WRONG != '/' else log_df.at[idx, 'VALUE_WRONG']
        log_df.at[idx, 'values'] = values if values != '/' else log_df.at[idx, 'values']
        log_df.at[idx, 'value_standards'] = value_standards if value_standards != '/' else log_df.at[idx, 'value_standards']
    else:
        log_df.loc[len(log_df)] = [variable, MISSING, DTYPE_WRONG, data_type, 
                                   type_standards, VALUE_WRONG, values, value_standards]

# Function to analyze and export analysis log
def check_and_export(standard_df_path, data_folder_path, log_file_path):
    # Load data standards
    standard_df   = pd.read_csv(standard_df_path)

    # Define folder path and Load new data
    all_files = [os.path.join(data_folder_path, f) for f in os.listdir(data_folder_path) if f.endswith('.csv')]
    print(all_files)
    
    new_data_df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    new_data_df.columns = new_data_df.columns.str.strip()

    # Columns to check for value mismatches
    value_check_columns = ['local_time', 'chassis_mode', 'task_stage', 'current_task', 
                        'target_location', 'mission_type', 'container1_type', 
                        'container2_type', 'vehicle_mode', 'lane_change_state']

    # Initialize the log DataFrame
    log_df = pd.DataFrame(columns=['variable', 'MISSING', 'DTYPE_WRONG', 
                                'data_type', 'type_standards', 'VALUE_WRONG', 
                                'values', 'value_standards'])

    # Check for each column in the standards file
    for column in standard_df['Variable Name']:
        MISSING = '/'
        DTYPE_WRONG = '/'
        data_type = ''
        type_standards = ''
        VALUE_WRONG = '/'
        values = ''
        value_standards = ''

        # Check if column is missing
        if column not in new_data_df:
            MISSING = 'YES'
        else:
            column_type = new_data_df[column].dtype
            expected_type = standard_df.loc[standard_df['Variable Name'] == column, 'Data Type'].values[0]
            
            # Check for type mismatch
            if (column_type == 'object' and expected_type != 'object') or \
            (column_type == 'int64' and expected_type != 'int64') or \
            (column_type == 'float64' and expected_type != 'float64'):
                DTYPE_WRONG = 'YES'
                data_type = str(column_type)
                type_standards = expected_type

            # Check for each column
            if column in value_check_columns:

                # Check for datetime format in 'local_time'
                if column == 'local_time':
                    datetime_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
                    VALUE_WRONG_flag = False
                    for value in new_data_df[column]:
                        if not datetime_pattern.match(str(value).strip()):
                            VALUE_WRONG_flag = True
                            break
                    if VALUE_WRONG_flag:
                        VALUE_WRONG = 'YES'
                
                # Process int columns
                elif column_type == 'int64':
                    sample_values = standard_df.loc[standard_df['Variable Name'] == column, 'Sample Values'].values[0].split(',')
                    sample_values = [int(v) for v in sample_values]  # Convert sample values to int
                    VALUE_WRONG_flag = False
                    for value in new_data_df[column].dropna().unique():
                        if value not in sample_values:
                            VALUE_WRONG_flag = True
                            break
                    if VALUE_WRONG_flag:
                        VALUE_WRONG = 'YES'
                        values = ', '.join(map(str, new_data_df[column].dropna().unique()))
                        value_standards = ', '.join(map(str, sample_values))
                            
                # Process float columns
                elif column_type == 'float64':
                    sample_values = standard_df.loc[standard_df['Variable Name'] == column, 'Sample Values'].values[0].split(',')
                    sample_values = [float(v) for v in sample_values]  # Convert sample values to float
                    VALUE_WRONG_flag = False
                    for value in new_data_df[column].dropna().unique():
                        if value not in sample_values:
                            VALUE_WRONG_flag = True
                            break
                    if VALUE_WRONG_flag:
                        VALUE_WRONG = 'YES'
                        values = ', '.join(map(str, new_data_df[column].dropna().unique()))
                        value_standards = ', '.join(map(str, sample_values))


                # Process object columns
                elif column_type == 'object':
                    sample_values = standard_df.loc[standard_df['Variable Name'] == column, 'Sample Values'].values[0].split(',')
                    VALUE_WRONG_flag = False
                    for value in new_data_df[column].dropna().unique():
                        value = str(value).strip()  # Strip leading/trailing spaces
                        if value not in sample_values:
                            VALUE_WRONG_flag = True
                            break
                    if VALUE_WRONG_flag:
                        VALUE_WRONG = 'YES'
                        values = ', '.join(new_data_df[column].dropna().unique())
                        value_standards = ', '.join(sample_values)
        
        # Add or update the log entry
        if MISSING == 'YES' or DTYPE_WRONG == 'YES' or VALUE_WRONG == 'YES':
            add_log_entry(log_df, variable=column, MISSING=MISSING, DTYPE_WRONG=DTYPE_WRONG, 
                            data_type=data_type, type_standards=type_standards, VALUE_WRONG=VALUE_WRONG, 
                            values=values, value_standards=value_standards)

    # Save log to a CSV file
    log_df.to_csv(log_file_path, index=False)

    print(f"Log file generated: {log_file_path}")
