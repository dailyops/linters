# Spindle - Spinnaker Template Linter

A linter tool to validate **Jinja2** and **SpEL (Spring Expression Language)** syntax within Spinnaker templates (originally) or general .j2 extension files. This script helps identify syntax errors, ensuring smooth pipeline execution.

---

## Features

- Validates **Jinja2** syntax, including custom tags (like `do`)
- Validates **SpEL** syntax within templates
- Checks for **balanced brackets and quotes** in SpEL expressions
- Identifies issues with **unrecognized Jinja2 filters**
- Displays **line numbers** for easy debugging

---

## Installation

Clone the repository:

```bash
git clone git@github.com:dailyops/linters.git
cd linters
pip3 install Jinja2
```

---

## Usage

Run the linter with the following command:

```bash
python spintax.py <template_file_path>
```

### Example

```bash
python3 spindle.py example-template.j2
```

---

## Output

The linter will output results in the following format:

```
[Jinja2] example-template.j2: Syntax OK
[SpEL] example-template.j2 (Line 12): Possible Syntax Error: ${execution['trigger']['user']}
```

- **Jinja2 Syntax OK**: No syntax issues detected.
- **SpEL Syntax OK**: No syntax issues detected.
- **Possible Syntax Error**: Detected potential issues with SpEL expressions.

---

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have feature suggestions. Contributions are always welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
