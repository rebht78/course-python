def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "power = 2" in __solution__, "Are you creating power variable correctly?"
    assert "base = 3" in __solution__, "Are you changing base variable?"
    assert "print(base ** 2)" in __solution__, "Are you printing the output correctly, use ** for raise to feature."
    

    __msg__.good("Bingo, Let's move to Chapter 2")
