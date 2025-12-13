# 故障排查指南 - 飞书消息未收到

## 问题：GitHub Actions运行成功但飞书没收到消息

### 排查步骤

#### 1. 检查GitHub Secrets配置

**确认Secrets名称完全正确（区分大小写）：**
- ✅ `DEEPSEEK_API_KEY` （不是 `deepseek_api_key` 或 `DEEPSEEK-API-KEY`）
- ✅ `FEISHU_WEBHOOK_URL` （不是 `feishu_webhook_url` 或 `FEISHU-WEBHOOK-URL`）

**检查方法：**
1. 进入仓库：Settings → Secrets and variables → Actions
2. 确认两个Secrets都存在
3. 检查名称是否完全匹配（包括大小写）

#### 2. 检查GitHub Actions日志

在Actions运行记录中查找以下信息：

**应该看到：**
```
✅ DEEPSEEK_API_KEY 已配置 (长度: XX 字符)
✅ FEISHU_WEBHOOK_URL 已配置 (URL前50字符: https://open.feishu.cn...)
✅ 飞书Webhook URL: 已配置
   URL前50字符: https://open.feishu.cn...
```

**如果看到：**
```
❌ DEEPSEEK_API_KEY 未配置
❌ FEISHU_WEBHOOK_URL 未配置
⚠️  警告：未配置飞书Webhook，无法发送分析结果
```
说明Secrets没有正确配置。

#### 3. 检查飞书机器人配置

**确认飞书机器人的参数映射：**

1. 访问 https://botbuilder.feishu.cn/home/my-app
2. 进入你的机器人应用
3. 检查"Webhook 触发"的参数配置

**正确的参数配置应该是：**
```json
{
  "message_type": "{{message_type}}",
  "content": {
    "total_titles": "{{content.total_titles}}",
    "timestamp": "{{content.timestamp}}",
    "report_type": "{{content.report_type}}",
    "text": "{{content.text}}"
  }
}
```

**特别注意：**
- `text` 字段必须映射到 `{{content.text}}`
- 这是消息的主要内容，如果映射错误，消息会发送成功但内容为空

#### 4. 检查飞书群组

- ✅ 确认机器人已添加到群组
- ✅ 确认机器人有发送消息的权限
- ✅ 检查群组设置，确保允许机器人发送消息

#### 5. 常见问题

**问题1：Secrets名称错误**
- ❌ 错误：`FEISHU_WEBHOOK_URL` 写成了 `FEISHU-WEBHOOK-URL`
- ✅ 正确：`FEISHU_WEBHOOK_URL`（使用下划线，全大写）

**问题2：Secrets值包含多余空格**
- 复制Webhook URL时可能包含前后空格
- 解决方法：重新创建Secret，确保没有空格

**问题3：飞书机器人参数映射错误**
- 如果 `text` 字段没有正确映射，消息会发送但内容为空
- 解决方法：检查并修正参数映射配置

**问题4：Webhook URL过期或无效**
- 飞书Webhook URL可能会过期
- 解决方法：重新生成Webhook URL并更新Secret

#### 6. 测试方法

**本地测试：**
```bash
# 测试飞书Webhook
python3 test_feishu_webhook.py "你的Webhook URL"

# 测试完整流程
export DEEPSEEK_API_KEY="你的API密钥"
export FEISHU_WEBHOOK_URL="你的Webhook URL"
python3 main.py --ai-analysis --force
```

**GitHub Actions测试：**
1. 进入 Actions 标签
2. 选择 "AI Analysis" workflow
3. 点击 "Run workflow" 手动触发
4. 查看详细日志

#### 7. 查看详细日志

在GitHub Actions日志中查找：
- `AI分析模式 - 配置检查` 部分
- `准备发送消息到飞书` 部分
- `飞书AI分析通知发送成功/失败` 部分

如果看到错误信息，根据错误提示进行修复。

## 快速检查清单

- [ ] GitHub Secrets名称正确（`DEEPSEEK_API_KEY` 和 `FEISHU_WEBHOOK_URL`）
- [ ] Secrets值正确（没有多余空格）
- [ ] 飞书机器人参数映射正确（特别是 `text` 字段）
- [ ] 机器人已添加到群组
- [ ] 机器人有发送消息权限
- [ ] GitHub Actions日志显示配置已加载
- [ ] 日志显示消息发送成功

## 如果仍然无法解决

1. 查看GitHub Actions的完整日志
2. 检查是否有错误信息
3. 尝试本地测试确认Webhook是否正常
4. 检查飞书机器人的配置和权限




