"""Test CLI functionality."""

from unittest.mock import patch

from fmla.cli import get_fmla_info, get_pip_guide, get_pip_info, main


def test_get_pip_info() -> None:
    """Test that PIP info is returned."""
    info = get_pip_info()
    assert isinstance(info, str)
    assert "PIP: Performance Improvement Plan" in info
    assert len(info) > 0


def test_get_pip_guide() -> None:
    """Test that PIP guide is returned."""
    guide = get_pip_guide()
    assert isinstance(guide, str)
    assert "Mental Guide to Surviving a PIP" in guide
    assert len(guide) > 0


def test_get_fmla_info() -> None:
    """Test that FMLA info is returned."""
    info = get_fmla_info()
    assert isinstance(info, str)
    assert "FMLA: Family and Medical Leave Act" in info
    assert len(info) > 0


def test_main_info_command() -> None:
    """Test that info command works."""
    with patch("builtins.print") as mock_print:
        result = main(["info"])
        assert result == 0
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "PIP: Performance Improvement Plan" in args[0]


def test_main_guide_command() -> None:
    """Test that guide command works."""
    with patch("builtins.print") as mock_print:
        result = main(["guide"])
        assert result == 0
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "Mental Guide to Surviving a PIP" in args[0]


def test_main_fmla_command() -> None:
    """Test that fmla command works."""
    with patch("builtins.print") as mock_print:
        result = main(["fmla"])
        assert result == 0
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        assert "FMLA: Family and Medical Leave Act" in args[0]


def test_main_no_args() -> None:
    """Test that help is shown when no command is provided."""
    with patch("argparse.ArgumentParser.print_help") as mock_print_help:
        result = main([])
        assert result == 1
        mock_print_help.assert_called_once()
