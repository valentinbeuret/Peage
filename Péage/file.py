class Elts():
    def  __init__(self,val,suiv):
        self.val=val
        self.suiv=suiv

class File():
    def __init__(self):
        self.tete=None
        self.queue=None

    def est_vide(self):
            if self.tete==None:
                return True
            return False

    def nb_elts(self):
            x=self.tete
            i=1
            while x.suiv!=None:
                x=x.suiv
                i+=1
            return i

    def elts(self):
        all =  []
        if self.est_vide():
            print("La file est vide")
            return None
        else:
            x=self.tete
            all.append(x)
            while x.suiv!=None:
                x=x.suiv
                all.append(x)

            return all

    def ajouter(self,v):
            elt=Elts(v,None)
            if self.est_vide():
                self.tete=elt
            else:
                self.queue.suiv=elt
            self.queue=elt

    def retirer(self):
        if self.est_vide():
            print("la file est vide !")
            return None
        else:
            v = self.tete.val
            if self.tete==self.queue:
                self.queue=None
            self.tete=self.tete.suiv
            return v

    def afficher(self):
        if self.est_vide():
            print("La file est vide")
        else:
            x=self.tete
            print(x.val,end=' ')
            while x.suiv!=None:
                x=x.suiv
                print('-->',x.val,end=' ')
            print()


