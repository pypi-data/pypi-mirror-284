# -*- coding: utf-8 -*-
from thonnycontrib.data_visualization.Graphical import graphic
import networkx as nx

def init_DB(self):
    self.setReduc=0
    self.G = nx.DiGraph()
    graphic.init_Graph(self)
    
def clearAll(self):
    self.G.clear()
    graphic.delete(self)
    graphic.scrollregion(self)
    
def addEdge(self, startNode, endNode, startPointer):
    if isThereNode(self, startNode) and isThereNode(self, endNode):
        if self.G.has_edge(startNode, endNode):
            if startPointer in self.G.edges[(startNode, endNode)]['start']:
                return
            else:
                self.G.edges[(startNode, endNode)]['start'].add(startPointer)
        else:
            self.G.add_edges_from([(startNode, endNode,{'start':{startPointer}})], arrowstyle='->', arrowsize=10)

def removeEdge(self, edgeCreated):
    edges = list(self.G.edges())
    for i in edges:
        ed = self.G.edges[(i[0], i[1])]['start']
        for startPointer in ed:
            if (i[0],i[1],startPointer) not in edgeCreated:
                if len(self.G.edges[(i[0], i[1])]['start'])<=1:
                    self.G.remove_edge(i[0], i[1])
                else:
                    self.G.edges[(i[0], i[1])]['start'].remove(startPointer)

def addNode(self, idNode, text = ""):
    if idNode == "Globals":
        self.G.add_nodes_from([('Globals', {'contenue': f'Globals', 'type': 'TypeA', 'couleur': 'deep sky blue', 'pos': (5, 5), 'taille':(0,0),'visible':False,'reduced':self.setReduc, 'reduc':(0,0), 'pointeur': []})])
    elif idNode == "Locals":
        #positionne le noeud "Locals" endessous du Graph déjà existant
        newY=5
        for n in self.G.nodes:
            if self.G.nodes[n]['pos'][1] + self.G.nodes[n]['taille'][1]+15>newY:
                newY=self.G.nodes[n]['pos'][1] + self.G.nodes[n]['taille'][1]+15
        self.G.add_nodes_from([('Locals', {'contenue': f'Locals', 'type': 'TypeB', 'couleur': 'lime green', 'pos': (5, newY), 'taille':(0,0),'visible':False,'reduced':self.setReduc, 'reduc':(0,0), 'pointeur': []})])
    else:
        self.G.add_nodes_from([(idNode,{'contenue': text, 'type': 'TypeC', 'couleur': 'turquoise', 'pos': None, 'taille':(0,0),'visible':False,'reduced':self.setReduc, 'reduc':(0,0), 'pointeur': []})])

#rajoute du texte à node
def addNodeText(self, node, text, newLigne=True):
    if newLigne:
        self.G.nodes[node]['contenue']+="\n"+text
    else:
        self.G.nodes[node]['contenue']+=text

#retire à G tout les noeuds qui ne se trouve pas dans self.nodeCreated
def removeNode(self, nodeCreated):
    nodes = dict(self.G.nodes())
    for i in nodes:
        if i not in nodeCreated:
            self.G.remove_node(i)

#remet un node à zero, en gardant sa postion et juste en lui retirant ses pointeur et son text
def nodeReset(self, node):
        self.G.nodes[node]['contenue'] = self.G.nodes[node]['contenue'].split("\n")[0]
        self.G.nodes[node]['pointeur'] = []

#rajoute un pointeur dans le graph
def addPointeur(self,nodeParent, namePointeur, idPointeur, createdFromParent):
    if namePointeur in createdFromParent:
        self.G.nodes[nodeParent]['pointeur'].append({'name':namePointeur,'id':idPointeur,'visible':createdFromParent[namePointeur],'pSize':(0,0,0,0)})
    else:
        self.G.nodes[nodeParent]['pointeur'].append({'name':namePointeur,'id':idPointeur,'visible':False,'pSize':(0,0,0,0)})

#change le pointeur pB de node à ouvert ou fermer
def changePointeur(self, node, pB):
    self.G.nodes[node]['pointeur'][pB]['visible'] = not self.G.nodes[node]['pointeur'][pB]['visible']

#utilisé quand le noeud est réduit
#fixe la valeur de self.G.nodes[node]['reduced'] en fonction des pointeur de node et de leur état
#change la taille de la boite node et la taille de reduc (le carré blanc avec + et -)
def changeReduc(self, node):
    if self.G.nodes[node]['reduced'] == 0:
        if len(self.G.nodes[node]['pointeur'])<1:
            self.G.nodes[node]['reduced'] = 1 #The node is reduced and doesn't have pointeur
        else:
            change = False
            etat = self.G.nodes[node]['pointeur'][0]['visible']
            for i in self.G.nodes[node]['pointeur']:
                if i['visible'] != etat:
                    change=True
                    break
            if change:
                self.G.nodes[node]['reduced'] = 2 #The node is reduced whit open and close pointeurs
            elif etat==True:
                self.G.nodes[node]['reduced'] = 3 #The node is reduced whit only open pointeur
            else:
                self.G.nodes[node]['reduced'] = 4 #The node is reduced whit only close pointeur
    else:
        self.G.nodes[node]['reduced'] = 0 #The node is not reduced
    self.G.nodes[node]['taille'], self.G.nodes[node]['reduc'] = graphic.getTailleBox(self, node)

#utilisé quand cliquer sur la boule pointeur verte, orange ou rouge quand le noeud est sous forme reduite et qu'il a des pointeur
#changer self.G.nodes[node]['reduced'] voir changeReduc pour savoir à quoi correspond les valeur possible
#ferme ou ouvre en même temps tout les pointeur de node
def changeReducPointeur(self, node):
    if self.G.nodes[node]['reduced']==2 or self.G.nodes[node]['reduced']==4 :
        self.G.nodes[node]['reduced'] = 3
        for pB in range(len(self.G.nodes[node]['pointeur'])):
            self.G.nodes[node]['pointeur'][pB]['visible']=True
    else:
        self.G.nodes[node]['reduced'] = 4
        for pB in range(len(self.G.nodes[node]['pointeur'])):
            self.G.nodes[node]['pointeur'][pB]['visible']=False

#afficher tout le graph avec tout modification qui aurais été fait avant
def draw_graph(self):
    # Clear canvas
    graphic.delete(self)
    for node in self.G.nodes():
        self.G.nodes[node]['visible']=False
    if self.G.has_node('Globals'):
        drawGraphIter(self, 'Globals')
    if self.G.has_node('Locals'):
        drawGraphIter(self, 'Locals')
    
    graphic.scrollregion(self)

# suite/iteration de draw_graph
def drawGraphIter(self, node):
    self.G.nodes[node]['visible']=True

    #trouver/verifier la taille et la position de reduc de la boite du node
    self.G.nodes[node]['taille'], self.G.nodes[node]['reduc'] = graphic.getTailleBox(self, node)
    #dessiner node
    graphic.boite(self, node)
    for i in range(len(self.G.nodes[node]['pointeur'])):#parcourir tout les pointeur pour trouver des noeud enfant à afficher
        if self.G.nodes[node]['pointeur'][i]['visible']:
            for edge in self.G.out_edges(node):
                if self.G.nodes[node]['pointeur'][i]['name'] in self.G.edges[edge]['start']:
                    if self.G.nodes[edge[1]]['visible'] == False:#si le noeud enfant n'est pas encore afficher: iteration
                        drawGraphIter(self, edge[1])
                    graphic.line(self, node, edge[1], i)#afficher edge du noeud parent vers le noeud enfant
                    break

#appelle pour tout recentrer
def reCentrer(self):
    # retiré tout ce qui est affiché et otu mettre à visible=False
    graphic.delete(self)
    for node in self.G.nodes():
        self.G.nodes[node]['visible']=False
    
    lowestY=None #n=la cordonner la plus basse du graph sans Locals et ses enfant
    if self.G.has_node('Globals'):
        lowestY=5
        lowestY=reCentrerIter(self, 'Globals', 5, 5, lowestY)
    
    if self.G.has_node('Locals'):
        Y=5
        if lowestY:
            Y=lowestY+15
        reCentrerIter(self, 'Locals', 5, Y, lowestY)
    
    graphic.scrollregion(self)

# suite/iteration de reCentrer
def reCentrerIter(self, node, X, Y, lowestY):
    self.G.nodes[node]['visible']=True
    self.G.nodes[node]['pos'] = (X, Y)
    graphic.boite(self, node)
    
    if self.G.nodes[node]['pos'][1]+self.G.nodes[node]['taille'][1]>lowestY:
        lowestY=self.G.nodes[node]['pos'][1]+self.G.nodes[node]['taille'][1]
    
    for i in range(len(self.G.nodes[node]['pointeur'])):# trouver tout le noeud enfant qui doivent être affiché
        if self.G.nodes[node]['pointeur'][i]['visible']:
            for edge in self.G.out_edges(node):
                if self.G.nodes[node]['pointeur'][i]['name'] in self.G.edges[edge]['start']:
                    if self.G.nodes[edge[1]]['visible'] == False:
                        # calculé la nouvelle position du noeud enfant à affiché trouver et iteration dessus
                        newX = self.G.nodes[node]['pos'][0] + self.G.nodes[node]['taille'][0]+15
                        newY = findNewY(self, node)
                        lowestY = reCentrerIter(self, edge[1], newX, newY, lowestY)
                    #afficher l'edge du noeud parent vers le noeud enfant
                    graphic.line(self, node, edge[1], i)
                    break
    
    return lowestY

# quand un noeud est bouger, changer sa position et dessiner tout le graph en conséquance #TODO à optimiser pas besoin de redessiner TOUT le graph
def moveNode(self, event, node, offset):
    if node is not None:
        new_x = graphic.getX(self, event.x) - offset[0]
        new_y = graphic.getY(self, event.y) - offset[1]

        self.G.nodes[node]['pos'] = (new_x, new_y)
        draw_graph(self)

# est appellé quand un nouveau noeud est créer et dois être affiché, il viens du pointeur "pB" du noeud "node"
# Va afficher l'edge du noeud parent "node" vers le nouveau noeud, le nouveau noeud et tout les noeud/edge suivant qui devrai être visible
def showNodeEdge(self, node, pB, FromExtend = True):
    self.G.nodes[node]['pointeur'][pB]['visible'] = not self.G.nodes[node]['pointeur'][pB]['visible']
    if FromExtend:
        graphic.DrawPointeur(self, node, pB)#si appellé de l'ouverture d'un pointeur d'un noeud qu iest étandu, alors changer sa couleur
    for edge in self.G.out_edges(node):
        if self.G.nodes[node]['pointeur'][pB]['name'] in self.G.edges[edge]['start']:
            showIter(self, node, edge[1], pB)

    graphic.scrollregion(self)

# suite/iteration de showNodeEdge
def showIter(self, node1, node2, pB):
    if self.G.nodes[node2]['visible']: #si le noeud est déjà afficher, afficher l'edge et s'arrêter là
        graphic.line(self, node1, node2, pB)
        return
    else:
        if self.G.nodes[node2]['pos']==None: #si le noeud n'a pas encore de position, lui en trouver une
            newX = self.G.nodes[node1]['pos'][0] + self.G.nodes[node1]['taille'][0]+15
            newY = findNewY(self, node1)
            self.G.nodes[node2]['pos'] = (newX, newY)
        
        self.G.nodes[node2]['visible']=True
        
        #enregistrer la taille et la position du bouton extend/reduc du nouveau noeud #TODO a optimisé pas sûr de l'utilite de revérifié à chaque fois la taille+reduc
        self.G.nodes[node2]['taille'], self.G.nodes[node2]['reduc'] = graphic.getTailleBox(self, node2)
        # dessiné le nouveau noeud + l'edge du noeud parent vers le nouveau
        graphic.boite(self, node2)
        graphic.line(self, node1, node2, pB)
        
        for i in range(len(self.G.nodes[node2]['pointeur'])):# pour tout les pointeurs ouvert du nouveau noeud, cherché le noeud suivant et depth first search
            if self.G.nodes[node2]['pointeur'][i]['visible']:
                for edge in self.G.out_edges(node2):
                    if self.G.nodes[node2]['pointeur'][i]['name'] in self.G.edges[edge]['start']:
                        showIter(self, node2, edge[1], i)
                        break

# utiliser quand il faut recentrer ou que un noeud n'a pas encore de position, permet de trouvé le YDown+15 le plus en bas parmis tout les noeud enfant visible de "node"
# retour un Y = YUp de node si node n'a pas de noeud enfant affiché
def findNewY(self,node):
    maxY= self.G.nodes[node]['pos'][1]
    for i in range(len(self.G.nodes[node]['pointeur'])):
        if self.G.nodes[node]['pointeur'][i]['visible']:
            for edge in self.G.out_edges(node):
                if self.G.nodes[node]['pointeur'][i]['name'] in self.G.edges[edge]['start']:
                    if self.G.nodes[edge[1]]['visible']:
                        if self.G.nodes[edge[1]]['pos'][1] + self.G.nodes[edge[1]]['taille'][1]+15>maxY:
                            maxY=self.G.nodes[edge[1]]['pos'][1] + self.G.nodes[edge[1]]['taille'][1]+15
                    break
    return maxY
    
    




# True si le neoud "node" est sous forme reduite
def isReduced(self, node):
    return self.G.nodes[node]['reduced']>0

# True si le neoud "node" est sous forme reduite et que tout les pointeur de se noeud sont ouvert
def isNodeOpen(self, node):
    return self.G.nodes[node]['reduced']==3

# True si le clique "x, y" se situe sur le pointeur "pB" rond et rouge ou vert du noeud "node" sous forme agrandis
def isCliqueOnPointeur(self, x, y, node, pB):
    return self.G.nodes[node]['pos'][0] + self.G.nodes[node]['pointeur'][pB]['pSize'][0] <= graphic.getX(self, x) <= self.G.nodes[node]['pos'][0] + self.G.nodes[node]['pointeur'][pB]['pSize'][2] and self.G.nodes[node]['pos'][1] + self.G.nodes[node]['pointeur'][pB]['pSize'][1] <= graphic.getY(self, y) <= self.G.nodes[node]['pos'][1] + self.G.nodes[node]['pointeur'][pB]['pSize'][3]

# True si le clique "x, y" se situe sur le carre blanc de reduction/agrandissement du noeud "node"
def isCliqueOnReduc(self, x, y, node):
    return self.G.nodes[node]['pos'][0] + self.G.nodes[node]['reduc'][0]-self.line_height/2 <= graphic.getX(self, x) <= self.G.nodes[node]['pos'][0] + self.G.nodes[node]['reduc'][0]+self.line_height/2 and self.G.nodes[node]['pos'][1] + self.G.nodes[node]['reduc'][1]-self.line_height/2 <= graphic.getY(self, y) <= self.G.nodes[node]['pos'][1] + self.G.nodes[node]['reduc'][1]+self.line_height/2

# True si le clique "x, y" se situe sur le pointeur rond et rouge, orange ou vert du noeud "node" sous forme reduite
def isCliqueOnReducPointeur(self, x, y, node):
    if self.G.nodes[node]['reduced']<2:
        return False
    return self.G.nodes[node]['pos'][0] + self.G.nodes[node]['reduc'][0]+self.line_height/2+self.padding <= graphic.getX(self, x) <= self.G.nodes[node]['pos'][0] + self.G.nodes[node]['reduc'][0]+self.line_height/2+self.padding+self.line_height and self.G.nodes[node]['pos'][1] + self.G.nodes[node]['reduc'][1]-self.line_height/2 <= graphic.getY(self, y) <= self.G.nodes[node]['pos'][1] + self.G.nodes[node]['reduc'][1]+self.line_height/2

# True si le pointeur "pB" du noeud "node" est cliqué/ouvert, en vert
def isPointeurOpen(self, node, pB):
    return self.G.nodes[node]['pointeur'][pB]['visible']

def isThereNode(self, name):
    return self.G.has_node(name)

def isThereEdge(self, startNode, endNode, startPointer):
    return self.G.has_edge(startNode, endNode) and startPointer in self.G.edges[(startNode, endNode)]['start']










def getOffset(self, event, node):
    return (graphic.getX(self, event.x) - self.G.nodes[node]['pos'][0], graphic.getY(self, event.y) - self.G.nodes[node]['pos'][1])


# retourn le noeud qui se trouve à la position de event.x, event.y : l'endroits où l'utilisateur à cliqué
def getClickedNode(self, event):
        # Check if clicked inside a node and return its id
        for node in reversed(list(self.G.nodes())):
            if self.G.nodes[node]['pos'] != None :
                xLeft = self.G.nodes[node]['pos'][0]
                xRight= self.G.nodes[node]['pos'][0] + self.G.nodes[node]['taille'][0]
                yTop  = self.G.nodes[node]['pos'][1]
                yDown = self.G.nodes[node]['pos'][1] + self.G.nodes[node]['taille'][1]
                if xLeft <= graphic.getX(self, event.x) <= xRight and yTop <= graphic.getY(self, event.y) <= yDown:
                    return node
        return None

def getPointeurId(self, node, pB):
    return self.G.nodes[node]['pointeur'][pB]['id']

def getPoiteurName(self, node, pB):
    return self.G.nodes[node]['pointeur'][pB]['name']

# retourne le nombre de poiteur qu'il y a dans le noeud "node"
def getLenPointeur(self, node):
    return len(self.G.nodes[node]['pointeur'])