<div align="center">
  <h1>promptxml</h1>
  <p>
    <img alt="License: MIT" src="https://img.shields.io/github/license/barabum0/promptxml">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/barabum0/promptxml">
    <a href="https://pypi.org/project/promptxml">
        <img alt="PyPI version" src="https://img.shields.io/pypi/v/promptxml.svg?logo=pypi&logoColor=FFE873">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
    <a href="https://github.com/PyCQA/isort">
        <img alt="formatted with: isort" src="https://img.shields.io/badge/formatted%20with-isort-blue.svg">
    </a>
    <a href="https://mypy-lang.org/">
        <img alt="formatted with: isort" src="https://www.mypy-lang.org/static/mypy_badge.svg">
    </a>
  </p>
</div>

## About

**promptxml** is a tool designed to create prompt instructions for neural networks in XML format. This tool helps structure and manage complex prompts, making it easier to feed instructions to neural networks in a well-organized XML format.

## Installation

To install **promptxml**, simply use pip:

```bash
pip install promptxml
```

## Usage

### Using `PromptItem`

```python
from promptxml import PromptItem

# Create a new PromptItem
item = PromptItem(label="guideline", value="Do something once")

# Print the XML representation
print(item.to_xml())
```

### Using `PromptSection`

```python
from promptxml import PromptSection, PromptItem

# Create a new PromptSection
section = PromptSection(label="guidelines")

# Add items to the section
section.add(
    PromptItem(label="guideline", value="Do something once"),
    PromptItem(label="guideline", value="Do something twice")
)

# Print the XML representation
print(section.to_xml())
```

### Nested `PromptSection` and `PromptItem`

```python
from promptxml import PromptItem, PromptSection

# Create a new section with nested items and sections
section = PromptSection(label="guidelines")

section.add(
    PromptItem(label="guideline", value="Do something once"),
    PromptItem(label="guideline", value="Do something twice"),
    PromptSection(
        label="guideline",
        items=[
            PromptItem(label="instruction", value="This is a complex instruction with nested list."),
            PromptSection(
                label="some_items",
                items=[
                    PromptItem(label="some_item", value="This is item 1"),
                    PromptItem(label="some_item", value="This is item 2"),
                    PromptItem(label="some_item", value="This is item 3"),
                ],
                instruction="instructions can also be in attributes!, and it can contain some \"quotes\" and 'other quotes'",
                second_attr="qwerty",
            ),
        ],
    ),
    PromptSection(
        label="guideline",
        items=[
            PromptItem(
                label="instruction",
                value="This is a second complex instruction with nested list built with build_multiple.",
            ),
            PromptSection(
                label="some_items",
                items=PromptItem.build_multiple(
                    label="some_item",
                    values=[
                        "This is item 1",
                        "This is item 2",
                        "This is item 3",
                    ],
                ),
            ),
        ],
    ),
)

# Print the XML representation and pretty-print it
print(section.to_xml())
print(section.make_pretty())
```

## Troubleshooting

If you encounter any issues, please visit the [issues section](https://github.com/barabum0/promptxml/issues) on GitHub to report a problem or seek assistance.

## Contribution

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request. For detailed contribution guidelines, please refer to the [CONTRIBUTION.md](CONTRIBUTION.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.