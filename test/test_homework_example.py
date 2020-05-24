from homework import rich
from homework import olly
from homework import olly_terse
from numpy import array_equal


def test_homework_example():
    input = [
        [1, 2],
        [2],
        [],
        [0, 1],
    ]
    expected = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
    ]

    competing_solutions = [
        olly.to_nx_graph,
        olly_terse.to_nx_graph,
        rich.to_nx_graph
    ]
    for solution in competing_solutions:
        assert array_equal(solution(input), expected)
