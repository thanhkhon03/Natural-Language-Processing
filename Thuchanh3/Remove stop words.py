import nltk
from nltk.corpus import stopwords

# Tải xuống dữ liệu NLTK cần thiết
nltk.download('stopwords')

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']


stop = stopwords.words('vietnamese')
# Loại bỏ mật khẩu tiếng Việt trong mỗi dòng văn bản
text_without_stopwords = [' '.join(word for word in line.split() if word.lower() not in stop) for line in text]

# In ra kết quả
print(text_without_stopwords)
