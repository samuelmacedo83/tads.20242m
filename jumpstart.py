import pandas as pd

# assim se cria uma tabela
tabela = pd.DataFrame({
    'Nome': ['Renata', 'Anderson', 'Paulo'],
    'Nota1': [10, 5, 9],
    'Nota2': [7, 3, 9 ]  
})

# selecionar as colunas ou mudar ordem
tabela[['Nota2','Nome', 'Nota1']]

# filtrando as tabelas
tabela.query('Nota1 > 7')
tabela.query('Nome == "Renata"')
tabela.query('Nome in ("Renata", "Paulo")')

# quebrando o códido pra 
# ficar mais legível
tabela \
    .query('Nota1 > 7')

(
  tabela
    .query('Nota1 > 7')  
)

# criando colunas
tabela \
    .assign(
      media = lambda x: (x['Nota1'] + x['Nota2'])/2 
    )
(tabela['Nota1'] + tabela['Nota2'])/2 