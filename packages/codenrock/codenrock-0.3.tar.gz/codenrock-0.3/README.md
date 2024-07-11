# Codenrock CLI

CLI для управления моделями ML на платформе Codenrock.

## Установка

```sh
pip install codenrock
```

## Использование

```sh
codenrock login --email your_email@example.com
codenrock create --name "Model Name" --description "Model Description" --path "/path/to/model"
codenrock update --id "model_id" --name "New Model Name" --description "New Description" --path "/path/to/new/model"
codenrock delete --id "model_id"
codenrock list
codenrock show --id "model_id"
```
