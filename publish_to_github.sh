#!/bin/bash

set -e

# 解压项目包
unzip telegram_search_bot.zip -d telegram_search_bot
cd telegram_search_bot

# 初始化 Git 仓库
git init
git remote add origin https://github.com/daduyun/telegram-search-bot.git
git add .
git commit -m "Initial commit - Telegram Search Bot with Docker support"

# 推送到 GitHub（首次）
git branch -M main
git push -u origin main
