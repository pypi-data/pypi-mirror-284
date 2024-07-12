# Puddle
A simple python package to translate png files to puddle files. Puddle files are a simple way to read and encode images, there is no real use case for this, this project is more of learning tool of how to create python packages.

## Installation

To install Puddle, first download the repository:
```bash
git clone https://github.com/jn202871/puddle
```
Then use pip to install the package:
```bash
cd puddle
pip install .
```

## Usage

To use puddle to convert files between png and puddle file types:
```bash
puddle convert example.png # For png to puddle
puddle convert example.puddle # For puddle to png
```

To view puddle files use:
```bash
puddle view example.puddle
```

## License
This project is licensed under the MIT License.