#!/usr/bin/env bash
set -uo pipefail

# OutrunBook 基线检查
#
# 核对 CLAUDE.md「仓库关系与代码真相源」表记录的对齐 commit 是否落后于对应代码仓库 HEAD。
# 漂移即文档描述的内容可能与最新代码脱节。发布前必须运行；任一仓库漂移则退出码非零。
#
# 用法：bash scripts/check-baseline.sh
# 漂移后：更新 CLAUDE.md 表格里的对齐 commit（全 hash），复核受影响机制页，再重跑本脚本。

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLAUDE="$REPO_DIR/CLAUDE.md"

# 表格行形如：
#   | **MemeverseV2** | `路径` | 角色 | `fullhash`(`short`，描述) |
# awk 以反引号切分：$2 = 仓库路径，$4 = 对齐 commit 全 hash。
rows=$(grep -E '^\| \*\*' "$CLAUDE" || true)
if [ -z "$rows" ]; then
  echo "check-baseline: 未在 $CLAUDE 找到仓库关系表行（应为 \`| ** 开头），中止" >&2
  exit 2
fi

fail=0
echo "检查文档对齐基线 vs 代码仓库 HEAD："
while IFS= read -r row; do
  repo=$(printf '%s' "$row" | awk -F'`' '{print $2}')
  aligned=$(printf '%s' "$row" | awk -F'`' '{print $4}')
  name=$(basename "$repo")
  printf '  %-11s 对齐 %s -> ' "$name" "${aligned:0:7}"

  if [ -z "$repo" ] || [ -z "$aligned" ]; then
    printf '解析失败：%s\n' "$(printf '%s' "$row" | sed 's/  */ /g')"
    fail=1
    continue
  fi
  if ! git -C "$repo" cat-file -e "${aligned}^{commit}" 2>/dev/null; then
    printf '错误：commit %s 在 %s 中不存在\n' "$aligned" "$name"
    fail=1
    continue
  fi
  head=$(git -C "$repo" rev-parse HEAD)
  if [ "$head" = "$aligned" ]; then
    echo "OK（对齐 commit == HEAD）"
  else
    n=$(git -C "$repo" rev-list --count "$aligned..HEAD")
    printf '漂移（对齐 commit 落后 HEAD %s 个提交）：\n' "$n"
    git -C "$repo" log --oneline --no-decorate "$aligned..HEAD" | head -20
    fail=1
  fi
done <<< "$rows"

echo
if [ "$fail" -ne 0 ]; then
  echo "check-baseline: 存在漂移 —— 请把 CLAUDE.md 对齐 commit 更新到最新、复核对应机制页后重跑。" >&2
  exit 1
fi
echo "check-baseline: 全部对齐，通过。"
