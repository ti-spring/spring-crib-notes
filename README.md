# Springアプリ開発ノウハウ集

Springでアプリケーションを開発する際に役立つノウハウ集です。

## ドキュメントのビルド方法

Dockerを使用してビルドできるようにしています。

まずコンテナイメージを作成します。

```sh
docker build -t spring-crib-notes-build .
```

コンテナでドキュメントをビルドします。

```sh
docker run --rm -v $PWD:/repos spring-crib-notes-build

# コマンドプロンプトの場合
docker run --rm -v "%CD%":/repos spring-crib-notes-build

# GitBashの場合
docker run --rm -v "/$(pwd -W)":/repos spring-crib-notes-build
```

`doc/_build/html`へドキュメントが生成されます。

## ライセンス

ドキュメントは、<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">クリエイティブ・コモンズ 表示 - 継承 4.0 国際 ライセンス</a>の下に提供されており、コードサンプルは<a rel="license" href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>の下に提供されています。
<br />
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /> </a>
