import string

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Xoá dấu câu khỏi mỗi dòng văn bản
text_without_punctuation = [''.join(char for char in line if char not in string.punctuation) for line in text]

# Xuất văn bản không dấu câu ra file.txt
output_file_path = 'Xoá dấu.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    for line_without_punctuation in text_without_punctuation:
        file.write(line_without_punctuation + '\n')

print(f"Text without punctuation written to {output_file_path}")
