import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

def evaluate_and_save():
    """
    Loads environment variables, reads dialogue files, calls the OpenAI API
    for evaluation, prints the result, and saves it to a timestamped text file.
    """
    # -----------------------------------------------------------------
    # 1. .envファイルから環境変数を読み込む
    # -----------------------------------------------------------------
    load_dotenv()

    # -----------------------------------------------------------------
    # 2. APIキーの設定 (環境変数から読み込み)
    # -----------------------------------------------------------------
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("エラー: OpenAI APIキーが見つかりません。")
        print(".envファイルを作成し、'OPENAI_API_KEY'を設定してください。")
        return
    
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"エラー: OpenAIクライアントの初期化に失敗しました: {e}")
        return

    # -----------------------------------------------------------------
    # 3. 評価プロンプトの定義
    # -----------------------------------------------------------------
    prompt_template = """
#役割設定
あなたは、AIチューターシステムの対話品質を評価する、経験豊富な教育工学の研究者です。これから提示する2つの対話ログ（対話A、対話B）を、以下の評価基準に基づいて厳密に比較・分析してください。

#評価基準
1.  指導の効率性: 学習者が理解に至れるよう、無駄なやり取りや混乱を招く発言が少ないか。
2.  指導の的確: 学習者の理解度や誤解を正確に捉え、適切なタイミングで適切なヒント（質問、例示など）を提供できているか。
3.  概念理解の深化: 単なる問題解決手順の教示に留まらず、学習者が概念の本質的な意味を理解できるよう促せているか。
4.  学習意欲の維持・向上: 学習者の興味を引き出し、自発的な学びを促すような対話になっているか。
5.  一貫性とゴール志向性: 対話全体を通して、一貫した学習目標に向かっているか。話が逸脱していないか。

#思考プロセス
まず、上記の5つの基準それぞれについて、対話Aと対話Bがどのように機能しているかを具体的に分析してください。その上で、総合的な判断を下してください。

#出力形式
以下のフォーマットに厳密に従って、評価結果を出力してください。
[総合評価]: (対話A、対話Bのいずれかを選択)
[評価理由]: (総合評価の根拠を、具体的な対話内容を引用しながら詳細に説明してください。)
[項目別スコア]:
- 指導の効率性: (対話A: X/5点, 対話B: Y/5点)
- 指導の的確性: (対話A: X/5点, 対話B: Y/5点)
- 概念理解の深化: (対話A: X/5点, 対話B: Y/5点)
- 学習意欲の維持・向上: (対話A: X/5点, 対話B: Y/5点)
- 一貫性とゴール志向性: (対話A: X/5点, 対話B: Y/5点)
---
#評価対象
[対話A]:
{dialogue_a}

[対話B]:
{dialogue_b}
---
"""

    # -----------------------------------------------------------------
    # 4. ファイルの読み込み
    # -----------------------------------------------------------------
    try:
        with open('dialogue_3_formatted.json', 'r', encoding='utf-8') as f:
            dialogue_a_content = json.dumps(json.load(f), indent=2, ensure_ascii=False)
        with open('dialogue_without_conductor_3.json', 'r', encoding='utf-8') as f:
            dialogue_b_content = json.dumps(json.load(f), indent=2, ensure_ascii=False)
    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません - {e.filename}")
        return
    except json.JSONDecodeError as e:
        print(f"エラー: JSONファイルの形式が不正です - {e}")
        return

    # -----------------------------------------------------------------
    # 5. プロンプトの構築
    # -----------------------------------------------------------------
    final_prompt = prompt_template.format(
        dialogue_a=dialogue_a_content,
        dialogue_b=dialogue_b_content
    )

    print("--- 評価リクエストを送信中... ---")

    # -----------------------------------------------------------------
    # 6. OpenAI APIの呼び出し
    # -----------------------------------------------------------------
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in educational engineering tasked with evaluating AI tutor dialogues."},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.5,
            max_tokens=2000,
        )
        evaluation_result = response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI APIの呼び出し中にエラーが発生しました: {e}")
        return

    # -----------------------------------------------------------------
    # 7. 結果の表示
    # -----------------------------------------------------------------
    print("\n--- 評価結果 ---")
    print(evaluation_result)
    print("----------------\n")
    
    # -----------------------------------------------------------------
    # 8. 評価結果をファイルに保存
    # -----------------------------------------------------------------
    try:
        # タイムスタンプ付きのファイル名を生成 (例: evaluation_result_20250808_020726.txt)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"evaluation_result_{timestamp}.txt"
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(evaluation_result)
            
        print(f"評価結果を '{output_filename}' に保存しました。")
    except Exception as e:
        print(f"ファイルへの書き込み中にエラーが発生しました: {e}")


if __name__ == '__main__':
    evaluate_and_save()