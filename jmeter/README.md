# JMeter（非機能テスト）

**状態：未作成（`load-test.jmx` はこれから作る）**

## 対象
- 自分のPC上で動かす OWASP Juice Shop（`http://localhost:3000`）
- **他人のサイトや公開サイトには、負荷をかけない。** Juice Shopは脆弱性を含む練習用アプリなので、外部に公開しない。

## 作るもの
- `load-test.jmx`：通常負荷のテストプラン（10同時ユーザー、立ち上げ10秒、1分間）
  - ログイン → 商品検索 → カート追加 の一連の操作
  - 確認する指標：平均・95パーセンタイル・最大の応答時間、エラー率（目標値は `docs/test-design.md` の「2-2. 非機能」）
- `data/users.csv`：テスト用ユーザー（ダミー。実在のアドレスではない）。CSV Data Set Config で読み込む。
- `results/`：実行結果（Gitには入れない）

## 作る前に確認すること
- Juice Shopの起動方法（Docker または npm）
- ログイン・商品検索・カート追加のリクエスト内容（ブラウザの開発者ツールの Network タブで確認。バージョンで変わることがある）

## 実行（非GUI）
```
jmeter -n -t jmeter/load-test.jmx -l jmeter/results/result.jtl -e -o jmeter/results/report
```
`results/report` は、空か、存在しない状態にしておく。
