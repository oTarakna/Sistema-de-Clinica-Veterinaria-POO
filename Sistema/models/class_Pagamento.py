from models.classe_Servico import Servico

class Pagamento:
    def __init__(self, id_pagamento: int, valor_total: float, forma_pagamento: str, pago: bool, servico_id: int) -> None:
        self.__id = id_pagamento
        self.__valor_total = valor_total
        self.__forma_pagamento = forma_pagamento
        self.__pago = pago
        self.__servico_id = servico_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    @property
    def forma_pagamento(self) -> str:
        return self.__forma_pagamento

    @property
    def pago(self) -> bool:
        return self.__pago

    @property
    def servico_id(self) -> int:
        return self.__servico_id

    def processar_pagamento(self) -> bool:
        self.__pago = True
        return self.__pago

    def __str__(self) -> str:
        status = "LIQUIDADO" if self.__pago else "PENDENTE"
        return f"Fatura ID: {self.__id} | Valor: R${self.__valor_total} | Forma: {self.__forma_pagamento} | Status: {status}"
