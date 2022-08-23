
class pagamento:
    def __init__(self, user_id, causale, importo, stato_pagato, stato_multato, data_scadenza):
        self.user_id = user_id
        self.causale = causale
        self.importo = importo
        self.stato_pagato = stato_pagato
        self.stato_multato = stato_multato
        self.data_scadenza = data_scadenza
    pass
