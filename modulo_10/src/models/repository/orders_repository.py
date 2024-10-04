from bson.objectid import ObjectId

class OdersRepository:
    def __init__(self, db_connection):
        self.__collection = "orders"
        self.__db_connection = db_connection

    def get_all(self) -> list:
        collection = self.__db_connection[self.__collection]
        return collection.find()

    def get_by_id(self, order_id) -> dict:
        collection = self.__db_connection[self.__collection]
        return collection.find_one({"_id": ObjectId(order_id)})

    def insert_one(self, order) -> dict:
        collection = self.__db_connection[self.__collection]
        return collection.insert_one(order)
    
    def insert_list_of_documents(self, orders_list: list) -> dict:
        collection = self.__db_connection[self.__collection]
        return collection.insert_many(orders_list)

    def update(self, order_id, order) -> dict:
        collection = self.__db_connection[self.__collection]
        return collection.update_one({"_id": ObjectId(order_id)}, {"$set": order})

    def delete(self, order_id) -> dict:
        collection = self.__db_connection[self.__collection]
        return collection.delete_one({"_id": ObjectId(order_id)})