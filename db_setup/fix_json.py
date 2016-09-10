import json
import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.dumps(eval(l))

f = open("../output.strict", 'w')
for l in parse("../meta_Video_Games.json.gz"):
  f.write(l + '\n')