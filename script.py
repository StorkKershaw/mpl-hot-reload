from random import randrange

import matplotlib.pyplot as plt

# 監視されるファイル
# 必ず main 関数を定義してください


def main():
    fig, ax = plt.subplots()
    ax.plot([randrange(10) for _ in range(10)])

    # matplotlib.figure.Figure クラスのインスタンスを返してください
    return fig

    # 同時にファイルへの保存も行う場合
    # return fig, "pdf"
    # サポートする拡張子は matplotlib に準じます
