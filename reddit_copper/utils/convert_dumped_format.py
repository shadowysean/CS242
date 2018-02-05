import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="source file to convert")
parser.add_argument("output", help="file path to dump")
parser.add_argument("--field", help="select a desirable filed to extract")
parser.add_argument("--prefix")
args = parser.parse_args()

json_data = open(args.input)
print '[INFO] Field to extract is ' + args.field
data = json.load(json_data)
if args.field:
    if args.prefix:
        selected_field_lst = [args.prefix + post[args.field][0].encode('ascii', 'ignore') + '\n' for post in data]
else:
    selected_field_lst = [','.join(post.items()[1].encode('ascii', 'ignore')) + '\n' for post in data]
with open(args.output, 'w') as f:
    f.writelines(selected_field_lst)
