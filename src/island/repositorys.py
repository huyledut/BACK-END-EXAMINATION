from src.base_repository import BaseRepository


class IslandRepository(BaseRepository):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_list_value(self, *args, **kwargs):
        return self.model.objects.all().values()