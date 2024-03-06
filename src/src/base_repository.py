class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, pk):
        return self.model.objects.get(pk=pk)

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, pk, **kwargs):
        instance = self.get_by_id(pk)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, pk):
        self.model.objects.filter(pk=pk).delete()