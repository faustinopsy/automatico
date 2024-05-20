# Agendador de Medicamentos

Este projeto é um agendador de medicamentos que exibe notificações e toca sons para lembrar o usuário de tomar seus medicamentos nos horários especificados.

## Funcionalidades

- Agendamento de alertas diários para tomar medicamentos
- Exibição de notificações na área de trabalho
- Reprodução de sons de alerta

## Requisitos

- Python 3.6+
- `schedule` (biblioteca para agendamento)
- `plyer` (biblioteca para notificações)
- `playsound` (biblioteca para reprodução de sons)
- `winsound` (biblioteca padrão do Windows para reprodução de sons)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/agendador-de-medicamentos.git
    cd agendador-de-medicamentos
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv agenda
    # Ativar no Windows
    .\agenda\Scripts\activate
    # Ativar no MacOS/Linux
    source agenda/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install schedule plyer playsound==1.2.2
    ```

## Uso

1. Execute o script:
    ```bash
    python main.py
    ```

2. Se o arquivo `medicamentos.txt` não existir, você será solicitado a inserir os medicamentos e horários diretamente no terminal.

3. O script agendará notificações diárias para os horários especificados.

## Compilar para Executável

Se você deseja compilar o script para um executável, siga os passos abaixo:

1. Instale o `pyinstaller`:
    ```bash
    pip install pyinstaller
    ```

2. Crie o executável:
    ```bash
    pyinstaller --onefile main.py
    ```

3. O executável será gerado no diretório `dist`. Execute-o com:
    ```bash
    ./dist/main.exe
    ```

## Exemplo de Arquivo `medicamentos.txt`

O arquivo `medicamentos.txt` deve seguir o formato abaixo:
- Medicamento A,08:00
- Medicamento B,12:00
- Medicamento C,20:00


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
agendador-de-medicamentos/
├── agenda/                  # Diretório do ambiente virtual (após criação)
├── dist/                    # Diretório do executável (após compilação)
├── main.py                  # Script principal
├── medicamentos.txt         # Arquivo de medicamentos (gerado após execução)
├── README.md                # Este arquivo
└── requirements.txt         # (Opcional) Lista de dependências
