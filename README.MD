# Range-Downloader

Downloader for resources that are stored in a numeric sequence. 
###### External dependency: requests (https://pypi.org/project/requests/)

## Project setup

#### Install dependency

```
pip install requests
```
#### Usage:

```
$ python main.py <base_url> <file_extension> <start_index (integer)> <end_index (integer)> <optional: string to append to filenames> <optional: index_to_skip_1 (integer)> <optional: index_to_skip_2 (integer)> ...
```

#### Example

```
$ python main.py https://Something-I-Want-To-Download/this png 1 5 test 3 4
```

Downloads:

```
https://Something-I-Want-To-Download.com/this1.jpg
https://Something-I-Want-To-Download.com/this2.jpg
https://Something-I-Want-To-Download.com/this5.jpg
```

Saved files:

```
% Project_Root % / Downloads / this / this1-test.png
% Project_Root % / Downloads / this / this2-test.png
% Project_Root % / Downloads / this / this5-test.png
% Project_Root % / Downloads / this / download.log
```
