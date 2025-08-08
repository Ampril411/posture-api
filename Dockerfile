# 使用官方 Python 基础镜像
FROM python:3.11-slim

# 安装系统依赖，包括 libgl1
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 启动命令
CMD ["python", "app.py"]
