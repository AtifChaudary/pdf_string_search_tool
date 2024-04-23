# PDF String Search Tool

This Python script allows you to search for a specific string within a PDF document. It utilizes the PyMuPDF library (`fitz`) for PDF processing and provides a command-line interface for ease of use.

## How to Use

1. **Installation**: Ensure you have Python installed on your system along with the necessary dependencies. You can install the required libraries by running:


`
pip install PyMuPDF requests
`


2. **Usage**: Run the script from the command line with the following arguments:


`
python pdf_string_search.py <pdf_url> <search_string>
`


- `<pdf_url>`: URL of the PDF file you want to search within.
- `<search_string>`: The string you want to find within the PDF.

3. **Output**: The script will print the coordinates of the found string in the format `[page_number, x0, y0, x1, y1]`, where:
- `page_number`: The page number where the string was found (1-indexed).
- `x0, y0, x1, y1`: Coordinates of the bounding box around the found string.

## Example

```bash
python pdf_string_search.py https://example.com/example.pdf "search_string"
```

# Dependencies
* PyMuPDF: A Python binding to the MuPDF C library, providing access to PDF parsing and rendering facilities.
* Requests: An elegant and simple HTTP library for Python, allowing easy retrieval of content from URLs.
