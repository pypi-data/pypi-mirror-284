#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2015-2023 SHS-AV s.r.l. (<http://www.zeroincombenze.org>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
    Zeroincombenze® unit test library for python programs Regression Test Suite
"""
from __future__ import print_function, unicode_literals
import os
import sys
sys.path.insert(0,
                os.path.dirname(os.path.dirname(os.getcwd()))
                if os.path.basename(os.getcwd()) == "tests"
                else os.path.dirname(os.getcwd()))
from zerobug import z0test                                                # noqa: E402

__version__ = "2.0.15"

MODULE_ID = 'zerobug'
TEST_FAILED = 1
TEST_SUCCESS = 0


def version():
    return __version__


class RegressionTest:
    def __init__(self, z0bug):
        # self.Z = z0bug
        z0bug.inherit_cls(self)

    def test_01(self, z0ctx):
        # sts = TEST_SUCCESS
        res = False
        if not z0ctx['dry_run']:
            self.root = self.Z.build_os_tree(z0ctx, self.os_tree)
        for path in self.os_tree:
            if not z0ctx['dry_run']:
                path = os.path.join(self.root, path)
                res = os.path.isdir(path)
            self.assertTrue(res, msg_info='mkdir %s')
        return self.ret_sts()

    def test_09(self, z0ctx):
        # sts = TEST_SUCCESS
        res = False
        if not z0ctx['dry_run']:
            self.Z.remove_os_tree(z0ctx, self.os_tree)
        for path in self.os_tree:
            if not z0ctx['dry_run']:
                path = os.path.join(self.root, path)
                res = os.path.isdir(path)
            self.assertFalse(res, msg_info='rmdir %s')
        return self.ret_sts()

    def setup(self, z0ctx):
        self.os_tree = [
            '16.0',
            '16.0/l10n-italy',
            '16.0/l10n-italy/l10n_it_base',
            '/tmp/zerobug',
        ]


#
# Run main if executed as a script
if __name__ == "__main__":
    exit(
        z0test.main_local(
            z0test.parseoptest(sys.argv[1:], version=version()), RegressionTest
        )
    )






