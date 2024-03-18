text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Separate words in each line of text
separated_words = [line.split() for line in text]

# Print the result
for line_words in separated_words:
    print(line_words)
