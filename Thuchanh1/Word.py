from docx import Document

def extract_text_from_word(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def write_text_to_file(text, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)


docx_path = "Chuong2_input_sample.docx"
output_file_path = "Word.txt"


word_text = extract_text_from_word(docx_path)
write_text_to_file(word_text, output_file_path)

print(f"Đã xuất dữ liệu file Word sang {output_file_path}")
