
# imap_test

## Introduction
This is a tool to convert Opendrive to Apollo base map, which is modified from
[apollo's imap tool](https://github.com/daohu527/imap), 
and supports generating adjacent reverse lanes of different roads.

## Quick Start
To generate Apollo base map from Opendrive file, you can run the following command:
```bash
# Method 1 [Recommended]
pip install imap_test
imap -f -i imap/data/town.xodr -o imap/data/base_map.txt
# Method 2
python3 imap/main.py -f -i imap/data/town.xodr -o imap/data/base_map.txt
# Method 3
python3 setup.py develop
imap -f -i imap/data/town.xodr -o imap/data/base_map.txt
```

If you want to generate adjacent reverse lanes for each lane, you can run the following command:
```bash
imap -f -i imap/data/town.xodr -o imap/data/base_map.txt -r
```
The `-r` option is used to generate adjacent reverse lanes.

For visualization, you can use the following command:
```bash
imap -m imap/data/apollo_map.txt
```

For global speed limit, you can use the following command:
```bash
imap -f -i imap/data/town.xodr -o imap/data/base_map.txt -sl 7.0
```
The `-sl` option is used to set the global speed limit, which is 
followed by a float number. Here, the global speed limit is set to 7.0 m/s.