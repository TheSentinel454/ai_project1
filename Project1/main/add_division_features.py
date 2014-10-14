from __future__ import division
import sys
import arff

new_features = {}
new_features['dell'] = {}
new_features['targus'] = {}

new_features['dell']['grid'] = {}
new_features['dell']['cornerdist'] = {}
new_features['dell']['meanthumbdist'] = {}

new_features['dell']['grid']['q'] = 1
new_features['dell']['grid']['w'] = 1
new_features['dell']['grid']['e'] = 1
new_features['dell']['grid']['r'] = 2
new_features['dell']['grid']['t'] = 2
new_features['dell']['grid']['y'] = 2
new_features['dell']['grid']['u'] = 2
new_features['dell']['grid']['i'] = 3
new_features['dell']['grid']['o'] = 3
new_features['dell']['grid']['p'] = 3
new_features['dell']['grid']['a'] = 4
new_features['dell']['grid']['s'] = 4
new_features['dell']['grid']['d'] = 4
new_features['dell']['grid']['f'] = 5
new_features['dell']['grid']['g'] = 5
new_features['dell']['grid']['h'] = 5
new_features['dell']['grid']['j'] = 5
new_features['dell']['grid']['k'] = 6
new_features['dell']['grid']['l'] = 6
new_features['dell']['grid']['z'] = 7
new_features['dell']['grid']['x'] = 7
new_features['dell']['grid']['c'] = 8
new_features['dell']['grid']['v'] = 8
new_features['dell']['grid']['b'] = 8
new_features['dell']['grid']['n'] = 8
new_features['dell']['grid']['m'] = 9
new_features['dell']['grid'][' '] = 0

new_features['dell']['cornerdist']['q'] = 6.1
new_features['dell']['cornerdist']['w'] = 6.25
new_features['dell']['cornerdist']['e'] = 6.75
new_features['dell']['cornerdist']['r'] = 7.5
new_features['dell']['cornerdist']['t'] = 8.4
new_features['dell']['cornerdist']['y'] = 8.4
new_features['dell']['cornerdist']['u'] = 7.5
new_features['dell']['cornerdist']['i'] = 6.75
new_features['dell']['cornerdist']['o'] = 6.25
new_features['dell']['cornerdist']['p'] = 6.1
new_features['dell']['cornerdist']['a'] = 4.65
new_features['dell']['cornerdist']['s'] = 4.95
new_features['dell']['cornerdist']['d'] = 5.65
new_features['dell']['cornerdist']['f'] = 6.5
new_features['dell']['cornerdist']['g'] = 7.6
new_features['dell']['cornerdist']['h'] = 7.6
new_features['dell']['cornerdist']['j'] = 6.5
new_features['dell']['cornerdist']['k'] = 5.65
new_features['dell']['cornerdist']['l'] = 4.95
new_features['dell']['cornerdist']['z'] = 3.8
new_features['dell']['cornerdist']['x'] = 4.7
new_features['dell']['cornerdist']['c'] = 5.8
new_features['dell']['cornerdist']['v'] = 7
new_features['dell']['cornerdist']['b'] = 7
new_features['dell']['cornerdist']['n'] = 5.8
new_features['dell']['cornerdist']['m'] = 4.7
new_features['dell']['cornerdist'][' '] = 7.25

new_features['dell']['meanthumbdist']['q'] = 3.2
new_features['dell']['meanthumbdist']['w'] = 2.3
new_features['dell']['meanthumbdist']['e'] = 2.15
new_features['dell']['meanthumbdist']['r'] = 2.8
new_features['dell']['meanthumbdist']['t'] = 3.85
new_features['dell']['meanthumbdist']['y'] = 3.85
new_features['dell']['meanthumbdist']['u'] = 2.8
new_features['dell']['meanthumbdist']['i'] = 2.15
new_features['dell']['meanthumbdist']['o'] = 2.3
new_features['dell']['meanthumbdist']['p'] = 3.2
new_features['dell']['meanthumbdist']['a'] = 2.25
new_features['dell']['meanthumbdist']['s'] = 1
new_features['dell']['meanthumbdist']['d'] = 0.9
new_features['dell']['meanthumbdist']['f'] = 2.05
new_features['dell']['meanthumbdist']['g'] = 3.4
new_features['dell']['meanthumbdist']['h'] = 3.4
new_features['dell']['meanthumbdist']['j'] = 2.05
new_features['dell']['meanthumbdist']['k'] = 0.9
new_features['dell']['meanthumbdist']['l'] = 1
new_features['dell']['meanthumbdist']['z'] = 0.9
new_features['dell']['meanthumbdist']['x'] = 1
new_features['dell']['meanthumbdist']['c'] = 2.15
new_features['dell']['meanthumbdist']['v'] = 3.5
new_features['dell']['meanthumbdist']['b'] = 3.5
new_features['dell']['meanthumbdist']['n'] = 2.15
new_features['dell']['meanthumbdist']['m'] = 1
new_features['dell']['meanthumbdist'][' '] = 4.55

infile = sys.argv[1]
splits = infile.split('.')
outfile = ''.join([splits[0], '_divfeatures.', splits[1]])

data = arff.load(open(infile, 'rb'))

attrs = ['grid', 'cornerdist', 'meanthumbdist']

new_attrs = [(u'grid', u'NUMERIC'), (u'cornerdist', u'NUMERIC'), (u'meanthumbdist', u'NUMERIC')]

data['attributes'] += new_attrs

new_data = []

for i, data_point in enumerate(data['data']):
    if 'maybefinal' in infile:
        new_values = [new_features['dell'][x][data_point[11]] for x in attrs]
    elif 'testoneuser' in infile:
        new_values = [new_features['dell'][x][data_point[8]] for x in attrs]
    else:
        print "Call Vinay. Exiting ..."
    data_point += new_values
    data['data'][i] = data_point

with open(outfile, 'wb') as f:
    arff.dump(data, f)
    



