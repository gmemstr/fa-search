Basic python script for easily searching FontAwesome icons locally.

Might support tagging and whatnot in the future, currently does simple array text search.

## Usage

To update the fa-icons.json file, download [the latest css file](https://use.fontawesome.com/releases/v5.3.1/css/all.css)
and run `python3 convert.py`.

To search, run `python3 search.py <keyword>` - if you omit the keyword it will prompt you to enter one.

Sample output:

```bash
➜  fa-search git:(master) ✗ ./search.py github
fa fa-github
fa fa-github-alt
fa fa-github-square
➜  fa-search git:(master) ✗ 
```