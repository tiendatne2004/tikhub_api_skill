# TikHub API Helper

TikHub API Helper is a Claude Code Agent Skill that helps users search, discover, and call TikHub APIs. TikHub provides multi-platform social media data APIs supporting Douyin, TikTok, Xiaohongshu, Instagram, YouTube, Twitter, Reddit, and more.

## Introduction

TikHub is a multi-platform social media data API service that provides RESTful interfaces to fetch data from major social platforms. This project is a Claude Code Agent Skill that allows you to easily call TikHub APIs when using Claude Code.

### Supported Platforms

| Platform | API Tag | Endpoint Count |
|----------|---------|----------------|
| TikTok Web | `TikTok-Web-API` | 58 |
| TikTok App | `TikTok-App-V3-API` | 76 |
| Douyin Web | `Douyin-Web-API` | 76 |
| Douyin App | `Douyin-App-V3-API` | 45 |
| Xiaohongshu Web | `Xiaohongshu-Web-API` | 26 |
| Instagram | `Instagram-V2-API` | 26 |
| YouTube | `YouTube-Web-API` | 16 |
| Twitter | `Twitter-Web-API` | 13 |
| Reddit | `Reddit-APP-API` | 23 |
| Bilibili | `Bilibili-Web-API` | 24 |
| Weibo | `Weibo-Web-V2-API` | 33 |
| Zhihu | `Zhihu-Web-API` | 32 |

## Features

- **API Search** - Search TikHub APIs by keyword, tag, or operation ID
- **API Calls** - Call TikHub APIs directly from command line
- **Multi-platform Support** - Supports 12+ platforms including TikTok, Douyin, Xiaohongshu
- **Bilingual Support** - Supports both Chinese and English keyword searches
- **Environment Authentication** - Read API tokens from `TIKHUB_API_TOKEN`

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/tikhub_api_skill.git
cd tikhub_api_skill
```

### 2. Verify Project Structure

Ensure the `.claude/skills/tikhub-api-helper/` directory contains:

```
.claude/skills/tikhub-api-helper/
├── SKILL.md           # Skill definition file
├── openapi.json       # OpenAPI specification
├── api_searcher.py    # API search utility
└── api_client.py      # API client
```

### 3. Get API Token (Optional)

Set your API token before calling authenticated endpoints:

1. Visit [TikHub User](https://www.tikhub.io) and log in
2. Click "API Keys" on the left sidebar to generate your API token
3. Export it in your shell before running the helper:

```bash
export TIKHUB_API_TOKEN="your API token"
```

## Usage

### Using with Claude Code

The Skill automatically activates when you ask about TikHub APIs in Claude Code:

```
# Example conversation
You: "How to get TikTok user profile?"
Claude: [Automatically calls tikhub-api-helper Skill to search relevant APIs]
```

### Using via Command Line

#### Search APIs

```bash
# Keyword search
python .claude/skills/tikhub-api-helper/api_searcher.py "user profile"
python .claude/skills/tikhub-api-helper/api_searcher.py "trending"
python .claude/skills/tikhub-api-helper/api_searcher.py "video comments"

# Search by tag
python .claude/skills/tikhub-api-helper/api_searcher.py tag:TikTok-Web-API

# View popular APIs
python .claude/skills/tikhub-api-helper/api_searcher.py popular

# List all tags
python .claude/skills/tikhub-api-helper/api_searcher.py tags

# View detailed information
python .claude/skills/tikhub-api-helper/api_searcher.py detail:tiktok_web_fetch_user_profile_get
```

#### Call APIs

```bash
# Health check (no authentication required)
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/health/check

# Get TikTok user profile
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_user_profile "sec_user_id=MS4wLjABAAAA..."

# Search videos
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_search_video "keyword=gaming"

# Get YouTube trending videos
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/youtube/web/get_trending_videos "country=US"

# Search Xiaohongshu notes
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/xiaohongshu/web_v2/fetch_search_notes "keyword=lego"
```

## API Basics

### Base URLs

- **China users**: `https://api.tikhub.dev` (bypasses GFW)
- **International**: `https://api.tikhub.io`

### Authentication

All requests require an API Token in the request header:

```json
{
  "Authorization": "Bearer Your_API_Token"
}
```

### Rate Limits

- **QPS**: 10 requests per second per endpoint
- **Timeout**: 30-60 seconds
- **Retry**: Max 3 retries on error

### Endpoint Format

All endpoints follow this pattern:

```
/api/v1/{platform}/{method}/{action}
```

Examples:
- `/api/v1/tiktok/web/fetch_user_profile` - TikTok Web user profile
- `/api/v1/douyin/app/fetch_video_detail` - Douyin App video detail
- `/api/v1/xiaohongshu/web/fetch_user_post` - Xiaohongshu user posts

## Common Use Cases

### Get User Profile

```bash
# TikTok
python .claude/skills/tikhub-api-helper/api_searcher.py "tiktok user profile"
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_user_profile "sec_user_id=USER_ID"

# Douyin
python .claude/skills/tikhub-api-helper/api_searcher.py "douyin user info"
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/douyin/web/fetch_user_profile "sec_user_id=USER_ID"
```

### Search Content

```bash
# Search TikTok videos
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_search_video "keyword=gaming"

# Search YouTube videos
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/youtube/web/search_video "search_query=music"

# Search Xiaohongshu notes
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/xiaohongshu/web_v2/fetch_search_notes "keyword=food"
```

### Get Trending/Hot Content

```bash
# TikTok trending videos
python .claude/skills/tikhub-api-helper/api_searcher.py "trending"

# Douyin billboard
python .claude/skills/tikhub-api-helper/api_searcher.py tag:Douyin-Billboard-API

# YouTube trending
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/youtube/web/get_trending_videos "country=US"
```

## Project Structure

```
tikhub_api_skill/
├── .claude/
│   └── skills/
│       └── tikhub-api-helper/      # Agent Skill directory
│           ├── SKILL.md             # Skill definition
│           ├── openapi.json         # OpenAPI specification (2.4MB)
│           ├── api_searcher.py      # API search utility
│           └── api_client.py        # API client
├── openapi说明.md                   # Chinese documentation
├── skills.md                        # Agent Skills general documentation
├── explore_openapi.py              # API exploration script
├── README.md                        # This file
└── README_EN.md                     # English README
```

## Error Handling

| Error | Solution |
|-------|----------|
| `401 Unauthorized` | Check if API token is valid |
| `429 Too Many Requests` | Rate limit exceeded, wait before retry |
| `Connection error` | Check network, China users try `.dev` domain |
| `Missing parameter` | Check API details for required parameters |

## Related Links

- **TikHub Official**: https://www.tikhub.io
- **API Documentation**: https://api.tikhub.io
- **Apifox Docs**: https://docs.tikhub.io
- **API Status**: Check the TikHub user dashboard.
- **GitHub**: https://github.com/TikHub

## License

This project is for learning and reference purposes only.

## Contributing

Issues and Pull Requests are welcome!
