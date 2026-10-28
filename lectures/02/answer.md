# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
{
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }

- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` = 0.09523809523809523　 / `content_rate` = 0.0
- 学習後：`format_rate` = 1.0 / `content_rate` = 0.9047619047619048
- 退行した質問：
[]
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
質問の答えに似てそうな解答を取ってきてそれっぽい解答をした。
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
学習前の分類は全てformat errorだったが、学習後の分類はassertedかneeds_reviewになった。今回は、間違ってる解答に対してもassertedが与えられていたが、モデルの大きさが小さかったために最終課題と課題がモデル上で区別されなかったことが原因かもしれないと思った。
- 学習で変わったこと・変わらなかったこと：
学習によってformatに関してはほぼ高い確率で正しい型に整合することが確かめられた。contentに関しては学習前は正しい確率が0であったが、これは、主にneed_reviewが学習前は上手く出力されていない為であるとわかった。内容そのものに関しては、そこまで質が向上したとは言えないという所感である。学習によって向上したのは専ら形式による出力の安定性であると思われる。
## 宿題

- 取り組んだレベル：基礎
- 変えた設定やデータ：lora_rを64に変えた。
- 結果（比較表や数字）：
lora_rが16の場合
{
  "summary": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.9047619047619048,
    "both_rate": 0.9047619047619048,
    "seconds": 61.2
  },
  "rows": [
    {
      "question": "提出の期限は？",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出期限の日付と時刻を教えてください",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "課題の締切は何月何日の何時ですか",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出場所は？",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "課題の提出はどこで行いますか",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出物を出す先を教えてください",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "PDF 以外でも出せますか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出するファイルの形式は何ですか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出ファイルは何形式で、いくつ出しますか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "相談できる時間帯は？",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "オフィスアワーの曜日と時間を教えてください",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "質問を受け付けてもらえるのは何曜日の何時からですか",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "締切後の扱いを教えてください",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出が締切に間に合わなかったらどうなりますか",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "期限後に提出した課題は受理されますか",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "成績はいつ出ますか",
      "raw": "{\"answer\": \"提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": true
    },
    {
      "question": "講義の録画は公開されますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "課題の文字数に制限はありますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "提出した課題へのフィードバックはもらえますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "参考文献の書き方に指定はありますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "オフィスアワーは事前予約が必要ですか",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": true
    }
  ]
}

lora_rが64の場合
{
  "summary": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.8571428571428571,
    "both_rate": 0.8571428571428571,
    "seconds": 42.5
  },
  "rows": [
    {
      "question": "提出の期限は？",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出期限の日付と時刻を教えてください",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "課題の締切は何月何日の何時ですか",
      "raw": "{\"answer\": \"課題の提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出場所は？",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "課題の提出はどこで行いますか",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出物を出す先を教えてください",
      "raw": "{\"answer\": \"提出先は学習ポータルの「課題」欄です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "PDF 以外でも出せますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": false
    },
    {
      "question": "提出するファイルの形式は何ですか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出ファイルは何形式で、いくつ出しますか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "相談できる時間帯は？",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "オフィスアワーの曜日と時間を教えてください",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "質問を受け付けてもらえるのは何曜日の何時からですか",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "締切後の扱いを教えてください",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "提出が締切に間に合わなかったらどうなりますか",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "期限後に提出した課題は受理されますか",
      "raw": "{\"answer\": \"期限後の提出は、期限から 48 時間以内なら減点のうえ受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
    {
      "question": "成績はいつ出ますか",
      "raw": "{\"answer\": \"提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": true
    },
    {
      "question": "講義の録画は公開されますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "課題の文字数に制限はありますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "提出した課題へのフィードバックはもらえますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "参考文献の書き方に指定はありますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": true
    },
    {
      "question": "オフィスアワーは事前予約が必要ですか",
      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": true
    }
  ]
}
- ファインチューニングが向く場面・向かない場面についての考察：
今回のfine turningの実験で、fine turningによってモデルの出力の形式を安定化させて、形式的なステップで出力を出させることが可能になると示唆される。一方で、出力の内容そのものや、尤もらしく答えるというミスに関してはfine turningで修正されていなかった。よって形式についてはfine turningで修正ができるが、内容そのものはモデルの性能に大きく依存すると分かった。