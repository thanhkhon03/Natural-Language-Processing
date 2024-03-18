from collections import Counter

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Nối tất cả các dòng thành một chuỗi
all_text = ' ' .join(text)

# Chia chuỗi thành các từ
words=all_text.split()

# Đếm tần số của mỗi từ
word_frequency = Counter (words)

print ("Tần số các từ xuất hiện là", word_frequency)