import subprocess
from pathlib import Path
from unittest.mock import patch

from genpnize import main


def test_genpnize_from_file_path(capsys):
    resource_dir_path = Path(__file__).parent / "resources"
    input_path = resource_dir_path / "file" / "input.txt"
    with patch("sys.argv", ["genpnize", str(input_path)]):
        main()

    expected = (resource_dir_path / "file" / "expected.txt").read_text()
    assert capsys.readouterr().out == expected


def test_genpnize_from_stdin():
    resource_dir_path = Path(__file__).parent / "resources"
    input_path = resource_dir_path / "stdin" / "input.txt"

    cat_process = subprocess.run(
        ["cat", str(input_path)], stdout=subprocess.PIPE, text=True
    )
    genpnize_process = subprocess.run(
        ["genpnize", "-"],
        input=cat_process.stdout,
        text=True,
        check=True,
        capture_output=True,
    )

    expected = (resource_dir_path / "stdin" / "expected.txt").read_text()
    assert genpnize_process.stdout == expected
