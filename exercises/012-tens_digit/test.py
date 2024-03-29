import io, sys, pytest, os, re, mock

@pytest.mark.it('The function tens_digit must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.tens_digit)

@pytest.mark.it('The function must return something')
def test_for_return(capsys, app):
    assert app.tens_digit(123) != None

@pytest.mark.it('The function must return a number')
def test_for_output_type(capsys, app):
    assert type(app.tens_digit(123)) == type(1)

@pytest.mark.it('We tried to pass 854345 as parameter and it did not return 4')
def test_for_file_output(capsys, app):
    assert app.tens_digit(854345) == (854345 // 10)%10


