FROM python:3.13-slim

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Node.js 和 npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 依賴管理工具
RUN pip install uv

# 複製依賴配置文件
COPY pyproject.toml uv.lock ./
COPY package*.json ./

# 安裝依賴
RUN uv sync
RUN npm ci --production

# 複製前端源碼和配置文件
COPY src/ ./src/
COPY tailwind.config.js ./

# 複製所有專案文件
COPY . .

# 建置前端資源和收集靜態檔案
RUN npm run build
RUN python manage.py collectstatic --noinput

# 設定環境變數
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=fitcal.settings
ENV PORT=8000

# 暴露端口（但實際使用的是環境變量中的端口）
EXPOSE 8000

# 使用 gunicorn 啟動應用
CMD gunicorn fitcal.wsgi:application --bind 0.0.0.0:$PORT --workers $WEB_CONCURRENCY

