from bs4 import BeautifulSoup

# Read HTML content from a file
with open('example.html', 'r', encoding='utf-8') as file:
    html_cont = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser')

# Extract text from all tags
all_tags = soup.find_all()
for tag in all_tags:
    print(tag.get_text())
