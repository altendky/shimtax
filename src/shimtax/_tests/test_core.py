def test_direct_coconut_works(pytester):
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


def test_direct_cursed_for_works(pytester):
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
