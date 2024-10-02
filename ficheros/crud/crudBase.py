from sqlalchemy.orm import Session

class CrudBase:

    def __init__(self,model):
        self.model = model

    async def get(self,db:Session,id):
        return db.query(self.model).get(id)


    async def post(self,db:Session,data:any):
        data = self.model(**data.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
        

    async def put(self,db:Session,data:any,id):    
        db.query(self.model).filter(self.model.id == id).update(data.dict())
        db.commit()
        return


    async def delete(self,db:Session,id):
        db.query(self.model).filter(self.model.id == id).delete()
        db.commit()
        return True

    
    async def get_filtered(self,db: "Session", filtros: list[str], desde:int, limite:int, orden:str):
        q = db.query(self.model)
        if filtros != None:
            for filtro in filtros:
                q = q.filter(eval("self.model."+filtro))
        q = q.order_by(eval("self.model."+orden)).offset(desde)
        if limite > 0:
             q = q.limit(limite)
        return q.all()
