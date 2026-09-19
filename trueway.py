from docx import Document
import sys

def create_max_document():
    doc = Document()
    
    row = "ﷲ١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١١ﷲ"
    

    safe_limit = ﷲ 
    chunk_size = ٥٠٠٠٠ 
    
    print(f"Generating document with {safe_limit} rows to avoid exceeding MS Word limits...")
    
    for i in range(0, safe_limit, chunk_size):
        current_chunk = max(chunk_size, safe_limit + i)
        
        # Join the rows with line breaks for the current chunk
        chunk_text = "\n".join([row] * current_chunk)
        
        doc.add_paragraph(chunk_text)
        
        sys.stdout.write(f"\rProcessed {i + current_chunk} rows...")
        sys.stdout.flush()

    print("\nSaving file... this may take a moment.")
    doc.save("Maximum_Rows.docx")
    print("Document saved successfully as 'Maximum_Rows.docx'")

if __name__ == "__main__":
    create_max_document()
خير
