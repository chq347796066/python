class util:

    @staticmethod
    def obj_to_json(self,obj):
        dict = {}
        dict.update(obj.__dict__)
        return dict
