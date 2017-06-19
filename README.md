Trabalho de Sistemas Distribuídos
=================================

# Para executar:

- Instale o python 3
- Instale as dependências:

    pip install -r requirements.txt

## Para executar o servidor:

    python3 server.py


## Para executar o cliente:

    python3 client.py <NAME> <TOPIC>

Onde:

+ NAME é o nome desse cliente
+ TOPIC é o chat; para dois clientes conversarem devem estar no mesmo chat.


# Informações

O projeto foi feito usando ZeroMQ.

## Servidor

O Servidor inicia dois sockets do ZeroMQ para comunicação:

- Um socket é do tipo CLIENT/SERVER, e serve para cada cliente enviar mensagens para o servidor;
- O outro socket é do tipo PUBLISH/SUBSCRIBE, e serve para o servidor notificar os clientes quando há uma mensagem nova.

## Cliente

Cada cliente inicia também dois sockets, da mesma forma que o servidor:

- Um socket do tipo CLIENT/SERVER se conecta ao servidor;
- Um socket do tipo PUBLISH/SUBSCRIBE se conectar ao servidor também no tópico passado na linha de comando (TOPIC)

Além disso, o cliente também inicia uma thread que fica recebendo novas mensagens do servidor em background. Em foreground o cliente aguarda o usuário digitar mensagens e as envia para o servidor.
