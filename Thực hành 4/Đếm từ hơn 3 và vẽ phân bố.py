import matplotlib.pyplot as plt

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Nối tất cả các dòng thành một chuỗi
all_text= ' '.join(text)

#Chia chuỗi thành các từ
words = all_text.split ()

# Đếm các từ có độ dài lớn hơn 3
word_counts = sum(1 for word in words if len(words)>3 )

# Vẽ sơ đồ phân tích
plt.bar(['Từ > 3'], [word_counts], color='skyblue')
plt.xlabel('Độ dài của từ')
plt.ylabel('Số từ lập lại')
plt.title('Từ có độ dài > 3')
plt.show()
