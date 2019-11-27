def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "first_number = 5" in __solution__, "Are you creating first_number variable correctly?"
    assert "second_number = 5" in __solution__, "Are you creating second_number variable correctly?"
    assert "result = first_number + second_number" in __solution__, "Are you adding first_number and second_number and assigning it to result?"
    assert "print(result)" in __solution__, "Are you printing the result variable correctly?"
    

    __msg__.good("Well done!")
