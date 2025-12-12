# AI分析功能使用说明

## 功能概述

本程序已添加AI分析功能，使用DeepSeek API对热点新闻进行智能分析和总结。

### 主要功能

1. **上午9点模式**：AI整理总结和分析所有平台前十条热点，给出当日情况
2. **晚上9点模式**：AI整理总结和分析所有平台各前十条热点，对比上午10点的结果并给出当日复盘，并附带上5条与关键字相关的热点内容

### 关键词配置

已修改为：**AI、人工智能、特朗普、美国、中国**

## 使用方法

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥和Webhook

#### 方式一：环境变量（推荐）

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
export FEISHU_WEBHOOK_URL="your-feishu-webhook-url"
```

#### 方式二：命令行参数

```bash
python main.py --ai-analysis --deepseek-api-key "your-api-key"
```

#### 方式三：配置文件

在 `config/config.yaml` 中配置飞书Webhook（DeepSeek API密钥仍需通过环境变量或命令行参数提供）

### 3. 运行方式

#### 方式一：手动运行（测试用）

```bash
# 使用测试脚本（推荐）
python test_ai_analysis.py

# 或直接使用main.py
python main.py --ai-analysis --deepseek-api-key "your-api-key"
```

#### 方式二：定时任务（自动运行）

```bash
# 设置环境变量
export DEEPSEEK_API_KEY="your-deepseek-api-key"
export FEISHU_WEBHOOK_URL="your-feishu-webhook-url"

# 启动定时任务
python scheduler.py
```

定时任务会在每天北京时间上午9点和晚上9点自动执行。

### 4. 获取API密钥和Webhook

#### DeepSeek API密钥

1. 访问 [DeepSeek官网](https://www.deepseek.com/)
2. 注册/登录账号
3. 在控制台获取API密钥

#### 飞书Webhook

1. 电脑浏览器打开 https://botbuilder.feishu.cn/home/my-app
2. 点击"新建机器人应用"
3. 进入创建的应用后，点击"流程涉及" > "创建流程" > "选择触发器"
4. 往下滑动，点击"Webhook 触发"
5. 复制Webhook地址
6. 在"参数"里面放入以下内容，然后点击"完成"：

```json
{
  "message_type": "text",
  "content": {
    "total_titles": "{{内容}}",
    "timestamp": "{{内容}}",
    "report_type": "{{内容}}",
    "text": "{{内容}}"
  }
}
```

7. 点击"选择操作" > "发送飞书消息"，勾选 "群消息"，选择群组
8. 消息标题填写"TrendRadar 热点监控"
9. 配置完成后，将Webhook地址配置到环境变量或config.yaml中

## 输出内容说明

### 上午9点输出

- 各平台前十条热点的AI分析和总结
- 当日情况报告
- 与关键词相关的5条热点（如果有）

### 晚上9点输出

- 各平台前十条热点的AI分析和总结
- 对比上午9点的结果
- 当日复盘报告
- 与关键词相关的5条热点

## GitHub部署

详细的GitHub部署说明请参考 [GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md)

### 快速部署步骤

1. Fork项目到你的GitHub账户
2. 配置GitHub Secrets：
   - `DEEPSEEK_API_KEY` - DeepSeek API密钥
   - `FEISHU_WEBHOOK_URL` - 飞书Webhook URL
3. 启用GitHub Actions
4. 程序会在每天北京时间09:00和21:00自动执行

## 注意事项

1. 确保系统时间正确（定时任务使用北京时间）
2. DeepSeek API需要网络连接
3. 飞书Webhook需要正确配置才能接收消息
4. 本地测试时，可以通过 `test_ai_analysis.py` 脚本进行测试
5. GitHub Actions使用UTC时间，已自动转换为北京时间

## 故障排除

### 问题：API调用失败

- 检查API密钥是否正确
- 检查网络连接
- 查看错误日志

### 问题：飞书消息未收到

- 检查Webhook URL是否正确
- 检查飞书机器人是否已添加到群组
- 查看程序日志确认是否发送成功

### 问题：定时任务未执行

- 检查系统时间是否正确
- 确认程序是否在运行
- 查看日志确认任务是否触发

