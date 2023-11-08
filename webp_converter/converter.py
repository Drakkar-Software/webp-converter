import os
import subprocess

IMAGES_EXT = [".png", ".jpg", ".jpeg"]
CONVERTOR_BIN = "cwebp"
OPTIONS = ["-lossless", "-exact"]


def get_output_file_name(entry):
    return f"{os.path.splitext(entry.name)[0]}.webp"


def get_command(entry, output):
    return [CONVERTOR_BIN] + OPTIONS + [entry.name, "-o", output]


def convert_image(entry):
    output = get_output_file_name(entry)
    if not os.path.exists(output):
        print(f"converting {entry.name} into {output}")
        subprocess.call(get_command(entry, output))


def convert_if_image(entry):
    lower_file_name = entry.name.lower()
    if any(lower_file_name.endswith(ext) for ext in IMAGES_EXT):
        convert_image(entry)


def explore_dir(dir_path):
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            try:
                os.chdir(entry)
                print(f"exploring {os.getcwd()}")
                explore_dir(".")
            finally:
                os.chdir("..")
                print(f"back to {os.getcwd()}")
        else:
            convert_if_image(entry)


if __name__ == '__main__':
    explore_dir(".")
