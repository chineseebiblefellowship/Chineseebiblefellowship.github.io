import os
import glob

# 定义插入内容的文件路径
insert_file_path = 'insert.html'

# 定义目标文件夹路径
source_folder = 'leviticus-chapters/'

# 读取插入内容
with open(insert_file_path, 'rb') as f:
    insert_content = f.read()

# 查找所有 HTML 文件
html_files = glob.glob(os.path.join(source_folder, 'leviticus-chapter-*.html'))

for file_path in html_files:
    try:
        with open(file_path, 'rb+') as file:
            content = file.read()
            
            # 查找 <body> 标签的位置
            body_pos = content.find(b'<body>')
            if body_pos != -1:
                # 插入内容
                body_pos_end = content.find(b'</body>', body_pos)
                if body_pos_end != -1:
                    new_content = (content[:body_pos + len(b'<body>')] +
                                   insert_content +
                                   content[body_pos + len(b'<body>'):body_pos_end] +
                                   content[body_pos_end:])
                    
                    # 写入修改后的内容
                    file.seek(0)
                    file.write(new_content)
                    file.truncate()
    except Exception as e:
        print(f"无法处理文件 {file_path}: {e}")

print("所有文件已修改。")
