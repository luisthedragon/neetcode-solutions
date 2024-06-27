# NEETCODE SOLUTIONS

My solutions to [Leetcode](https://leetcode.com/) problems following the [neetcode.io](https://neetcode.io) suggested path

## Getting started

The following steps will allow you to run the solutions locally

Create a virtual environment

        python -m venv .venv
        source .venv/bin/activate

It is recommend to use the python-leetcode-runner library

        pip install -r requirements.txt

To run a test use pyleet

        cd {{folder}}
        pyleet filename.py

For example:

        cd "Arrays & Hashing"
        pyleet 1_contains_duplicate.py

Example output:

        Test 1 - ([1, 2, 3, 1])...................................................................................................................................PASSED
        Test 2 - ([1, 2, 3, 4])...................................................................................................................................PASSED
        Test 3 - ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]).................................................................................................................PASSED
        All cases passed!
