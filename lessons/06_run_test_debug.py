"""练习运行、断点和调试。"""


def compute_average(scores: list[float]) -> float:
    total = 0.0
    for score in scores:
        total += score
    return total / len(scores)


def classify_score(score: float) -> str:
    if score >= 90:
        return "excellent"
    if score >= 60:
        return "pass"
    return "retry"


def main() -> None:
    scores = [88.0, 92.0, 76.0]
    average = compute_average(scores)
    label = classify_score(average)
    print(f"average={average:.2f}, label={label}")


if __name__ == "__main__":
    main()


# 练习 1：运行
# 按 <leader>rr 运行当前文件。
# 预期输出：average=85.33, label=pass
#
# 练习 2：设置断点
# 把光标放到 total += score 这一行，按 <leader>db。
# 再按 <leader>dc，选择 Launch current file。
#
# 练习 3：单步调试
# 调试停住后，用方向键控制（仅在调试会话中生效）：
# - ↓：step over，执行当前行，不进入函数
# - →：step into，进入函数
# - ←：step out，跳出函数
# - ↑：restart frame，重启当前栈帧
# 其他：
# - <leader>dr：打开 Debug REPL
# - <leader>dt：停止调试
# - <leader>du：打开/关闭调试 UI
#
# 练习 4：观察变量
# 在 DAP UI 里观察 scores、score、total、average、label 的变化。
