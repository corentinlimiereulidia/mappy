import functools
import logging
import re
import sys

class Agg_viewmode():
    def __init__(self, mode_name, count, zooms):
        self.mode_name = mode_name 
        self.count = count
        self.zooms = zooms
        
    def __str__(self):
        return self.mode_name + "\t" + str(self.count) + "\t" + ','.join(map(str, self.zooms))
        
    def __add__(self, agg2):
        assert(agg2.mode_name == self.mode_name)
        return Agg_viewmode(self.mode_name, self.count + agg2.count, self.zooms.union(agg2.zooms))
        

def parse_line(line):
    return re.search('/map/1\.0/slab/([^/]*)/256/([^/]*)', line)

def aggregate(aggregations, match):
    mode_name, zoom = match.groups()
    new_agg_viewmode = Agg_viewmode(mode_name, 1, {zoom})

    if not aggregations or aggregations[-1].mode_name != mode_name:
        return aggregations + [new_agg_viewmode]

    return aggregations[:-1] + [aggregations[-1] + new_agg_viewmode]


if __name__ == "__main__":
    remove_endline = lambda x : x.rstrip('\n')

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename, "r") as input_file:
            file_content = map(remove_endline, input_file.readlines())
    else:
        file_content = map(remove_endline, sys.stdin.readlines())
    
    matches = map(parse_line, file_content)
    matches_filtered = filter(lambda x : x is not None, matches)
    aggregations = functools.reduce(aggregate, matches_filtered, [])
    print(*aggregations, sep="\n")
