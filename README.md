Caltech Pedestrian Dataset Converter
============================

# Original
This is forked from https://github.com/mitmul/caltech-pedestrian-dataset-converter. I couldn't read *.seq files with the original in my environment, so I merged another source(https://gist.github.com/psycharo/7e6422a491d93e1e3219/) to the original.

# Requirements

- OpenCV 3.0+ (with Python binding)
- Python 2.7+, 3.4+, 3.5+
- NumPy 1.10+
- SciPy 0.16+

# Caltech Pedestrian Dataset

```
$ bash shells/download.sh
$ python scripts/convert_annotations.py
$ python scripts/convert_seqs.py
```

Each `.seq` movie is separated into `.png` images. Each image's filename is consisted of `{set**}_{V***}_{frame_num}.png`. According to [the official site](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/), `set06`~`set10` are for test dataset, while the rest are for training dataset.

(Number of objects: 346621)

# Draw Bounding Boxes

```
$ python tests/test_plot_annotations.py
```
