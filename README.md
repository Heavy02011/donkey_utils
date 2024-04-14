# Donkey Utils

`donkey_utils` is a Python library designed to simplify the handling and processing of data for DonkeyCar projects. It provides a set of tools for file extraction, directory management, image processing, and data manipulation.

## Features

- **File Extraction**: Functions to extract ZIP, GZ, and TAR.GZ files.
- **Directory Management**: Utilities to change and verify the current working directory.
- **Image Processing**: Tools to display images and manage image data.
- **Data Handling**: Functions to convert data into structured formats like pandas DataFrames.

## Installation

You can install `donkey_utils` directly from PyPI:

```bash
xxx pip install donkey_utils
```

To install from source, clone the repository and use the setup file:

```bash
git clone https://github.com/yourusername/donkey_utils.git
cd donkey_utils
python setup.py install
```

## Usage

Here are some quick examples of what you can do with `donkey_utils`:

### Extract Files

```python
from donkey_utils.extraction import extract_all_zips
extract_all_zips('/path/to/source', '/path/to/destination')
```

### Change Working Directory

```python
from donkey_utils.file_management import setdir
setdir('/new/directory/path')
```

### Display Images

```python
from donkey_utils.image_processing import display_images_from_df
import pandas as pd

df = pd.DataFrame({
    'image_file_name': ['path/to/image1.jpg', 'path/to/image2.jpg']
})
display_images_from_df(df, 'image_file_name', 5)
```

### Convert Tub Data to DataFrame

```python
from donkey_utils.dataframe_utilities import tub_to_dataframe
df = tub_to_dataframe('/path/to/tub')
```

## Contributing

We welcome contributions from the community. Here are some ways you can contribute:

- Submit bugs and feature requests.
- Review code and improve documentation.
- Submit pull requests with new features and bug fixes.

## License

`donkey_utils` is made available under the MIT License. For more details, see the LICENSE file in the repository.

## Support

If you have any questions or need help, please open an issue on the GitHub repository.

Thank you for using or contributing to `donkey_utils`!
