# Range-Downloader

Downloader for files/resources that are stored in a numeric sequence

## Project setup

Install dependency

```
pip install requests
```

### Usage:

```
$ python src/main.py <start_index (integer)> <end_index (integer)> <base_url> <extension> <index_to_skip_1> <index_to_skip_2> <index_to_skip_3> ...
```

### Example

```
$ python src/main.py 1 5 https://Something-I-Want-To-Download/this png 3 4
```

Downloads:
```
% Project_Root % / Downloads / this / this1.png
% Project_Root % / Downloads / this / this2.png
% Project_Root % / Downloads / this / this5.png
```
