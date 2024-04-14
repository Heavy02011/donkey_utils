from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show_tub_images(tub_path, n=10):
    print("tub_path: ", tub_path)
    tub = Tub(tub_path)
    fig, axes = plt.subplots(1, n, figsize=(20, 2))
    if n == 1:
        axes = [axes]
    
    for count, record in enumerate(tub):
        if count >= n:
            break
        
        img_path = record["cam/image_array"]  # Assuming this is the path
        img_path_full = tub_path + "/images/" + img_path 
        print(count, img_path_full)
        # If img_path is not an actual path, but directly the image array, skip this load step.
        img = Image.open(img_path_full)  # Load image
        img_arr = np.array(img)  # Convert image to array
        
        axes[count].imshow(img_arr)
        axes[count].axis('off')

    plt.show()

def show_tub_record_contents(tub, record_limit=10):
    """
    Prints the keys and contents from records in a given tub, excluding 'cam/image_array'.

    Args:
    - tub (Tub): Tub object loaded with the tub directory.
    - record_limit (int, optional): Number of records to process. Defaults to 10.
    """
    # Iterate over records, but limit to a certain number for brevity
    for i, record in enumerate(tub):
        if i >= record_limit:
            break
        
        # Assuming record is a dictionary-like object; adjust if it's different
        keys = list(record.keys())
        # Optionally exclude 'cam/image_array' from the list if present
        filtered_keys = [key for key in keys if key != 'cam/image_array']
        
        # Prepare the content to be displayed for each key
        content = {key: record[key] for key in filtered_keys}
        
        print(f"Record {i+1} keys and content (excluding image data): {content}")

