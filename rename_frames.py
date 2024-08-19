# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:15:15 2024

@author: joshb
"""

import os

# Define the base directory and the range of parts
base_dir = r"C:\Users\joshb\OneDrive - University of Toronto\Documents\GitHub\cartoon-movies-stimuli\bluestreets_subtitled_frames_compressed" #adjust naming for barmaid/bluestreets
parts = [f"bluestreets_subtitled_part{num}" for num in range(1, 15)] #adjust naming for barmaid/bluestreets

# Iterate through each part directory
for part in parts:
    part_dir = os.path.join(base_dir, part)
    
    # Check if the directory exists
    if not os.path.exists(part_dir):
        print(f"Directory {part_dir} does not exist. Skipping...")
        continue
    
    # Iterate through each file in the directory
    for filename in os.listdir(part_dir):
        if filename.startswith("frame_") and filename.endswith(".jpg"):
            # Construct the new filename
            new_filename = filename.replace("frame_", "frames", 1)
            
            # Construct the full old and new file paths
            old_filepath = os.path.join(part_dir, filename)
            new_filepath = os.path.join(part_dir, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {old_filepath} to {new_filepath}")

print("Renaming completed!")
