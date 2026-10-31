# 06. CI戦略

## 実行タイミング

| タイミング | 目的 | 実行対象 | ワークフロー | 現状 |
|---|---|---|---|---|
| Pull Request | 高速フィードバック | Lint / API Smoke / UI Smoke / 主要A11y | pr-quality-gate.yml | 設計中。現行test.ymlを段階移行する。 |
| mainへのマージ | 主要機能の回帰 | API Regression / UI主要導線 / A11y | regression.yml | 設計中。現行test.ymlを維持しつつ追加する。 |
| 夜間 | 網羅性重視 | UI全回帰 / APIデータパターン / クロスブラウザ | nightly.yml | 未実装。 |
| 性能 | 非機能確認 | JMeter Smoke / Load | performance.yml | 未実装。Stress/Spikeはローカルまたは承認環境で必要時実施。 |

## 移行方針

1. 現行のtest.ymlを削除せず維持する。
2. PR品質ゲートを追加し、短いSmokeのみを実行する。
3. 回帰・夜間・性能ワークフローは対象を段階的に分離する。
4. 失敗時にはスクリーンショット、Playwright trace、Newman結果、JMeterレポートを確認できるようにする。

## 現在のCI

- PRとpushでUI・APIを実行する単一test.ymlを保持する。
- UI失敗時にtest-resultsをArtifactとして保存する。
- PR品質ゲート、回帰、夜間、性能の分割は未完了。
