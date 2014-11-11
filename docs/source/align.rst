Align
=====

This tool to calculate the word error rate (WER). The word error rate is
defined as

:math:`WER = \frac{\text{#insertions} + \text{#deletions} + \text{#substitutions}}{\text{Words in the reference}}`

.. code:: bash

    $ asr align --help
    usage: asr align [-h] [-s1 S1] [-s2 S2]

    align

    optional arguments:
      -h, --help  show this help message and exit
      -s1 S1      sequence 1
      -s2 S2      sequence 2
