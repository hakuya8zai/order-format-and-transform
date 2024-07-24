# orderFormatTransform

## Repo 架構

```
asiaYo/
├── app/
│   ├── api/
│   │   ├── order.py            # orders API route
├── order/
│   ├── order_services.py       # 商業邏輯
│   ├── utils/
│   │   ├── transformers/
│   │   │   ├── currency_transformer.py    # 金額轉換
│   │   ├── validators/
│   │   │   ├── order_validators.py        # 驗證功能
│   ├── models/
│   │   ├── order_models.py     # 資料模型
│   ├── schemas/
│   │   ├── order_schemas.py    # 資料格式
├── main.py                     # FastAPI app
├── README.md
├── requirements.txt
```
