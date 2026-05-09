TOOLS_METADATA = {

    # =========================
    # BUILT-IN CONNECTORS
    # =========================

    "gmail": {
        "category": "communication",
        "capabilities": [
            "email",
            "messaging",
            "drafting",
            "search"
        ]
    },

    "google_calendar": {
        "category": "productivity",
        "capabilities": [
            "calendar",
            "scheduling",
            "meetings"
        ]
    },

    "google_drive": {
        "category": "storage",
        "capabilities": [
            "file_storage",
            "document_access",
            "search"
        ]
    },

    "slack": {
        "category": "communication",
        "capabilities": [
            "messaging",
            "team_chat",
            "search"
        ]
    },

    "notion": {
        "category": "knowledge",
        "capabilities": [
            "notes",
            "documentation",
            "knowledge_base"
        ]
    },

    "onedrive": {
        "category": "storage",
        "capabilities": [
            "file_storage",
            "document_access"
        ]
    },

    "sharepoint": {
        "category": "enterprise",
        "capabilities": [
            "document_management",
            "enterprise_search"
        ]
    },

    "microsoft_365": {
        "category": "enterprise",
        "capabilities": [
            "email",
            "documents",
            "calendar"
        ]
    },

    "google_docs": {
        "category": "documents",
        "capabilities": [
            "document_editing",
            "document_reading"
        ]
    },

    "google_sheets": {
        "category": "data",
        "capabilities": [
            "spreadsheet",
            "analytics",
            "structured_data"
        ]
    },

    # =========================
    # MCP SERVERS
    # =========================

    "tavily": {
        "category": "research",
        "capabilities": [
            "search",
            "web_research",
            "knowledge"
        ]
    },

    "context7": {
        "category": "development",
        "capabilities": [
            "documentation",
            "api_reference",
            "libraries"
        ]
    },

    "task_master_ai": {
        "category": "planning",
        "capabilities": [
            "task_planning",
            "workflow_management"
        ]
    },

    "github": {
        "category": "development",
        "capabilities": [
            "code",
            "repository",
            "pull_requests",
            "issues"
        ]
    },

    "postgres": {
        "category": "data",
        "capabilities": [
            "database",
            "sql",
            "analytics"
        ]
    },

    "supabase": {
        "category": "data",
        "capabilities": [
            "database",
            "auth",
            "storage"
        ]
    },

    "linear": {
        "category": "project_management",
        "capabilities": [
            "issues",
            "task_tracking"
        ]
    },

    "sentry": {
        "category": "monitoring",
        "capabilities": [
            "error_tracking",
            "monitoring",
            "debugging"
        ]
    },

    "jira": {
        "category": "project_management",
        "capabilities": [
            "issues",
            "tickets",
            "task_tracking"
        ]
    },

    "confluence": {
        "category": "knowledge",
        "capabilities": [
            "wiki",
            "documentation",
            "knowledge_base"
        ]
    },

    # =========================
    # COMMUNICATION
    # =========================

    "discord": {
        "category": "communication",
        "capabilities": [
            "messaging",
            "community_management"
        ]
    },

    "microsoft_teams": {
        "category": "communication",
        "capabilities": [
            "messaging",
            "meetings"
        ]
    },

    "telegram": {
        "category": "communication",
        "capabilities": [
            "messaging",
            "channels"
        ]
    },

    "twilio": {
        "category": "communication",
        "capabilities": [
            "sms",
            "voice"
        ]
    },

    "intercom": {
        "category": "support",
        "capabilities": [
            "customer_support",
            "chat"
        ]
    },

    "zendesk": {
        "category": "support",
        "capabilities": [
            "tickets",
            "customer_support"
        ]
    },

    "hubspot": {
        "category": "crm",
        "capabilities": [
            "crm",
            "sales_pipeline"
        ]
    },

    "salesforce": {
        "category": "crm",
        "capabilities": [
            "crm",
            "forecasting",
            "accounts"
        ]
    },

    # =========================
    # DEVOPS
    # =========================

    "docker": {
        "category": "devops",
        "capabilities": [
            "containers",
            "deployment"
        ]
    },

    "vercel": {
        "category": "deployment",
        "capabilities": [
            "hosting",
            "deployment"
        ]
    },

    "aws": {
        "category": "cloud",
        "capabilities": [
            "cloud",
            "infrastructure",
            "storage"
        ]
    },

    "cloudflare": {
        "category": "cloud",
        "capabilities": [
            "cdn",
            "dns",
            "edge_computing"
        ]
    },

    "gitlab": {
        "category": "development",
        "capabilities": [
            "repository",
            "ci_cd"
        ]
    },

    "npm": {
        "category": "development",
        "capabilities": [
            "packages",
            "dependencies"
        ]
    },

    "playwright": {
        "category": "automation",
        "capabilities": [
            "browser_automation",
            "testing"
        ]
    },

    "stealth_browser": {
        "category": "automation",
        "capabilities": [
            "web_scraping",
            "browser_automation"
        ]
    },

    # =========================
    # DATA
    # =========================

    "bigquery": {
        "category": "data",
        "capabilities": [
            "analytics",
            "sql",
            "warehouse"
        ]
    },

    "snowflake": {
        "category": "data",
        "capabilities": [
            "warehouse",
            "analytics"
        ]
    },

    "mongodb": {
        "category": "data",
        "capabilities": [
            "nosql",
            "documents"
        ]
    },

    "airtable": {
        "category": "data",
        "capabilities": [
            "spreadsheet",
            "database"
        ]
    },

    "google_analytics": {
        "category": "analytics",
        "capabilities": [
            "traffic",
            "web_analytics"
        ]
    },

    "mixpanel": {
        "category": "analytics",
        "capabilities": [
            "product_analytics",
            "funnels"
        ]
    },

    # =========================
    # FILES
    # =========================

    "markdownify": {
        "category": "documents",
        "capabilities": [
            "markdown_conversion",
            "document_processing"
        ]
    },

    "excel": {
        "category": "documents",
        "capabilities": [
            "spreadsheet",
            "excel_processing"
        ]
    },

    "firecrawl": {
        "category": "research",
        "capabilities": [
            "web_scraping",
            "crawl"
        ]
    },

    "dropbox": {
        "category": "storage",
        "capabilities": [
            "file_storage"
        ]
    },

    "box": {
        "category": "storage",
        "capabilities": [
            "enterprise_storage"
        ]
    },

    # =========================
    # SPECIALIZED
    # =========================

    "fastmcp": {
        "category": "mcp",
        "capabilities": [
            "mcp_creation"
        ]
    },

    "mcphub": {
        "category": "mcp",
        "capabilities": [
            "mcp_management"
        ]
    },

    "codebase_memory": {
        "category": "memory",
        "capabilities": [
            "knowledge_graph",
            "code_memory"
        ]
    }
}