# Data Quality Tool

A Python tool to check data quality against predefined standards.

## Installation

To install this package, ensure you have `pip` version 24:

```bash
# Upgrade pip to version 24
pip install --upgrade pip==24
```

# Then install the package
```
pip install toc_quality_check
```

1. Clone the repository.
2. Navigate to the project directory.
3. Install the package:

```sh
pip install .
```

## Usage

1. Put your data standards csv file and data folder with new data under the project dir
2. Run the tool
3. The analysis log will be automatically generated under the new data folder

```sh
quality_check <standard_df_path> <data_folder_path>
```

<standard_df_path>: Path to the data standards CSV file.

<data_folder_path>: Path to the folder containing data files to check.