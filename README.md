# Notify

## Tutorial de configuração

Acesse o arquivo ```.config_notify.json```, coloque o token do bot onde está escrito ```Inserir token```, o chatID também é necessário, insira onde está escrito ```Inserir chatID```.

## Configuração de execução

Para executar com melhor eficiencia insira esse comando em seu terminal.

```shell
sudo ln -s "$(pwd)/notify.sh" /usr/bin/notify

```

Isso irá tornar o executável visível em todo sistema, caso não faça isso será necessário rodar.

```shell
$(pwd)/notify.sh
```

## Exemplo de execução

Execute apenas ```notify``` e tenha o help da ferramenta

### Exemplo 1

```shell
notify mensagemDesejada
```

- Nesse exemplo temos uma mensagem com apenas uma palavra

### Exemplo 2

```shell
notify "mensagem desejada"
```

- Nesse exemplo temos uma mensagem composta por mais de uma palavra, informe entre aspas

### Exemplo 3

```shell
notify -v "mensagem desejada"
```

- Nesse exemplo terá um output informando que a mensagem foi enviada
