from homework import rich
from homework import olly
from homework import olly_terse
from numpy import array_equal


def test_homework_example():
    input = [
        [1,2],
        [2],
        [],
        [0,1],
    ]
    expected = [
        [0,1,1,0],
        [0,0,1,0],
        [0,0,0,0],
        [1,1,0,0],
    ]

    assert array_equal(rich.to_nx_graph(input), expected)

    assert array_equal(olly.to_nx_graph(input), expected)
    assert array_equal(olly_terse.to_nx_graph(input), expected)