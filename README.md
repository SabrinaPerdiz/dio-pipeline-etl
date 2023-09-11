# ETL na tradução de idiomas

### Apresentação
Em meu projeto utilizando o processo ETL, criei um script para traduzir para o português frases aleatórias dentro de um tema definido pelo usuário. O objetivo é retornar citações creditadas para serem usadas em redações, publicidades, etc.

### Ferramentas
Para obter as frases de acordo com o tema utilizei a API do site FavQs, que disponibiliza a ferramenta gratuitamente, necessitando somente um cadastro informando o e-mail.
<br>
Para realizar a tradução, utilizei a biblioteca googletrans.

>OBS: Por não se tratar de um recurso oficial fornecido pelo Google e sim criada a partir da API oficial, acaba tendo alguns erros em termos de tradução/grafia, no entanto, o resultado é satisfatório e os problemas podem ser relevados por não serem o foco deste projeto.

### Processo ETL
<b>Extração:</b> feita ao chamar o endpoint https://favqs.com/api/quotes' para obter as frases do tema informado

<b>Transformação:</b> tradução das frases para o português

<b>Carregamento:</b> csv gerado com as frases salvo na máquina

### Links Úteis
Documentação da API do site FavQs: https://favqs.com/api
<br>
Documentação da biblioteca googletrans: https://py-googletrans.readthedocs.io/en/latest/
<br>
Documentação da API do Google de tradução: https://cloud.google.com/translate/docs/reference/rest