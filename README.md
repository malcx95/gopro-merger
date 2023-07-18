# GoPro video merger

Isn't it annoying how a GoPro splits up large videos into several files? This script merges
the split clips in a folder of GoPro footage into their full lengths. Requires Python and `ffmpeg` installed. Only tested on Linux.

## Usage

Given a folder of GoPro footage (with original names) run

```
python gopro.py -i <input folder> -o <output folder>
```

The merged videos will be saved in `<output folder>`.
