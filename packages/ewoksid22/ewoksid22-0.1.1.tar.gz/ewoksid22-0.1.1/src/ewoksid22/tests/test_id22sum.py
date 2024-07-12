from ..id22sum import parse_scan_numbers


def test_parse_scan_numbers():
    first, last, exclude = parse_scan_numbers(10, 20)
    assert first == 10
    assert last == 20
    assert exclude is None

    first, last, exclude = parse_scan_numbers(10, 20, include_scans=(11,))
    assert first == 11
    assert last == 11
    assert exclude is None

    first, last, exclude = parse_scan_numbers(10, 20, include_scans=(11, 12, 13))
    assert first == 11
    assert last == 13
    assert exclude is None

    first, last, exclude = parse_scan_numbers(10, 20, exclude_scans=(12, 15))
    assert first == 10
    assert last == 20
    assert exclude == "12,15"

    first, last, exclude = parse_scan_numbers(
        10, 20, include_scans=(11, 12, 13), exclude_scans=(12,)
    )
    assert first == 11
    assert last == 13
    assert exclude == "12"

    first, last, exclude = parse_scan_numbers(
        10,
        20,
        include_scans=((11, 12, 13), "16,17", ("18",), None),
        exclude_scans=(2, 13, ("17", 20), None),
    )
    assert first == 11
    assert last == 18
    assert exclude == "13,17"

    first, last, exclude = parse_scan_numbers(10, 12, exclude_scans=(10, 11, 12))
    assert first is None
    assert last is None
    assert exclude is None
