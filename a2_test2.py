"""
CSC148, Winter 2021
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Jonathan Calver, Sophia Huynh,
         Maryam Majedi, and Jaisie Sin.

All of the files in this directory are:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh,
                   Maryam Majedi, and Jaisie Sin.

===== Module Description =====

This module contains sample test cases that you can use to test your code.
These are a very incomplete set of test cases! We will be testing your code on
a much more thorough set of tests.

The self-test on MarkUs runs all of the tests below, along with a few others.
Make sure you run the self-test on MarkUs after submitting your code!

Once you have the entire program completed, that is, after Task 5, your
code should pass all of the tests we've provided. As you develop your code,
test cases for parts that you haven't written yet will fail, of course.

But as you work through the earlier phases of the assignment, you can run the
individual tests below for each method as you complete it. We encourage you to
add further test cases in this file to improve your confidence in your code.

Tip: if you put your mouse inside a pytest function and right click, the "run"
menu will give you the option of running just that test function.
"""
from sudoku_puzzle import *
from word_ladder_puzzle import *
from expression_tree import *
from expression_tree_puzzle import *
from solver import *
import sys
sys.setrecursionlimit(4000)

# Below is an incomplete set of tests: these tests are mostly the provided
# doctest examples.
#
# We encourage you to write additional test cases and test your own code,
# using the provided test cases as a template!


def test_sudoku_fail_fast_doctest() -> None:
    """Test SudokuPuzzle.fail_fast on the provided doctest."""
    s = SudokuPuzzle(4, [["A", "B", "C", "D"],
                         ["C", "D", " ", " "],
                         [" ", " ", " ", " "],
                         [" ", " ", " ", " "]],
                     {"A", "B", "C", "D"})

    assert s.fail_fast() is False

    s = SudokuPuzzle(4, [["B", "D", "A", "C"],
                         ["C", "A", "B", "D"],
                         ["A", "B", " ", " "],
                         [" ", " ", " ", " "]],
                     {"A", "B", "C", "D"})
    assert s.fail_fast() is True


def test_has_unique_solution_doctest() -> None:
    """Test has_unique_solution on a SudokuPuzzle with a non-unique solution."""
    s = SudokuPuzzle(4, [["D", "C", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["C", " ", "A", " "],
                         ["A", " ", "C", " "]],
                     {"A", "B", "C", "D"})

    assert s.has_unique_solution() is False

    a = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["D", " ", "A", " "],
                         ["A", " ", "C", " "]],
                     {"A", "B", "C", "D"})

    assert a.has_unique_solution() is True
    unsolved = [[' ', ' ', ' ', '2', '6', ' ', '7', ' ', '1'],
                ['6', '8', ' ', ' ', '7', ' ', ' ', '9', ' '],
                ['1', '9', ' ', ' ', ' ', '4', '5', ' ', ' '],
                ['8', '2', ' ', '1', ' ', ' ', ' ', '4', ' '],
                [' ', ' ', '4', '6', ' ', '2', '9', ' ', ' '],
                [' ', '5', ' ', ' ', ' ', '3', ' ', '2', '8'],
                [' ', ' ', '9', '3', ' ', ' ', ' ', '7', '4'],
                [' ', '4', ' ', ' ', '5', ' ', ' ', '3', '6'],
                ['7', ' ', '3', ' ', '1', '8', ' ', ' ', ' ']]
    b = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})

    assert b.has_unique_solution() is True


def test_dfs_solver_example() -> None:
    """Test DfsSolver.solve on a SudokuPuzzle."""
    # This SudokuPuzzle is a more filled-in version of the one in the
    # example from the handout.
    s = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["D", " ", "A", " "],
                         ["A", " ", "C", " "]],
                     {"A", "B", "C", "D"})

    solver = DfsSolver()
    actual = solver.solve(s)[-1]

    expected = SudokuPuzzle(4, [["C", "D", "B", "A"],
                                ["B", "A", "D", "C"],
                                ["D", "C", "A", "B"],
                                ["A", "B", "C", "D"]],
                            {"A", "B", "C", "D"})

    assert actual == expected


def test_dfs_sudoku() -> None:
    unsolved = [[' ', ' ', ' ', '2', '6', ' ', '7', ' ', '1'],
            ['6', '8', ' ', ' ', '7', ' ', ' ', '9', ' '],
            ['1', '9', ' ', ' ', ' ', '4', '5', ' ', ' '],
            ['8', '2', ' ', '1', ' ', ' ', ' ', '4', ' '],
            [' ', ' ', '4', '6', ' ', '2', '9', ' ', ' '],
            [' ', '5', ' ', ' ', ' ', '3', ' ', '2', '8'],
            [' ', ' ', '9', '3', ' ', ' ', ' ', '7', '4'],
            [' ', '4', ' ', ' ', '5', ' ', ' ', '3', '6'],
            ['7', ' ', '3', ' ', '1', '8', ' ', ' ', ' ']]
    s = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solved = [['4', '3', '5', '2', '6', '9', '7', '8', '1'],
                ['6', '8', '2', '5', '7', '1', '4', '9', '3'],
                ['1', '9', '7', '8', '3', '4', '5', '6', '2'],
                ['8', '2', '6', '1', '9', '5', '3', '4', '7'],
                ['3', '7', '4', '6', '8', '2', '9', '1', '5'],
                ['9', '5', '1', '7', '4', '3', '6', '2', '8'],
                ['5', '1', '9', '3', '2', '6', '8', '7', '4'],
                ['2', '4', '8', '9', '5', '7', '1', '3', '6'],
                ['7', '6', '3', '4', '1', '8', '2', '5', '9']]
    expected = SudokuPuzzle(9, solved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solver = DfsSolver()
    actual = solver.solve(s)[-1]
    assert actual == expected


def test_bfs_solver_example() -> None:
    """Test BfsSolver.solve on a SudokuPuzzle."""
    # This SudokuPuzzle is a more filled-in version of the one in the
    # example from the handout.
    s = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["D", " ", "A", " "],
                         ["A", " ", "C", " "]],
                     {"A", "B", "C", "D"})

    solver = BfsSolver()
    actual = solver.solve(s)[-1]

    expected = SudokuPuzzle(4, [["C", "D", "B", "A"],
                                ["B", "A", "D", "C"],
                                ["D", "C", "A", "B"],
                                ["A", "B", "C", "D"]],
                            {"A", "B", "C", "D"})

    assert actual == expected


def test_bfs_sudoku() -> None:
    unsolved = [[' ', ' ', ' ', '2', '6', ' ', '7', ' ', '1'],
                ['6', '8', ' ', ' ', '7', ' ', ' ', '9', ' '],
                ['1', '9', ' ', ' ', ' ', '4', '5', ' ', ' '],
                ['8', '2', ' ', '1', ' ', ' ', ' ', '4', ' '],
                [' ', ' ', '4', '6', ' ', '2', '9', ' ', ' '],
                [' ', '5', ' ', ' ', ' ', '3', ' ', '2', '8'],
                [' ', ' ', '9', '3', ' ', ' ', ' ', '7', '4'],
                [' ', '4', ' ', ' ', '5', ' ', ' ', '3', '6'],
                ['7', ' ', '3', ' ', '1', '8', ' ', ' ', ' ']]
    s = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solved = [['4', '3', '5', '2', '6', '9', '7', '8', '1'],
              ['6', '8', '2', '5', '7', '1', '4', '9', '3'],
              ['1', '9', '7', '8', '3', '4', '5', '6', '2'],
              ['8', '2', '6', '1', '9', '5', '3', '4', '7'],
              ['3', '7', '4', '6', '8', '2', '9', '1', '5'],
              ['9', '5', '1', '7', '4', '3', '6', '2', '8'],
              ['5', '1', '9', '3', '2', '6', '8', '7', '4'],
              ['2', '4', '8', '9', '5', '7', '1', '3', '6'],
              ['7', '6', '3', '4', '1', '8', '2', '5', '9']]
    expected = SudokuPuzzle(9, solved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solver = BfsSolver()
    actual = solver.solve(s)[-1]
    assert actual == expected


def test_word_ladder_eq_doctest() -> None:
    """Test WordLadder.__eq__ on the provided doctest"""
    wl1 = WordLadderPuzzle("me", "my", {"me", "my", "ma"})
    wl2 = WordLadderPuzzle("me", "my", {"me", "my", "mu"})
    wl3 = WordLadderPuzzle("me", "my", {"ma", "me", "my"})
    assert wl1.__eq__(wl2) is False
    assert wl1.__eq__(wl3) is True


def test_word_ladder_str_doctest() -> None:
    """Test WordLadder.__str__ on the provided doctest"""
    wl1 = WordLadderPuzzle("me", "my", {"me", "my", "ma"})
    wl2 = WordLadderPuzzle("me", "my", {"me", "my", "mu"})
    assert str(wl1) == 'me -> my'
    assert str(wl2) == 'me -> my'


def test_word_ladder_extensions_doctest() -> None:
    """Test WordLadder.__str__ on the provided doctest"""
    wl1 = WordLadderPuzzle("me", "my", {"me", "be", "my"})
    wl2 = WordLadderPuzzle("be", "my", {"me", "be", "my"})
    wl3 = WordLadderPuzzle("my", "my", {"me", "be", "my"})

    msg1 = f"{wl1.extensions()} is missing some valid puzzle states"
    msg2 = f"{wl1.extensions()} contains extra invalid puzzle states"

    assert all([wlp in wl1.extensions() for wlp in [wl2, wl3]]), msg1
    assert all([wlp in [wl2, wl3] for wlp in wl1.extensions()]), msg2


def test_word_ladder_is_solved_doctest() -> None:
    """Test WordLadder.is_solved on the provided doctest"""
    wl1 = WordLadderPuzzle("me", "me", {"me", "my"})
    wl2 = WordLadderPuzzle("me", "my", {"me", "my"})
    assert wl1.is_solved() is True
    assert wl2.is_solved() is False


def test_word_ladder_get_difficulty() -> None:
    """Test WordLadder.get_difficulty on TRIVIAL and EASY puzzles."""
    wl1 = WordLadderPuzzle("done", "done", {"done"})
    assert wl1.get_difficulty() == TRIVIAL

    wl2 = WordLadderPuzzle("come", "done", {"come", "cone", "done"})
    assert wl2.get_difficulty() == EASY


def test_expression_tree_eval_doctest() -> None:
    """Test ExprTree.eval on the provided doctest"""
    exp_t = ExprTree('+', [ExprTree(3, []),
                           ExprTree('*', [ExprTree('x', []),
                                          ExprTree('y', [])]),
                           ExprTree('x', [])])
    look_up = {}
    exp_t.populate_lookup(look_up)
    assert exp_t.eval(look_up) == 3

    look_up['x'] = 7
    look_up['y'] = 3
    assert exp_t.eval(look_up) == 31


def test_expression_tree_populate_lookup_doctest() -> None:
    """Test ExprTree.populate_lookup on the provided doctest"""
    expr_t = ExprTree('a', [])
    look_up = {}
    expr_t.populate_lookup(look_up)
    assert look_up['a'] == 0
    assert len(look_up) == 1


def test_expression_tree_construct_from_list_doctest() -> None:
    """Test ExprTree.construct_from_list on the provided doctest"""
    # This test relies on ExprTree.__str__ working correctly.
    example = [[5]]
    exp_t = construct_from_list(example)
    assert str(exp_t) == '5'

    example = [['+'], [3, 'a']]
    exp_t = construct_from_list(example)
    assert str(exp_t) == '(3 + a)'

    example = [['+'], [3, '*', 'a', '+'], ['a', 'b'], [5, 'c']]
    exp_t = construct_from_list(example)
    assert str(exp_t) == '(3 + (a * b) + a + (5 + c))'

    example = [['+'], ['+', '*', '+', 3], ['a', 2], [3, 'b'], [5, '+', 8], [6, 8]]
    exp_t = construct_from_list(example)
    assert str(exp_t) == '((a + 2) + (3 * b) + (5 + (6 + 8) + 8) + 3)'


def test_expression_tree_substitute_doctest() -> None:
    """Test ExprTree.substitute on the provided doctest"""
    # This test relies on ExprTree.__str__ working correctly.
    exp_t = ExprTree('a', [])
    exp_t.substitute({'a': 1})
    assert str(exp_t) == '1'

    exp_t = ExprTree('*', [ExprTree('a', []),
                           ExprTree('*', [ExprTree('a', []),
                                          ExprTree(1, [])])])
    exp_t.substitute({'a': 2, '*': '+'})
    assert str(exp_t) == '(2 + (2 + 1))'


def test_expression_tree_str_doctest() -> None:
    """Test ExprTree.__str__ on the provided doctest"""

    exp_t = ExprTree('+', [ExprTree('a', []),
                           ExprTree('b', []),
                           ExprTree(3, [])])
    assert str(exp_t) == '(a + b + 3)'

    exp_t = ExprTree(None, [])
    assert str(exp_t) == '()'

    exp_t = ExprTree(5, [])
    assert str(exp_t) == '5'

    exp_t = ExprTree('+', [ExprTree('*', [ExprTree(7, []),
                                          ExprTree('+',
                                                   [ExprTree(6, []),
                                                    ExprTree(6, [])])]),
                           ExprTree(5, [])])
    assert str(exp_t) == '((7 * (6 + 6)) + 5)'

    exp_t = ExprTree('+', [ExprTree(3, []),
                           ExprTree('*', [ExprTree('x', []),
                                          ExprTree('y', [])]),
                           ExprTree('x', [])])
    assert str(exp_t) == '(3 + (x * y) + x)'


def test_expression_tree_eq_doctest() -> None:
    """Test ExprTree.__eq__ on the provided doctest"""
    t1 = ExprTree(5, [])
    assert t1.__eq__(ExprTree(5, []))

    t2 = ExprTree('*', [ExprTree(5, []), ExprTree(2, [])])
    assert t2.__eq__(ExprTree('*', [ExprTree(5, []), ExprTree(2, [])]))
    assert t2.__eq__(ExprTree('*', [])) is False


def test_expression_tree_puzzle_is_solved_doctest() -> None:
    """Test ExpressionTreePuzzle.is_solved on the provided doctest"""
    exp_t = ExprTree('+', [ExprTree('a', []), ExprTree('b', [])])
    puz = ExpressionTreePuzzle(exp_t, 7)
    assert puz.is_solved() is False
    puz.variables['a'] = 7
    assert puz.is_solved() is False
    puz.variables['a'] = 5
    puz.variables['b'] = 2
    assert puz.is_solved() is True


def test_expression_tree_puzzle_str_doctest() -> None:
    """Test ExpressionTreePuzzle.__str__ on the provided doctest"""
    exp_t = ExprTree('+', [ExprTree('*',
                                    [ExprTree('a', []),
                                     ExprTree('+', [ExprTree('b', []),
                                                    ExprTree(6, []),
                                                    ExprTree(6, []),
                                                    ])]),
                           ExprTree(5, [])])
    puz = ExpressionTreePuzzle(exp_t, 61)
    assert str(puz) == "{'a': 0, 'b': 0}\n((a * (b + 6 + 6)) + 5) = 61"


def test_expression_tree_puzzle_extensions_doctest() -> None:
    """Test ExpressionTreePuzzle.extensions on the provided doctest"""
    exp_t = ExprTree('a', [])
    puz = ExpressionTreePuzzle(exp_t, 7)
    exts_of_puz = puz.extensions()
    assert len(exts_of_puz) == 9

    exts_of_an_ext = exts_of_puz[0].extensions()
    assert len(exts_of_an_ext) == 0

    exp_t = ExprTree('+', [ExprTree('a', []), ExprTree('b', [])])
    exp_t = ExprTree('a', [ExprTree('b', [])])
    puz = ExpressionTreePuzzle(exp_t, 8)
    exts_of_puz = puz.extensions()
    assert len(exts_of_puz) == 18

    exp_t = ExprTree('+', [ExprTree('+', [ExprTree('a', []), ExprTree('d', [])]),
                           ExprTree('b', []), ExprTree('c', [])])
    puz = ExpressionTreePuzzle(exp_t, 8)
    exts_of_puz = puz.extensions()
    assert len(exts_of_puz) == 36


def test_expression_tree_puzzle_fail_fast_true() -> None:
    """Test ExpressionTreePuzzle.fail_fast on an unsolvable puzzle."""
    exp_t = ExprTree('+', [ExprTree('a', []), ExprTree('b', [])])
    puz = ExpressionTreePuzzle(exp_t, 7)
    puz.variables['a'] = 9

    assert puz.fail_fast() is True


def test_expression_tree_puzzle_fail_fast_false() -> None:
    """Test ExpressionTreePuzzle.fail_fast on a solvable puzzle."""
    exp_t = ExprTree('+', [ExprTree('a', []), ExprTree('b', [])])
    puz = ExpressionTreePuzzle(exp_t, 7)
    puz.variables['a'] = 2

    assert puz.fail_fast() is False


def test_word_latter_example() -> None:
    words = {'coal', 'coat', 'goal', 'meal', 'meat', 'moat'}
    from_word = 'coat'
    to_word = 'goal'
    slide_example = WordLadderPuzzle(from_word, to_word, words)
    solution = WordLadderPuzzle(to_word, to_word, words)

    bfs = BfsSolver()
    bfs_solution = bfs.solve(slide_example)
    assert len(bfs_solution) == 3
    assert bfs_solution[-1] == solution

    dfs = DfsSolver()
    dfs_solution = dfs.solve(slide_example)
    assert dfs_solution[-1] == solution

    assert slide_example.get_difficulty() == 'easy'


def test_word_latter_china_to_aster() -> None:
    words = {'china', 'chins', 'cains', 'carns', 'cares',
             'carer', 'cater', 'eater', 'ester', 'aster',
             'poops', 'dicks', 'japan', 'whipwhip', 'naenae'
             'chips', 'dads', 'chooch', 'dbaby', 'kares',
             'dares', 'wears', 'pears', 'lairs'}
    from_word = 'china'
    to_word = 'aster'
    slide_example = WordLadderPuzzle(from_word, to_word, words)
    solution = WordLadderPuzzle(to_word, to_word, words)

    bfs = BfsSolver()
    bfs_solution = bfs.solve(slide_example)
    assert len(bfs_solution) == 10
    assert bfs_solution[-1] == solution

    dfs = DfsSolver()
    dfs_solution = dfs.solve(slide_example)
    assert dfs_solution[-1] == solution

    assert slide_example.get_difficulty() == 'hard'


def test_expression_puzzle_max_dfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 107)
    s = DfsSolver()
    a = s.solve(puz)
    solution = a[-1]
    assert solution._tree.eval(solution.variables) == 107


def test_expression_puzzle_min_dfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 11)
    s = DfsSolver()
    a = s.solve(puz)
    solution = a[-1]
    assert solution._tree.eval(solution.variables) == 11


def test_expression_puzzle_unsolvable_small_dfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 10)
    s = DfsSolver()
    a = s.solve(puz)
    assert a == []


def test_expression_puzzle_unsolvable_big_dfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 108)
    s = DfsSolver()
    a = s.solve(puz)
    assert a == []


def test_expression_puzzle_max_bfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 107)
    s = BfsSolver()
    a = s.solve(puz)
    solution = a[-1]
    assert solution._tree.eval(solution.variables) == 107


def test_expression_puzzle_min_bfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 11)
    s = BfsSolver()
    a = s.solve(puz)
    solution = a[-1]
    assert solution._tree.eval(solution.variables) == 11


def test_expression_puzzle_unsolvable_small_bfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 10)
    s = BfsSolver()
    a = s.solve(puz)
    assert a == []


def test_expression_puzzle_unsolvable_big_bfs() -> None:
    a = [['+'], [3, '*', 'a', '+'], ['b', 'c'], [5, 'd']]
    tree = construct_from_list(a)
    puz = ExpressionTreePuzzle(tree, 108)
    s = BfsSolver()
    a = s.solve(puz)
    assert a == []


def test_dfs_already_solved() -> None:
    words = {'coal', 'coat', 'goal', 'meal', 'meat', 'moat'}
    puzzle_already_solved = WordLadderPuzzle('coal', 'coal', words)
    solved_state = WordLadderPuzzle('coal', 'coal', words)
    s = DfsSolver()
    solution = s.solve(puzzle_already_solved)
    assert len(solution) == 1
    assert solution[0] == solved_state


def test_bfs_already_solved() -> None:
    words = {'coal', 'coat', 'goal', 'meal', 'meat', 'moat'}
    puzzle_already_solved = WordLadderPuzzle('coal', 'coal', words)
    solved_state = WordLadderPuzzle('coal', 'coal', words)
    s = BfsSolver()
    solution = s.solve(puzzle_already_solved)
    assert len(solution) == 1
    assert solution[0] == solved_state


def test_dfs_no_solution() -> None:
    words = {'aaaa', 'bbbb', 'cccc', 'dddd'}
    unsolvable = WordLadderPuzzle('aaaa', 'dddd', words)
    s = DfsSolver()
    solution = s.solve(unsolvable)
    assert len(solution) == 0


def test_bfs_no_solution() -> None:
    words = {'aaaa', 'bbbb', 'cccc', 'dddd'}
    unsolvable = WordLadderPuzzle('aaaa', 'dddd', words)
    s = BfsSolver()
    solution = s.solve(unsolvable)
    assert len(solution) == 0


def test_eval_one_root() -> None:
    tree = ExprTree(5, [])
    assert tree.eval({}) == 5


def test_expression_tree_str_doctest1() -> None:
    exp_t = ExprTree('+', [ExprTree('a', []), \
                           ExprTree('b', []), \
                           ExprTree(3, [])])
    assert str(exp_t) == '(a + b + 3)'
    exp_t = ExprTree(None, [])
    assert str(exp_t) == '()'
    exp_t = ExprTree(5, [])
    assert str(exp_t) == '5'

    exp_t = ExprTree('+', [ExprTree('*', [ExprTree(7, []), \
                                          ExprTree('+', \
                                                   [ExprTree(6, []), \
                                                    ExprTree(6, [])] \
                                                   )]), \
                           ExprTree(5, [])])
    assert str(exp_t) == '((7 * (6 + 6)) + 5)'

    exp_t = ExprTree('+', [ExprTree(3, []), \
                           ExprTree('*', [ExprTree('x', []), \
                                          ExprTree('y', [])]), \
                           ExprTree('x', [])])
    assert str(exp_t) == '(3 + (x * y) + x)'


def test_expression_tree_eq() -> None:
    tree1 = ExprTree('*', [ExprTree(1, [],), ExprTree(2, [],)])
    tree2 = ExprTree('*', [ExprTree(1, [],), ExprTree(2, [],)])
    assert tree1 == tree2
    tree2 = ExprTree('+', [ExprTree(1, [],), ExprTree(2, [],)])
    assert tree1 != tree2
    tree2 = ExprTree('*', [ExprTree(2, [],), ExprTree(2, [],)])
    assert tree1 != tree2
    tree2 = ExprTree('*', [ExprTree(1, [],), ExprTree(2, [],), ExprTree(3, [],)])
    assert tree1 != tree2


def test_substitute() -> None:
    tree = ExprTree('*', [ExprTree(1, []), ExprTree(2, [])])
    from_to = {'*': '+', 1: 300, 2: 500}
    tree.substitute(from_to)
    assert tree == ExprTree('+', [ExprTree(300, []), ExprTree(500, [])])
    assert from_to == {'*': '+', 1: 300, 2: 500}


def test_substitute_empty_dict() -> None:
    tree = ExprTree('*', [ExprTree(1, []), ExprTree(2, [])])
    from_to = {}
    tree.substitute(from_to)
    assert tree == ExprTree('*', [ExprTree(1, []), ExprTree(2, [])])
    assert from_to == {}


def test_populate_lookup_no_varialble() -> None:
    tree = ExprTree(1, [])
    dic = {}
    tree.populate_lookup(dic)
    assert dic == {}


def test_populate_lookup_one_variable() -> None:
    tree = ExprTree('a', [])
    dic = {}
    tree.populate_lookup(dic)
    assert dic == {'a': 0}


def test_populate_lookup_overrides_one_variable() -> None:
    tree = ExprTree('a', [])
    dic = {'a': 123}
    tree.populate_lookup(dic)
    assert dic == {'a': 0}


def test_populate_lookup_adds_one_variable() -> None:
    tree = ExprTree('a', [])
    dic = {'b': 123}
    tree.populate_lookup(dic)
    assert dic == {'b': 123, 'a': 0}


def test_populate_lookup_large_example() -> None:
    tree3 = ExprTree('a', [])
    tree2 = ExprTree('*', [ExprTree('b', []), ExprTree('c', [])])
    tree1 = ExprTree('*', [tree3, tree2])
    dic = {}
    tree1. populate_lookup(dic)
    assert dic == {'a': 0, 'b': 0, 'c': 0}


def test_expr_puzzle_extensions_doesnt_mutate_variables() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])
    puz = ExpressionTreePuzzle(tree, 0)
    assert puz.variables == {'x': 0, 'y': 0}

    extensions = puz.extensions()

    assert len(extensions) > 0

    assert puz.variables == {'x': 0, 'y': 0}

    assert puz._tree == ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])


def test_expr_puzzle_doesnt_mutate_nodes() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])
    puz = ExpressionTreePuzzle(tree, 0)

    extensions = puz.extensions()
    for extension in extensions:
        assert extension._tree == ExprTree('+', [ExprTree('x', []),
                                                 ExprTree('y', [])])


def test_expr_puzzle_extensions_filled_out_variables_dict() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])
    puz = ExpressionTreePuzzle(tree, 0)
    puz.variables = {'x': 7, 'y': 9}
    assert not puz.is_solved()
    assert puz.extensions() == []
    s = BfsSolver()
    solution = s.solve(puz)
    assert len(solution) == 0


def test_solvers_ignore_states_in_seen() -> None:
    words = {'mac', 'bac', 'hac', 'zac', 'lac', 'cac'}
    puz = WordLadderPuzzle('mac', 'zac', words)
    solution = WordLadderPuzzle('zac', 'zac', words)
    seen = set()
    seen.add(str(solution))
    dfs = DfsSolver()
    assert dfs.solve(puz, seen) == []
    bfs = BfsSolver()
    assert bfs.solve(puz, seen) == []


def test_has_unique_solution_one_cell_left_to_fit() -> None:
    board = [['4', '3', '5', '2', '6', '9', '7', '8', '1'],
              ['6', '8', '2', '5', '7', '1', '4', '9', '3'],
              ['1', '9', '7', '8', '3', '4', '5', '6', '2'],
              ['8', '2', '6', '1', '9', '5', '3', '4', '7'],
              ['3', '7', '4', '6', '8', '2', '9', '1', '5'],
              ['9', '5', '1', '7', '4', '3', '6', '2', '8'],
              ['5', '1', '9', '3', '2', '6', '8', '7', '4'],
              ['2', '4', '8', '9', '5', '7', '1', '3', '6'],
              ['7', '6', '3', '4', '1', '8', '2', '5', ' ']]
    puz = SudokuPuzzle(9, board, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    assert puz.has_unique_solution()


def test_dfs_dont_mutate_puzzle() -> None:
    from_word = "mac"
    to_word = "hac"
    words = {'aac','bac','cac','lac','mac','rac','tac','hac'}
    puz = WordLadderPuzzle(from_word, to_word, words)
    bfs = BfsSolver()
    bfs_sol = bfs.solve(puz)
    assert puz == WordLadderPuzzle(from_word, to_word, words)


def test_bfs_dont_mutate_puzzle() -> None:
    from_word = "mac"
    to_word = "hac"
    words = {'aac','bac','cac','lac','mac','rac','tac','hac'}
    puz = WordLadderPuzzle(from_word, to_word, words)
    dfs = DfsSolver()
    dfs_sol = dfs.solve(puz)
    assert puz == WordLadderPuzzle(from_word, to_word, words)


def test_expr_puzzle_fail_fast_doesnt_mutate() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])
    vars = {'x': 0, 'y': 0}
    puz = ExpressionTreePuzzle(tree, 0)
    fail = puz.fail_fast()
    assert puz._tree == ExprTree('+', [ExprTree('x', []), ExprTree('y', [])])
    assert puz.variables == {'x': 0, 'y': 0}
    assert puz.target == 0


def test_expr_puzzle_fail_fast_too_big() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', []), ExprTree('z', [])])
    puz = ExpressionTreePuzzle(tree, 0)
    assert puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 2)
    assert puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 3)
    assert not puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 4)
    assert not puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 7)
    puz.variables['x'] = 5
    puz.variables['y'] = 8
    assert puz.fail_fast()


def test_expr_puzzle_fail_fast_too_small() -> None:
    tree = ExprTree('+', [ExprTree('x', []), ExprTree('y', []), ExprTree('z', [])])
    puz = ExpressionTreePuzzle(tree, 26)
    assert not puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 27)
    assert not puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 28)
    assert puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 28)
    puz = ExpressionTreePuzzle(tree, 11)
    puz.variables['x'] = 9
    assert not puz.fail_fast()
    puz = ExpressionTreePuzzle(tree, 10)
    puz.variables['x'] = 9
    assert puz.fail_fast()


def test_has_unique_empty_board() -> None:
    s = SudokuPuzzle(4, [[" ", " ", " ", " "],
                         [" ", " ", " ", " "],
                         [" ", " ", " ", " "],
                         [" ", " ", " ", " "]],
                     {"A", "B", "C", "D"})
    assert not s.has_unique_solution()


def test_sudoku_fail_fast_slides() -> None:
    s = SudokuPuzzle(4, [["A", " ", "B", " "],
                         ["B", " ", "D", "C"],
                         [" ", " ", "A", " "],
                         [" ", " ", "C", " "]],
                     {"A", "B", "C", "D"})
    assert s.fail_fast()
    s = SudokuPuzzle(4, [["C", " ", "B", " "],
                         ["B", " ", "D", "C"],
                         [" ", " ", "A", " "],
                         [" ", " ", "C", " "]],
                     {"A", "B", "C", "D"})
    assert not s.fail_fast()


# Passes but takes really long
def test_not_fun_sudoku_dfs() -> None:
    unsolved = [[' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', '6', ' ', ' ', ' ', ' ', '3'],
                [' ', '7', '4', ' ', '8', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', '2'],
                [' ', '8', ' ', ' ', '4', ' ', ' ', '1', ' '],
                ['6', ' ', ' ', '5', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', '1', ' ', '7', '8', ' '],
                ['5', ' ', ' ', ' ', ' ', '9', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ']]
    s = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solved = [['1', '2', '6', '4', '3', '7', '9', '5', '8'],
              ['8', '9', '5', '6', '2', '1', '4', '7', '3'],
              ['3', '7', '4', '9', '8', '5', '1', '2', '6'],
              ['4', '5', '7', '1', '9', '3', '8', '6', '2'],
              ['9', '8', '3', '2', '4', '6', '5', '1', '7'],
              ['6', '1', '2', '5', '7', '8', '3', '9', '4'],
              ['2', '6', '9', '3', '1', '4', '7', '8', '5'],
              ['5', '4', '8', '7', '6', '9', '2', '3', '1'],
              ['7', '3', '1', '8', '5', '2', '6', '4', '9']]
    expected = SudokuPuzzle(9, solved, {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
    solver = DfsSolver()
    actual = solver.solve(s)[-1]
    assert actual == expected


def test_not_fun_sudoku_bfs() -> None:
    unsolved = [[' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', '6', ' ', ' ', ' ', ' ', '3'],
                [' ', '7', '4', ' ', '8', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', '2'],
                [' ', '8', ' ', ' ', '4', ' ', ' ', '1', ' '],
                ['6', ' ', ' ', '5', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', '1', ' ', '7', '8', ' '],
                ['5', ' ', ' ', ' ', ' ', '9', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ']]
    s = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7',
                                   '8', '9'})
    solved = [['1', '2', '6', '4', '3', '7', '9', '5', '8'],
              ['8', '9', '5', '6', '2', '1', '4', '7', '3'],
              ['3', '7', '4', '9', '8', '5', '1', '2', '6'],
              ['4', '5', '7', '1', '9', '3', '8', '6', '2'],
              ['9', '8', '3', '2', '4', '6', '5', '1', '7'],
              ['6', '1', '2', '5', '7', '8', '3', '9', '4'],
              ['2', '6', '9', '3', '1', '4', '7', '8', '5'],
              ['5', '4', '8', '7', '6', '9', '2', '3', '1'],
              ['7', '3', '1', '8', '5', '2', '6', '4', '9']]
    expected = SudokuPuzzle(9, solved, {'1', '2', '3', '4', '5', '6', '7',
                                        '8', '9'})
    solver = DfsSolver()
    actual = solver.solve(s)[-1]
    assert actual == expected


def test_not_fun_sudoku_unique_solution() -> None:
    unsolved = [[' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', '6', ' ', ' ', ' ', ' ', '3'],
                [' ', '7', '4', ' ', '8', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', '2'],
                [' ', '8', ' ', ' ', '4', ' ', ' ', '1', ' '],
                ['6', ' ', ' ', '5', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', '1', ' ', '7', '8', ' '],
                ['5', ' ', ' ', ' ', ' ', '9', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ']]
    s = SudokuPuzzle(9, unsolved, {'1', '2', '3', '4', '5', '6', '7',
                                   '8', '9'})
    assert s.has_unique_solution()


if __name__ == '__main__':
    import pytest
    pytest.main(['a2_test2.py', '-v'])
