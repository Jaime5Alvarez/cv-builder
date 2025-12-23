# CV Builder 📄

A professional CV builder using [RenderCV](https://github.com/sinaatalay/rendercv) to generate beautiful CVs from YAML files. Build your CV once and export it to multiple formats with a single command.

## ✨ Features

- 📝 **YAML-based**: Define your CV in a simple, readable YAML format
- 🎨 **Multiple themes**: Choose from various professional themes
- 📦 **Multiple formats**: Generate PDF, PNG, HTML, Markdown, and Typst
- 🖼️ **Photo support**: Include your professional photo
- 🔧 **Easy to customize**: Modify colors, fonts, layout, and more
- ⚡ **Fast generation**: Quick compilation using Typst

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd cv-builder
```

2. Install dependencies:
```bash
uv sync
```

## 📖 Usage

### Generate CV with default settings

```bash
uv run main.py
```

This generates your CV from `cvs-yml/jaime_alvarez.yml` by default.

### Generate CV from a specific file

```bash
uv run main.py cvs-yml/example.yml
```

### Get help

```bash
uv run main.py --help
```

## 📁 Project Structure

```
cv-builder/
├── cvs-yml/                    # CV YAML files
│   ├── jaime_alvarez.yml       # Your CV
│   ├── example.yml             # Example CV
│   ├── jaime_alvarez_photo.jpeg # Your photo

├── assets/                     # Source assets
├── main.py                     # Main script
├── pyproject.toml             # Project dependencies
└── README.md                  # This file
```

## 🎨 Customization

### Edit Your CV

Edit `cvs-yml/jaime_alvarez.yml` to update your information:

```yaml
cv:
  name: Your Name
  label: Your Job Title
  email: your.email@example.com
  # ... more fields
```

### Add Your Photo

Place your photo in the `cvs-yml/` directory and reference it in your YAML:

```yaml
photo: your_photo.jpg
```

### Customize Design

Add a `design` section to your YAML file to customize colors, fonts, and layout. See [RenderCV documentation](https://docs.rendercv.com) for all available options.

## 📤 Output Formats

The script generates multiple formats:

| Format | File | Description |
|--------|------|-------------|
| **PDF** | `*_CV.pdf` | Professional PDF ready to send |
| **PNG** | `*_CV_*.png` | Preview images of each page |
| **HTML** | `*_CV.html` | Web version of your CV |
| **Markdown** | `*_CV.md` | Plain text Markdown format |
| **Typst** | `*_CV.typ` | Source Typst file (for editing) |

## 🛠️ Technologies Used

- **[RenderCV](https://github.com/sinaatalay/rendercv)**: CV generation engine
- **[Typst](https://typst.app/)**: Modern typesetting system
- **[uv](https://github.com/astral-sh/uv)**: Fast Python package manager
- **Python 3.12+**: Core language

## 📝 Tips

- Keep your YAML file clean and organized
- Use quantifiable achievements in your experience
- Include relevant keywords for ATS (Applicant Tracking Systems)
- Update your photo to a professional headshot
- Test different themes to find the best look

## 📚 Resources

- [RenderCV Documentation](https://docs.rendercv.com)
- [RenderCV GitHub](https://github.com/sinaatalay/rendercv)
- [YAML Syntax](https://yaml.org/)

## 📄 License

This project is open source and available for personal use.

---

Built with ❤️ using RenderCV
