# Data Quality Tool

## Overview

The Data Quality Tool is designed to help you check and ensure the quality of your data by comparing it against defined standards. It can also generate a data value standard file based on manual input or from a CSV data file.

## Features

- **Check and Export Data Quality Log:**
  - Checks for missing variables
  - Checks for value mismatches based on defined standards
- **Generate Data Value Standard File:**
  - Generate from manual input
  - Generate from an existing CSV data file

## Installation

To install this package, ensure you have `pip` version 24:

```bash
# Upgrade pip to version 24
pip install --upgrade pip==24
```

Then install the package:

```
pip install data-standards-check
```

## Usage

1. Put all the data in one folder, make sure the standard file is named as `data_standards.csv` if it's predefined
2. Run the tool in sh
3. The analysis log will be automatically generated under the new data folder

```sh
# Check data quality and export log
data_check check <data_folder_path>

# Generate data value standard file
data_check generate <data_folder> [--input_file <input_file>]
```