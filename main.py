import subprocess
import sys
from pathlib import Path


def main():
    yaml_path = Path("cvs-yml/example.yml")

    if not yaml_path.exists():
        print(f"Error: File not found {yaml_path}")
        return 1

    print(f"Generating CV from {yaml_path}...")

    try:
        _ = subprocess.run(["rendercv", "render", str(yaml_path)], text=True, check=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error generating CV (exit code: {e.returncode})")
        return e.returncode
    except FileNotFoundError:
        print("Error: rendercv is not installed or not in PATH")
        return 1


if __name__ == "__main__":
    sys.exit(main())
