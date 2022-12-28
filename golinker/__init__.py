import typing

class GoLinker(object):

    def __init__(self, storage):
        self.storage = storage
    
    def Get(self,key: str) -> typing.Optional[str]:
        return self.storage.Get(key)
    
    def Set(self,key:str,target:str):
        self.storage.Set(key,target)
    
    def All(self):
        ret = []
        for k,v  in self.storage.All().items():
            ret.append({"name":k,"target":v})
        return ret