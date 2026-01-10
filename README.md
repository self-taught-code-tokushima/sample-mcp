# sample-mcp

[FastMCP](https://gofastmcp.com) を使った MCP サーバーの最小実装サンプルです。
stdio、HTTP、SSE の3つのトランスポートモードに対応しています。

## 必要環境

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## インストール

```bash
git clone <repository-url>
cd sample-mcp
uv sync
```

## 使い方

### stdio (デフォルト)

Claude Desktop などの MCP クライアントと連携する際の標準的なモード。

```bash
uv run python -m sample_mcp.server_stdio
```

### HTTP (Streamable HTTP)

ネットワーク経由でアクセス可能なモード。FastMCP で推奨されるトランスポート。

```bash
uv run python -m sample_mcp.server_http
# エンドポイント: http://127.0.0.1:8000/mcp
```

### SSE (Server-Sent Events)

レガシーモード。後方互換性のために提供。

```bash
uv run python -m sample_mcp.server_sse
# エンドポイント: http://127.0.0.1:8000/sse
```

## Claude Desktop での設定

### stdio モード

`claude_desktop_config.json` に以下を追加:

```json
{
  "mcpServers": {
    "sample-mcp": {
      "command": "uvx",
      "args": ["--from", "/path/to/sample-mcp", "sample-mcp-stdio"]
    }
  }
}
```

### HTTP モード

1. サーバーを起動: `uv run python -m sample_mcp.server_http`
2. `claude_desktop_config.json` に以下を追加:

```json
{
  "mcpServers": {
    "sample-mcp-http": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## Claude Code での設定

以下では `-s project` でプロジェクトに設定している。

### stdio モード

```bash
claude mcp add -s project --transport stdio sample-mcp -- uvx --from "D:\\mcp-tools\\sample-mcp" sample-mcp-stdio
```

プロジェクトルートに `.mcp.json` が作成される。

```json
{
  "mcpServers": {
    "sample-mcp": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "C:\\your-path\\your-path",
        "sample-mcp-stdio"
      ],
      "env": {}
    }
  }
}
```

### HTTP モード

サーバーは起動は Claude Desktop と同様。

```bash
claude mcp add -s project --transport http sample-mcp-http http://127.0.0.1:8000/mcp
```

プロジェクトルートに `.mcp.json` が作成される。

```json
{
  "mcpServers": {
    "sample-mcp-http": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## ファイル構成

```
src/sample_mcp/
├── server.py          # MCPインスタンスとツール定義
├── server_stdio.py    # stdio トランスポート
├── server_http.py     # HTTP トランスポート
└── server_sse.py      # SSE トランスポート
```

## 提供されるツール

| ツール名 | 説明 |
|---------|------|
| `hello` | 名前を受け取って挨拶を返す |

## ライセンス

MIT
