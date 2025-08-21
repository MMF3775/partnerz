import builtins
import pytest

import task1.main as main


def test_cli(monkeypatch, capsys):
    inputs = iter([
        "knowledge_base",
        "1",
        "0",
        "2",
        "What is Intercom?",
        "3"
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    try:
        main.run()
    except StopIteration:
        pass

    captured = capsys.readouterr()
    assert captured.out.strip() != ""