import sys

import pytest


def test_direct_coconut_works(pytester: pytest.Pytester) -> None:
    pytester.makeconftest(
        """
        import coconut.convenience
        """
    )
    pytester.makepyfile(
        """
        # coding: coconut
    
        def test():
            capitals = "ABC"
            x = capitals |> str.lower
            assert x == "abc" 
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}


@pytest.mark.xfail(
    condition=sys.version_info >= (3, 9),
    reason="cursed-for fails in this pytester case for Python 3.9+",
    strict=True,
)
def test_direct_cursed_for_works(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(
        """
        # coding: cursed_for
        
        def test():
            values = []
            for (i = 0; i < 4; i += 1):
                values.append(i)
        
            assert values == [0, 1, 2, 3]
        """
    )
    run_result = pytester.runpytest()

    result_outcomes = run_result.parseoutcomes()
    assert result_outcomes == {"passed": 1}
