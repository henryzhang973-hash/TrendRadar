#!/usr/bin/env python3
# coding=utf-8
"""
测试飞书Webhook是否正常工作
"""

import requests
import json
from datetime import datetime
import pytz


def get_beijing_time():
    """获取北京时间"""
    return datetime.now(pytz.timezone("Asia/Shanghai"))


def test_feishu_webhook(webhook_url: str):
    """测试飞书Webhook"""
    print("="*60)
    print("测试飞书Webhook")
    print("="*60)
    print(f"Webhook URL: {webhook_url[:50]}...")
    print()
    
    headers = {"Content-Type": "application/json"}
    
    # 测试消息1：简单文本消息
    print("测试1：发送简单文本消息...")
    payload1 = {
        "msg_type": "text",
        "content": {
            "text": "这是一条测试消息，用于验证飞书Webhook是否正常工作。"
        }
    }
    
    try:
        response1 = requests.post(webhook_url, headers=headers, json=payload1, timeout=30)
        print(f"状态码: {response1.status_code}")
        print(f"响应: {response1.text}")
        if response1.status_code == 200:
            result1 = response1.json()
            print(f"响应JSON: {json.dumps(result1, ensure_ascii=False, indent=2)}")
            if result1.get("code") == 0:
                print("✅ 测试1成功：简单文本消息发送成功")
            else:
                print(f"❌ 测试1失败：错误码 {result1.get('code')}，错误信息：{result1.get('msg')}")
        else:
            print(f"❌ 测试1失败：HTTP状态码 {response1.status_code}")
    except Exception as e:
        print(f"❌ 测试1出错：{e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("-"*60)
    print()
    
    # 测试消息2：模拟AI分析消息格式
    print("测试2：发送AI分析消息格式...")
    now = get_beijing_time()
    payload2 = {
        "msg_type": "text",
        "content": {
            "total_titles": 5,
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
            "report_type": "测试分析报告",
            "text": "📊 测试分析报告\n\n━━━━━━━━━━━━━━━━━━━\n\n这是一条测试AI分析消息，用于验证消息格式是否正确。"
        }
    }
    
    try:
        response2 = requests.post(webhook_url, headers=headers, json=payload2, timeout=30)
        print(f"状态码: {response2.status_code}")
        print(f"响应: {response2.text}")
        if response2.status_code == 200:
            result2 = response2.json()
            print(f"响应JSON: {json.dumps(result2, ensure_ascii=False, indent=2)}")
            if result2.get("code") == 0:
                print("✅ 测试2成功：AI分析消息格式发送成功")
            else:
                print(f"❌ 测试2失败：错误码 {result2.get('code')}，错误信息：{result2.get('msg')}")
        else:
            print(f"❌ 测试2失败：HTTP状态码 {response2.status_code}")
    except Exception as e:
        print(f"❌ 测试2出错：{e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("="*60)
    print("测试完成")
    print("="*60)


if __name__ == "__main__":
    import sys
    import os
    
    # 从环境变量或命令行参数获取Webhook URL
    if len(sys.argv) > 1:
        webhook_url = sys.argv[1]
    else:
        webhook_url = os.environ.get("FEISHU_WEBHOOK_URL", "").strip()
    
    if not webhook_url:
        print("错误：未提供飞书Webhook URL")
        print("使用方法：")
        print("  python3 test_feishu_webhook.py <webhook_url>")
        print("或者设置环境变量：")
        print("  export FEISHU_WEBHOOK_URL='your-webhook-url'")
        print("  python3 test_feishu_webhook.py")
        sys.exit(1)
    
    test_feishu_webhook(webhook_url)

