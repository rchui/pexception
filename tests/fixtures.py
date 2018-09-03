STACK = [
    '  File "test.py", line 22, in <module>\n    main()\n',
    '  File "test.py", line 5, in main\n    another_really_long_name()\n',
    '  File "test.py", line 9, in another_really_long_name\n    another_really_really_really_long_name()\n',
    '  File "test.py", line 13, in another_really_really_really_long_name\n    another_really_really_really_really_long_name()\n',
    '  File "test.py", line 17, in another_really_really_really_really_long_name\n    raise Exception(\'Hello World\')\n',
]

PARSED = (
    9,
    45,
    2,
    [
        ('"test.py"', '<module>', '22', 'main()'),
        ('"test.py"', 'main', '5', 'another_really_long_name()'),
        ('"test.py"', 'another_really_long_name', '9', 'another_really_really_really_long_name()'),
        (
            '"test.py"',
            'another_really_really_really_long_name',
            '13',
            'another_really_really_really_really_long_name()',
        ),
        ('"test.py"', 'another_really_really_really_really_long_name', '17', "raise Exception('Hello World')"),
    ],
)

FORMATTED = [
    'From \x1b[31m"test.py"\x1b[0m in \x1b[34m<module>                                     \x1b[0m line \x1b[32m22\x1b[0m at \x1b[33mmain()\x1b[0m',
    'From \x1b[31m"test.py"\x1b[0m in \x1b[34mmain                                         \x1b[0m line \x1b[32m 5\x1b[0m at \x1b[33manother_really_long_name()\x1b[0m',
    'From \x1b[31m"test.py"\x1b[0m in \x1b[34manother_really_long_name                     \x1b[0m line \x1b[32m 9\x1b[0m at \x1b[33manother_really_really_really_long_name()\x1b[0m',
    'From \x1b[31m"test.py"\x1b[0m in \x1b[34manother_really_really_really_long_name       \x1b[0m line \x1b[32m13\x1b[0m at \x1b[33manother_really_really_really_really_long_name()\x1b[0m',
    'From \x1b[31m"test.py"\x1b[0m in \x1b[34manother_really_really_really_really_long_name\x1b[0m line \x1b[32m17\x1b[0m at \x1b[33mraise Exception(\'Hello World\')\x1b[0m',
]
