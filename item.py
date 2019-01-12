class item(object):
    
    def __init__(self, s):
        s = s.lstrip('(')
        s = s.rstrip(')')
        self.content =  s.partition(',')
        
    def __eq__(self, other):
        return self.content ==other.content
    def __ge__(self,other):
        return self.content[2]>=other.content[2]
    def __gt__(self, other):
        return self.content[2]>other.content[2]
    def __str__(self):
        return content
            