import pdfkit

def create_pdf_from_url(url, filename="article.pdf"):

    config = pdfkit.configuration(wkhtmltopdf="C:\\Users\\User\\Documents\\ArchiverProject\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    options = {
        'javascript-delay': '5000',  # Wait 5 seconds for JS to load content
        'no-stop-slow-scripts': None,
        'custom-header': [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/92.0.4515.107 Safari/537.36')
        ],
        'custom-header-propagation': '',
        'print-media-type': '',
        'load-error-handling': 'ignore',      # ignore errors when loading content
        'load-media-error-handling': 'ignore'   # ignore errors for media content
    }
    try:
        pdfkit.from_url(url, filename, options=options, configuration=config)
    except Exception as e:
        pass
    print(f"PDF saved as {filename}")

if __name__ == '__main__':
    url = input("Enter the article URL: ")
    create_pdf_from_url(url, filename="article.pdf")