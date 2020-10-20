#IFAI é o nome que demos para o Assistente virtual.


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('IFAI')

#Perguntas e respostas.
conversa = ['Ola', 'Ola, em que posso te ajudar?',
            'Qual o horario da aula de matematica?', '8 horas.', 
            'Qual o link da video aula?', 'Link: meet.com/aa23s',
            'O professor de matematica esta disponivel?', 'Sim, o professor de matematica está disponivel.',
            'Vai ter aula hoje?', 'Sim, hoje terá aula.'
            ]

#Treino do bot com a conversa pré-programada
trainer = ListTrainer(bot)
trainer.train(conversa)

#Irá mostrar o chat entre o usuário e o bot
while True:
    mensagem = input('Você: ')
    resposta = bot.get_response(mensagem)

    print('IFAI: ', resposta)
