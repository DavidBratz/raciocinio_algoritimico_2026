personagens = {
    'Naruto': ['Sábio', 'Kurama', 'Barion', 'Sábio dos seis caminhos', 'MK'],
    'Sasuke': ['Marca da maldição', 'Sábio dos seis caminhos', 'Sharingan', 'Mangekyo Sharingan', 'Susano'],
    'Sakura': ['Byakugou', 'Academia', 'Ninja médica', 'Cem curas', 'Invocação']
}

print("=================================================================================================================================================")

print("Modos do Naruto:",personagens['Naruto'])
print("Modos do Sasuke:",personagens['Sasuke'])
print("Modos da Sakura:",personagens['Sakura'])

print("=================================================================================================================================================")

personagens['Naruto'] = personagens['Naruto'] + ['Base']
personagens['Sasuke'] = personagens['Sasuke'] + ['Base']
personagens['Sakura'] = personagens['Sakura'] + ['Base']

print("Modos do Naruto atualizado pós adição:",personagens['Naruto'])
print("Modos do Sasuke atualizado pós adição:",personagens['Sasuke'])
print("Modos da Sakura atualizado pós adição:",personagens['Sakura'])

personagens['Naruto'].remove('Kurama')
personagens['Sasuke'].remove('Susano')
personagens['Sakura'].remove('Academia')

print("=================================================================================================================================================")

print("Modos do Naruto atualizado pós remoção:",personagens['Naruto'])
print("Modos do Sasuke atualizado pós remoção:",personagens['Sasuke'])
print("Modos da Sakura atualizado pós remoção:",personagens['Sakura'])

print("=================================================================================================================================================")
