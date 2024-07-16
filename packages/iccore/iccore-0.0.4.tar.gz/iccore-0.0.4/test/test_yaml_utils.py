from pathlib import Path

from iccore.yaml_utils import read_yaml 


def test_iccore():
    test_dir = Path(__file__).parent / "data"
    test_yaml = test_dir / "test_yaml.yml"

    content = read_yaml(test_yaml)
    assert content["test"] == "yaml"
