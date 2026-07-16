# limit.py

def check_limit(tries, secret, digits):
    """
    桁数から制限回数を計算し、ゲームオーバーか判定します。
    """
    # --------------------------------------------------
    # 桁数に応じた制限回数の設定（チームで自由に調整してください！）
    
    max_tries = (digits-1)*5
    # --------------------------------------------------

    # 既に制限回数に達している（前のターンで失敗している）場合
    if tries >= max_tries:
        print(f"\n【ゲームオーバー】制限回数（{max_tries}回）に達しました！")
        print(f"正解は 【{secret}】 でした。また挑戦してね！")
        return True
    
    # あと何回挑戦できるかをプレイヤーにお知らせ
    remaining = max_tries - tries
    print(f"（残り挑戦回数: {remaining}回）")
    return False