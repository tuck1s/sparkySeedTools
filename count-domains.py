#!/usr/bin/env python3
import argparse, csv, sys, dns.resolver

def domainpart(n):
    # A valid email address contains exactly one @, otherwise return None = invalid
    parts = n.split('@')
    if len(parts) == 2:
        return parts[1]
    return None

class DomainList:
    def __init__(self):
        self.domains = {}

    def add(self, name):
        dn = domainpart(name)
        if dn in self.domains:
            self.domains[dn] += 1 # Already seen = increment count
        else:
            self.domains[dn] = 1

    def dump(self, mx):
        fmtstr = '{},{},"{}"' if mx else '{},{}'
        print(fmtstr.format('domain', 'count', 'MX'))
        for k, v in self.domains.items():
            if mx:
                result = dns.resolver.resolve(k, 'MX')
                provider = ' '.join(exdata.exchange.to_text() for exdata in result)
            else:
                provider = ''
            print(fmtstr.format(k, v, provider))

# -----------------------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------------------
# Read and validate command-line arguments. You can put multiple input files in the args
parser = argparse.ArgumentParser(
    description='List the distinct domains (and their frequency) from file(s) of email addresses')
parser.add_argument('-mx', action='store_true', help='show MX record lookup')
parser.add_argument('files', metavar='file', type=argparse.FileType('r'), default=[sys.stdin], nargs='*',
    help='input filename. If omitted, will read from stdin')
args = parser.parse_args()
dl = DomainList()
for fh in args.files:
    if fh.isatty():
        sys.stderr.write('(Awaiting input from stdin)\n') # show the user we're waiting for input, withut touching the stdout stream
    f = csv.reader(fh)
    for line in f: # walk through each line in the file
        for addr in line: # may be more than one address per line (comma-separated)
            if domainpart(addr):
                dl.add(addr)
            else:
                print('File {}:\t{} Not an email address - skipping'.format(fh.name, addr))
dl.dump(args.mx)