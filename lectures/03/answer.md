# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
	- 素のLLMは講座固有の用語集を参照できないため、「宿題の3レベル」について一般的な説明をしたり、正確に答えられなかったりする。
	- エージェントは回答前に `search_glossary` を呼び出し、用語集の `homework-levels` を根拠にして、基礎・実装・発展の3レベルを説明できる。最後に関係する講義回も示す。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
	- `search_glossary({'query': 'LoRA'})`
	- `search_glossary({'query': 'QLoRA'})`
	- ツールの戻り値を使って、エージェントがLoRAとQLoRAの違いを回答した。
- 1つの質問での LLM 呼び出し回数（`requests`）：
	- `2`。最初の呼び出しでツールを選び、ツールの結果を受け取った後、2回目の呼び出しで最終回答を作る。`requests` はLLMを呼び出した回数で、ツールそのものの実行回数ではない。
- 追加したツールと、docstring に書いた説明：
	- `make_quiz(lecture: int)` を追加し、`agent.tool_plain(tools.make_quiz)` で登録した。
	- docstringには「『第N回の確認問題を出して』のように、講義内容を復習する問題を作るときに使う。用語集からその回の用語を1つ選び、問題と答えを返す」と書いた。
	- 指定された回の用語を用語集から集め、1つをランダムに選び、「『用語』の意味は？」という問題と、その用語の `definition` をJSONで返す。

## 宿題

- 取り組んだレベル：基礎
- やったこと：`app/tools.py` の `search_glossary` の docstring だけを変更した。変更前は「`query` には調べたい用語を1つだけ入れる」、変更後は「`query` には関連する用語をまとめて入れる」とした。同じ質問 `LoRAとQLoRAの違いは？` を、変更前後で `--trace` 付きで実行した。
- 結果：変更前は `search_glossary({'query': 'LoRA'})` と `search_glossary({'query': 'QLoRA'})` が呼ばれ、`requests=2`、`tool_calls=2` だった。変更後は `search_glossary({'query': 'LoRA QLoRA'})` が1回だけ呼ばれ、`requests=2`、`tool_calls=1` になった。変更後の最終回答はLoRAとQLoRAの違いを説明できたが、用語集から返ったのはLoRAの情報だけだった。
- 気づき・疑問：docstring の説明を変えるだけで、ツールの引数と呼び出し回数が変わった。まとめて検索すると呼び出し回数は減るが、用語集の検索実装によっては複数の用語を取りこぼす可能性があるため、今回のような比較では「用語を1つだけ入れる」方が確実な場合もある。

### INSTRUCTIONS の変更

- `app/agent.py` の `INSTRUCTIONS` に「確認問題を求められたら、対象の回を `lecture` に指定して `make_quiz` を使う」と追加した。
- `uv run python -m app.agent --trace "第2回の内容から確認問題を1問出して"` で確認したところ、`make_quiz({'lecture': 2})` が呼ばれ、`requests=2`、`tool_calls=1` だった。第2回の用語から「PEFT」が選ばれ、確認問題として出力された。
- docstring の変更とは別に、エージェント全体の指示で具体的なツールの使い方を指定すると、確認問題の質問から対象回を判断して `make_quiz` に誘導できることが分かった。

### 実装レベル

- `app/tools.py` に `save_learning_log(topic: str, note: str) -> str` を追加した。`learning_log/` を作成し、日時をファイル名にした JSON として学習内容を保存する。
- docstring には、学習内容をファイルに残したいときに使うことと、保存は取り消しにくいので呼び出す前に利用者の確認を得ることを書いた。
- `app/agent.py` では `agent.tool_plain(tools.save_learning_log, requires_approval=True)` として登録し、`output_type` に `DeferredToolRequests` を追加した。
- CLIで承認待ちになった場合は、保存してよいかを `[y/N]` で確認する。承認した場合は `DeferredToolResults` を渡して会話を再開し、拒否した場合は `ToolDenied` を返す。
- `TestModel` で確認したところ、保存ツールは実行前に `DeferredToolRequests` となり、承認対象に `save_learning_log` が含まれた。全テストは `15 passed` だった。

### 発展（a）Google ADK 版

- `adk_agent/glossary_agent/` を追加し、`agent.py` で ADK の `Agent` を組み立てた。`app.agent` の `INSTRUCTIONS` と、`search_glossary`・`get_lecture_summary`・`make_quiz` をそのまま読み込んで使った。
- Pydantic AI 版は `Agent` に指示とツールを登録し、CLIやトレースも自分で実装している。一方、ADK 版は `root_agent` を定義して `instruction` と `tools` を渡すだけで、対話用の `adk run` を利用できる。
- `PYTHONPATH=. uv run --with google-adk adk run adk_agent/glossary_agent` で起動し、`LoRAとQLoRAの違いは？` を入力した。ADK 版でも用語集を使った LoRA と QLoRA の違いを説明し、関係する回として第2回を示した。
- ADK の実行結果には、Pydantic AI 版の `--trace` のようなツール名・引数・`requests` の表示はなかった。ただし、回答内容は両方とも用語集に沿っており、Pydantic AI は実行ループや承認処理を細かく書けるのに対して、ADK はエージェントの定義を短く書ける点が違いだと分かった。
