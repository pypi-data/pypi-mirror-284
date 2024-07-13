from pathlib import Path

CURRENT_PATH = Path()
SOURCE_DIR_PATH = CURRENT_PATH / "source"


def init():
    for dir in [
        "entities",
        "frameworks_and_devices",
        "interface_adapters",
        "use_cases",
    ]:
        dir_path = SOURCE_DIR_PATH / dir

        dir_path.mkdir(
            exist_ok=True,
            parents=True,
        )
        (dir_path / "__init__.py").touch(
            exist_ok=True,
        )
