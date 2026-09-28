# Course Roadmap

Programming Lab Iでは、15回を通して同じMaze programを育てていきます。

```text
One small script
→ Objects
→ Data structures
→ Algorithms
→ Modules
→ Tests
→ Collaborative development
→ Software
```

## 4つの段階

| Weeks | 段階 |
| --- | --- |
| 1–5 | 基礎の復習とオブジェクト指向 |
| 6–9 | データ構造とアルゴリズム |
| 10–12 | ソフトウェアとしての構造化・テスト・再現可能性 |
| 13–15 | 共同開発・コードレビュー・CI・Release |

## 全15回の予定

| 回 | 学修テーマ | 主な学修内容 | Mazeをどう育てるか |
| --- | --- | --- | --- |
| 1 | イントロダクションと前期の復習 | Python、VS Code、Git/GitHub、既存コードを実行する・読む・変更する | 小さなstarter programを実行し、読み、少し変更してcommitする |
| 2 | クラスとオブジェクト | class、object、attribute、method | 関連するdataとfunctionを、objectとしてまとめる |
| 3 | コンストラクタとカプセル化 | `__init__`、`self`、object state、property、情報の隠蔽 | objectの状態を安全に扱えるようにする |
| 4 | 継承とコードの再利用 | inheritance、parent / child class、`super()` | 共通部分を再利用し、種類の違う要素を追加する |
| 5 | ポリモーフィズムと共通インターフェース | override、common interface、interchangeable implementations | 同じ呼び出し方で、異なる振る舞いを入れ替えられるようにする |
| 6 | データ構造① | list、tuple、list comprehension | Mazeや位置の表し方を見直す |
| 7 | データ構造② | dict、set、stack、queue | 目的に合ったdata structureを選んで使う |
| 8 | 探索アルゴリズム | search、DFS、BFS、recursion、Maze Solver | Mazeを自動で解くSolverを作る |
| 9 | ソートと計算量 | sorting、algorithm comparison、execution time、Big-Oの基礎 | 複数のalgorithmを比較・計測する |
| 10 | モジュールとパッケージ | module、package、import、responsibility separation | 1つのfileを責任ごとに分割する |
| 11 | 例外処理・デバッグ・自動テスト | try / except、debugger、pytest、normal / abnormal cases | 異常な入力に備え、自動テストを追加する |
| 12 | ファイル操作・データ・再現可能性 | file I/O、`with`、CSV / JSON、reproducibility | Mazeや結果をfileから読み込み・保存する |
| 13 | Git/GitHubによる共同開発 | Issue、branch、commit、merge、conflict、Pull Request、code review | 複数人でbranchとPull Requestを使って機能を追加する |
| 14 | 他者・生成AIのコードを読む・検証する・改善する | code reading、code review、refactoring、AI-assisted coding、human verification | 他者や生成AIのコードを読み、検証し、改善する |
| 15 | 統合・CI・Release | clean code、integration、GitHub Actions、CI、final verification、GitHub Release | 統合・自動検証を行い、softwareとしてReleaseする |
