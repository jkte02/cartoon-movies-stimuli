# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """Compress the image and save it to the output path."""
    with Image.open(input_path) as img:
        img.save(output_path, format='JPEG', quality=quality)

def compress_images_in_directory(input_dir, output_dir, quality=85):
    """Recursively compress all PNG images in the directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.png'):
                input_path = os.path.join(root, file)
                # Create corresponding output path
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                output_dirname = os.path.dirname(output_path)
                
                if not os.path.exists(output_dirname):
                    os.makedirs(output_dirname)

                # Compress and save the image
                compress_image(input_path, output_path.replace('.png', '.jpg'), quality)

# Define the input and output directories
input_directory = r"C:\Users\joshb\OneDrive - University of Toronto\Desktop\UofT (PhD)\FRP\Cartoon Movies Stimuli\barmaid_subtitled_frames_18fps" #replace naming with appropriate directory
output_directory = r"C:\Users\joshb\OneDrive - University of Toronto\Documents\GitHub\cartoon-movies-stimuli\barmaid_subtitled_frames_compressed_18fps" #replace naming with appropriate directory

# Compress the images
compress_images_in_directory(input_directory, output_directory, quality=85)
