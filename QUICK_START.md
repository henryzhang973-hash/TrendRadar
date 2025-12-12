# 快速开始 - GitHub部署

## 🚀 5分钟快速部署

### 步骤1：Fork项目
1. 访问项目仓库
2. 点击右上角 "Fork" 按钮

### 步骤2：配置Secrets（必需）

进入你的Fork仓库：**Settings → Secrets and variables → Actions → New repository secret**

添加以下两个Secrets：

| Secret名称 | 说明 | 示例 |
|-----------|------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API密钥 | `sk-xxxxx...` |
| `FEISHU_WEBHOOK_URL` | 飞书Webhook URL | `https://open.feishu.cn/...` |

### 步骤3：启用Actions

1. 进入仓库的 **Actions** 标签
2. 如果提示启用，点击 **"I understand my workflows, go ahead and enable them"**

### 步骤4：测试运行（可选）

1. 进入 **Actions** 标签
2. 选择 **"AI Analysis"** workflow
3. 点击 **"Run workflow"** 手动触发一次测试

### 步骤5：完成！

✅ 程序会在每天北京时间 **09:00** 和 **21:00** 自动执行
✅ 分析结果会自动发送到你的飞书群组

---

## 📋 详细说明

- **完整部署指南**：查看 [GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md)
- **功能使用说明**：查看 [AI_ANALYSIS_README.md](AI_ANALYSIS_README.md)

## ⚙️ 获取API密钥和Webhook

### DeepSeek API密钥
1. 访问 https://www.deepseek.com/
2. 注册/登录账号
3. 在控制台获取API密钥

### 飞书Webhook
1. 访问 https://botbuilder.feishu.cn/home/my-app
2. 创建机器人应用
3. 配置Webhook触发器
4. 复制Webhook地址

详细步骤请参考 [AI_ANALYSIS_README.md](AI_ANALYSIS_README.md)

