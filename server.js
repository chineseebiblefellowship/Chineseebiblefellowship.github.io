const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 5023;

// 提供当前目录的静态文件
app.use(express.static(__dirname));

// 返回 test.html 文件
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// 获取歌曲列表的路由
app.get('/songs', (req, res) => {
    const hymnsDir = path.join(__dirname, 'Hymns');
    
    fs.readdir(hymnsDir, (err, files) => {
        if (err) {
            return res.status(500).json({ message: '无法读取歌曲列表' });
        }
        // 过滤掉文件名中包含数字的文件
        const songs = files.filter(file => file.endsWith('.mp3') && !/\d/.test(file));
        res.json(songs);
    });
});

// 启动服务器
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
