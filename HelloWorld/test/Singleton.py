import threading


class Singleton:

    __lock=threading.Lock()

    @classmethod
    def instance(clazz,*args,**kwargs):
        with Singleton._lock:
            if not hasattr(Singleton,"_instance"):
                Singleton._instance=Singleton(*args,**kwargs)
        return Singleton._instance


if __name__=="__main__":
    s1=Singleton.instance()
    s2=Singleton.instance()
    s3=Singleton.instance()
    s4=Singleton.instance()
    print("s1 %s"%s1)
    print("s2 %s"%s2)
    print("s3 %s"%s3)
    print("s4 %s"%s4)
    




