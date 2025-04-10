# 📈 JSONPlaceholder API 测试项目

本项目使用 **requests + pytest** 对开放接口组合 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 进行功能性、状态码和参数化的接口测试，包括 GET/提交/PUT/删除 等 CRUD 操作。

---

## 🧠 技术栏

- Python 3.x
- requests
- pytest
- pytest-html (生成 HTML 报告)

---

## 📂 项目结构

```
api_test_project/
├── apis/
│   └── json_api.py          # 接口封装（GET/POST/PUT/DELETE）
├── tests/
│   └── test_posts.py        # Pytest 测试脚本
├── conftest.py              # Pytest 日志配置
├── requirements.txt         # 依赖包
├── pytest.ini               # pytest 配置
└── report.html              # HTML 报告
```

---

## ✅ 已实现功能

| 编号 | 功能 | 描述 |
|------|--------|------|
| TC01 | GET 查询文章 | 获取 ID = 1 的文章信息 |
| TC02 | GET 用户信息 | 获取 ID = 1 的用户 |
| TC03 | GET 评论列表 | 根据 postId 获取评论列表 (参数化) |
| TC04 | GET 未找到 | 查询不存在文章，返回 404 |
| TC05 | POST 新增文章 | 提交新文章，预期 201 状态 |
| TC06 | PUT 修改文章 | 修改旧文章内容 |
| TC07 | DELETE 删除文章 | 删除文章（虚拟删除） |

---

## 🚀 运行测试

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行所有测试 + 生成报告
```bash
pytest tests/ --html=report.html
```

> 报告生成后可用浏览器打开 `report.html`

---

## 💬 作者

该项目由 **许泽辰 (Zechen Xu)** 实战经验经手编写，适合用于简历展示、面试行为讲解和上手培训。

欢迎 Fork 或扩展更多接口场景，清楚、效率、实用 🚀

