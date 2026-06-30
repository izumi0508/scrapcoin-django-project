# ScrapCoin

## 專案介紹

一個使用Django建立的虛擬貨幣市場資料平台，整合Binance API，自動蒐集白名單幣種的歷史K線資料，並透過REST API提供查詢服務。

## 技術架構
Backend
- Django
- Django REST Framework

Database
- PostgreSQL

Crawler
- Binance REST API

Testing
- Django Test Framework

Deployment
- Docker（進行中）

## 功能

✅ WatchList 管理

✅ 歷史K線收集

✅ REST API

✅ Filtering

✅ Ordering

✅ Serializer

✅ Model Test

✅ API Test

🚧 Docker

🚧 Scheduler

🚧 Deployment

## API

## 如何安裝

## 如何使用

更新最近一筆K線
python manage.py fetch_kline

## 專案結構

scrapcoin/

├── crypto/

│   ├── models.py<br>
│   ├── views.py<br>
│   ├── serializers.py<br>
│   ├── tests/<br>
│   └── management/<br>
│       └── commands/  

├── requirements.txt

├── docker-compose.yml

└── README.md

## 未來規劃

[✓] Price API

[✓] Historical Kline

[✓] WatchList

[✓] PostgreSQL

[✓] Testing

[ ] Docker

[ ] Scheduler

[ ] Redis Cache

[ ] Celery

[ ] WebSocket

[ ] Deploy

[ ] Frontend Dashboard

## Author
