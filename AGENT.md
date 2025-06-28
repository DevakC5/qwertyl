# AGENT.md - BusinessAstra Development Guide

## Commands
- **Run app**: `python main.py`
- **Test auth**: `python test_auth.py`
- **Test chat history**: `python test_chat_history.py`
- **Test sandbox isolation**: `python test_no_restart.py`
- **Run single test**: `python test_<module>.py`

## Architecture
- **Flask web app** with Together AI integration for chat functionality
- **Authentication**: User management with JSON file storage (users.json)
- **Sandbox execution**: Isolated Python/LaTeX/Manim code execution in temp directories
- **File uploads**: Temporary storage in uploads_temp/ before Together AI processing
- **Static outputs**: Generated files organized in static/outputs/{images,documents,videos}/
- **Templates**: Jinja2 templates in templates/ (index.html, login.html, register.html)
- **Rate limiting**: Built-in rate limiter for API calls (5 req/60s, 50k tokens/60s)

## Code Style
- **Imports**: Standard library first, third-party, then local imports
- **Error handling**: Try-catch blocks with logging, return error responses as JSON
- **Logging**: Use `logger.info/debug/warning/error` for all operations
- **Session management**: Flask sessions for user state and message history
- **File paths**: Use `os.path.join()` for cross-platform compatibility
- **Security**: Password hashing with Werkzeug, login_required decorator for routes
- **API responses**: Return JSON with success/error status and appropriate HTTP codes
