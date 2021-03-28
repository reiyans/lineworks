# `lineworks` -LINE WORKS APIを呼び出すPythonライブラリ
**lineworks**は、ビジネスチャット[LINE WORKS](https://line.worksmobile.com/jp/)のAPIを呼び出すためのPythonライブラリです。
トークBotを使ったアプリケーション作成の効率化のために開始しました。


# インストール
pipを使用してlineworksをインストールします。

`pip install lineworks`

### 依存関係
[cryptography](https://pypi.org/project/cryptography/)、[PyJWT](https://pypi.org/project/PyJWT/)及び[requests](https://pypi.org/project/requests/)に依存しています。
サーバーAPIを呼び出す際にはアクセストークンが必要です。
アクセストークンを取得する際にはJWTを生成/電子署名を行いますが、そのJWT生成/電子署名にPyJWTを使用します。
cryptographyは、PyJWTが電子署名アルゴリズムRS256を使用するのに必要です。
詳細はPyJWTの[documentation](https://pyjwt.readthedocs.io/en/latest/installation.html)をご覧ください。


# クイックスタート
本ライブラリの使用例をご紹介致します。
なお、本ライブラリの使用にはLINE WORKS API情報が必要です。使用前に、[LINE WORKS Developer Console](https://developers.worksmobile.com/jp/console/openapi/main)で発行してください。

## `TalkBotApi`クラスのインスタンスを生成する
`TalkBotApi`クラスは、アクセストークン取得メソッド`get_access_token()`とサーバーAPI呼び出しメソッド`call_server_api()`を持つ`ServerApi`クラスの子クラスです。
トークBot APIを呼び出すために、`TalkBotApi`クラスのインスタンスを生成します。
なお、Developer Consoleで登録したBotを利用する場合、キーワード引数`bot_no`に当該BotのBot No.を渡します。

```
>>> from lineworks import TalkBotApi
>>> api_id = "your api id."
>>> server_api_consumer_key = "your server api consumer key"
>>> server_id = "your server id."
>>> private_key = "your private key."
>>> domain_id = "your domain id."
>>> bot_no = "your bot number."
>>> talk_bot = TalkBotApi(api_id, server_api_consumer_key, server_id, private_key, domain_id, "your bot no.(option)")
```

### 補足
ソースコードをサーバーにデプロイする場合、API情報をソースコードに含めることはセキュリティの観点からもお勧めできません。
.envファイルを作成して同ファイルにアクセスする、環境変数に登録して`os.environ.get()`でアクセスするなどの対策をしてください。

## `TalkBotApi`クラスのメソッドを使用する
`TalkBotApi`クラスのメソッドは、①登録済みBotを使用するものと②それ以外に大別されます。
前者を使用する場合は必ず、`TalkBotApi`クラスのインスタンス生成時、キーワード引数`bot_no`に使用するBotのBot No.を渡してください。
使用方法は以下のとおりです（使用方法の詳細は各メソッドのdocstringをご覧ください）。

### ①登録済みのBotを使用するもの
```python
from lineworks import TalkBotApi

api_id = "your api id."
server_api_consumer_key = "your server api consumer key"
server_id = "your server id."
private_key = "your private key."
domain_id = "your domain id."
bot_no = "your bot number."

talk_bot = TalkBotApi(api_id, server_api_consumer_key, server_id, private_key, domain_id, "your bot no.(option)")

# トークBotの修正
talk_bot.bot_fix(name="テストBot", photo_url="https://www.example.com/~.jpg", description="Botの説明を修正しました。",
                 managers=["test1@example.com", "test2@example.com"])

# トークBotの削除
talk_bot.remove_bot()

# トークBot詳細情報の紹介
talk_bot.query_bot_info()

# トークBotのドメイン登録
talk_bot.bot_domain_registration(use_public=True)

# トークBotドメイン公開設定の修正
talk_bot.bot_domain_fix(use_public=False)

# トークBotのドメイン削除
talk_bot.bot_domain_delete()

# Botを含むトークルーム作成
talk_bot.create_room(account_ids=["test1@example.com", "test2@exaple.com"], title="テストルーム")

# Botトークルームのメンバーリスト照会
talk_bot.query_room_member_list(room_id="12345")

# Botの退室
talk_bot.bot_leaving_room(room_id="12345")

# メッセージ送信（Text）
talk_bot.send_text_message(send_text="こんにちは", account_id="test1@example.com")
```

### ②それ以外
```python
from lineworks import TalkBotApi

api_id = "your api id."
server_api_consumer_key = "your server api consumer key"
server_id = "your server id."
private_key = "your private key."
domain_id = "your domain id."
bot_no = "your bot number."

talk_bot = TalkBotApi(api_id, server_api_consumer_key, server_id, private_key, domain_id, "your bot no.(option)")

# トークBotの登録
talk_bot.register_bot(name="テストBot", photo_url="https://www.example.com/~.jpg", description="これはテスト用Botです。",
                      managers=["test1@example.com", "test2@example.com"])

# トークBotリスト照会
talk_bot.query_bot_list()
```
