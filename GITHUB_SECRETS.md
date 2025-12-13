# GitHub Secrets 配置 - 直接复制

## 配置步骤

1. 进入你的GitHub仓库：`https://github.com/henryzhang973-hash/TrendRadar`
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 按照下面的配置添加两个Secrets

---

## Secret 1: DEEPSEEK_API_KEY

**Name（名称）:**
```
DEEPSEEK_API_KEY
```

**Secret（值）:**
```
sk-f7d071fdb38040ef890ee131fe7ff8d8
```

---

## Secret 2: FEISHU_WEBHOOK_URL

**Name（名称）:**
```
FEISHU_WEBHOOK_URL
```

**Secret（值）:**
```
https://open.feishu.cn/open-apis/bot/v2/hook/4d27c57c-f7ec-4ed3-a4e5-89afe1b8ec78
```

---

## 配置检查清单

- [ ] 两个Secret都已添加
- [ ] 名称完全匹配（区分大小写）
- [ ] 值没有多余的空格
- [ ] 已保存

## 验证配置

配置完成后，可以：
1. 进入 **Actions** 标签
2. 选择 **AI Analysis** workflow
3. 点击 **Run workflow** 手动触发一次
4. 查看日志，应该看到：
   ```
   ✅ DEEPSEEK_API_KEY 已配置
   ✅ FEISHU_WEBHOOK_URL 已配置
   ```




