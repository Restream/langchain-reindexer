# Reindexer Vector Store for LangChain

Этот пакет предоставляет интеграцию векторного хранилища для базы данных [Reindexer](https://reindexer.io/) с фреймворком [LangChain](https://github.com/hwchase17/langchain).

## Установка

```bash
pip install langchain-reindexer
```

## Использование

Сначала необходимо установить пакет Reindexer для Python:

```bash
pip install pyreindexer
```

Затем вы можете использовать векторное хранилище в вашем приложении LangChain:

```python
from langchain_community.vectorstores import ReindexerVectorStore
from langchain_openai import OpenAIEmbeddings

# Инициализация векторного хранилища
vector_store = ReindexerVectorStore(
    embedding=OpenAIEmbeddings(),
    rx_connector_config={"dsn": "builtin:///tmp/my_db"},
    rx_namespace="my_namespace",
)

# Добавление документов
from langchain_core.documents import Document

documents = [
    Document(page_content="foo", metadata={"baz": "bar"}),
    Document(page_content="thud", metadata={"bar": "baz"}),
]

ids = vector_store.add_documents(documents=documents)

# Поиск
results = vector_store.similarity_search(query="thud", k=1)
```

## Возможности

- Добавление и удаление документов
- Поиск по сходству с оценкой и без
- Фильтрация по метаданным
- Поиск максимальной предельной релевантности (MMR)
- Асинхронная поддержка
- Сохранение и загрузка конфигурации векторного хранилища