#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `repoclone` package."""


import unittest
from click.testing import CliRunner

from repoclone import repoclone
from repoclone import cli
from repoclone import repoclone as main

class TestRepoclone(unittest.TestCase):
    """Tests for `repoclone` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 2
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0

    def test_repoclone_main(self):
        """Test the repoclone main."""
        result = main.repoclone()
        assert result == 2

