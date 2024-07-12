# RenderKit

RenderKit is a lightweight HTML rendering engine designed to convert HTML elements into Tkinter widgets for Python GUI applications.

For more, check out the [github repository](https://github.com/cj-praveen/RenderKit).

## Basic Usage
```python
# Import the RenderKit class from the module
from RenderKit import RenderKit

# Read the HTML file and store its content
with open("filename.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Create an instance of RenderKit with the HTML content
RenderKit(html_content)
```

## License
Free and Open-source under [MIT License](LICENSE)
