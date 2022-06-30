import psycopg2

class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParams(self):
        self.dadosconexao = "host=localhost dbname=pokeapp user=postgres password=123qwe"
        return self
    
    def alteraBD(self, stringSQL, values):
        conn = None
        try:
            conn = psycopg2.connect(config.setParams(self).dadosconexao)

            sessao = conn.cursor()

            sessao.execute(stringSQL, values)

            conn.commit()

            sessao.close()
        
        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return 'sucesso'
    

