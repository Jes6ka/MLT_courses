## part1 : preprocessing.
## part2 : make ID3 algorithm part, training system from labelled data (category is author)
## part3 : evaluation.

# Specific task for each part
Set feature and get attributes.

Make the above file in arff format.

Make ID3 algorithm, since we are handling continous numbers, we need certain point to split and get GAIN from Entropy.

When we are spliting the authors with certain attribute, we can use, random, or making gap between min-max of attributes and spliting only 10parts or so.(making 10 classes for one attribute value, e.g., 1-3, 3-5, 5-7, 7-9, ...)

# references
https://discuss.analyticsvidhya.com/t/decision-tree-with-continuous-variables/201/6

http://support.sas.com/resources/papers/proceedings13/095-2013.pdf
