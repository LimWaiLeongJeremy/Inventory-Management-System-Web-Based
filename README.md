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
| **Backend** | Python/Flask |
| **Database** | SQL (PostgreSQL) |
| **Security** | Prepared SQL Statements, Password Hashing |
| **Deployment** | Web Server (Werkzeug) |
| **Development Tools** | Git, VS Code |

---

## 📋 Project Scope

### 1️⃣ **Scope**
- ✅ Mobile-friendly responsive website
- ✅ Different user views (Admin, Supervisor & Normal User)
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

#### Admin:
- All standard user and Supervisors capabilities
- Manage user accounts and profiles, including adding, editing, and deleting users

### 3️⃣ **Technical Requirements**
- 🔒 **Secure SQL Database** with prepared statements
- 🎨 **User-Friendly Interface** - Easy to learn and navigate
- 🧹 **Clean UI** - Clutter-free design
- 🎛️ **Role-Based Menus** - Contextual displays for different user types
- 📝 **Transaction Logging** - Complete audit trail
- 📱 **Mobile Responsive** - Works on laptops and mobile devices

---

## 📅 Development Timeline

## 📅 Development Timeline

| Week | Milestone | Results | Status |
|---|---|---|---|
| Week 1–2 | Planning and Setup | 1. Finalizing requirements<br>2. Setup development environment<br>3. Create DB<br>4. Setup Git repo<br>5. Design basic UI wireframe | Completed |
| Week 3–5 | Foundation (Backend + DB) | 1. Working DB<br>2. Auth function-ality<br>3. Basic API endpoint | Completed / In Progress |
| Week 6–8 | Core Inventory Features | 1. Stock movement recording<br>2. Stock level updater<br>3. Transactional history | Not Started |
| Week 9–11 | Frontend Development and New Features | 1. Mobile responsive UI<br>2. Admin overview<br>3. Interactive forms<br>4. Brainstorming on SQL features | Not Started |
| Week 12–13 | Testing | 1. Data loading (if any)<br>2. Unit testing<br>3. Report generation | Not Started |
| Week 14–15 | Polish, QA and Presentation | 1. Polish and UI/UX application<br>2. Polish and QA documentation<br>3. Presentation (if any) | Not Started |
| Week 16 | Submission | Final project submission | Not Started |

**Total Duration:** 16 Weeks

---

## 🏗️ Project Structure

```
inventory-management-system/
│
├── backend/                # Server-side code
│   ├── controllers/        # API endpoints
│   ├── models/             # Database models
│   ├── services/           # Business logic
│   ├── repo/               # Database logic and querys
|   |   └── query/          # Querys
│   ├── templates/          # Frontend
│   ├── database/           # Database configuration files
│   ├── app.py              # Initilization of python app
│   ├── config.py           # Database connection configuration
│   └── requirments.txt     # Dependencies requirement file
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
- Web server (Pythin/Flask) *install requirments.txt
- Node.js 14+ 
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/inventory-management-system.git

# Navigate to project directory
cd inventory-management-system/backend

# Install dependencies
pip install -r requirements.txt      

# Set up database
Add a .env file with the DATABASE_URL in backend directory

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

### Phase 1 (Weeks 1-2) - Foundation ✅
- [x] Requirements gathering
- [x] Setup repository
- [x] Setup Dev Env
- [x] UI/UX mockups
- [x] Setup DB


### Phase 2 (Weeks 3-11) - Development 🚧
- [x] working DB
- [x] Backend API development
- [ ] Authentication API
- [ ] Frontend implementation
- [ ] Core features integration

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

### Academic Context
This project was developed as part of my academic studies at Republic Polytechnic.  
**Project ID:** SOI-2024-2420-0033  
**Course:** Part-time Diploma in Software Engineering/TGS-2023035743 
**Duration:** 15 Weeks (2026)

While this is an academic project, the code is open-sourced under MIT License to:
- 📚 Demonstrate best practices in software development
- 🤝 Allow others to learn from the implementation
- 💼 Showcase technical skills for professional opportunities
- 🌟 Contribute to the open-source community

---

## 📧 Contact

**Project Maintainer:** 
**Email:**   
**Project Link:** [https://github.com/LimWaiLeongJeremy/Inventory-Management-System-Web-Based](https://github.com/LimWaiLeongJeremy/Inventory-Management-System-Web-Based)

---

## 🙏 Acknowledgments

This project was developed as part of my coursework at Republic Polytechnic.  
Special thanks to my instructors and peers for their guidance and feedback.

**Note:** This is an educational project designed to solve real-world inventory management challenges for SME businesses.

---

## 📌 Project Status

**Current Phase:** Planning & Requirements  
**Completion:** 10%  
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