from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fetch_article import fetch_article

def create_pdf(article, filename="article.pdf"):
    """
    Creates a PDF file containing the article title and content.
    """
    # Create a canvas with letter-sized pages
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Set starting y position (with margin)
    y = height - 50

    # Write the title in bold
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, article['title'])
    y -= 30  # move down

    # Write the content in a regular font
    c.setFont("Helvetica", 12)
    
    # Use a text object to handle multiple lines and basic wrapping
    text_object = c.beginText(50, y)
    text_object.setLeading(15)  # space between lines
    text_object.textLines(article['content'])
    
    c.drawText(text_object)

    # Save the PDF file
    c.save()
    print(f"PDF saved as {filename}")

if __name__ == '__main__':
    # For demonstration, fetch an article and create a PDF:
    url = input("Enter the article URL: ")
    article = fetch_article(url)
    if article:
        print("Fetched article:", article['title'])
        create_pdf(article, filename="article.pdf")