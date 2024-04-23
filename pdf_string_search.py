import argparse
import fitz  # PyMuPDF library for working with PDFs
import requests

def find_string_in_pdf(pdf_url, search_string):
    try:
        # Open the PDF document
        doc = fitz.open(stream=requests.get(pdf_url, stream=True).content, filetype="pdf")
        result = []
        # Iterate through each page
        for page in doc:
            # Search for the text using text rectangles
            text_blocks = page.get_text("blocks")
            for block in text_blocks:
                block_text = block[4]  # Extract the text content from the block
                if search_string in block_text:
                    x0, y0, x1, y1 = block[:4]
                    page_width = page.mediabox.width
                    page_height = page.mediabox.height
                    y_inverted = page_height - y0 # Invert y-coordinate
                    result.append([page.number+1, x0, y_inverted, x0, y0])

    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")
        return None

    if result:
        return result
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for a string in a PDF file.')
    parser.add_argument('pdf_url', type=str, help='URL of the PDF file')
    parser.add_argument('search_string', type=str, help='String to search in the PDF')
    args = parser.parse_args()

    coordinates = find_string_in_pdf(args.pdf_url, args.search_string)
    print(coordinates)
