<img src="logoSmartChill.png">
<h1 align="center" style="font-weight: bold;">SmartChill </h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#routes">Endpoints da API</a> •
</p>

<p align="center">
    <b>  Faz parte do trabalho da disciplina de back-end da faculdade UNIT no período 24.2. O SmartChill é um sistema inteligente para gestão e monitoramento de dispositivos de refrigeração, com foco em otimização energética e preservação de alimentos.</b>
</p>
<p align="center">
 # Principais funcionalidades:

Monitoramento de Estoque: Permite ao usuário verificar os itens disponíveis na geladeira em tempo real, auxiliando no controle de alimentos e evitando desperdícios.
Notificações de Validade: Envia alertas sobre a data de vencimento dos produtos armazenados, garantindo o consumo seguro dos alimentos.
Lista de Compras Automatizada: Sugere itens para reposição com base no consumo habitual e nos produtos em falta, facilitando o planejamento de compras
</p>

<h2 id="tech">💻 Tecnologias</h2>

- **Java**: Desenvolvimento do backend para gerenciar lógica de negócios e funcionalidades do lado do servidor.
- **MongoDB**: Banco de dados para armazenar configurações, logs de temperatura e preferências do usuário.
- **Node.js**: Camada de middleware para comunicação em tempo real e integrações com APIs.
- **Spring Boot**: Framework utilizado para criar APIs RESTful robustas.
- **React.js**: Frontend para desenvolver uma interface interativa e amigável.
- **Docker**: Containerização para facilitar o deploy e escalabilidade.
- **Git/GitHub**: Controle de versão e colaboração no desenvolvimento.

<h2 id="started">🚀 Começando</h2>

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/smartchill.git
2. Navegue para o diretório do projeto:

cd smartchill

3. Construa e execute o backend:
cd backend
./mvnw spring-boot:run

4.Inicie o frontend:
cd frontend
npm install
npm start

<h2 id="routes"> Endpoints da API</h2>

GET /api/temperatures: Recupera logs de temperatura.
POST /api/settings: Atualiza configurações de refrigeração.
DELETE /api/alerts/:id: Remove notificações de alerta.


Crie sua branch de funcionalidade: git checkout -b funcionalidade/SuaFuncionalidade
Faça commit das suas alterações: git commit -m 'Adiciona SuaFuncionalidade'
Envie para a branch: git push origin funcionalidade/SuaFuncionalidade
Abra um pull request.


link do figma do projeto 
https://www.figma.com/proto/6MjEEhAA70prVOXgXDmaHB/Geladeira-Inteligente?node-id=1-2&t=lj7ljm2M1YsZ2z8b-1&starting-point-node-id=47%3A35
