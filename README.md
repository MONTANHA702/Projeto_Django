# 📝 Curso Django

Projeto em desenvolvimento durante o aprendizado de Django, consistindo em um blog pessoal com sistema de autores, artigos e categorias por eixo tecnológico.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.10](https://www.python.org/)
- [Django 5.2](https://www.djangoproject.com/)
- [Django Jazzmin](https://django-jazzmin.readthedocs.io/) — tema moderno para o admin
- [TinyMCE](https://www.tiny.cloud/) — editor de texto rico para artigos
- [SQLite](https://www.sqlite.org/) — banco de dados para desenvolvimento

---

## 📦 Funcionalidades

- Cadastro de autores com nome, biografia e e-mail
- Publicação de artigos com editor rich text (TinyMCE)
- Categorização de artigos por eixo tecnológico
- Listagem de autores e seus respectivos artigos
- Painel administrativo customizado com Jazzmin
- Páginas de documentação integradas

---

## ⚙️ Como rodar o projeto

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Projeto_Django.git
cd Projeto_Django
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Rode as migrações:**
```bash
python manage.py migrate
```

**5. Crie um superusuário:**
```bash
python manage.py createsuperuser
```

**6. Inicie o servidor:**
```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Painel admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📁 Estrutura do Projeto

```
cursodjango/
├── cursodjango/        # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
├── motorartigos/       # App principal
│   ├── models.py       # Autor, EixoTecnologia, Artigo
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/             # Imagens e arquivos estáticos
├── manage.py
└── README.md
```

---

## 👨‍💻 Autor

Desenvolvido como projeto prático do curso de Django.

---

## 📄 Licença

Este projeto é de uso educacional e livre para estudo.
