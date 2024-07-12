import os
import sys
from data_quality_tool.quality_check import get_current_date_indicator, check_and_export

def main():
    if len(sys.argv) != 3:
        print("Usage: quality_check <standard_df_path> <data_folder_path>")
        sys.exit(1)
    
    standard_df_path = sys.argv[1]
    data_folder_path = sys.argv[2]
    date_indicator = get_current_date_indicator()
    log_file_path = os.path.join(data_folder_path, f'check_log_{date_indicator}.csv')
    
    check_and_export(standard_df_path, data_folder_path, log_file_path)

if __name__ == '__main__':
    main()
