# GitHub部署指南

## 概述

本指南将帮助你在GitHub上部署和运行AI分析功能。

## 部署步骤

### 1. Fork项目（如果还没有）

1. 访问项目仓库
2. 点击右上角的 "Fork" 按钮
3. 等待Fork完成

### 2. 配置GitHub Secrets

在你的Fork仓库中，需要配置以下Secrets：

#### 必需配置

1. **DEEPSEEK_API_KEY**
   - 路径：Settings → Secrets and variables → Actions → New repository secret
   - 名称：`DEEPSEEK_API_KEY`
   - 值：你的DeepSeek API密钥（例如：`sk-xxxxx...`）

2. **FEISHU_WEBHOOK_URL**
   - 路径：Settings → Secrets and variables → Actions → New repository secret
   - 名称：`FEISHU_WEBHOOK_URL`
   - 值：你的飞书机器人Webhook URL

#### 可选配置（如果需要其他通知方式）

- `TELEGRAM_BOT_TOKEN` - Telegram Bot Token
- `TELEGRAM_CHAT_ID` - Telegram Chat ID
- `DINGTALK_WEBHOOK_URL` - 钉钉Webhook URL
- `WEWORK_WEBHOOK_URL` - 企业微信Webhook URL

### 3. 配置文件检查

确保以下文件存在且配置正确：

1. **config/config.yaml**
   - 检查配置文件是否存在
   - 确保平台配置正确

2. **config/frequency_words.txt**
   - 确保关键词配置正确（已设置为：AI、人工智能、特朗普、美国、中国）

### 4. 启用GitHub Actions

1. 进入你的仓库
2. 点击 "Actions" 标签
3. 如果提示启用Actions，点击 "I understand my workflows, go ahead and enable them"

### 5. 验证部署

#### 方式一：手动触发测试

1. 进入 "Actions" 标签
2. 选择 "AI Analysis" workflow
3. 点击 "Run workflow" 按钮
4. 选择分支（通常是 `main` 或 `master`）
5. 点击 "Run workflow"

#### 方式二：等待自动执行

- 程序会在每天北京时间 **09:00** 和 **21:00** 自动执行
- 可以在 "Actions" 标签中查看执行历史和日志

## Workflow说明

### AI Analysis Workflow

- **文件位置**：`.github/workflows/ai-analysis.yml`
- **执行时间**：
  - 每天 UTC 01:00（北京时间 09:00）- 当日情况分析
  - 每天 UTC 13:00（北京时间 21:00）- 当日复盘分析
- **手动触发**：支持通过GitHub Actions界面手动触发

### 原有Crawler Workflow

- **文件位置**：`.github/workflows/crawler.yml`
- **功能**：原有的热点爬取功能（每小时执行一次）
- **说明**：与AI分析功能独立运行，互不影响

## 查看执行结果

### 在GitHub上查看

1. 进入 "Actions" 标签
2. 点击对应的workflow运行记录
3. 查看 "Run AI Analysis" 步骤的日志

### 在飞书中查看

- 如果配置正确，分析结果会自动发送到飞书群组
- 检查飞书机器人是否正常工作

## 故障排除

### 问题：Workflow执行失败

**检查清单：**
1. ✅ 是否配置了 `DEEPSEEK_API_KEY`？
2. ✅ 是否配置了 `FEISHU_WEBHOOK_URL`？
3. ✅ 配置文件是否存在？
4. ✅ GitHub Actions是否已启用？

**查看日志：**
- 进入 Actions → 选择失败的运行 → 查看详细日志

### 问题：未收到飞书消息

**检查清单：**
1. ✅ `FEISHU_WEBHOOK_URL` 是否正确？
2. ✅ 飞书机器人是否已添加到群组？
3. ✅ 查看workflow日志，确认是否发送成功

### 问题：API调用失败

**可能原因：**
1. API密钥无效或过期
2. API配额已用完
3. 网络连接问题

**解决方法：**
- 检查DeepSeek API密钥是否有效
- 查看API使用情况
- 检查workflow日志中的错误信息

## 时间说明

- GitHub Actions使用UTC时间
- 本配置已转换为北京时间（UTC+8）
- 执行时间：
  - 北京时间 09:00 = UTC 01:00
  - 北京时间 21:00 = UTC 13:00

## 注意事项

1. **API配额**：注意DeepSeek API的使用配额，避免超出限制
2. **执行频率**：GitHub Actions有执行时间限制，不要设置过于频繁的任务
3. **敏感信息**：永远不要将API密钥或Webhook URL提交到代码仓库，使用Secrets存储
4. **时区问题**：确保理解UTC和北京时间的转换关系

## 更新配置

如果需要更新配置：

1. 修改 `config/config.yaml` 或 `config/frequency_words.txt`
2. 提交更改到仓库
3. 下次执行时会自动使用新配置

如果需要更新Secrets：

1. 进入 Settings → Secrets and variables → Actions
2. 找到对应的Secret
3. 点击 "Update" 更新值

## 支持

如果遇到问题，可以：
1. 查看GitHub Actions日志
2. 检查配置文件
3. 参考项目文档
4. 提交Issue到项目仓库

