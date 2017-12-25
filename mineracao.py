import nltk

#nltk.download()

d = {'Bicicleta Monark Barra Circular Aro 26 Vermelha': 5, 'Bandeja para Servir com Alca Brinox Atina 1421/140 28x41 cm Inox': 5, 'Fone de Ouvido Maxprint Retratil 604336 1 M Branco': 5, 'Conjunto de Talheres Tramontina 24 Pecas 23399/991 Lamina de Aco Inox Cabos de Polipropileno Acai': 5, 'Jarra de Plastico 3 Litros Coza 20314/0096 Laranja': 5, 'Conjunto de Copos 6 Pecas Martiplast KT3550 Plastico Vermelho': 5, 'PORTA-RETRATO DE METAL COMUM TAMANHO 4X6 MARCA LATCOR MOD H46-118': 5, 'PORTA-RETRATO DE METAL COMUM TAMANHO 5X7 MARCA LATCOR MOD H46-61OI': 5, 'Jarra de Plastico 2,2 Litros Martiplast Bely Vitra JV550 Vermelha': 5, 'Freezer Vertical Brastemp Frost Free BVG24HBANA 197 Litros Classe A 110V Branco': 5, 'Balanca Mecanica Accumed Balmac Cinza Ate 150 kg': 2, 'Pote Redondo sem Tampa 61220/221 22cm 2,9 Litros Inox': 5}
c = []
for i in d:
    c.append(i)
#print(c)

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
#stopwordsnltk += stopwords
def removestopwords(texto):
    frases = []
    for palavras in texto:
        semstop = [p.lower() for p in palavras.split() if (p.lower() not in stopwordsnltk and p.replace('.','',1).isdigit() == False and  p.replace(',','',1).isdigit() == False and  p.replace('/','',1).isdigit() == False and  p.replace('x','',1).isdigit() == False and  p.replace('X','',1).isdigit() == False and len(p)!= 1)]
        frases.append((semstop,  'match'))
    return frases
print(removestopwords(c))