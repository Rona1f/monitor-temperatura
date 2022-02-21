# Monitor de temperatura

Este projeto monitora temperatura e umidade em um ambiente, emite alertas via email em caso de picos de temperatura e envia os dados a um servidor que podem ser visualizados em uma página web. 

O software consiste em um código em python que faz leituras através de um sensor de temperatura e umidade DHT11 ligado a um Raspberry pi. Quando detecta um aumento acima de um valor de corte na temperatura, é enviado um email informando que algo pode estar errado no ambiente. 



## Instalação 

O projeto está disponível na página do github: http://github.com/rona1f/monitor-temperatura. 

Basta usar o comando: git clone http://github.com/rona1f/monitor-temperatura 

Isso irá criar um diretório com o projeto em /pi/home/  

 

## Descrição 

temperatura.py: é o arquivo python principal 

/server: é a pasta com os arquivos do monitor web 

start-sensor-temp.sh: script para iniciar o ambiente python e executar o programa 

 

## Inicializando sessão 

Este sistema pode ser configurado para iniciar no início de uma sessão do raspberry. Para isso, basta adicionar ao arquivo .profile (localizado em /home/pi) o comando que executa o arquivo start-sensor-temp.sh: source /home/pi/monitor-temperatura/start-sensor-temp.sh 

O script deve ser modificado da seguinte forma: todos os dispositivos da rede devem executar os comandos referentes ao python.  

Apenas um dos raspberry deve executar os comandos referentes ao node.js, nos demais, essas linhas devem estar comentadas ou ser excluídas. 

 

## Configuração do codigo python 

Em temperatura.py há uma área com variáveis que devem ser alteradas. É importante que o nome do dispositivo seja único. 

 

 

## Hardware 

O sensor deve ser ligado ao Raspberry pi conforme a imagem abaixo. O pino de dados por padrão está na porta 4, e em caso de mudança, deve ser modificado também no codigo temperatura.py.  


Conferir o modelo do sensor para saber as posições dos pinos VCC, GND e DATA 

[![0mMZJ9.png](https://iili.io/0mMZJ9.png)](https://freeimage.host/br)

Fonte: https://www.youtube.com/watch?v=nTomhTSao4g&t=220s 

 

 

### Links uteis: 

Aula completa sobre o sensor e como usá-lo com o raspberry: https://www.youtube.com/watch?v=nTomhTSao4g&t=220s 

 