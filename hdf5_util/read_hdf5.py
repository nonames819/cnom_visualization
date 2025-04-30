"""
Script to read HDF5 file and save datasets as numpy arrays.

Example usage as a script:
    python read_hdf5.py --input_path /path/to/input.hdf5 --output_dir /path/to/output

Example usage as a module:
    from read_hdf5 import print_hdf5_shape
    print_hdf5_shape(
        input_path='/path/to/input.hdf5',
        output_dir='/path/to/output'
    )
"""

import h5py
import os
import numpy as np
import argparse
import json


def print_hdf5_shape(
    input_path=None,
    output_dir=None
):
    """
    Read HDF5 file and save structure information to a text file.
    
    Args:
        input_path (str): Path to the input HDF5 file
        output_dir (str): Directory to save the structure information
        
    Returns:
        None
    """
    # Ensure output directory exists
    assert input_path is not None, "Input path must be provided"
    assert output_dir is not None, "Output directory must be provided"
    
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "hdf5_structure.txt")

    with open(output_file, 'w') as f:
        def write_structure(root, node):
            """Recursively write HDF5 structure"""
            if isinstance(node, h5py.Group):
                f.write(f"{root} - Group\n")
                for key in node.keys():
                    write_structure(f"{root}/{key}", node[key])
            elif isinstance(node, h5py.Dataset):
                f.write(f"{root} - Dataset, Shape: {node.shape}, Type: {node.dtype}\n")

        with h5py.File(input_path, 'r') as hf:
            f.write(f"HDF5 File: {input_path}\n")
            f.write("=" * 50 + "\n")
            write_structure('', hf)

def print_hdf5_shape_json(
    input_path=None,
    output_dir=None
):
    """
    Read HDF5 file and save shape information of all datasets.
    
    Args:
        input_path (str): Path to the input HDF5 file
        output_dir (str): Directory to save the shape information
        
    Returns:
        None
    """
    assert input_path is not None, "Input path must be provided"
    assert output_dir is not None, "Output directory must be provided"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create dictionary to store shape information
    shape_info = {
        "input_file": input_path,
        "shapes": {}
    }

    # Read HDF5 file
    with h5py.File(input_path, 'r') as f:
        def collect_shapes(name, obj):
            if isinstance(obj, h5py.Dataset):
                shape_info["shapes"][name] = list(obj.shape)
        
        f.visititems(collect_shapes)
    
    # Save shape information to JSON file
    info_path = os.path.join(output_dir, "dataset_shapes.json")
    with open(info_path, 'w') as f:
        json.dump(shape_info, f, indent=4)
    print(f"Shape information saved to {info_path}")


def main():
    """Parse command line arguments and call print_hdf5_shape function"""
    parser = argparse.ArgumentParser(description='Read HDF5 file and save datasets as numpy arrays')
    parser.add_argument('--input_path', type=str, 
                       default="/data/chd_data/awe_data/robomimic/datasets/square/ph/image.hdf5",
                       help='Path to input HDF5 file')
    parser.add_argument('--output_dir', type=str,
                       default="/data/chd_data/my_lib/cnom_visualization/output",
                       help='Directory to save output numpy arrays')
    
    args = parser.parse_args()
    print_hdf5_shape(args.input_path, args.output_dir)

if __name__ == "__main__":
    main()