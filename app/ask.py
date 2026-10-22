"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import time

from google import genai
from google.genai import errors
from google.genai import types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def _print_usage(response, elapsed: float) -> None:
    usage = response.usage_metadata
    print(f"[応答時間] {elapsed:.2f}秒")
    if usage is not None:
        print(f"[入力トークン数] {usage.prompt_token_count}")
        print(f"[出力トークン数] {usage.candidates_token_count}")


def ask(question: str, temperature: float | None = None) -> str:
    client = genai.Client(api_key=get_api_key())
    started_at = time.perf_counter()
    request_options = {}
    if temperature is not None:
        request_options["config"] = types.GenerateContentConfig(
            temperature=temperature
        )
    response = client.models.generate_content(
        model=MODEL,
        contents=question,
        **request_options,
    )
    _print_usage(response, time.perf_counter() - started_at)

    return response.text


def chat(initial_question: str | None = None) -> None:
    """Chat APIで会話履歴を保ちながら、複数の質問に答える。"""
    client = genai.Client(api_key=get_api_key())
    conversation = client.chats.create(model=MODEL)

    questions = [initial_question] if initial_question else []
    print("終了するには exit または Ctrl-D を入力してください。")
    while True:
        if questions:
            question = questions.pop(0)
        else:
            try:
                question = input("質問> ").strip()
            except EOFError:
                print()
                break

        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        started_at = time.perf_counter()
        response = conversation.send_message(question)
        _print_usage(response, time.perf_counter() - started_at)
        print(response.text)


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument(
        "--chat",
        action="store_true",
        help="会話履歴を保ちながら続けて質問する",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        help="回答のランダムさ（例: 0.0、1.0）",
    )
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    try:
        if args.chat:
            chat(args.question)
        else:
            print(f"[質問] {args.question}\n")
            print(ask(args.question, temperature=args.temperature))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
