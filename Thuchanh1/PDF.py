import fitz  

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    pdf_document.close()
    return text

def write_text_to_file(text, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

pdf_path = "Chuong2_input_sample.pdf"
output_file_path = "Chuong2_input_sample.txt"


pdf_text = extract_text_from_pdf(pdf_path)
write_text_to_file(pdf_text, output_file_path)

print(f"Đã xuất dữ liệu file PDF sang {output_file_path}")
