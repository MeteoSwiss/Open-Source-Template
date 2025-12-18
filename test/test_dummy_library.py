"""
Copyright (c) 2025 MeteoSwiss, contributors listed in AUTHORS

Distributed under the terms of the BSD 3-Clause License.

SPDX-License-Identifier: BSD-3-Clause
"""

from open_source_template.main import another_dummy_func, dummy_func


def test_dummy_func():
    """Test the correctness of dummy_func."""

    assert dummy_func(3.2) == 3


def test_another_dummy_func():
    """Test the correctness of another_dummy_func."""

    assert another_dummy_func(5) == 5.0
