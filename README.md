# djangoでmongodbを利用したサンプルAPI

ODMとしてdjongoを利用する。

## 環境構築

```bash=
docker compose up
```

## sample command

データのPOST

```bash=
curl -XPOST -H 'Content-Type:application/json' -d '{"title": "sample book","description": "sample","author":{"name": "hoge", "age": 20}}' http://localhost:8000/api/book/
```

データのGET
```bash=
curl -XGET -H 'Content-Type:application/json' http://localhost:8000/api/book/
```
