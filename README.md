# Flask Datadog APM Demo

這是一個示範如何在 Flask 應用程式中整合 Datadog APM 的專案。

## 功能

- 基本的 Flask Web 應用程式
- Datadog APM 整合
- Docker 容器化部署
- 簡單的 API 端點示範

## 安裝需求

- Python 3.10+
- Docker
- Docker Compose
- Datadog 帳號

## 快速開始

1. 克隆專案：
```bash
git clone [您的 GitHub 倉庫 URL]
cd flask-datadog-apm
```

2. 設定環境變數：
```bash
# 在 docker-compose.yml 中設定您的 Datadog API 金鑰
DD_API_KEY=your_api_key_here
```

3. 啟動服務：
```bash
docker-compose up -d
```

4. 訪問應用程式：
```bash
curl http://localhost:5000/check-datadog
```

## API 端點

- `GET /`: 顯示歡迎訊息
- `GET /check-datadog`: 檢查 Datadog 網站可用性

## 監控

在 Datadog APM 中，您可以看到：
- 請求追蹤
- 性能指標
- 錯誤追蹤

## 授權

MIT License 