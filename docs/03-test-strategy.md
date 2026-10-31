# 03. テスト戦略

## テスト層の役割

| 層 | 主な目的 | 対象 | 実行頻度 |
|---|---|---|---|
| UI Smoke | 主要導線の破壊を高速検出 | ログイン、カート、チェックアウト | PR |
| UI Regression | 主要機能の回帰確認 | Playwright/Python/pytest | main・夜間 |
| API Smoke | 入出力・ステータス・主要条件の確認 | JSONPlaceholder Newman | PR |
| API Regression | 正常・異常・境界・認証/認可・スキーマ | Postman/Newman | main・夜間 |
| A11y | 主要画面の機械的なアクセシビリティ確認 | TODO: axe等の導入後 | PR・main |
| Performance | 応答時間・エラー率・スループットの確認 | JMeter | 必要時・夜間候補 |
| Exploratory / Manual | UX、探索的シナリオ、人の判断が必要な確認 | 実画面 | リリース前 |

## 自動化方針

- APIを優先し、組合せと境界値を高速・安定に確認する。
- UIは主要ユーザージャーニーに絞り、Page Objectで保守性を確保する。
- 性能テストは機能テストとは分離し、目的に応じてSmoke/Load/Stress/Spikeを使う。
- 自動判定の価値が低いUXや探索的確認は手動テストとして残す。

## 終了基準

1. PR品質ゲートで重大なUI/API破壊が検出されないこと。
2. 既存回帰テストがmainへの変更で実行されること。
3. 失敗時にスクリーンショット、トレース、Newman/JMeter結果を確認できること。
4. 未実装項目がTODOとして明示され、実装済みと誤認されないこと。

## 現在の制約

- アクセシビリティ自動テストはまだ導入していない。
- APIテストはJSONPlaceholderの収集済みPostmanコレクションに限定される。
- 夜間クロスブラウザ実行は設計済みだが、現行CIでは未実装である。
