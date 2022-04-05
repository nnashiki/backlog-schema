# backlog-schema
backlog.com の pydantic model を提供。

## 使い方

現段階では backlog.com の Webhook "課題の追加" の request body をパースできる model を提供中です。

詳しくは `backlog-schema/tests/test_backlog_schema.py` の def test_parse_add_task_request_raw をご確認ください。


## 開発方法

以下手順を実行して、ローカルソースを利用したテストができます。

```shell
$ cd backlog-schema
$ poetry shell
$ pytest
```

## publish

- `poetry build`
- `poetry publish` 
    - `poetry publish` すると user と password の確認が求められます。
- https://cocoatomo.github.io/poetry-ja/repositories/
