import argparse
import os
import subprocess

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Process GoPro videos")

    parser.add_argument("-i", "--input", type=Path,
                        required=True, help="Path to input folder")
    parser.add_argument("-o", "--output", type=Path,
                        required=True, help="Path to output folder")
    args = parser.parse_args()

    input_path: Path = args.input
    output_path: Path = args.output

    if not output_path.exists():
        output_path.mkdir(exist_ok=True)

    files = [f for f in os.listdir(input_path) if ".mp4" in f.lower()]

    videoclips = {}
    for f in files:
        name = f[4:].split(".")[0]
        if name not in videoclips:
            videoclips[name] = []
        videoclips[name].append(f)

    for name, files in videoclips.items():
        print(f"Processing {name} with files {files}")
        list_file_name = "list.txt"
        with open(list_file_name, "w") as f:
            f.write("\n".join(
                [f"file '{input_path / file_name}'" for file_name in files]
            ))
        subprocess.run([
            "ffmpeg", "-f", "concat", "-safe", "0", "-i", list_file_name, "-c", "copy", output_path / (name + ".mp4")
        ])
        os.remove(list_file_name)


if __name__ == "__main__":
    main()
