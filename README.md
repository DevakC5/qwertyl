# BusinessAstra 🚀

**Enterprise-Ready AI Business Assistant with Advanced Document Processing**

[![Production Ready](https://img.shields.io/badge/Production-Ready-green.svg)](https://github.com/DevakC5/qwertyl)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

BusinessAstra is a sophisticated AI-powered business assistant that combines advanced document processing, intelligent conversation categorization, and professional report generation in a secure, production-ready platform.

![BusinessAstra Dashboard](https://via.placeholder.com/800x400/1a1a1a/ffffff?text=BusinessAstra+Dashboard)

---

## ✨ **Key Features**

### 🧠 **Intelligent AI Assistant**
- **Multi-Model Support**: Integration with Together AI and Gemini
- **Smart Categorization**: 7 AI-powered conversation categories
- **Context-Aware Responses**: Maintains conversation history and context
- **Code Execution**: Sandboxed Python, ReportLab, and Manim execution

### 📄 **Advanced Document Processing**
- **Word Documents** (.docx/.doc) → Text extraction with table support
- **Excel Spreadsheets** (.xlsx/.xls) → Data extraction with sheet structure
- **PowerPoint Presentations** (.pptx/.ppt) → Slide text extraction
- **PDF Processing** → Smart text extraction + image conversion fallback
- **Image Analysis** → Direct image processing for AI analysis

### 📊 **Professional Report Generation**
- **ReportLab Integration**: Create professional PDFs programmatically
- **Business Templates**: Charts, tables, and formatted documents
- **Data Visualization**: Matplotlib integration for charts and graphs
- **Export Options**: Multiple format support with organized file management

### 🔐 **Enterprise Security**
- **CSRF Protection**: Flask-WTF with token validation
- **Security Headers**: CSP, HSTS, XSS protection via Talisman
- **Rate Limiting**: Multi-tier protection (API, uploads, authentication)
- **Secure Sessions**: HTTPOnly, Secure, SameSite cookie configuration
- **Input Validation**: Comprehensive file and data validation

### 🗄️ **Smart Data Management**
- **SQL Database**: PostgreSQL with SQLAlchemy ORM
- **Auto-Categorization**: AI-powered conversation classification
- **Rich Metadata**: Track code usage, file uploads, analysis types
- **Migration System**: Seamless upgrade from JSON to SQL storage

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.12+
- PostgreSQL (recommended for production)
- Redis (optional, for enhanced rate limiting)

### **Installation**

#### **Option 1: Docker (Recommended)**
```bash
# Clone the repository
git clone https://github.com/DevakC5/qwertyl.git
cd qwertyl

# Configure environment
cp .env.example .env
# Edit .env with your API keys and configuration

# Deploy with Docker
docker-compose up --build -d
```

#### **Option 2: Manual Setup**
```bash
# Clone and setup
git clone https://github.com/DevakC5/qwertyl.git
cd qwertyl

# Install dependencies
pip install -r requirements_production.txt

# Configure environment
cp .env.example .env
# Edit .env with your configuration

# Deploy
./deploy.sh
```

### **Configuration**
Create a `.env` file with your configuration:

```env
# Application
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/businessastra

# AI Configuration
TOGETHER_API_KEY=your-together-ai-key
TOGETHER_MODEL_NAME=meta-llama/Llama-3.3-70B-Instruct-Turbo-Free

# Security
WTF_CSRF_ENABLED=true
FORCE_HTTPS=true

# Rate Limiting
REDIS_URL=redis://localhost:6379/0
```

---

## 📋 **Architecture**

### **System Components**
```mermaid
graph TB
    A[Nginx Reverse Proxy] --> B[Gunicorn WSGI Server]
    B --> C[Flask Application]
    C --> D[SQLAlchemy ORM]
    C --> E[Together AI API]
    C --> F[Document Processor]
    D --> G[PostgreSQL Database]
    F --> H[ReportLab PDF Generator]
    F --> I[Sandbox Executor]
    C --> J[Redis Cache]
```

### **Database Schema**
- **Users**: Authentication and profile management
- **Categories**: Smart conversation categorization (7 types)
- **Conversations**: Chat history with rich metadata
- **Messages**: Individual chat messages with code detection
- **FileUploads**: Document processing history and metadata

### **Security Layers**
1. **Nginx**: Rate limiting, SSL termination, static file serving
2. **Flask-Limiter**: Application-level rate limiting
3. **Talisman**: Security headers and CSP
4. **SQLAlchemy**: SQL injection prevention
5. **CSRF Protection**: Token-based form protection

---

## 📂 **Project Structure**

```
businessastra/
├── 🐳 Deployment
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── nginx.conf
│   ├── gunicorn.conf.py
│   └── deploy.sh
├── ⚙️ Configuration
│   ├── config.py
│   ├── .env.example
│   └── wsgi.py
├── 🧠 Core Application
│   ├── main.py
│   └── templates/
├── 🧪 Testing
│   ├── test_auth.py
│   ├── test_document_processing.py
│   ├── test_sql_categorization.py
│   └── test_reportlab_functionality.py
├── 📦 Dependencies
│   ├── requirements_production.txt
│   └── requirements_document_processing.txt
└── 📚 Documentation
    ├── PRODUCTION_CHECKLIST.md
    ├── PRODUCTION_READY_SUMMARY.md
    └── deployment guides
```

---

## 🎯 **Use Cases**

### **Business Analytics**
- Upload CSV/Excel files for instant analysis
- Generate professional charts and visualizations
- Create automated business reports
- Export data insights as PDFs

### **Document Management**
- Process Word documents for content extraction
- Analyze PowerPoint presentations
- Convert and analyze PDF documents
- Organize files with smart categorization

### **Code Development**
- Execute Python scripts in secure sandbox
- Generate PDFs with ReportLab
- Create mathematical animations with Manim
- Test and validate business logic

### **Professional Reporting**
- Create branded business reports
- Generate data-driven presentations
- Export multi-format documents
- Automate report generation workflows

---

## 🔧 **Development**

### **Local Development**
```bash
# Development environment
FLASK_ENV=development python main.py

# Run tests
python -m pytest tests/

# Check health
curl http://localhost:5000/health
```

### **Testing**
```bash
# Run specific test suites
python test_auth.py
python test_document_processing.py
python test_sql_categorization.py
```

### **API Endpoints**
- **Health Check**: `GET /health` - System health status
- **Metrics**: `GET /metrics` - Performance metrics
- **Chat**: `POST /chat` - AI conversation endpoint
- **Upload**: `POST /upload` - Document upload and processing
- **Execute**: `POST /execute_code` - Code execution in sandbox

---

## 🛡️ **Security**

BusinessAstra implements enterprise-grade security:

- **🔐 Authentication**: Secure user registration and login
- **🛡️ CSRF Protection**: Token-based form protection
- **⚡ Rate Limiting**: Multi-level abuse prevention
- **🔒 Secure Headers**: CSP, HSTS, XSS protection
- **📊 Input Validation**: Comprehensive file and data validation
- **🔄 Session Security**: Secure cookie configuration

---

## 📊 **Monitoring**

### **Health Monitoring**
```json
GET /health
{
  "status": "healthy",
  "components": {
    "database": "ok",
    "together_api": "ok", 
    "document_processing": {...}
  }
}
```

### **Performance Metrics**
```json
GET /metrics
{
  "uptime": 3600,
  "database": {"users": 150, "conversations": 1200}
}
```

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Together AI** for powerful language model integration
- **Flask** ecosystem for robust web framework
- **ReportLab** for professional PDF generation
- **SQLAlchemy** for elegant database management
- **Docker** for containerization support

---

## 📞 **Support**

- **Documentation**: Check the `/docs` folder for detailed guides
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Join GitHub Discussions for community support
- **Health Check**: Monitor application status at `/health`

---

**Built with ❤️ for enterprise productivity**

[![GitHub stars](https://img.shields.io/github/stars/DevakC5/qwertyl?style=social)](https://github.com/DevakC5/qwertyl/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DevakC5/qwertyl?style=social)](https://github.com/DevakC5/qwertyl/network/members)
