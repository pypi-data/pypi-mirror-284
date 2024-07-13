from pathlib import Path

CURRENT_PATH = Path()


def add_aliases():
    bashrc_path = CURRENT_PATH.home() / ".bashrc"
    bashrc_path.touch(
        exist_ok=True,
        mode=0o644,
    )
    lines = []
    with bashrc_path.open() as bashrc_file:
        for line in bashrc_file.readlines():
            if not line.startswith("alias code"):
                lines.append(line)
    lines.extend(
        [
            'alias code-dart="code --profile Dart"\n',
            'alias code-default="code --profile Default"\n',
            'alias code-python="code --profile Python"\n',
        ]
    )
    with bashrc_path.open(
        mode="w",
    ) as bashrc_file:
        bashrc_file.writelines(lines)
