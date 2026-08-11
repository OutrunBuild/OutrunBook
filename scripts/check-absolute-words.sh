#!/usr/bin/env bash
set -uo pipefail

# OutrunBook 绝对性营销词检查
#
# 检索公开产品文档中的绝对性营销词，用于发布前核对：保留的每一处
# 都必须附链上约束或明确限定条件（产品模型内 / 保护期内 / 正常机制下 /
# 否定用法等）。脚本只做机械化检索（防漏），语义限定由人工逐处核对。
#
# 白名单 = 已确认附有限定条件的 (相对路径:检索词) 组合。命中且不在
# 白名单 → 退出码非零，列出明细供核对。确认限定后：改文档，或往
# confirmed 数组加一行。
#
# 注意：白名单只防「新增绝对词漏核」，不防同一组合内把限定词删掉——
# 修改文档时仍应复核已有限定。新写文档请避免裸用绝对词，直接附限定。
#
# 用法：bash scripts/check-absolute-words.sh

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

WORDS=(无风险 始终 不会 确保 杜绝 自动兜底 保本 所有人同价)

# 已确认限定组合（相对仓库根的路径:检索词）。每引入一处新命中，先核对限定，再决定改文档或加此行。
confirmed=(
  "reference/participation-map.md:无风险"
  "memeverse/genesis.md:无风险"
  "ecosystem/playbooks.md:无风险"
  "ecosystem/flywheel.md:无风险"
  "outstake/staking-modes.md:始终"
  "outstake/uasset.md:始终"
  "memeverse/yt-flash-swap.md:始终"
  "reference/faq.md:始终"
  "outstake/sy-adapters.md:不会"
  "memeverse/dao-governance.md:不会"
  "reference/faq.md:不会"
  "outstake/uasset.md:不会"
  "memeverse/yt-flash-swap.md:不会"
  "memeverse/pol-splitter.md:不会"
  "memeverse/genesis-credit.md:不会"
  "memeverse/hook.md:不会"
  "memeverse/polend.md:不会"
  "memeverse/preorder.md:不会"
  "memeverse/genesis.md:不会"
  "memeverse/memecoin-staking.md:不会"
  "memeverse/omnichain.md:不会"
  "ecosystem/business-model.md:不会"
  "ecosystem/playbooks.md:不会"
  "outstake/staking-modes.md:不会"
  "ecosystem/flywheel.md:不会"
  "memeverse/lifecycle.md:不会"
  "memeverse/four-pools.md:确保"
  "reference/faq.md:杜绝"
  "reference/participation-map.md:保本"
  "ecosystem/playbooks.md:保本"
)

# 检索范围：公开产品文档。排除 .claude/（内部工作稿）与 CLAUDE.md（仓库指令）。
targets="README.md SUMMARY.md vision.md outstake memeverse ecosystem reference"

hits=0
unconfirmed=0
for word in "${WORDS[@]}"; do
  files=$(grep -rl "$word" $targets --include='*.md' 2>/dev/null || true)
  [ -z "$files" ] && continue
  while IFS= read -r f; do
    key="$f:$word"
    n=$(grep -c "$word" "$f" || true)
    if printf '%s\n' "${confirmed[@]}" | grep -qxF "$key"; then
      printf '  ok    %-38s %-6s x%s\n' "$f" "$word" "$n"
    else
      printf '  FAIL  %-38s %-6s x%s\n' "$f" "$word" "$n"
      grep -n "$word" "$f" | sed 's/^/        /'
      unconfirmed=$((unconfirmed + 1))
    fi
    hits=$((hits + 1))
  done <<< "$files"
done

echo
if [ "$unconfirmed" -ne 0 ]; then
  echo "check-absolute-words: $unconfirmed 个 (文件,检索词) 组合有白名单外的命中 —— 逐处核对限定条件，改文档或加入白名单后重跑。" >&2
  exit 1
fi
echo "check-absolute-words: 全部 $hits 个 (文件,检索词) 组合均已确认限定，通过。"
