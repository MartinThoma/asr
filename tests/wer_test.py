#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose

# asr modules
import asr.align as align


# Tests
def execution_test():
    align.main("What a bright day", "What a day")
    align.get_parser()


def wer_test():
    wer = align.calculate_wer("What a bright day".split(),
                              "What a day".split())
    nose.tools.assert_equal(wer, 0.25)
    wer = align.calculate_wer("What a day".split(),
                              "What a bright day".split())
    nose.tools.assert_equal(wer, 1.0/3)
    wer = align.calculate_wer("What a bright day".split(),
                              "What a light day".split())
    nose.tools.assert_equal(wer, 0.25)
