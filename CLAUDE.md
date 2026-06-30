# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a TikHub API skill repository. TikHub is a multi-platform social media data API service that provides RESTful endpoints for platforms including Douyin (抖音), TikTok, Xiaohongshu (小红书), Lemon8, Bilibili, Kuaishou, Weibo, WeChat, Instagram, YouTube, Twitter, Threads, Reddit, and Zhihu.

The repository contains a Claude Code Agent Skill (`tikhub-api-helper`) that helps users search, discover, and call TikHub APIs.

## Architecture

```
tikhub_api_skill/
├── .claude/
│   └── skills/
│       └── tikhub-api-helper/      # Main Agent Skill
│           ├── SKILL.md             # Skill definition (YAML frontmatter + instructions)
│           ├── openapi.json         # OpenAPI 3.1.0 spec (2.4MB, auto-generated)
│           ├── api_searcher.py      # Search/discover APIs from OpenAPI spec
│           └── api_client.py        # Make HTTP requests to TikHub APIs
├── openapi说明.md                   # Chinese documentation (token reference)
├── skills.md                        # Generic Agent Skills documentation (unrelated)
└── explore_openapi.py              # One-off exploration script
```

### Key Components

**`.claude/skills/tikhub-api-helper/`** - The Agent Skill directory:
- `SKILL.md`: Defines the skill with YAML frontmatter (name, description) and instructions for Claude
- `api_searcher.py`: Python class `TikHubAPISearcher` for searching the OpenAPI spec by keyword, tag, or operation_id
- `api_client.py`: Python class `TikHubAPIClient` for making authenticated HTTP requests to TikHub APIs
- `openapi.json`: Full OpenAPI specification (should live in the skill directory, not root)

The skill is **model-invoked** - Claude autonomously decides when to use it based on the user's query matching the skill's description.

## API Authentication

All API requests require an API Token in the Authorization header:

```json
{
  "Authorization": "Bearer Your_API_Token"
}
```

For development/testing, a default token is embedded in `api_client.py` (from `openapi说明.md:33`):
```python
DEFAULT_TOKEN = ""
```

## API Base URLs

- **China users**: `https://api.tikhub.dev` (bypasses GFW)
- **International**: `https://api.tikhub.io`

## Common Commands

### Search for APIs

```bash
# From repository root - search by keyword
python .claude/skills/tikhub-api-helper/api_searcher.py "user profile"
python .claude/skills/tikhub-api-helper/api_searcher.py "trending"
python .claude/skills/tikhub-api-helper/api_searcher.py "视频评论"

# List all APIs for a specific platform tag
python .claude/skills/tikhub-api-helper/api_searcher.py tag:TikTok-Web-API
python .claude/skills/tikhub-api-helper/api_searcher.py tag:Douyin-App-V3-API

# List popular/common APIs
python .claude/skills/tikhub-api-helper/api_searcher.py popular

# List all available tags/categories
python .claude/skills/tikhub-api-helper/api_searcher.py tags

# Get detailed info for a specific API (parameters, request body, responses)
python .claude/skills/tikhub-api-helper/api_searcher.py detail:tiktok_web_fetch_user_profile_get
```

### Make API Requests

```bash
# Health check (no authentication required)
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/health/check

# Get user profile (GET with query params)
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_user_profile "sec_user_id=MS4wLjABAAAA..."

# Search videos
python .claude/skills/tikhub-api-helper/api_client.py GET /api/v1/tiktok/web/fetch_search_video "keyword=gaming"

# POST request with JSON body
python .claude/skills/tikhub-api-helper/api_client.py POST /api/v1/tiktok/web/generate_xgnarly '{"url": "https://..."}'
```

### Supported Platform Tags

| Platform | Tag Name | Endpoint Count |
|----------|----------|----------------|
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

## Rate Limits

- **QPS**: 10 requests per second per endpoint
- **Timeout**: 30-60 seconds
- **Retry**: Max 3 retries on error

## Working with openapi.json

The OpenAPI specification is ~2.4MB. Use these strategies:

```bash
# Read first N bytes
head -c 5000 .claude/skills/tikhub-api-helper/openapi.json

# Use the api_searcher.py script instead of direct parsing
python .claude/skills/tikhub-api-helper/api_searcher.py <query>

# Use Read tool with offset/limit for large files
```

## External References

- **API Documentation**: https://api.tikhub.io
- **Apifox Docs**: https://docs.tikhub.io
- **API Status**: Check the TikHub user dashboard.
- **GitHub**: https://github.com/TikHub
