import sys

import pytest

import shimtax._core
import shimtax.errors


def test_pattern_none() -> None:
    result = next(shimtax._core.pattern.finditer("shimtax"))
    assert result["rest"] == ""


def test_pattern_two() -> None:
    result = next(shimtax._core.pattern.finditer("shimtax:a:b"))
    assert result["rest"] == ":a:b"


def test_get_codec_names_none() -> None:
    assert shimtax._core.get_codec_names("shimtax") == []


def test_get_codec_names_two() -> None:
    assert shimtax._core.get_codec_names("shimtax:a:b") == ["a", "b"]


def test_get_codec_names_raises_for_extra_text() -> None:
    with pytest.raises(shimtax.errors.CodingNotFound):
        shimtax._core.get_codec_names("shimtax:a+")


def test_just_aaa_to_bbb_works(
    pytester: pytest.Pytester,
    enable_aaa_to_bbb: None,
) -> None:
    pytester.makepyfile(
        """
        # coding: shimtax:aaa_to_bbb

        def test():
            to_be_converted = "aaa"
            expected_result = "bbb"
            assert to_be_converted == expected_result
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}


def test_just_ccc_to_ddd_works(
    pytester: pytest.Pytester,
    enable_ccc_to_ddd: None,
) -> None:
    pytester.makepyfile(
        """
        # coding: shimtax:ccc_to_ddd

        def test():
            to_be_converted = "ccc"
            expected_result = "ddd"
            assert to_be_converted == expected_result
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}


def test_just_two_work(
    pytester: pytest.Pytester,
    enable_aaa_to_bbb: None,
    enable_ccc_to_ddd: None,
) -> None:
    pytester.makepyfile(
        """
        # coding: shimtax:aaa_to_bbb:ccc_to_ddd

        def test():
            to_be_converted = "aaaccc"
            expected_result = "bbbddd"
            assert to_be_converted == expected_result
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}


@pytest.mark.no_shimtax
def test_unregistered_fails(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(
        """
        # coding: shimtax
        
        def test():
            assert False
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"errors": 1}


@pytest.mark.no_shimtax
def test_register_passes(pytester: pytest.Pytester) -> None:
    pytester.makeconftest(
        """
        import shimtax
        
        shimtax.register()
        """
    )
    pytester.makepyfile(
        """
        # coding: shimtax

        def test():
            assert True
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}
