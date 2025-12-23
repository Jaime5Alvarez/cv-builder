# CV Builder

A simple CV builder using RenderCV to generate professional CVs from YAML files.

## Setup

Install dependencies:

```bash
uv sync
```

## Usage

Run the CV builder:

```bash
uv run main.py
```

The script will generate your CV from the YAML file located in `cvs-yml/example.yml` and output the results in `cvs-yml/rendercv_output/`.

## Output

The generated files include:
- PDF version
- PNG preview
- Markdown version
- HTML version
- Typst source file
