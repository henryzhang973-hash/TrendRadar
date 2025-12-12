#!/usr/bin/env python3
# coding=utf-8
"""
定时任务脚本：每天上午9点和晚上9点自动运行AI分析
"""

import os
import sys
import time
import schedule
from datetime import datetime
import pytz

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import NewsAnalyzer, get_beijing_time


def run_ai_analysis():
    """运行AI分析任务"""
    print(f"\n{'='*60}")
    print(f"定时任务触发 - {get_beijing_time().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # 从环境变量获取API密钥
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        print("错误：未设置环境变量 DEEPSEEK_API_KEY")
        print("请设置环境变量：export DEEPSEEK_API_KEY='your-api-key'")
        return
    
    try:
        analyzer = NewsAnalyzer()
        analyzer.run_ai_analysis_mode(api_key)
        print(f"\n任务完成 - {get_beijing_time().strftime('%Y-%m-%d %H:%M:%S')}\n")
    except Exception as e:
        print(f"任务执行失败: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数：设置定时任务"""
    print("="*60)
    print("TrendRadar AI分析定时任务启动")
    print("="*60)
    print(f"当前时间: {get_beijing_time().strftime('%Y-%m-%d %H:%M:%S')}")
    print("定时任务设置:")
    print("  - 每天 09:00 (北京时间) 执行当日情况分析")
    print("  - 每天 21:00 (北京时间) 执行当日复盘分析")
    print("="*60)
    print("\n等待定时任务触发...\n")
    
    # 检查API密钥
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        print("警告：未设置环境变量 DEEPSEEK_API_KEY")
        print("请设置环境变量：export DEEPSEEK_API_KEY='your-api-key'")
        print("\n程序将继续运行，但任务执行时会失败\n")
    
    # 设置定时任务
    # 注意：schedule库使用系统本地时间
    # 这里我们使用自定义的时间检查逻辑，确保使用北京时间
    beijing_now = get_beijing_time()
    
    print(f"当前北京时间: {beijing_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("定时任务将在每天 09:00 和 21:00 (北京时间) 执行\n")
    
    # 也可以手动触发一次（用于测试）
    current_hour = beijing_now.hour
    
    if current_hour == 9 or current_hour == 21:
        print(f"当前北京时间为 {current_hour}:00，立即执行一次任务...\n")
        run_ai_analysis()
    
    # 持续运行，每分钟检查一次是否到了执行时间
    print("定时任务已启动，等待触发...\n")
    while True:
        beijing_time = get_beijing_time()
        current_hour = beijing_time.hour
        current_minute = beijing_time.minute
        
        # 检查是否到了执行时间（09:00 或 21:00）
        if (current_hour == 9 or current_hour == 21) and current_minute == 0:
            # 避免重复执行（只在整点执行一次）
            if not hasattr(run_ai_analysis, '_last_run_hour') or run_ai_analysis._last_run_hour != current_hour:
                run_ai_analysis._last_run_hour = current_hour
                run_ai_analysis()
        
        # 每分钟检查一次
        time.sleep(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已停止")
        sys.exit(0)
    except Exception as e:
        print(f"\n程序运行出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

