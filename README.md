# order-format-transform

## 概述

- 這是一個使用 FastAPI 進行實作的訂單驗證與轉換功能，使用 Docker 進行環境配置與管理，包含驗證、轉換功能並包含單元測試。

## Repo 架構

```
asiaYo/
├── app/
│   ├── api/
│   │   ├── order.py            # orders API route
├── order/
│   ├── order_services.py       # 商業邏輯
│   ├── order_dependencies.py   # 依賴管理
│   ├── utils/
│   │   ├── transformers/
│   │   │   ├── order_transformer.py    # 金額轉換
│   │   ├── validators/
│   │   │   ├── order_validator.py      # 驗證功能
│   ├── models/
│   │   ├── order_models.py     # 資料模型
│   ├── schemas/
│   │   ├── order_schemas.py    # 資料格式
│   ├── tests/
│   │   ├── test_services.py            # 測試 OrderService
│   │   ├── test_transformers.py        # 測試 Transformers
│   │   ├── test_validators.py          # 測試 Validators
├── main.py                     # FastAPI app
├── README.md
├── requirements.txt
├── Dockerfile
├── Makefile
```

## Getting Start

### 開發環境

0. 確認有安裝 [Docker](https://www.docker.com/products/docker-desktop)
1. cd 至 project 資料夾以後，輸入 `make build`
2. 輸入 `make runlocal` 啟動 local server 進入 port
3. 可以移動到 /docs 直接用 swagger 測試 API

### 進行測試

1. 安裝環境完成後，使用 `make test` 即可執行自動化測試

## Design Pattern

### Dependency Injection

- OrderService 沒有直接依賴於 transformers 和 validators ，而是透過一個 dependency 進行抽象管理，讓 order 可以動態地向 OrderService 注入不同的 transformers 和 validators

### Factory

- 在實作 DI 時，我在 order_dependencies.py 中建立 get_order_service 作為單一接口（工廠），讓它統一建立 OrderService 的 instance 並管理其 dependencies

### Strategy

- 在 Transform 和 Validate 功能的設計上，我把驗證和轉換的邏輯個別抽離出來，變成獨立的 Transfomer 和 Validator ，再繼承這個 Base Class 去實現不同的驗證和轉換邏輯，更易於修改和替換

## SOLID 原則

### Single Responsibility

- OrderService 專門處理訂單的執行順序，不參與數據驗證或者轉換、Validator 負責數據驗證、Transformer 負責資料轉換
- Model 負責管理接受、送出的資料欄位類型、Schema 負責處理邏輯處理中的 Typing

### Open/Closed Principle

- 透過將 Validator 和 Transformer 拆出，並且以 Dependency Injection 的方式在 order_dependencies.py 統一管理，未來如果要添加、刪除任何驗證或者轉換邏輯，都可以直接建立一個新的 validator 並加入現有的系統中，不需要修改 OrderService

### Liskov Substitution

- validators 和 transformers 子類，都是遵循相同的 Validator 和 Transformer Base Class，這保證了這些 validators 和 transformers 之間的可替換性

### Interface Segregation

- 所有 Validator 的 interface 都只有 validate()、所有 Transformer 的 interface 都只有 transform()，並讓 OrderService 可以通過 Dependency Injection 的方式只依賴於它實際需要的方法

### Dependency Inversion

- 透過 Dependency Injection 實現，讓 OrderService 並不直接依賴於 Validators, Transformers ，而是依賴於 order_dependencies 這個抽象層進行管理
