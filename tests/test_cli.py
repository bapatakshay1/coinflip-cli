import pytest

from coinflip.cli import flip, main


def test_flip_returns_heads_or_tails():
    assert flip() in ("heads", "tails")


def test_default_invocation_prints_single_result(capsys):
    exit_code = main([])
    out = capsys.readouterr().out.strip()
    assert exit_code == 0
    assert out in ("heads", "tails")


@pytest.mark.parametrize("count", [1, 5, 10, 100])
def test_count_summary_sums_to_n(capsys, count):
    exit_code = main(["--count", str(count)])
    lines = capsys.readouterr().out.strip().splitlines()
    assert exit_code == 0
    assert len(lines) == 2

    heads = int(lines[0].split(":")[1])
    tails = int(lines[1].split(":")[1])
    assert lines[0].startswith("heads:")
    assert lines[1].startswith("tails:")
    assert heads + tails == count


@pytest.mark.parametrize("bad_value", ["0", "-5", "abc", "1.5", ""])
def test_invalid_count_rejected(capsys, bad_value):
    exit_code = main(["--count", bad_value])
    err = capsys.readouterr().err
    assert exit_code != 0
    assert "coinflip" in err
