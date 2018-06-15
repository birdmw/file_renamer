import argparse
import os
import shutil


def copytree(src, dst, append, symlinks=False, ignore=None):
    for item in os.listdir(src):
        item_split = item.split('.')
        item_split[0] += str(append)
        item_renamed = ".".join(item_split)
        print(os.path.join(src, item))
        print("=====")
        s = os.path.join(src, item)
        d = os.path.join(dst, item_renamed)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input directory")
    parser.add_argument("output", help="output directory")
    parser.add_argument("append", help="what to append to filename")
    args = parser.parse_args()
    src_dir = args.input
    dst_dir = args.output
    append = args.append
    copytree(src_dir, dst_dir, append)