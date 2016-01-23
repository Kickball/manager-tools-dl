# manager-tools-dl

manager-tools-dl allows you to download the podcasts available on [manager-tools.com](https://www.manager-tools.com/).

manager-tools-dl is inspired by [youtube-dl](https://github.com/rg3/youtube-dl/).

## Requirements

**Python**

This module requires Python 2.7.9 or newer, this is because of urllib ([1](https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning), [2](https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning)).

**Packages**

This package requires the following modules:
* urllib2 (external)
* requests
* re
* os
* argparse

Packages marked as external are not preinstalled in most operating systems and should be installed.

## Usage
```manager-tools-dl.py [-h] [-v] [-r | -nd] [-t {manager,career,all}]
                 [-o OUTPUT_DIRECTORY]```

### Arguments

```
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -r, --resume          resume past download
  -nd, --no-download    don't download podcasts
  -t {manager,career,all}, --type {manager,career,all}
                        type of podcasts to download
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        podcast download directory
```
