## Reunião 19/10/2018
* Trocar ícone do acolhido para pessoas se abraçando e do trocar o do doador para o coração
* http://www.mansaodocaminho.com.br/novo2015/wp-content/uploads/2018/06/Doa%C3%A7%C3%B5es3-768x366.jpg
* Colocar grau de parentesco do responsável do acolhido
* [BD] Acolhidos da mesma família possuem o mesmo ID de família, mas são cadastrados só na tabela de acolhidos

## Reunião 01/03/2019
* Vamos usar o django-widget-tweaks
* Verificar telefones do doador (fica mesmo "telefone 1", "telefone 2"?)
    Colocar que nem agenda de celular, com um "+" do lado e o tipo de telefone (salva numa tb separada)

## Reunião 02/03/2019
* Tirar o atributo "foto" na model de Acolhido no diagrama de classes

## Para as próximas reuniões:
* Revisar todas as models do diagrama de classe
* Opção de vestimentas de acolhido e voluntariado do doador como no "Boteco do Gallão"
* Verificar nomes dos formulários no HTML (tem a ver com as URLs?)
* Melhorar botões dos formulários
* Trocar o azul do sistema por uma cor mais interessante
* Ajustar a tela de doações para ficar mais "intituitiva", com uma doação cheia de itens
* Refazer todas as URLs dentro dos formulários, para algo menos chumbado
* Como gravar um acolhido com foreign keys das tabelas de residência e trabalho?
* Colocar FK de Acolhido nas models de Residência e Trabalho
* É necessário especificar o tipo de telefone do doador? (Casa, celular ou comercial)