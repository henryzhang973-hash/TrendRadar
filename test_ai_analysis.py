#!/usr/bin/env python3
# coding=utf-8
"""
本地测试脚本：测试AI分析功能
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import NewsAnalyzer, get_beijing_time


def main():
    """测试AI分析功能"""
    print("="*60)
    print("TrendRadar AI分析功能测试")
    print("="*60)
    
    # 获取API密钥
    api_key = input("请输入DeepSeek API密钥（或按Enter使用环境变量DEEPSEEK_API_KEY）: ").strip()
    if not api_key:
        api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    
    if not api_key:
        print("\n错误：未提供DeepSeek API密钥")
        print("请通过以下方式之一提供：")
        print("  1. 在提示时输入")
        print("  2. 设置环境变量：export DEEPSEEK_API_KEY='your-api-key'")
        return
    
    # 获取飞书Webhook
    feishu_webhook = input("请输入飞书Webhook URL（或按Enter使用环境变量FEISHU_WEBHOOK_URL）: ").strip()
    if not feishu_webhook:
        feishu_webhook = os.environ.get("FEISHU_WEBHOOK_URL", "").strip()
    
    if not feishu_webhook:
        print("\n警告：未提供飞书Webhook URL")
        print("分析结果将不会发送到飞书")
        print("请通过以下方式之一提供：")
        print("  1. 在提示时输入")
        print("  2. 设置环境变量：export FEISHU_WEBHOOK_URL='your-webhook-url'")
        print("  3. 在config/config.yaml中配置")
        response = input("\n是否继续测试（不发送到飞书）？(y/n): ").strip().lower()
        if response != 'y':
            return
    else:
        # 临时设置环境变量
        os.environ["FEISHU_WEBHOOK_URL"] = feishu_webhook
    
    # 临时设置API密钥
    os.environ["DEEPSEEK_API_KEY"] = api_key
    
    print(f"\n当前时间: {get_beijing_time().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"当前小时: {get_beijing_time().hour}")
    print("\n开始执行AI分析...\n")
    
    try:
        analyzer = NewsAnalyzer()
        analyzer.run_ai_analysis_mode(api_key)
        print("\n测试完成！")
    except Exception as e:
        print(f"\n测试失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

