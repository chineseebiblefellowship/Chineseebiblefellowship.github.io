import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

def generate_html(chapters):
    html_content = '''<html>
<head>
    <title>圣经章节</title>
</head>
<body>
'''
    for title, text in chapters:
        html_content += f'<h1>{title}</h1>\n'
        lines = text.split('\n')
        verse_number = 1
        for line in lines:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            
            # Check if the line starts with a digit (indicating a verse)
            if line[0].isdigit():
                parts = line.split(' ', 1)
                if len(parts) == 2:
                    number, content = parts
                    html_content += f'<div class="verse">\n'
                    html_content += f'    <span class="verse-number">{number}</span> {content}\n'
                    html_content += f'</div>\n'
            else:
                # If the line does not start with a digit, add a default verse number
                html_content += f'<div class="verse">\n'
                html_content += f'    <span class="verse-number">{verse_number}</span> {line}\n'
                html_content += f'</div>\n'
                verse_number += 1
    
    html_content += '''</body>
</html>'''
    
    return html_content

def generate_and_display_html():
    num_chapters = simpledialog.askinteger("输入章节数量", "请输入要生成的章节数量：", minvalue=1)
    if not num_chapters:
        return
    
    chapters = []
    for i in range(num_chapters):
        title = simpledialog.askstring("输入章节标题", f"输入第 {i+1} 个章节的标题：")
        if not title:
            messagebox.showwarning("警告", "章节标题不能为空")
            return
        
        text = simpledialog.askstring("输入章节内容", f"输入第 {i+1} 个章节的内容（用换行符分隔）：")
        if not text:
            messagebox.showwarning("警告", "章节内容不能为空")
            return
        
        chapters.append((title, text))
    
    html_content = generate_html(chapters)
    
    # Display HTML content in a new window
    display_window = tk.Toplevel(root)
    display_window.title("生成的 HTML")

    # Create a ScrolledText widget to display the HTML content
    html_display = scrolledtext.ScrolledText(display_window, width=80, height=20, wrap=tk.WORD, font=('Arial', 12))
    html_display.pack(padx=10, pady=10)
    html_display.insert(tk.END, html_content)
    html_display.config(state=tk.DISABLED)  # Make the text read-only
    
    messagebox.showinfo("完成", "所有章节已成功生成并显示！")

# 创建主窗口
root = tk.Tk()
root.title("圣经章节 HTML 生成器")

# 创建主框架
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# 创建按钮
generate_button = tk.Button(frame, text="生成并显示 HTML", command=generate_and_display_html, font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', relief=tk.RAISED)
generate_button.pack(pady=10)

# 启动主循环
root.mainloop()
