def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "favorite_detective = 'Sherlock'" in __solution__, "Are you creating favorite_detective variable correctly?"
    assert "favorite_quote = '\"Game is ON!\"'" in __solution__, "Are you changing favorite_quote variable? Kindly do not change it."
    assert "print(favorite_detective+': '+favorite_quote)" in __solution__, "Are you printing the output correctly, check the instructions properly?"
    

    __msg__.good("You are awesome, Let's go to next section!")
