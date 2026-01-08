# TikHub API Helper

TikHub API 助手是一个 Claude Code Agent Skill，用于帮助用户搜索、发现和调用 TikHub API。TikHub 提供了多平台社交媒体数据 API，支持抖音、TikTok、小红书、Instagram、YouTube、Twitter、Reddit 等平台。

## 简介

TikHub 是一个多平台社交媒体数据 API 服务，提供 RESTful 接口来获取各大社交平台的数据。本项目是一个 Claude Code Agent Skill，可以让你在使用 Claude Code 时轻松调用 TikHub API。

### 支持的平台

| 平台 | API 标签 | 端点数量 |
|------|----------|----------|
| TikTok Web | `TikTok-Web-API` | 58 |
| TikTok App | `TikTok-App-V3-API` | 76 |
| 抖音 Web | `Douyin-Web-API` | 76 |
| 抖音 App | `Douyin-App-V3-API` | 45 |
| 小红书 Web | `Xiaohongshu-Web-API` | 26 |
| Instagram | `Instagram-V2-API` | 26 |
| YouTube | `YouTube-Web-API` | 16 |
| Twitter | `Twitter-Web-API` | 13 |
| Reddit | `Reddit-APP-API` | 23 |
| Bilibili | `Bilibili-Web-API` | 24 |
| 微博 | `Weibo-Web-V2-API` | 33 |
| 知乎 | `Zhihu-Web-API` | 32 |

## 功能特性

- **API 搜索** - 通过关键词、标签或操作 ID 搜索 TikHub API
- **API 调用** - 直接通过命令行调用 TikHub API
- **多平台支持** - 支持抖音、TikTok、小红书等 12+ 平台
- **中英文支持** - 支持中英文关键词搜索
- **自动鉴权** - 内置开发环境 API Token

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/tikhub_api_skill.git
cd tikhub_api_skill
```

### 2. 确保项目结构正确

确保 `.claude/skills/tikhub-api-helper/` 目录包含以下文件：

```
.claude/skills/tikhub-api-helper/
├── SKILL.md           # Skill 定义文件
├── openapi.json       # OpenAPI 规范
├── api_searcher.py    # API 搜索工具
└── api_client.py      # API 客户端
```

### 3. 获取 API Token（可选）

代码中已内置开发环境用的 API Token。如需使用自己的 Token：

1. 访问 [TikHub User](https://www.tikhub.io) 登录
2. 点击左侧 API Keys 生成你的 API Token
3. 设置变量：

```bash
在 api_client.py 23行，配置 DEFAULT_TOKEN = "你的 API Token"
```

## 使用方法

### 通过 Claude Code 使用

当你在 Claude Code 中询问关于 TikHub API 的问题时，该 Skill 会自动激活：

```
# 示例对话
你: "调研各外国平台讨论 deepseek的帖子"
Claude: [自动调用 tikhub-api-helper Skill 搜索相关 API]
```
 

## API 基础信息

### 请求地址

- **中国用户**: `https://api.tikhub.dev` (绕过 GFW)
- **国际用户**: `https://api.tikhub.io`

### 鉴权方式

所有需要在请求头中携带 API Token：

```json
{
  "Authorization": "Bearer Your_API_Token"
}
```

### 请求限制

- **QPS**: 每个端点每秒 10 次请求
- **超时**: 30-60 秒
- **重试**: 错误时最多重试 3 次

### 端点格式

所有端点遵循以下格式：

```
/api/v1/{platform}/{method}/{action}
```

例如：
- `/api/v1/tiktok/web/fetch_user_profile` - TikTok Web 用户资料
- `/api/v1/douyin/app/fetch_video_detail` - 抖音 App 视频详情
- `/api/v1/xiaohongshu/web/fetch_user_post` - 小红书用户帖子

## 常见用例

### 获取用户资料

```bash
# TikTok
python .claude/skills/tikhub-api-helper/api_searcher.py "tiktok 用户资料"
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_user_profile "sec_user_id=USER_ID"

# 抖音
python .claude/skills/tikhub-api-helper/api_searcher.py "douyin 用户信息"
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/douyin/web/fetch_user_profile "sec_user_id=USER_ID"
```

### 搜索内容

```bash
# 搜索 TikTok 视频
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_search_video "keyword=游戏"

# 搜索 YouTube 视频
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/youtube/web/search_video "search_query=music"

# 搜索小红书笔记
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/xiaohongshu/web_v2/fetch_search_notes "keyword=美食"
```

### 获取热门/趋势内容

```bash
# TikTok 热门视频
python .claude/skills/tikhub-api-helper/api_searcher.py "trending"

# 抖音热点榜
python .claude/skills/tikhub-api-helper/api_searcher.py tag:Douyin-Billboard-API

# YouTube 热门
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/youtube/web/get_trending_videos "country=CN"
```

## 项目结构

```
tikhub_api_skill/
├── .claude/
│   └── skills/
│       └── tikhub-api-helper/      # Agent Skill 目录
│           ├── SKILL.md             # Skill 定义
│           ├── openapi.json         # OpenAPI 规范 (2.4MB)
│           ├── api_searcher.py      # API 搜索工具
│           └── api_client.py        # API 客户端
├── openapi说明.md                   # 中文说明文档
├── skills.md                        # Agent Skills 通用文档
├── explore_openapi.py              # API 探索脚本
├── README.md                        # 本文件
└── README_EN.md                     # 英文版 README
```

## 错误处理

| 错误 | 解决方案 |
|------|----------|
| `401 Unauthorized` | 检查 API Token 是否有效 |
| `429 Too Many Requests` | 超出速率限制，请等待后重试 |
| `Connection error` | 检查网络连接，中国大陆用户尝试使用 `.dev` 域名 |
| `Missing parameter` | 检查 API 详细信息确认必需参数 |

## 相关链接

- **TikHub 官网**: https://www.tikhub.io
- **API 文档**: https://api.tikhub.io
- **Apifox 文档**: https://docs.tikhub.io
- **API 状态监控**: https://monitor.tikhub.io
- **GitHub**: https://github.com/TikHub

## 许可证

本项目仅供学习和参考使用。

## 贡献

欢迎提交 Issue 和 Pull Request！
