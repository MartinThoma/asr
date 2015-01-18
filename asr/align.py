#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculate the word error rate (WER) of two word sequences."""


def calculate_wer(reference, hypothesis):
    """
        Calculation of WER with Levenshtein distance.
        Works only for iterables up to 254 elements (uint8).
        O(nm) time and space complexity.

        >>> calculate_wer("who is there".split(), "is there".split())
        1
        >>> calculate_wer("who is there".split(), "".split())
        3
        >>> calculate_wer("".split(), "who is there".split())
        3
    """
    # initialisation
    import numpy
    d = numpy.zeros((len(reference)+1)*(len(hypothesis)+1), dtype=numpy.uint8)
    d = d.reshape((len(reference)+1, len(hypothesis)+1))
    for i in range(len(reference)+1):
        for j in range(len(hypothesis)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(reference)+1):
        for j in range(1, len(hypothesis)+1):
            if reference[i-1] == hypothesis[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion    = d[i][j-1] + 1
                deletion     = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(reference)][len(hypothesis)]/float(len(reference))


def get_parser():
    """Get a parser object"""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s1", dest="s1", help="sequence 1")
    parser.add_argument("-s2", dest="s2", help="sequence 2")
    return parser


def main(s1, s2):
    wer = calculate_wer(s1.split(), s2.split())
    print("%0.4f" % wer)


if __name__ == '__main__':
    args = get_parser().parse_args()
    main(args.s1, args.s2)
