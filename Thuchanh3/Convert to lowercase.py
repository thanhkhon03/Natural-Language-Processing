import pandas as pd

text = ['Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Vì sao Nhật Bản thất bại ở Asian Cup 2023?',
        'Sai lầm chiến thuật', 
        'Sự thiếu quyết tâm của cầu thủ', 
        'Phản ứng chậm chạp từ HLV Hajime Moriyasu', 
        'Hậu trường bất ổn góp phần khiến Nhật Bản', 
        'Bị loại ở tứ kết Asian Cup.']

df = pd.DataFrame({'tweet': text})

# Chuyển thành tất cả thành chữ thường
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Xuất DataFrame thành file.txt
output_file_path = 'Chuyển thành chữ thường.txt'
df.to_csv(output_file_path, index=False, header=False, sep='\t', encoding='utf-8')

print(f"Processed text written to {output_file_path}")

