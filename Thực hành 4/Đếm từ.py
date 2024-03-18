text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Nối tất cả các dòng thành một chuỗi
all_text = ' ' .join(text)

# Đếm số từ 
word_count = len(all_text.split())

print("Số từ của văn bản là ",word_count)