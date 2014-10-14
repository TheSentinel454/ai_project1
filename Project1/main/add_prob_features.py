from __future__ import division
import string
import csv
import arff
import sys

subs = {}
with open('./ConfusionTables/substitutionstable.csv', 'rt') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i != 0:
            c = row[0]
            subs[c] = {}
            for j, p in enumerate(row[1:]):
                subs[c][chr(ord('a') + j)] = int(p)

subs[' '] = {}
for c in string.lowercase:
    subs[' '][c] = 0
    subs[c][' '] = 0
subs[' '][' '] = 0

sub_totals = {}
for c in string.lowercase:
    total = 0
    for char in string.lowercase:
        total += subs[c][char]
    sub_totals[c] = total
total = 0
for c in string.lowercase:
    total += sub_totals[c]
for c in string.lowercase:
    sub_totals[c] = sub_totals[c]/total
sub_totals[' '] = 0
    
insertions = {}
with open('./ConfusionTables/insertionstable.csv', 'rt') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i != 0:
            c = row[0]
            insertions[c] = {}
            for j, p in enumerate(row[1:]):
                insertions[c][chr(ord('a') + j)] = int(p)

insertions[' '] = {}
for c in string.lowercase:
    insertions[' '][c] = 0
    insertions[c][' '] = 0
insertions[' '][' '] = 0

insert_totals_current = {}
for c in string.lowercase:
    total = 0
    for char in string.lowercase:
        total += insertions[char][c]
    insert_totals_current[c] = total
total = 0
for c in string.lowercase:
    total += insert_totals_current[c]

for c in string.lowercase:
    insert_totals_current[c] = insert_totals_current[c]/total
insert_totals_current[' '] = 0

insert_totals_prev = {}
for c in string.lowercase:
    total = 0
    for char in string.lowercase:
        total += insertions[c][char]
    insert_totals_prev[c] = total
total = 0
for c in string.lowercase:
    total += insert_totals_prev[c]

for c in string.lowercase:
    insert_totals_prev[c] = insert_totals_prev[c]/total
insert_totals_prev[' '] = 0

sub_attrs = ['sub' + c for c in string.lowercase]
insert_attrs = ['insert' + c for c in string.lowercase]

new_attrs = sub_attrs + ['subprob'] + insert_attrs + ['insertprob_current', 'insertprob_prev']
new_attrs = [(x, u'NUMERIC') for x in new_attrs]

infile = sys.argv[1]
print infile
splits = infile.split('.')
outfile = ''.join([splits[0], '_probfeatures.', splits[1]])
print outfile

data = arff.load(open(infile, 'rb'))
data['attributes'] += new_attrs

for i, data_point in enumerate(data['data']):

    if 'maybefinal' in infile:
        current_char = data_point[11]
        prev_char = data_point[10]
    elif 'testoneuser' in infile:
        current_char = data_point[8]
        prev_char = data_point[7]
    else:
        print "Call Vinay. Exiting ..."
    new_values = [subs[current_char][c] for c in string.lowercase]
    new_values.append(sub_totals[current_char])
    new_values += [insertions[c][prev_char] for c in string.lowercase]
    new_values.append(insert_totals_current[current_char])
    new_values.append(insert_totals_prev[prev_char])
    data_point += new_values
    data['data'][i] = data_point

with open(outfile, 'wb') as f:
    arff.dump(data, f)
    



