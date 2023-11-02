# Thrive-Rename-Json

Thrive-Rename-Json is a tool designed to format the JSON files in the open-source project "Thrive" by Revolutionary Games. It specifically focuses on capitalizing the first letter in property names, converting camelCase to PascalCase, while avoiding variables that might break the current codebase. This project is released under the Apache License.

## Installation

To use Thrive-Rename-Json, follow these installation steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Thrive-Rename-Json.git
   cd Thrive-Rename-Json
   ```

## Usage
To use Thrive-Rename-Json, open a command line and run the thrive_rename_json.py script with 1 or 2 arguments:

1. If only 1 argument is provided, it will reformat all the JSON files in the directory specified in argument 1.

`python thrive_rename_json.py /path/to/directory`

2. If two arguments are provided, and they make up a complete file path, it will either reformat the specified file or take no action if the file does not match the criteria.

`python thrive_rename_json.py /first/part/of/path /rest/of/path`

This feature is useful if you have variables stored instead of paths, as it allows you to specify a single file to format.

## License
This project is licensed under the Apache License, meaning you are free to use, modify, and distribute the code, provided you comply with the terms of the license.

## Acknowledgments
This project is created to contribute to the "Thrive" open-source project by Revolutionary Games. Thanks to the Thrive community for the opportunity to make code improvements.

## Support
If you encounter any issues or have questions, please feel free to open an issue.

Happy formatting!
