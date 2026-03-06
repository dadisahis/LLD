class SQLQuery:
    def __init__(self, builder):
        self.table = builder._table
        self.columns = list(builder._columns)
        self.conditions = list(builder._conditions)
        self.order_by = builder._order_by
        self.order_direction = builder._order_direction
        self.limit = builder._limit
        self.offset = builder._offset

    def to_sql(self):
        query = f"SELECT {', '.join(self.columns) if self.columns else '*'} FROM {self.table}"
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)
        if self.order_by:
            query += f" ORDER BY {self.order_by} {self.order_direction}"
        if self.limit is not None:
            query += f" LIMIT {self.limit}"
        if self.offset is not None:
            query += f" OFFSET {self.offset}"
        return query
    
    class Builder:
        def __init__(self, table):
            self._table = table
            self._columns = []
            self._conditions = []
            self._order_by = None
            self._order_direction = "ASC"
            self._limit = None
            self._offset = None

        def select(self, *columns):
            self._columns.extend(columns)
            return self
        
        def where(self, condition):
            self._conditions.append(condition)
            return self
        def order_by(self, column, direction="ASC"):
            self._order_by = column
            self._order_direction = direction
            return self
        
        def limit(self, limit):
            self._limit = limit
            return self
        def offset(self, offset):       
            self._offset = offset
            return self

        def build(self):
            return SQLQuery(self)
    

if __name__ == '__main__':
    query = SQLQuery.Builder("users").select("id", "name", "email").where("age >18").order_by("name").limit(10).offset(5).build()
    print(query.to_sql())


    print("Another query:")
    query2 = SQLQuery.Builder("orders").select("order_id", "amount").where("status = 'shipped'").build()
    print(query2.to_sql())


            