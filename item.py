class item(object):
    
    def __init__(self, s):
        s = s.lstrip('(')
        s = s.rstrip(')')
        self.content =  s.split(', ')
        
    def __eq__(self, other):
        if other==None:
            return False 
        return self.content == other.content
    def __ge__(self,other):
        return int(self.content[2])>=int(other.content[2])
    def __gt__(self, other):
        return int(self.content[2])>int(other.content[2])
    
            