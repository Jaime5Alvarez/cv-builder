import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate CV using RenderCV from YAML file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run main.py                           # Uses default: cvs-yml/jaime_alvarez.yml
  uv run main.py cvs-yml/example.yml       # Generates CV from example.yml
  uv run main.py path/to/custom.yml        # Generates CV from custom file
        """
    )
    
    parser.add_argument(
        "yaml_file",
        nargs="?",
        default="cvs-yml/jaime_alvarez.yml",
        help="Path to the YAML CV file (default: cvs-yml/jaime_alvarez.yml)"
    )
    
    args = parser.parse_args()
    yaml_path = Path(args.yaml_file)

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
