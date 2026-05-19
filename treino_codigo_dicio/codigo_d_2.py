personagens = {
    'Naruto': ['Sábio', 'Kurama', 'Barion', 'Sábio dos seis caminhos', 'MK'],
    'Sasuke': ['Marca da maldição', 'Sábio dos seis caminhos', 'Sharingan', 'Mangekyo Sharingan', 'Susano'],
    'Sakura': ['Byakugou', 'Academia', 'Ninja médica', 'Cem curas', 'Invocação']
}

print("Modos do Naruto:",personagens['Naruto'])
print("Modos do Sasuke:",personagens['Sasuke'])
print("Modos da Sakura:",personagens['Sakura'])

personagens['Naruto'] = personagens['Naruto'] + ['Base']
personagens['Sasuke'] = personagens['Sasuke'] + ['Base']
personagens['Sakura'] = personagens['Sakura'] + ['Base']

print("Modos do Naruto atualizado:",personagens['Naruto'])
print("Modos do Sasuke atualizado:",personagens['Sasuke'])
print("Modos da Sakura atualizado:",personagens['Sakura'])
