# WhaleAlertMonitor

**WhaleAlertMonitor** — это мониторинг крупных переводов токенов в Ethereum. Отличный инструмент для трейдеров, аналитиков и ботов.

## 🔍 Что делает

- Следит за событиями Transfer ERC-20 токена
- Выводит в консоль крупные переводы ("киты")
- Поддерживает любую точность токена и порог

## ⚙️ Настройка

Создайте `.env` файл:

```
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_KEY
TOKEN_CONTRACT=0xYourTokenAddress
MIN_THRESHOLD=100000
DECIMALS=18
```

- `MIN_THRESHOLD` — минимальное количество токенов для отображения
- `DECIMALS` — десятичные знаки токена

## ▶️ Запуск

```
pip install -r requirements.txt
python whale_alert_monitor.py
```

## 💡 Применение

- Отслеживание действий китов
- Алгоритмическая торговля
- Сигналы для Telegram/Discord

## 🛡 Требования

- Контракт должен быть стандартным ERC-20
- Подключение к Ethereum через Infura

## 📜 License

MIT
