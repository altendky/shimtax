import pytest


def test_direct_aaa_to_bbb_works(pytester: pytest.Pytester, enable_aaa_to_bbb) -> None:
    pytester.makepyfile(
        """
        # coding: aaa_to_bbb

        def test():
            to_be_converted = "aaa"
            expected_result = "bbb"
            assert to_be_converted == expected_result
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}


def test_direct_ccc_to_ddd_works(pytester: pytest.Pytester, enable_ccc_to_ddd) -> None:
    pytester.makepyfile(
        """
        # coding: ccc_to_ddd

        def test():
            to_be_converted = "ccc"
            expected_result = "ddd"
            assert to_be_converted == expected_result
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}
