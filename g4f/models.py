from g4f import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str

    class gpt_35_turbo:
        name: str = 'CuberAI Beta 1.1'
        base_provider: str = 'brainshop'
        best_provider: Provider.Provider = Provider.Wewordle,
    }
