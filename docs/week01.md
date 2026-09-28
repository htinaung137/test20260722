# Week 1: イントロダクションと前期の復習

**Run → Read → Change → Commit**

この資料は、授業中の実習手順と、Week 1を欠席した人のCatch-up Guideを兼ねています。
一人で進める場合も、30～45分程度で最低限の内容を終えられます。

## 準備

以下が使える状態にしておいてください。

- Python 3
- VS Code
- Git
- Terminal（Windowsでは PowerShell や Git Bash など）

## Step 1: Repositoryをclone

```bash
git clone <REPOSITORY_URL>
```

`<REPOSITORY_URL>` は授業で案内されるURLに置き換えてください。

## Step 2: Repositoryへ移動

```bash
cd programming-lab-maze
```

VS Codeで `programming-lab-maze` フォルダを開いておくと、この後の作業がしやすくなります。

## Step 3: Mazeを実行

```bash
python starter.py
```

`python` が見つからない場合は `python3 starter.py` を試してください。

## Step 4: Mazeを操作

- `W` / `A` / `S` / `D` を入力してEnterを押し、`P`（Player）を `G`（Goal）まで移動させてください。
- `#`（Wall）には進めないことを確認してください。
- `W/A/S/D/Q` 以外を入力するとどうなるか試してください。
- もう一度実行し、`Q` で途中終了できることも確認してください。

## Step 5: Code Reading

VS Codeで `starter.py` を開き、以下を探してください。
見つけたら、変数名・function名や行番号をメモしておきましょう。

1. Mazeの形を保存している変数はどれか？
2. Playerの現在位置を保存している変数はどれか？
3. Mazeを表示しているfunctionはどれか？
4. Playerの移動に関係するfunctionはどれか？
5. wallを通過できないようにしている処理はどこか？
6. program全体を繰り返し動かしている部分はどこか？

ヒント：位置は `x`（左から何文字目か）と `y`（上から何行目か）で表されています。どちらも `0` から数えます。

### 考えてみよう

> このprogramが10倍大きくなったら、
> 現在の書き方のどこが管理しにくくなると思いますか？

正解は一つではありません。気づいたことを自由にメモしておいてください。Week 2で使います。

## Step 6: Small Modification

以下から1つ選んで、`starter.py` を変更してください。

- wallを1か所変更する
- Goal位置を変更する
- Playerのstart位置を変更する
- PlayerやGoalの表示文字を変更する
- Mazeを少しだけ拡張する

注意：

- 変更後も、startからgoalまで到達できることを確認してください。
- Mazeの各行の文字数はそろえておきましょう。
- start位置やGoal位置は、wall（`#`）ではない場所にしてください。

## Step 7: 再実行

```bash
python starter.py
```

変更が反映されていることを確認してください。
エラーが出た場合は、メッセージを読み、どの行で問題が起きているかを確認して修正しましょう。

## Step 8: Gitで変更を確認

```bash
git status
```

`starter.py` が modified と表示されることを確認してください。

変更内容を詳しく見たい場合は、次のcommandも使えます。

```bash
git diff
```

## Step 9: Commit

```bash
git add .
git commit -m "Complete Week 1 exercise"
```

初めてcommitするときに名前やemailの設定を求められた場合は、授業の案内に従って `git config` を設定してから、もう一度commitしてください。

commit後にもう一度 `git status` を実行し、変更がcommitされたことを確認しましょう。

## Week 1 Ready Checklist

- [ ] repositoryをcloneできた
- [ ] starter.pyを実行できた
- [ ] Mazeを操作できた
- [ ] Maze / Player / Goalがどこで表現されているか確認できた
- [ ] functionを読んで役割を確認できた
- [ ] コードを1か所変更した
- [ ] 変更後に再実行した
- [ ] git statusを確認した
- [ ] git add / git commitを実行した

**ここまでできればWeek 2 Readyです。**
