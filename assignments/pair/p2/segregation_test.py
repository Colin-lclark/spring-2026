import segregation


def test_grid_size():
    board = segregation.grid(
        segregation.SQUARE_TYPES,
        0.4,
        0.4,
        10
    )

    assert len(board) == 10
    assert len(board[0]) == 10


def test_grid_counts():
    board = segregation.grid(
        segregation.SQUARE_TYPES,
        0.4,
        0.4,
        10
    )

    red = 0
    blue = 0
    empty = 0

    for row in board:
        for cell in row:
            if cell == segregation.SQUARE_TYPES['red']:
                red += 1
            elif cell == segregation.SQUARE_TYPES['blue']:
                blue += 1
            elif cell == segregation.SQUARE_TYPES['empty']:
                empty += 1

    assert red == 40
    assert blue == 40
    assert empty == 20


def test_full_satisfaction_true():
    board = [
        ['X','O'],
        ['O','X']
    ]

    result = segregation.fullSatsifaction(
        board,
        segregation.SQUARE_TYPES
    )

    assert result is True


def test_full_satisfaction_false():
    board = [
        ['*X','O'],
        ['O','X']
    ]

    result = segregation.fullSatsifaction(
        board,
        segregation.SQUARE_TYPES
    )

    assert result is False