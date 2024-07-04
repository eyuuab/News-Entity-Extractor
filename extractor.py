import spacy
from newspaper import Article
from collections import defaultdict

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

def get_article_text(url):
    """Downloads and parses the article from the given URL."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def extract_entities(text):
    """Extracts named entities from the text using SpaCy."""
    doc = nlp(text)
    entities = defaultdict(list)
    for ent in doc.ents:
        entities[ent.label_].append(ent.text)
    return entities

def highlight_entities(text, entities):
    """Highlights entities in the text by surrounding them with brackets and their label."""
    doc = nlp(text)
    highlighted_text = text
    for ent in reversed(doc.ents):
        start = ent.start_char
        end = ent.end_char
        highlighted_text = highlighted_text[:start] + f"[{ent.text}]({ent.label_})" + highlighted_text[end:]
    return highlighted_text


url = "https://bbc.com/future/article/20240510-floppy-disks-why-some-people-are-still-in-love-with-this-obsolete-computer-storage-technology"
article_text = get_article_text(url)

print("Original Text:")
print(article_text[:500])

extracted_entities = extract_entities(article_text)

print("\nExtracted Entities:")
for entity_type, entity_list in extracted_entities.items():
    print(f"{entity_type}: {', '.join(set(entity_list))}")


highlighted_text = highlight_entities(article_text[:500], extracted_entities)
print("\nHighlighted Text:")
print(highlighted_text)
