from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

# Nối tất cả các dòng thành một chuỗi
all_text = ' '.join(text)

# Tạo khối Word Cloud
wordcloud = WordCloud(width=800 , height=400 ,background_color='white').generate(all_text)

# Hiển thị đám mây từ
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
