# sparkySeedTools

[![Build Status](https://travis-ci.com/tuck1s/sparkySeedTools.svg?branch=master)](https://travis-ci.com/tuck1s/sparkySeedTools)

## count-domains

Extract and count the distinct domains of email addresses.

The output is in “comma separated variable” (CSV) format, so it can be processed by other tools.

### Usage
```
./count-domains.py -h
usage: count-domains.py [-h] [-mx] [file [file ...]]

List the distinct domains (and their frequency) from file(s) of email addresses

positional arguments:
  file        input filename. If omitted, will read from stdin

optional arguments:
  -h, --help  show this help message and exit
  -mx         show MX record lookup

```

### Example

```
./count-domains.py -mx test_list.txt
domain,count,"MX"
gmail.com,1,"gmail-smtp-in.l.google.com. alt4.gmail-smtp-in.l.google.com. alt1.gmail-smtp-in.l.google.com. alt2.gmail-smtp-in.l.google.com. alt3.gmail-smtp-in.l.google.com."
yahoo.com,2,"mta5.am0.yahoodns.net. mta6.am0.yahoodns.net. mta7.am0.yahoodns.net."
```
