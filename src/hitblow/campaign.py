from .game import play


def campaign_mode():
    print("===Hit & Blow チャレンジモード===")
    print("3桁, 4桁, 5桁のステージを順番にクリアしろ！")

    stages = [3, 4, 5]

    for d in stages:
        print(f"\n☆☆☆ ステージ: {d} 桁 ☆☆☆")

        is_cleared = play(digits=d)

        if is_cleared:
            print(f"ステージ: {d} 桁 クリア！")
        else:
            print("ゲームオーバー... ここからは進めない！")
            break
    else:
        print("\n================================")
        print("おめでとう！ 全ステージクリア！")
        print("================================")


if __name__ == "__main__":
    campaign_mode()
