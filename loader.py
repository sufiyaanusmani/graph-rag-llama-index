from pathlib import Path
from ebooklib import epub
from llama_index.core import SimpleDirectoryReader

def _extract_epub_metadata(book_path: str) -> dict:
    book_path = Path(book_path)
    if not book_path.exists():
        raise FileNotFoundError(f"EPUB file not found at path: {book_path}")
    book = epub.read_epub(str(book_path))

    return {
        "title": book.get_metadata("DC", "title")[0][0].rstrip(".epub") if book.get_metadata("DC", "title") else "N/A",
        "author": book.get_metadata("DC", "creator")[0][0] if book.get_metadata("DC", "creator") else "",
        "language": book.get_metadata("DC", "language")[0][0] if book.get_metadata("DC", "language") else "",
        "description": book.get_metadata("DC", "description")[0][0] if book.get_metadata("DC", "description") else "",
        "type": "epub",
        "embeddings": "openaiembeddings"
    }


def load_epubs_from_dir(input_dir):
    return SimpleDirectoryReader(input_dir=input_dir, file_metadata=_extract_epub_metadata).load_data()