#Sever Application that grabs a password from a dictionary
#for the user to guess

from twisted.internet import protocol, reactor
import random

class passCrack(protocol.Protocol):
    def __init__(self, data):
        #dic = open('dictionary.txt','r')
        #passlist = []
        #for word in dic:
        #    passlist.append(word.strip('\n'))
        passlist = ('ninja','frodo','luigi','nullify','sonic','mario','peach','wario','yoshi','walle','zelda','leela','felix','ralph','link','navi','deku','onox','zant','impa','sage','tatl','anju','guru','ganon','agahnim','bellum','demise','ghirahim','majora','malladus','twinrova','vaati','veran','usurper','epona','fi','groose','kaepora','gaebora','daphnes','nohansen','linebeck','marin','midna','tingle','beeble','biggoron','dampe','malon','mamamu','mutoh','postman','skullkid','syrup','talon')
        word = random.randint(0, (len(passlist)-1))
        num = random.randint(0, 9)
        num2 = random.randint(0, 9)
        self.password = passlist[word]+str(num)+str(num2)
        self.username = 'SET'
        #print 'The password it is '+self.password

    def connectionMade(self):
        client = self.transport.getPeer()
        print '<connection> ',
        print client
        self.transport.write('Username: ')

    def handle_GETUSERNAME(self, username):
        if username.strip('\r\n') == 'admin':
            self.username = 'admin'
            self.transport.write('Password: ')
        else:
            self.transport.write('Error!\nTry Again!\nUsername: ')

    def dataReceived(self, data):
        guess = data.strip("\r\n")
        if self.username == 'SET':
            self.handle_GETUSERNAME(data)
        else:
            #print 'The guess is '+guess
            #print 'The pass  is '+self.password
            if len(guess) == len(self.password):
                if self.password in guess:
                    print '<correct> ',
                    print self.transport.getPeer()
                    self.transport.write('               You are CORRECT!\n')
                    rand = random.randint(0, 4)
                    #rand = 4
                    if rand == 0:
                        #Bender
                        self.transport.write("     _________________________________\n    |.--------_--_------------_--__--.|\n    ||    /\ |_)|_)|   /\ | |(_ |_   ||\n    ;;`,_/``\|__|__|__/``\|_| _)|__ ,:|\n   ((_(-,-----------.-.----------.-.)`)\n    \__ )        ,'     `.        \ _/\n    :  :        |_________|       :  :\n    |-'|       ,'-.-.--.-.`.      |`-|\n    |_.|      (( (*  )(*  )))     |._|\n    |  |       `.-`-'--`-'.'      |  |\n    |-'|        | ,-.-.-. |       |._|\n    |  |        |(|-|-|-|)|       |  |\n    :,':        |_`-'-'-'_|       ;`.;\n     \  \     ,'           `.    /._/\n      \/ `._ /_______________\_,'  /\n       \  / :   ___________   : \,'\n        `.| |  |           |  |,'\n          `.|  |           |  |\n            |  |           |  |\nFun on a Bun!\n")
                    if rand == 1:
                        #Raptor
                        self.transport.write("                                                        .--.__\n                                                      .~ (@)  ~~~---_\n                                                     {     `-_~,,,,,,)\n                                                     {    (_  ',\n                                                      ~    . = _',\n                                                       ~-   '.  =-'\n                                                         ~     :\n      .                                             _,.-~     ('');\n      '.                                         .-~        \  \ ;\n        ':-_                                _.--~            \  \;      _-=,.\n          ~-:-.__                       _.-~                 {  '---- _'-=,.\n             ~-._~--._             __.-~                     ~---------=,.`\n                 ~~-._~~-----~~~~~~       .+++~~~~~~~~-__   /\n                      ~-.,____           {   -     +   }  _/\n                              ~~-.______{_    _ -=\ / /_.~\n                                   :      ~--~    // /         ..-\n                                   :   / /      // /         ((\n                                   :  / /      {   `-------,. ))\n                                   :   /        ''=--------. }o\n                      .=._________,'  )                     ))\n                      )  _________ -''                     ~~\n                     / /  _ _\n                    (_.-.'O'-'.\nIt's a Unix system...\nI know this\n")
                    if rand == 2:
                        #Bat
                        self.transport.write("                      _..-'(                       )`-.._\n                   ./'. '||\\.       (\_/)       .//||` .`\.\n                ./'.|'.'||||\\|..    )O O(    ..|//||||`.`|.`\.\n             ./'..|'.|| |||||\`````` '`''` ''''''/||||| ||.`|..`\.\n           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.\n          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`\ \n         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`\n        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`\n        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|\n        V    V         V          }' `\ /' `{          V         V    V\n        `    `         `               V               '         '    '\nBats are cool!\n")
                    if rand == 3:
                        #Shark
                        self.transport.write("                         __\n      o                 /' ) \n                      /'   (                          ,\n                  __/'     )                        .' `;\n   o      _.-~~~~'          ``---..__             .'   ;\n     _.--'   b)                      ``--...____.'   .'\n    (     _.      )).      `-._                     <\n     `vvvvvvv-)-.....___.-     `-.         __...--'-.'.\n       `^^^^^'-------.....`-.___.'----... .'         `.;\n                                         `-`           ` \nRawr! A shark!\n")
                    if rand == 4:
                        #Python
                        self.transport.write("                           ____\n  ________________________/ O  \___/\n <_/_\_/_\_/_\_/_\_/_\_/_______/   \ \nLOL Python\n")
                    self.transport.loseConnection()
                else:
                    self.transport.write('Try again\nPassword: ')
            else:
                self.transport.write('Try again\nPassword: ')

class passFactory(protocol.Factory):
    def __init__(self):
        self.password = ''
        self.username = ''

    def buildProtocol(self, addr):      
        return passCrack(self.password)

PORT = 8675
reactor.listenTCP(PORT, passFactory())
print 'Server running on port '+str(PORT)
reactor.run()
