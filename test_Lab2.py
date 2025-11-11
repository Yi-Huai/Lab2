import Lab2

def test_calc_min_max_temperature():
    print ("Test calc min max temp")
    result = []
    input_list = [5,67,32,15,89,23,41]
    expected_result = [5,89]
    result = Lab2.calc_min_max_temperature(input_list)
    assert result == expected_result

def test_calc_average_temperature():
    result = []
    input_list = [5,67,32,15,89,23,41]
    expected_result = [5,89]
    result = Lab2.calc_min_max_temperature(input_list)
    assert result == expected_result

def test_calc_median_temperature():
    result = 0
    input_list = [5,15,25,35,45]
    expected_result =25
    result = Lab2.calc_min_max_temperature(input_list)
    assert result == expected_result

