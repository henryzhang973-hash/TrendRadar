# 手动运行指南

## GitHub Actions 手动运行

### 步骤：

1. **进入仓库 Actions 页面**
   - 访问：https://github.com/henryzhang973-hash/TrendRadar
   - 点击顶部的 **Actions** 标签

2. **选择 Workflow**
   - 在左侧边栏找到 **AI Analysis** workflow
   - 点击进入

3. **手动触发**
   - 点击右侧的 **Run workflow** 按钮（蓝色按钮）
   - 选择分支（通常是 `main`）
   - 点击绿色的 **Run workflow** 按钮

4. **查看运行结果**
   - 等待几秒钟，会看到新的运行记录出现
   - 点击运行记录查看详细日志
   - 在日志中可以看到：
     - 配置检查结果
     - 数据爬取进度
     - AI分析生成状态
     - 飞书消息发送结果

### 截图说明：

```
GitHub仓库页面
  └─ Actions标签
      └─ AI Analysis (左侧边栏)
          └─ Run workflow (右侧按钮) ← 点击这里
              └─ 选择分支: main
                  └─ Run workflow (绿色按钮) ← 确认运行
```

## 本地手动运行

### 方式一：使用 --force 参数（推荐）

```bash
# 1. 设置环境变量
export DEEPSEEK_API_KEY="sk-f7d071fdb38040ef890ee131fe7ff8d8"
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/4d27c57c-f7ec-4ed3-a4e5-89afe1b8ec78"

# 2. 强制运行（不检查时间）
python3 main.py --ai-analysis --force
```

### 方式二：使用测试脚本

```bash
# 设置环境变量
export DEEPSEEK_API_KEY="sk-f7d071fdb38040ef890ee131fe7ff8d8"
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/4d27c57c-f7ec-4ed3-a4e5-89afe1b8ec78"

# 运行测试脚本
python3 test_ai_analysis.py
```

## 自动运行时间

程序会在以下时间**自动运行**（无需手动操作）：

- **每天 09:00（北京时间）** - 当日情况分析
- **每天 21:00（北京时间）** - 当日复盘分析

## 常见问题

### Q: 为什么需要 --force 参数？

A: 程序默认只在 9:00 和 21:00 运行。使用 `--force` 可以强制在任何时间运行，用于测试。

### Q: GitHub Actions 手动运行需要 --force 吗？

A: 不需要。GitHub Actions 会根据当前时间自动判断是上午模式还是晚上模式。

### Q: 如何知道运行是否成功？

A: 查看 GitHub Actions 日志：
- 看到 "飞书AI分析通知发送成功" 表示成功
- 检查飞书群组是否收到消息

### Q: 运行失败怎么办？

A: 查看日志中的错误信息：
- 如果显示 "未配置飞书Webhook"，检查 Secrets 配置
- 如果显示 "AI分析生成失败"，检查 API 密钥和网络连接
- 如果显示 "飞书通知发送失败"，检查 Webhook URL 和飞书机器人配置




