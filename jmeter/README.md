# JMeter（非機能テスト）

**状態：ローカル負荷テスト実装済み。CIへの本番負荷実行は未実装。**

## 対象
- 自分のPC上で動かす OWASP Juice Shop（`http://localhost:3000`）
- **他人のサイトや公開サイトには、負荷をかけない。** Juice Shopは脆弱性を含む練習用アプリなので、外部に公開しない。

## 作るもの
- `juice-shop-loadtest.jmx`：Juice Shop向けの負荷テストプラン
  - ログイン → 商品検索 → カート追加 の一連の操作
  - 確認する指標：平均・95パーセンタイル・最大の応答時間、エラー率
- `data/users.csv`：テスト用ユーザー。CSV Data Set Configで利用する。
- `results.jtl`：実行結果のサンプル
- `report/`：生成済みHTMLレポート
- `scripts/analyze_jmeter.py`：JTLを集計し、閾値超過を判定する

## 作る前に確認すること
- Juice Shopの起動方法（Docker または npm）
- ログイン・商品検索・カート追加のリクエスト内容（ブラウザの開発者ツールの Network タブで確認。バージョンで変わることがある）

## 実行（非GUI）

```powershell
jmeter -n -t jmeter/juice-shop-loadtest.jmx -l jmeter/results.jtl -e -o jmeter/report
```

`jmeter/report`は空または未作成の状態で実行します。

## 集計

```powershell
python scripts/analyze_jmeter.py jmeter/results.jtl
python scripts/analyze_jmeter.py jmeter/results.jtl --max-p95-ms 1000 --max-error-rate-pct 5
```

閾値は学習用の仮置きです。実運用ではサービスのSLOに合わせて設定します。
