# QA Automation Portfolio

テスト設計 → 自動化（UI・API）→ 負荷テスト → CI まで、QAの流れを一通り実践したポートフォリオです。

![tests](https://github.com/Ishii74/qa-automation-portfolio/actions/workflows/test.yml/badge.svg)

---

## 📌 取り組んだ内容

| 種類 | 対象 | ツール | フォルダ |
|---|---|---|---|
| UIテスト（機能） | [SauceDemo](https://www.saucedemo.com)（公開デモサイト） | Python / pytest / Playwright | `tests/ui/` |
| APIテスト | [JSONPlaceholder](https://jsonplaceholder.typicode.com)（練習用API） | Postman / Newman | `tests/api/` |
| 負荷テスト（非機能） | OWASP Juice Shop（自分のPC上） | JMeter | `jmeter/` |
| 自動実行（CI） | push のたびに UI・API テストを実行 | GitHub Actions | `.github/workflows/` |

---

## 📝 テスト設計

自動化の前に、テスト設計を作成しています。

| 成果物 | 内容 |
|---|---|
| 要求分析 | 品質目標を、あってはならない（Never）／出来なければならない（Must）／あったらいいな（Want）に分類 |
| FV表 | 機能ごとの確認項目を、Checking（仕様どおりの確認）と Testing（誤動作を狙った確認）に分けて整理 |
| テストマップ | 機能 × テスト観点で、網羅性を確認 |
| テストケース | FV表とテストマップから作成（手順・期待結果つき） |
| テスト計画書 | 範囲、自動化の対象、スケジュール、リスク、実施記録 |

- 自動化の対象は、FV表の「自動化」列で決めています（Checking を中心に選定。Testing は設計のみ）。
- 設計の資料は `docs/` にあります。

---

## 📁 フォルダ構成

```text
├─ docs/                    テスト設計・テスト計画書
├─ tests/ui/                Playwright の UIテスト
├─ tests/api/               Postman のコレクション
├─ pages/                   Page Object（画面ごとのロケーターと操作）
├─ jmeter/                  負荷テスト（Juice Shop）
├─ conftest.py              pytest の共通フィクスチャ
├─ pytest.ini               pytest の設定
└─ .github/workflows/       GitHub Actions（CI）
```

---

## ▶ 実行方法

Python 3.12（64bit）と Node.js が必要です。

### UIテスト（Playwright）

```bash
python -m venv .venv
.venv\Scripts\activate          # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest
```

ブラウザの動きを見たい場合：

```bash
pytest --headed --slowmo 500
```

### APIテスト（Postman / Newman）

```bash
npm install -g newman
newman run tests/api/jsonplaceholder.postman_collection.json
```

### 負荷テスト（JMeter）

Juice Shop を自分のPCで起動し（`http://localhost:3000`）、非GUIで実行します。

```bash
jmeter -n -t jmeter/load-test.jmx -l jmeter/results/result.jtl -e -o jmeter/results/report
```

`jmeter/results/report` は、空か、存在しない状態にしてから実行します。

### テスト結果

失敗したテストのスクリーンショットとトレースは、`test-results/` に保存されます。

---

## ⚠ 注意

- テスト対象は、公開デモサイト・練習用API・自分のPC上の環境だけです。他人のサイトや本番環境には、負荷をかけません。
- Juice Shop は、脆弱性を含む練習用アプリです。外部には公開しません。
- SauceDemo は仕様書がないため、画面の挙動から要求を推定しています。
- 負荷テストの目標値（応答時間・エラー率）は、学習用の仮置きです。

---

## ✨ このポートフォリオで示していること

- テスト設計（要求分析 → FV表 → テストマップ → テストケース）
- UI自動化（Playwright / pytest / Page Object）
- API自動化（Postman / Newman）
- 負荷テスト（JMeter）
- CIでの自動実行（GitHub Actions）
