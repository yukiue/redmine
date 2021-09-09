# Redmine

コマンドラインから [Redmine](https://www.redmine.org/) を操作するコード

- `update-status.py`

  指定した ISSUE_ID の STATUS ('ToDo' or 'Doing' or 'Done') を更新する

  usage: `python3 update-status.py [ISSUE_ID] [STATUS]`

  example: `python3 update-status.py 1 Done`

- `close-issues.py`

  指定した複数の ISSUE_ID のチケットのステータスを全て 'Done' にする

  usage: `python3 close-issues.py [ISSUE_ID...]`

  example: `python3 close-issues.py 1 2 3`

- `get-event.py`

  終了時刻が過ぎたイベントの開催通知の一覧を表示する

  usage: `python3 get-event.py`

# Note
- 変数 `SERVER_URL` は環境に合わせて変更する
- 環境変数 `REDMINE_API_ACCESS_KEY` を設定する
