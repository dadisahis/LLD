class SQLQuery:
    class Builder:
            def __init__(self, table):
                self._table = table
                self._cols = []
                self._conditions = []
                self._order_by = []
                self._limit = 0
                self._offset =0
            def select(self, *cols):
                self._cols.extend(cols)
                return self
    
            def where(self, condition):
                self._conditions.append(condition)
                return self
            def order_by(self, order):
                self._order_by.append(order)
                return self
    
            def limit(self, limit):
                self._limit = limit
                return self
            def offset(self, offset):
                self._offset = offset
                return self
            def build(self):
                return SQLQuery(self)
    def __init__(self, builder: Builder):
        self.table = builder._table
        self.columns = list(builder._cols)
        self.conditions = list(builder._conditions)
        self.order_by = list(builder._order_by)
        self.limit_val = builder._limit
        self.offset_val = builder._offset

    def to_sql(self):
        cols = ', '.join(self.columns) if self.columns else '*'
        sql = f"SELECT {cols} from {self.table}"
        if self.conditions:
            sql+= " WHERE " + " AND ".join(self.conditions)
        if self.order_by:
            sql+= " ORDER BY "+ ', '.join([f"{col} {dir}" for col, dir in self.order_by])
        if self.limit_val > 0:
            sql+= f" LIMIT {self.limit_val}"
        if self.offset_val > 0:
            sql+= f" OFFSET {self.offset_val}"
        return sql

    

if __name__ == "__main__":
    query1 = SQLQuery.Builder("users").select("id","name","email").where("name='Adithya'").order_by(["id", "ASC"]).limit(10).offset(10).build()
    print(query1.to_sql())

