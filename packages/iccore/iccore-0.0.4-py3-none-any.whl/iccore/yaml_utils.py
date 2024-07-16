from pathlib import Path
import logging

import yaml

logger = logging.getLogger(__name__)


def read_yaml(path: Path):
    with open(path, encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error("Yaml exception: %s", e)
            raise e
