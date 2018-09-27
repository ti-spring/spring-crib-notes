# テーブル認証を使ったログイン画面サンプル


## 実行手順
### 1. アプリケーションの起動
```bash
mvn spring-boot:run
```

### 2. ログインを行う
以下のページにアクセスすることでログイン画面を表示できます。

* http://localhost:8080

ユーザ名とパスワードに以下の情報を入力しログイン処理を行います。
ログインが成功すると、ログインユーザ名が表示されるページに遷移します。

| ユーザ名 | パスワード |
|----------|------------|
| admin    | password_  |