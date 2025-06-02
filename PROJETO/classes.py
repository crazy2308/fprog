#Projeto  realizado por Pedro Alves (ist1114108) e José Lima (ist1114120)

# este ficheiro cria todas as funções e classes e precisamos para definir o projeto final
# Muitas vezes o código não tem qualquer comentário pois é repetição de código já comentado anteriormente, ou seja, é o mesmo código mas com pequenas alterações para se adaptar ao tier que estamos a implementar. Muitas vezes é explicado anteriormente, por isso não é necessário repetir o comentário.

from graphics import *
from math import * #Utiliza-se esta biblioteca para facilitar o cálculo da distância entre dois pontos para consumir bateria, utiliza-se a função sqrt
from time import sleep #Unica forma de utilizar o tempo de espera entre movimentos, ou seja, para suavizar o movimento do robô

class Waiter: # Classe que define o robo, a bateria, e os movimentos do robo
    def __init__(self, window, center_point, body_radius, battery_level, posicoes_mesa, posicoes_Div):

        self.window = window # Janela onde o robo será desenhado
        self.center = center_point # Ponto central do robo
        self.body_radius = body_radius # Raio do corpo do robo
        self.battery_level = battery_level # Nível de bateria do robo
        self.posicoes_mesa = posicoes_mesa # Lista de posições das mesas
        self.posicoes_Div = posicoes_Div # Lista de posições das divisões
        self.obstaculos = []  # Lista para armazenar os obstáculos
        self.obstaculos_imagens = []  # Lista para armazenar as imagens dos obstáculos
        self.posicao_x = self.center.getX() # Posição X do robo
        self.posicao_y = self.center.getY() # Posição Y do robo
        self.body_parts = [] # Lista para armazenar as partes do corpo do robo

        # Corpo do robô
        self.body = Circle(self.center, self.body_radius)
        self.body.setFill("white")
        self.body.draw(self.window)
        self.body_parts.append(self.body)

        # Indicador de bateria
        battery_radius = (self.body_radius / 4)
        self.battery = Circle(self.center, battery_radius)
        self.battery.setFill("green")
        self.battery.draw(self.window)
        self.body_parts.append(self.battery)

    def consumir_bateria(self, distancia): #define a função que consome bateria e dá um debug
        quantidade = 0.1  # Quantidade de bateria consumida por unidade de distância
        self.battery_level -= quantidade * distancia  # Consome bateria proporcional à distância percorrida
        if self.battery_level < 0:
            self.battery_level = 0
        self.cor_bateria()
        self.atualizar_mostrador() # Atualiza o mostrador de bateria
        print(f"Bateria atual: {self.battery_level:.0f}%") #Debug da bateria
    
    def carregar_bateria(self, x, y):
        if 95 <= x <= 99 and 143 <= y <= 147:  # Verifica se o robo está na estação de carregamento, existe um intervalo em vez de um ponto exato para evitar problemas de precisão
            for i in range(10):  # 10 vezes, 10 unidades por vez
                if self.battery_level < 100:
                    self.battery_level += 10
                    if self.battery_level > 100:
                        self.battery_level = 100 # Garante que a bateria não ultrapassa 100%
                    self.atualizar_mostrador()
                    self.cor_bateria()
                    time.sleep(0.2)  # tempo entre cargas
                    print(f"Bateria atual: {self.battery_level:.0f}%") # Debug da bateria para quando o robo está a carregar
    

    def mostrador(self, battery_level): # Cria o mostrador da bateria
        self.rect = Rectangle(Point(3, 142), Point(40, 149))
        self.rect.setOutline("black")
        self.rect.setFill("green")
        self.rect.draw(self.window)

        self.battery_text = Text(self.rect.getCenter(), f"Bateria: {battery_level:.0f}%")
        self.battery_text.setSize(10)
        self.battery_text.setTextColor("black")
        self.battery_text.draw(self.window)

    def atualizar_mostrador(self): # Atualiza o texto do mostrador com o nível atual de bateria
        self.battery_text.setText(f"Bateria: {self.battery_level:.0f}%")

    # Define a cor da bateria e do mostrador com base no nível da mesma
    def cor_bateria(self):
        if self.battery_level > 60:
            self.battery.setFill("green")
            self.rect.setFill("green")
        elif self.battery_level > 30:
            self.battery.setFill("yellow") 
            self.rect.setFill("yellow")
        elif self.battery_level > 0:
            self.battery.setFill("red")
            self.rect.setFill("red")
        if self.battery_level <= 0:
            self.battery.setFill("black")
            self.rect.setFill("black")

    # Dividiomos métodos de movimento em tiers para diferentes comportamentos:
    def mover_tier1(self, destino_x, destino_y): # Tier 1: Movimento simples, sem colisões ou obstáculos
       
        passos = 100
        # Calcula o deslocamento em X e Y para cada passo, desta forma cada movimento é suave mas é feito sempre no mesmo número de passos, ou seja demora o mesmo tempo independentemente da distância
        dx = (destino_x - self.posicao_x) / passos 
        dy = (destino_y - self.posicao_y) / passos

        for i in range(passos): #Repete o movimento para cada passo
            novo_x = self.posicao_x + dx
            novo_y = self.posicao_y + dy

            for parte in self.body_parts:
                parte.move(dx, dy)

            self.posicao_x = novo_x
            self.posicao_y = novo_y
            time.sleep(0.005) # Pequena pausa para suavizar o movimento


    def mover_tier2(self, destino_x, destino_y): # Tier 2: Movimento com verificação de colisões e obstáculos     

        passos = 100
        dx = (destino_x - self.posicao_x) / passos
        dy = (destino_y - self.posicao_y) / passos

        for i in range(passos):

            novo_x = self.posicao_x + dx
            novo_y = self.posicao_y + dy

            click = self.window.checkMouse() # Verifica se houve clique durante o movimento
            if click:
                print("Clique durante o movimento!") #Debug do clique
                self.obstaculo(click)  # Adiciona obstáculo

            colisao, posicao = self.colisao(novo_x, novo_y)

            if colisao == "bateu":
                print(f"Colisão detectada com obstáculo na posição {posicao}!") #Debug da colisão, a posição é o índice do obstáculo na lista
                time.sleep(2.0) # Pausa para simular o tempo de remoção do obstáculo
                self.obstaculos.pop(posicao) # Remove o obstáculo da lista
                self.obstaculos_imagens[posicao].undraw() # Remove a imagem do obstáculo da janela
                self.obstaculos_imagens.pop(posicao)  #Remove a imagem da lista


            for parte in self.body_parts:
                parte.move(dx, dy)

            self.posicao_x = novo_x
            self.posicao_y = novo_y

            self.consumir_bateria(sqrt(dx**2 + dy**2)) # Consome bateria proporcional à distância percorrida
            time.sleep(0.005)

    def mover_tier3(self, destino_x, destino_y): # Tier 3: Movimento com verificação de colisões, obstáculos e interação com mesas  

        passos = 100
        dx = (destino_x - self.posicao_x) / passos
        dy = (destino_y - self.posicao_y) / passos

        for i in range(passos):

            novo_x = self.posicao_x + dx
            novo_y = self.posicao_y + dy

            click = self.window.checkMouse()
            if click:
                print("Clique durante o movimento!")
                self.obstaculo(click)

            colisao, posicao = self.colisao(novo_x, novo_y)

            if colisao == "bateu":
                print(f"Colisão detectada com obstáculo na posição {posicao}!")
                time.sleep(2.0)
                self.obstaculos.pop(posicao)
                self.obstaculos_imagens[posicao].undraw()
                self.obstaculos_imagens.pop(posicao)


            for parte in self.body_parts:
                parte.move(dx, dy)

            self.posicao_x = novo_x
            self.posicao_y = novo_y

            self.consumir_bateria(sqrt(dx**2 + dy**2))
            time.sleep(0.005)

    def table_check(self, click_point, mesas):

        for mesa in mesas:
            if mesa.det_table(click_point):  # Verifica se o clique está dentro da mesa
                print("Clique detectado em uma mesa!") # Debug do clique na mesa
                return True  # Indica que o clique foi em uma mesa
        return False  # Indica que o clique não foi em uma mesa
    
    def go_to_table_tier1(self, mesas):
        ponto1 = Point(97.0, 135.0)  # Docking station
        ponto2 = Point(97.0, 145.0)  # Ponto de destino do robô
        ponto_intermedio = Point(75, 136)  # Ponto de transição

        # Desenha a imagem em todas as mesas e guarda as referências
        imagens = []
        for mesa in mesas:
            center = mesa.rect.getCenter()
            img = Image(center, 'bifana.png')
            img.draw(self.window)
            imagens.append((mesa, img))

        # Para cada mesa, segue o percurso restrito, espera, retira a imagem, vai ao ponto intermédio, espera, segue para a próxima
        for mesa, img in imagens:
            center = mesa.rect.getCenter()
            if mesa.ident == "EE":
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "EC":
                self.mover_tier1(center.getX() + 15, 135.0)
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(center.getX() + 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "DC":
                self.mover_tier1(center.getX() - 15, 135.0)
                self.mover_tier1(center.getX() - 15, center.getY())
                self.mover_tier1(center.getX() - 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            elif mesa.ident == "DD":
                self.mover_tier1(center.getX() + 15, 135.0)
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(center.getX() + 13, center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(center.getX() + 15, center.getY())
                self.mover_tier1(self.posicao_x, 135.0)
                self.mover_tier1(ponto_intermedio.getX(),ponto_intermedio.getY())
                sleep(1.0)
            else:
                # Caso não seja nenhum dos identificadores acima, faz um movimento simples
                self.mover_tier1(center.getX(), center.getY())
                sleep(2.0)
                img.undraw()
                self.mover_tier1(ponto_intermedio.getX(), ponto_intermedio.getY())
                sleep(1.0)

        # No fim, volta à docking station
        self.mover_tier1(ponto1.getX(), ponto1.getY())
        self.mover_tier1(ponto2.getX(), ponto2.getY())

    def go_to_table_tier2(self, click_point, mesas):
        ponto1 = Point(97.0, 135.0)  # Ponto inicial do robô
        ponto2 = Point(75.0, 136.0)  # Ponto de destino do robô
        ponto3 = Point(97.0, 145.0)  # Ponto de destino do robô
        
        for mesa in mesas:
            if mesa.det_table(click_point):  # Verifica se o clique está dentro da mesa
                mesa.rect.setFill("green")  # Muda a cor da mesa para verde para destacar o clique
                print("Clique detectado em uma mesa!") # Debug do clique na mesa
                center = mesa.rect.getCenter() # Obtém o centro da mesa
                img = Image(center, 'bifana.png') # Cria a imagem da bifana
                    
                self.mover_tier2(ponto1.getX(), ponto1.getY())  # Move o robô para o ponto inicial
                
                if mesa.ident in ["EE"]: #Movimento para as mesas que estão na coluna esquerda
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    sleep(2.0) # Está a receber o pedido da bifana
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(self.posicao_x, 135.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0) # Está a buscar a imagem da bifana na mesa
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    img.draw(self.window) # Desenha a imagem da bifana na mesa
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY()) # Volta ao ponto inicial

                if mesa.ident in ["EC"]: #Movimento para as mesas que estão na coluna esquerda central
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                if mesa.ident in ["DC"]: #Movimento para as mesas que estão na coluna direita central
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() - 15, center.getY())
                    self.mover_tier2(center.getX() - 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                if mesa.ident in ["DD"]: #Movimento para as mesas que estão na coluna direita
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(self.posicao_x, 135.0)
                    self.mover_tier2(ponto2.getX(), ponto2.getY())
                    self.mover_tier2(75, 136)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 13, center.getY())
                    img.draw(self.window)
                    sleep(2.0)
                    self.mover_tier2(center.getX() + 15, center.getY())
                    self.mover_tier2(center.getX() + 15, 135.0)
                    self.mover_tier2(ponto1.getX(), ponto1.getY())
                    self.mover_tier2(ponto3.getX(), ponto3.getY())

                mesa.rect.setFill(mesa.cor_original) # Restaura a cor original da mesa após a entrega
                self.carregar_bateria(self.posicao_x, self.posicao_y) # Acompanha o movimento do robô para carregar a bateria quando no local correto
            
                return True  # Indica que o clique foi em uma mesa
        return False  # Indica que o clique não foi em uma mesa
    
    def colisao(self, novo_x, novo_y): #Define as colisões com as cervejas

        for i, (x1, x2, y1, y2) in enumerate(self.obstaculos): #Repete para cada obstáculo
            if x1 <= novo_x <= x2 and y1 <= novo_y <= y2:
                print("Colisão detectada com um obstáculo!") #Debug da colisão
                return "bateu", i  
        return 0, 0
        

    def obstaculo(self, click_point): # Define a função que adiciona um obstáculo na janela com os limites definidos

        x = click_point.getX()
        y = click_point.getY()

        if 68 <= x <= 102 and 130 <= y <= 150:  # Coordenadas da bancada
            print("Zona proibida! Obstáculo não será criado.")
            return
        
        if 135 <= x <= 150 and 0 <= y <= 15:  # Coordenadas da zona de saída
            print("Zona proibida! Obstáculo não será criado.")
            return
        
        if 3 <= x <= 40 and 142 <= y <= 149:  # Coordenadas do mostrador de bateria
            print("Clique no mostrador de bateria. Obstáculo não será criado.")
            return
        
        for (x1, y1, x2, y2) in self.posicoes_mesa: # Verifica se o clique está dentro de uma mesa
            if x1 <= x <= x2 and y1 <= y <= y2:
                print("Clique em mesa. Obstáculo não será criado.")       
                return
        for (x1, x2, y1, y2) in self.posicoes_Div: # Verifica se o clique está dentro de uma divisão
            if x1 <= x <= x2 and y1 <= y <= y2:
                print("Clique em divisão. Obstáculo não será criado.")       
                return
                 
        print("Clique detectado fora das mesas!") #Debug do clique fora das mesas, ou seja, no chão
        cerveja = Image(Point(x, y), "jola.png") # Cria a imagem da cerveja
        cerveja.draw(self.window) # Desenha a imagem da cerveja na janela

        # Define os limites do obstáculo com base na posição do clique, para saber aonde é que o robo pára
        x1 = x - 10
        x2 = x + 10
        y1 = y - 8
        y2 = y + 8

        self.obstaculos.append((x1,x2,y1,y2))  # Adiciona a cerveja à lista de obstáculos
        self.obstaculos_imagens.append(cerveja)  # Adiciona a imagem da cerveja à lista de imagens

    def go_to_table_tier3(self, mesas):
        
        #Tier 3: O utilizador clica em 3 mesas. O robô calcula a ordem ótima e faz as entregas.
        

        ponto_dock = Point(97.0, 135.0)
        ponto_intermedio = Point(75.0, 136.0)
        ponto_final = Point(97.0, 145.0)

        mesas_selecionadas = []

        # Esperar 3 cliques válidos em mesas
        while len(mesas_selecionadas) < 3:
            click = self.window.getMouse()
            for mesa in mesas:
                if mesa.det_table(click) and mesa not in mesas_selecionadas:
                    mesa.rect.setFill("green")
                    mesas_selecionadas.append(mesa)
                    print(f"Mesa {mesa.ident} selecionada.")

        # Gerar todas as 6 permutações manualmente
        a, b, c = mesas_selecionadas
        ordens = [
            [a, b, c],
            [a, c, b],
            [b, a, c],
            [b, c, a],
            [c, a, b],
            [c, b, a]
        ]

        ponto_inicial = Point(self.posicao_x, self.posicao_y)
        melhor_ordem = None
        menor_distancia = float("inf")

        for ordem in ordens:
            atual = ponto_inicial
            total = 0
            for mesa in ordem:
                centro = mesa.rect.getCenter()
                dx = centro.getX() - atual.getX()
                dy = centro.getY() - atual.getY()
                total += sqrt(dx**2 + dy**2)
                atual = centro
            if total < menor_distancia:
                menor_distancia = total
                melhor_ordem = ordem

        # Iniciar percurso
        self.mover_tier3(ponto_dock.getX(), ponto_dock.getY())
        self.mover_tier3(ponto_intermedio.getX(), ponto_intermedio.getY())

        for mesa in melhor_ordem:
            center = mesa.rect.getCenter()
            img = Image(center, 'bifana.png')

            # Verifica bateria antes da entrega
            if self.battery_level < 10:
                print("Bateria insuficiente para continuar.")
                break

            # Mover até à mesa
            if mesa.ident in ["EE", "DC"]:
                self.mover_tier3(center.getX() - 15, 135.0)
                self.mover_tier3(center.getX() - 15, center.getY())
                self.mover_tier3(center.getX() - 13, center.getY())
            elif mesa.ident in ["EC", "DD"]:
                self.mover_tier3(center.getX() + 15, 135.0)
                self.mover_tier3(center.getX() + 15, center.getY())
                self.mover_tier3(center.getX() + 13, center.getY())
            else:
                self.mover_tier3(center.getX(), center.getY())

            sleep(1.5)
            img.draw(self.window)
            sleep(1.0)

            # Voltar para o corredor
            if mesa.ident in ["EE", "DC"]:
                self.mover_tier3(center.getX() - 15, center.getY())
            elif mesa.ident in ["EC", "DD"]:
                self.mover_tier3(center.getX() + 15, center.getY())
            self.mover_tier3(self.posicao_x, 135.0)

        # Voltar e carregar bateria
        self.mover_tier3(ponto_dock.getX(), ponto_dock.getY())
        self.mover_tier3(ponto_final.getX(), ponto_final.getY())
        self.carregar_bateria(self.posicao_x, self.posicao_y)

        # Restaurar cores
        for mesa in mesas_selecionadas:
            mesa.rect.setFill(mesa.cor_original)

    def obstaculo(self, click_point):

        x = click_point.getX()
        y = click_point.getY()

        if 68 <= x <= 102 and 130 <= y <= 150:
            print("Zona proibida! Obstáculo não será criado.")
            return
        
        if 135 <= x <= 150 and 0 <= y <= 15:
            print("Zona proibida! Obstáculo não será criado.")
            return
        
        if 3 <= x <= 40 and 142 <= y <= 149:
            print("Clique no mostrador de bateria. Obstáculo não será criado.")
            return
        
        for (x1, y1, x2, y2) in self.posicoes_mesa:
            if x1 <= x <= x2 and y1 <= y <= y2:
                print("Clique em mesa. Obstáculo não será criado.")       
                return
        for (x1, x2, y1, y2) in self.posicoes_Div:
            if x1 <= x <= x2 and y1 <= y <= y2:
                print("Clique em divisão. Obstáculo não será criado.")       
                return
                 
        print("Clique detectado fora das mesas!")
        cerveja = Image(Point(x, y), "jola.png")
        cerveja.draw(self.window)

        x1 = x - 10
        x2 = x + 10
        y1 = y - 8
        y2 = y + 8

        self.obstaculos.append((x1,x2,y1,y2))
        self.obstaculos_imagens.append(cerveja)

class Button: # Cria um botão 

    def is_click_in_button(point, button):
        p1 = button.getP1()
        p2 = button.getP2()
        return p1.getX() < point.getX() < p2.getX() and p1.getY() < point.getY() < p2.getY()
    
    def create_button(win, p1, p2, label_text):  
        button = Rectangle(p1, p2)
        button.draw(win)
        label = Text(button.getCenter(), label_text)
        label.draw(win)
        return button, label  # Retorna o objeto label ao invés do texto   

class Table: # Classe que define as mesas, com a cor, posição e identificação, vão buscar os dados ao sala49.txt mais tarde
    def __init__(self, win, x1, y1, x2, y2, color, ident):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)
        self.ident = ident
        self.cor_original = color

    def det_table(self, point): # Verifica se o ponto está dentro da mesa

        x = point.getX()
        y = point.getY()
        x1 = self.rect.getP1().getX()
        y1 = self.rect.getP1().getY()
        x2 = self.rect.getP2().getX()
        y2 = self.rect.getP2().getY()

        return x1 <= x <= x2 and y1 <= y <= y2

class Divisao: # Classe que define as divisões, com a cor e posição
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)

class Cozinha: # Classe que define a cozinha, com a cor e posição
    def __init__(self, win, x1, y1, x2, y2, color):
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(color)
        self.rect.setOutline("black")
        self.rect.draw(win)

class Estacao: # Classe que define a estação de carregamento, com a cor e posição
    def __init__(self, win, x1, y1, radius, color):
        self.circ = Circle(Point(x1, y1), radius)
        self.circ.setFill(color)
        self.circ.setOutline("black")
        self.circ.draw(win)

class Saida: # Classe que define o ponto de saída, com a cor e posição, pois este tem um retangulo por debaixo do botão que é uma imagem
    def __init__(self, win, x1, y1, x2, y2):
        self.win = win
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.draw(win)
        self.button, self.label = Button.create_button(win, Point(x1, y1), Point(x2, y2), "SAIR") 
        centro = self.rect.getCenter()
        Image(centro, "sair2.png").draw(self.win)

class Sala: # Classe que define e desenha a sala, onde são desenhadas as mesas, divisões, cozinha e estação de carregamento
    def __init__(self):
        self.win2 = GraphWin("Zé das Bifanas", 600, 600)
        self.x1 = 0.0
        self.x2 = 150
        self.y1 = 0
        self.y2 = 150
        self.win2.setCoords(self.x1, self.y1, self.x2, self.y2)
        self.fundo = Image(Point(75, 75), "chao_madeira_v3.gif")
        self.fundo.draw(self.win2)
        self.mesas = []  # Lista para armazenar as mesas
        self.posicoes_mesa = []  # Lista para armazenar as posições das mesas
        self.posicoes_Div = []  # Lista para armazenar as posições das divisões

    def desenhar(self, sala49): # Função que desenha a sala, lê o ficheiro sala49.txt e cria as mesas, divisões, cozinha e estação de carregamento
        arquivo = open("sala49.txt", "r") # Abre o ficheiro sala49.txt para leitura
        with arquivo as dados: # Lê o ficheiro e guarda os dados
            for linha in dados: 
                if linha.strip() == "" or linha.startswith("#"):  # Ignorar linhas vazias ou comentários
                    continue
                partes = linha.strip().split() # Divide a linha em partes
                tipo = partes[0] # O primeiro elemento é o tipo de objeto a ser criado

                if tipo.startswith("M"):  # Mesas
                    x1 = float(partes[1]) 
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    ident = partes[6] # Identificador de local da mesa
                    mesa = Table(self.win2, x1, y1, x2, y2, cor, ident)
                    self.posicoes_mesa.append((x1, y1, x2, y2))
                    self.mesas.append(mesa)  # Adiciona a mesa à lista
                
                elif tipo == "DIV":
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Divisao(self.win2, x1, y1, x2, y2, cor) 
                    self.posicoes_Div.append((x1, x2, y1, y2)) # Adiciona a posição da divisão à lista
                
                elif tipo == "C": # Cozinha
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    cor = partes[5]
                    Cozinha(self.win2, x1, y1, x2, y2, cor) 

                elif tipo == "E": # Estação de carregamento
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    radius = float(partes[3])
                    cor = partes[4]
                    Estacao(self.win2, x1, y1, radius, cor)

                elif tipo == "S": # Saída
                    x1 = float(partes[1])
                    y1 = float(partes[2])
                    x2 = float(partes[3])
                    y2 = float(partes[4])
                    self.saida = Saida(self.win2, x1, y1, x2, y2)  # Guarda referência
    
    def run(self, sala49): # Função que executa o desenho da sala e as mesas
        self.desenhar(sala49)

    def devolver_mesas(self): # Função que devolve a lista de mesas
        return self.posicoes_mesa
    
    def devolver_Div(self): # Função que devolve a lista de divisões
        return self.posicoes_Div