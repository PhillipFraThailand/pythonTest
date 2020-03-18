## Assertion test in Python

The file __inc_dec.py__ contains the two methods to be tested

* __increment__ increments a input _x_ with 1 and returns it

* __decrement__ which decrements the input by 1 and returns it

The file __test_unitttest.py__ contains two methods that tests __inc_dec.py__ with assertion tests

* The file contains a class __Test_TestIncrementDecrement__ 

* The class contains two methods: __test_increment__ and __test_decrement__

* __test_increment__ runs two checks: assertNotEqual which tests that the input (3) doesn't return 2 or 5, and assertEqual to check that the output is 4 when given 3

* __test_decrement__ does the same, but with decrement
