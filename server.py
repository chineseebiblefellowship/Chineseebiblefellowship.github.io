import socket
import os

def create_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server is running on http://{host}:{port}/")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # 解析请求行
        request_line = request.split('\n')[0]
        request_path = request_line.split(' ')[1]

        # 发送HTTP响应
        response = build_http_response(request_path)
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

def build_http_response(request_path):
    # 确定文件扩展名和内容类型
    file_extension = os.path.splitext(request_path)[1]
    if file_extension == '.html':
        content_type = 'text/html; charset=UTF-8'
    elif file_extension == '.css':
        content_type = 'text/css; charset=UTF-8'
    elif file_extension == '.js':
        content_type = 'application/javascript; charset=UTF-8'
    else:
        content_type = 'text/plain; charset=UTF-8'

    # 构建文件路径
    file_path = os.path.join(os.getcwd(), request_path[1:] if request_path.startswith('/') else request_path)

    # 检查文件是否存在
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
        response_header = f"""\
HTTP/1.1 200 OK
Content-Type: {content_type}
Content-Length: {len(content)}
Connection: close

"""
        response = response_header + content.decode('utf-8') if file_extension in ['.html', '.css', '.js'] else response_header + content
    else:
        response = f"""\
HTTP/1.1 404 Not Found
Content-Type: text/plain; charset=UTF-8
Content-Length: 22
Connection: close

404 Not Found
"""

    return response

create_server('192.168.1.102', 8000)