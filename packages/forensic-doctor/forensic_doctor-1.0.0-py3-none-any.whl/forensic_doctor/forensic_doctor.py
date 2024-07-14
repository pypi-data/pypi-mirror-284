#!/usr/bin/python3

import pytsk3
import pyewf
import os
import argparse

def open_image(image_path):
    ewf_handle = pyewf.handle()
    ewf_handle.open(image_path)
    return ewf_handle

def extract_file(filesystem, file_entry, output_path):
    with open(output_path, 'wb') as f:
        file_size = file_entry.info.meta.size
        offset = 0
        size = 1024 * 1024  # Read in chunks of 1MB
        while offset < file_size:
            available_to_read = min(size, file_size - offset)
            file_data = file_entry.read_random(offset, available_to_read)
            if not file_data:
                break
            f.write(file_data)
            offset += len(file_data)
    return output_path

def traverse_directory(filesystem, directory, output_dir):
    recovered_files = []
    for entry in directory:
        if entry.info.name.name in [b'.', b'..']:
            continue
        try:
            f_type = entry.info.meta.type
            if f_type == pytsk3.TSK_FS_META_TYPE_DIR:
                sub_directory = entry.as_directory()
                recovered_files.extend(traverse_directory(filesystem, sub_directory, output_dir))
            elif f_type == pytsk3.TSK_FS_META_TYPE_REG:
                if entry.info.meta.flags & pytsk3.TSK_FS_META_FLAG_UNALLOC:
                    file_name = entry.info.name.name.decode(errors="ignore")
                    output_path = os.path.join(output_dir, file_name)
                    recovered_file = extract_file(filesystem, entry, output_path)
                    recovered_files.append(recovered_file)
        except AttributeError:
            pass
    return recovered_files

def recover_files(image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    ewf_handle = open_image(image_path)
    img_info = pytsk3.Img_Info(ewf_handle)
    filesystem = pytsk3.FS_Info(img_info)
    root_directory = filesystem.open_dir("/")
    return traverse_directory(filesystem, root_directory, output_dir)

def recover_file(image_path, file_path, output_path):
    ewf_handle = open_image(image_path)
    img_info = pytsk3.Img_Info(ewf_handle)
    filesystem = pytsk3.FS_Info(img_info)
    file_entry = filesystem.open(file_path)
    return extract_file(filesystem, file_entry, output_path)

def main():
    parser = argparse.ArgumentParser(description="Forensic Doctor: A forensic tool for recovering deleted files from disk images.")
    subparsers = parser.add_subparsers(dest='command')

    parser_recover_path = subparsers.add_parser('--recover--path', help='Recover files from a given path in the disk image.')
    parser_recover_path.add_argument('image_path', type=str, help='Path to the disk image.')
    parser_recover_path.add_argument('input_path', type=str, help='Path in the disk image to recover from.')
    parser_recover_path.add_argument('--output', type=str, default=None, help='Output directory to save recovered files.')

    parser_recover_file = subparsers.add_parser('--recover--file', help='Recover a specific file from the disk image.')
    parser_recover_file.add_argument('image_path', type=str, help='Path to the disk image.')
    parser_recover_file.add_argument('file_path', type=str, help='Path of the file in the disk image to recover.')
    parser_recover_file.add_argument('--output', type=str, default=None, help='Output path to save the recovered file.')

    args = parser.parse_args()

    if args.command == '--recover--path':
        output_dir = args.output if args.output else args.input_path
        recovered_files = recover_files(args.image_path, output_dir)
        if recovered_files:
            for file in recovered_files:
                print(f"Recovered: {file}")
        else:
            print("No files recovered.")
    
    elif args.command == '--recover--file':
        output_path = args.output if args.output else os.path.basename(args.file_path)
        recovered_file = recover_file(args.image_path, args.file_path, output_path)
        if recovered_file:
            print(f"Recovered: {recovered_file}")
        else:
            print("File not recovered.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
                  
