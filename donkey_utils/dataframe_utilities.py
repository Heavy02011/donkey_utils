import pandas as pd
from donkeycar.parts.tub_v2 import Tub

def tub_to_dataframe(tub_path):
    """
    Reads a tub and its records into a pandas DataFrame, including image file names.

    Args:
    - tub_path (str): Path to the tub directory.

    Returns:
    - DataFrame: Pandas DataFrame containing the tub records.
    """
    # Load the tub
    tub = Tub(tub_path)
    
    # Initialize a list to hold each record's data
    data = []
    
    # Iterate over each record in the tub
    for record in tub:
        # Extract data from the record. Adjust keys as necessary for your tub structure.
        # Here, we assume 'cam/image_array' holds the image file name and we extract other desired keys
        record_data = {
            'image_file_name': record['cam/image_array'],  # Assuming this holds the image path or name
        }
        
        # Optionally add other data from the record
        for key in record.keys():
            if key != 'cam/image_array':  # Skip the image data if it's large or binary
                record_data[key] = record[key]
        
        data.append(record_data)
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    
    return df

def tub2pd(tub):
    """
    Converts a DonkeyCar tub into a pandas DataFrame.

    Each record in the tub is transformed into a row in the DataFrame, including image file names and other data.
    Missing values are removed by dropping rows with any NaN values after the conversion.

    Args:
    - tub_path (str): The file system path to the tub directory.

    Returns:
    - pandas.DataFrame: A DataFrame where each row represents a tub record. Columns correspond to the keys in the tub records,
      including 'image_file_name' for the path or name of the image file in each record.

    Note:
    This function assumes the tub records are dictionaries with consistent keys across records. The 'cam/image_array'
    key is expected to contain the image file name or a path to the image. If the structure of your tub data differs,
    adjustments to the function may be necessary.
    """
    df = pd.DataFrame(tub).dropna()
    return df

import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

def display_images_from_df(df, image_column='image_file_name', n=5, tub_path=None):
    """
    Displays a specified number of images from a pandas DataFrame containing image file names.
    
    Args:
    - df (pandas.DataFrame): The DataFrame containing image file names.
    - image_column (str): The column name in df that contains the image file names. Defaults to 'image_file_name'.
    - n (int): The number of images to display. Defaults to 5.
    - image_dir (str, optional): The directory path where images are stored if not specified in df.
      If None, paths in df are assumed to be absolute. Defaults to None.
    """
    # Iterate through the DataFrame up to n rows
    for i, row in df.head(n).iterrows():
        # Get image path; prepend with image_dir if necessary
        image_path = row[image_column] if tub_path is None else os.path.join(tub_path+"/images/", row[image_column])
        
        # Load and display the image
        try:
            image = Image.open(image_path)
            plt.figure(figsize=(5, 5))
            plt.imshow(image)
            plt.axis('off')
            plt.show()
        except FileNotFoundError:
            print(f"Image not found: {image_path}")

# Example usage assuming df2 is your DataFrame and it includes an 'image_file_name' column
# If the image paths are not absolute, specify the image_dir parameter
# display_images_from_df(df2, image_column='image_file_name', n=5, image_dir='/path/to/images')

import pandas as pd

def sample_dataframe(df, n):
    """
    Selects a random sample of size n from a DataFrame and returns it as a new DataFrame.

    Args:
    - df (pandas.DataFrame): The original DataFrame to sample from.
    - n (int): The number of rows to randomly sample from the DataFrame.

    Returns:
    - pandas.DataFrame: A new DataFrame containing the randomly sampled rows.
    """
    # Ensure n does not exceed the number of rows in df
    n = min(n, len(df))
    
    # Use the sample method to select n random rows
    sample_df = df.sample(n=n)
    
    return sample_df

import pandas as pd

import pandas as pd

# The function remains the same as provided previously

def flatten_row_to_string(df, row_index, separator=', '):
    """
    Flatten a specific row of a Pandas DataFrame into a string.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - row_index (int): The index of the row to flatten.
    - separator (str): The separator used between key-value pairs in the output string.

    Returns:
    - str: The flattened row as a string.
    """
    if row_index not in df.index:
        return "Row index out of range."
    
    row_dict = df.iloc[row_index].to_dict()
    flattened_string = separator.join(f"{key}={value}" for key, value in row_dict.items())
    
    return flattened_string

# Make sure the row_index is within the range of the DataFrame's index
##row_index = 0  # for example, choosing the first row, which is valid
#if row_index in df.index:
#    flattened_row_string = flatten_row_to_string(df, row_index)
#    print(flattened_row_string)
#else:
#    print(f"Row index {row_index} out of range.")

# Example usage
#data = {
#    'Name': ['John', 'Anna'],
#    'Age': [30, 25],
#    'City': ['New York', 'Paris']
#}
#df = pd.DataFrame(data)

#flattened_row_string = flatten_row_to_string(df, 0)
#print(flattened_row_string)


# Example usage
# Assuming df is your original DataFrame
# df_sampled = sample_dataframe(df, n=5)
# print(df_sampled)


# Example usage
#tub_path = '/path/to/your/tub'  # Replace with the actual path to your tub
#df = tub_to_dataframe(tub_path)
#print(df.head())  # Show the first few records to verify
        
# Example usage
# Assuming 'tub' is a Tub object already loaded with tub data
# show_tub_record_contents(tub, record_limit=10)

# Example usage
#tub_path = '/path/to/your/tub'  # Replace with the actual path to your tub
#show_tub_record_keys(tub_path, record_limit=10)


###s##
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show_tub_images(tub_path, n=10):
    pass  # Placeholder for actual implementation

def display_images_from_df(df, image_column='image_file_name', n=5, tub_path=None):
    pass  # Placeholder for actual implementation


####
import pandas as pd
from donkeycar.parts.tub_v2 import Tub

def tub_to_dataframe(tub_path):
    pass  # Placeholder for actual implementation

def tub2pd(tub):
    pass  # Placeholder for actual implementation

def sample_dataframe(df, n):
    pass  # Placeholder for actual implementation

def flatten_row_to_string(df, row_index, separator=', '):
    pass  # Placeholder for actual implementation
