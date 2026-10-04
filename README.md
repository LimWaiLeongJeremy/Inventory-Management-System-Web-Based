# 📦 Inventory Management System (Web-Based)

[![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)](https://github.com/yourusername/inventory-management-system)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Web-green)](https://github.com/yourusername/inventory-management-system)
[![Academic](https://img.shields.io/badge/Project-Academic-purple)](https://github.com/yourusername/inventory-management-system)


> **Project ID:** SOI-2024-2420-0033  
> **Duration:** 15 Weeks  
> **Type:** Full-Stack Web Application

A mobile-friendly, web-based inventory management system designed to eliminate manual recording processes, reduce human errors, and streamline production inventory tracking for businesses.

---

## 🎯 Project Overview

Currently, companies manually record production inventory, leading to inefficiencies and human errors due to numerous tedious steps. This system enables employees to digitally track daily product movements, perform stock-taking, and generate comprehensive reports—all through an intuitive web interface.

### 🌟 Key Benefits
- ✅ **Eliminates manual recording** errors
- ✅ **Saves time** with streamlined workflows
- ✅ **Real-time tracking** of inventory movements
- ✅ **Comprehensive reporting** for better decision-making
- ✅ **Mobile-friendly** for on-the-go access
- ✅ **Scalable** for SMEs (pet shops, IT stores, mini supermarkets)

---

## 🚀 Features

### Core Functionality
- 📥 **Inbound Production Entry** - Record incoming products
- 📤 **Outbound Production Tracking** - Log outgoing inventory
- 🔄 **Movement Recording** - Track product transfers between locations
- 📊 **Stock-Taking Module** - Perform physical inventory counts
- 📈 **Real-Time Stock Levels** - Monitor current inventory at a glance

### Reporting & Analytics
- 📋 **Inbound/Outbound Reports** - Track product flow
- 🚚 **Movement/Transfer Reports** - Location-based tracking
- 📝 **Transaction Logs** - Complete audit trail
- 💹 **Current Stock Level Reports** - Instant inventory overview

### User Management
- 👤 **Role-Based Access Control**
  - **Normal Users:** Data entry and viewing
  - **Supervisors:** Full access including stock-taking and reporting
- 🔐 **Secure Authentication** - User login and session management

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Frontend** | HTML, CSS, JavaScript (Responsive Design) |
| **Backend** | Python/Flask/Node.js *(to be determined)* |
| **Database** | SQL (MySQL/PostgreSQL) *(to be determined)* |
| **Security** | Prepared SQL Statements, Password Hashing |
| **Deployment** | Web Server (Apache/Nginx) *(to be determined)* |
| **Development Tools** | Git, VS Code |

---

## 📋 Project Scope

### 1️⃣ **Scope**
- ✅ Mobile-friendly responsive website
- ✅ Different user views (Admin & Normal User)
- ✅ Inbound/Outbound production number entry
- ✅ Report generation and viewing
- ✅ Stock-taking and current stock level tracking
- ✅ Presentation slides with project documentation

### 2️⃣ **User Requirements**

#### Standard Users:
- Enter inbound production numbers
- Enter outbound production numbers
- Record product movements between locations

#### Supervisors:
- All standard user capabilities
- Perform stock-taking operations
- Generate and view comprehensive reports (Inbound/Outbound/Movement/Transactions/Stock Levels)

### 3️⃣ **Technical Requirements**
- 🔒 **Secure SQL Database** with prepared statements
- 🎨 **User-Friendly Interface** - Easy to learn and navigate
- 🧹 **Clean UI** - Clutter-free design
- 🎛️ **Role-Based Menus** - Contextual displays for different user types
- 📝 **Transaction Logging** - Complete audit trail
- 📱 **Mobile Responsive** - Works on laptops and mobile devices

---

## 📅 Development Timeline

| Phase | Duration | Milestones |
|-------|----------|-----------|
| **Planning & Requirements** | Week 1-2 | Requirements gathering, documentation |
| **Design** | Week 3-5 | Database schema, UI/UX mockups |
| **Development** | Week 6-11 | Backend, frontend, core features, reporting |
| **Testing** | Week 12-14 | QA, UAT, bug fixes |
| **Deployment** | Week 15 | Training, go-live, handover |

**Total Duration:** 15 Weeks

---

## 🏗️ Project Structure

```
inventory-management-system/
│
├── backend/              # Server-side code
│   ├── api/             # API endpoints
│   ├── models/          # Database models
│   ├── controllers/     # Business logic
│   └── config/          # Configuration files
│
├── frontend/            # Client-side code
│   ├── assets/          # Images, CSS, JS
│   ├── views/           # HTML templates
│   └── components/      # Reusable UI components
│
├── database/            # Database scripts
│   ├── schema.sql       # Database structure
│   └── seed.sql         # Sample data
│
├── docs/                # Documentation
│   ├── requirements.md  # Project requirements
│   ├── api-docs.md      # API documentation
│   └── user-guide.md    # User manual
│
├── tests/               # Test files
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚦 Getting Started

### Prerequisites
- Web server (Apache/Nginx)
- SQL Database (MySQL 5.7+ or PostgreSQL 12+)
- PHP 7.4+ / Python 3.8+ / Node.js 14+ *(depending on final tech choice)*
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/inventory-management-system.git

# Navigate to project directory
cd inventory-management-system

# Install dependencies
# (Commands will be added once tech stack is finalized)

# Set up database
# Import schema.sql into your SQL database

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# Start the application
# (Start commands will be added once tech stack is finalized)
```

---

## 👥 User Roles

| Role | Permissions |
|------|------------|
| **Admin** | Full system access, user management, all reports |
| **Supervisor** | Stock-taking, report generation, view all transactions |
| **Normal User** | Data entry (inbound/outbound/movements), view stock levels |

---

## 📊 Key Metrics & Success Criteria

- ✅ **Reduce manual entry time** by 60%
- ✅ **Decrease recording errors** by 80%
- ✅ **Improve inventory accuracy** to 95%+
- ✅ **User adoption rate** of 90% within 2 weeks
- ✅ **System uptime** of 99%+

---

## 🗺️ Roadmap

### Phase 1 (Weeks 1-5) - Foundation ✅
- [ ] Requirements gathering
- [ ] Database design
- [ ] UI/UX mockups

### Phase 2 (Weeks 6-11) - Development 🚧
- [ ] Backend API development
- [ ] Frontend implementation
- [ ] Core features integration
- [ ] Reporting module

### Phase 3 (Weeks 12-14) - Testing 📝
- [ ] Unit & integration testing
- [ ] Security testing
- [ ] User acceptance testing

### Phase 4 (Week 15) - Launch 🚀
- [ ] Production deployment
- [ ] User training
- [ ] Documentation delivery

---

## 📖 Documentation

- [Requirements Document](docs/requirements.md)
- [API Documentation](docs/api-docs.md)
- [User Guide](docs/user-guide.md)
- [Database Schema](docs/database-schema.md)
- [Development Timeline](docs/timeline.md)

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🔒 Security

- All SQL queries use **prepared statements** to prevent SQL injection
- User passwords are **hashed and salted**
- Session management with **secure tokens**
- Regular **security audits** during development

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Project Maintainer:** 
**Email:**   
**Project Link:** [https://github.com/LimWaiLeongJeremy/Inventory-Management-System-Web-Based](https://github.com/LimWaiLeongJeremy/Inventory-Management-System-Web-Based)

---

## 🙏 Acknowledgments

- Designed for SME businesses including pet shops, IT & gadget stores, and mini supermarkets
- Built to address real-world inventory management challenges
- Special thanks to all stakeholders and end-users for their valuable feedback

---

## 📌 Project Status

**Current Phase:** Planning & Requirements  
**Completion:** 0%  
**Next Milestone:** Design (Week 3)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for better inventory management

</div>

---

## 📸 Screenshots

*Screenshots will be added as the project progresses*

### Dashboard Preview
```
[Coming Soon]
```

### Mobile View
```
[Coming Soon]
```

### Reports Module
```
[Coming Soon]
```