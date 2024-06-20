import sys

def convert(s: str, numRows: int) -> str:
    # 行数が1または文字列の長さ以下の場合、そのまま文字列を返す
    if numRows == 1 or numRows >= len(s):
        return s

    # 各行の文字を保持するリストを初期化
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # 文字列の各文字をジグザグパターンで対応する行に追加
    for char in s:
        rows[current_row] += char
        # 最上行または最下行に達した場合、進行方向を反転
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # 現在の行を更新
        current_row += 1 if going_down else -1

    # 各行の文字を連結して結果を返す
    return ''.join(rows)

def print_zigzag(s: str, numRows: int) -> None:
    # 行数が1の場合、文字列をそのまま表示して終了
    if numRows == 1:
        print(s)
        return

    # ジグザグパターンを保持する2次元配列を初期化
    zigzag = [[' ' for _ in range(len(s))] for _ in range(numRows)]
    row, col = 0, 0
    going_down = True

    # 文字列の各文字をジグザグパターンで2次元配列に配置
    for char in s:
        zigzag[row][col] = char
        # 最上行に達した場合、進行方向を下向きに設定
        if row == 0:
            going_down = True
        # 最下行に達した場合、進行方向を上向きに設定
        elif row == numRows - 1:
            going_down = False

        # 行と列のインデックスを更新
        if going_down:
            row += 1
        else:
            row -= 1
            col += 1

    # ジグザグパターンを表示
    for row in zigzag:
        print(''.join(row).rstrip())

if __name__ == "__main__":
    s = sys.argv[1]
    numRows = int(sys.argv[2])
    result = convert(s, numRows)
    print(result)
    print_zigzag(s, numRows)
