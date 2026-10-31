# QA Automation Portfolio

品質リスク分析、テスト手法の選定、自動化範囲とCI運用を実践するQAポートフォリオです。  
API・UI・性能テストを、検出価値、実行頻度、保守コストに基づいて使い分けています。

![tests](https://github.com/Ishii74/qa-automation-portfolio/actions/workflows/test.yml/badge.svg)

## 示すスキル

- 品質リスク分析と優先順位付け
- UI、API、性能、手動テストの役割分担
- 自動化する・しない判断の根拠づけ
- Playwright / pytest / Page Objectによる主要導線の回帰
- Postman / NewmanによるAPIテスト
- JMeterによる目的別負荷テスト
- GitHub Actionsによるテスト自動実行

## テスト戦略

| リスク | 主担当 | 補完層 |
|---|---|---|
| ログイン失敗 R-01 | API + UI | 手動、A11y候補 |
| 権限外アクセス R-02 | API | UI代表例、手動 |
| カート状態不整合 R-03 | UI/E2E | API |
| 購入結果の不整合 R-04 | API + UI | 性能・A11y・手動の限定確認 |
| 表示・操作性 R-05 | 手動 + A11y | UI |
| 負荷時の劣化 R-06 | JMeter | API確認 |

## 実装済み領域

| 種類 | 対象 | 実装 |
|---|---|---|
| UIテスト | SauceDemo | `tests/ui/`、`pages/` |
| APIテスト | JSONPlaceholder | `tests/api/jsonplaceholder.postman_collection.json` |
| 負荷テスト成果物 | OWASP Juice Shop（ローカル） | `jmeter/` |
| 性能結果の集計 | JMeter JTLの平均・p95・最大・エラー率 | `scripts/analyze_jmeter.py` |
| CI | push / pull request | `.github/workflows/test.yml` |
| 依存関係セキュリティ | PR・週次のPython依存関係監査 | `.github/workflows/security.yml` |
| テスト設計 | リスク分析、継続改善、カバレッジ | `docs/01-system-overview.md`から始まる設計書 |

アクセシビリティ自動テスト、夜間クロスブラウザ、回帰・夜間・性能ワークフローの分割、Datadog等によるAPM可観測性連携は未実装です。

## 選定理由

- APIは正常・異常・境界値・認証/認可を高速かつ再現性の高い形で確認できるため、自動化を優先します。
- UIはログイン、カート、チェックアウトなど主要導線に限定し、Page Objectで保守性を確保します。
- 性能は機能テストでは検出しづらい非機能リスクのため、JMeterを通常の機能CIと分離します。
- UXや探索的テストは人の判断が必要なため、自動化対象から外し、手動テストとして残します。

---

## 設計ドキュメント

- [システム概要](docs/01-system-overview.md)
- [品質リスク分析](docs/02-quality-risk-analysis.md)
- [テスト戦略](docs/03-test-strategy.md)
- [自動化選定](docs/04-automation-selection.md)
- [テストカバレッジマップ](docs/05-test-coverage-map.md)
- [CI戦略](docs/06-ci-strategy.md)
- [品質指標](docs/07-quality-metrics.md)
- [改善履歴](docs/08-improvement-log.md)

---

## 実行方法

### UIテスト

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest tests/ui
```

ブラウザの動きを確認する場合は次を使います。

```powershell
pytest tests/ui --headed --slowmo 500
```

### APIテスト

```powershell
npm install -g newman
newman run tests/api/jsonplaceholder.postman_collection.json
```

### 負荷テスト

Juice Shopをローカルで起動し、JMeterのGUIまたは非GUIモードで実行します。

```powershell
jmeter -n -t jmeter/juice-shop-loadtest.jmx -l jmeter/results.jtl -e -o jmeter/report
```

`jmeter/report`は空または未作成の状態で実行してください。負荷テストは自分のローカル環境だけで実施します。

### 性能結果の集計

```powershell
python scripts/analyze_jmeter.py jmeter/results.jtl
python scripts/analyze_jmeter.py jmeter/results.jtl --max-p95-ms 1000 --max-error-rate-pct 5
```

集計結果は平均、p95、最大応答時間、サンプル数、エラー率を示します。閾値は学習用の仮置きです。

### セキュリティ監査

PRと毎週月曜日、または手動実行時に`pip-audit`でPython依存関係を確認します。監査で検出された既知脆弱性は、影響と修正方法を確認して対応します。

## 継続的品質改善

性能劣化や不具合は、`検知 → 観測 → 原因仮説 → 改善 → 再検証`の順で扱います。JMeter JTLは`analyze_jmeter.py`でBefore/Afterに集計します。Datadogが未導入の環境では、まずJMeter指標、HTTPステータス、ログ、ローカル環境情報を観測します。導入済みのAPM、Logs、Metrics、Tracesとテスト結果を関連付ける仕組みはTODOです。

## レポートと失敗証跡

- Playwright失敗時は`test-results/`へスクリーンショット・トレースを保存します。
- `jmeter/report/`には生成済みのHTMLレポートがあります。
- GitHub Actionsの失敗ジョブからUIテストのArtifactを確認できます。
- 製品不具合、テスト不具合、環境不具合、外部依存不具合を分けて扱います。

## 注意

- SauceDemoは仕様書がないため、画面挙動から要求を推定しています。
- Juice Shopは脆弱性を含む練習用アプリです。外部公開や本番利用は行いません。
- 負荷テストの応答時間・エラー率は学習用の仮置き閾値です。
