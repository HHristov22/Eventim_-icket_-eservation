class QueryCreator :
    
    def dropTable(tableName : str) -> str :
        query = "DROP TABLE IF EXISTS '{}';".format(tableName)
        return query
    
    def createTable(tableName : str, columnNameAndDefinitionPairs : str) :
        query = "CREATE TABLE IF NOT EXISTS {} (".format(tableName)

        firstPair = True
        for pair in columnNameAndDefinitionPairs :
            if firstPair :
                firstPair = False
            else :
                query += ", "

            query += "{} {}".format(pair[0], pair[1])

        query += ");"

        return query
    
    def insertInto(tableName : str, columnValuePairs : list) -> str :
        firstPair = True
        columnsString = valueString = ""
        for pair in columnValuePairs :
            if firstPair :
                firstPair = False
            else :
                columnsString += ", "
                valueString += ", "
            
            columnsString += "'{}'".format(pair[0])
            valueString += "'{}'".format(pair[1])

            query = "INSERT INTO '{}' ({}) VALUES ({});".format(tableName,columnsString,valueString)

        return query
    
    def select(tableName : str, columnNames : list, sqlCondition : str = "") -> str :
        query = "SELECT "

        firstColumn = True
        for columnName in columnNames :
            if columnName != '*' :
                columnName = "'{}'".format(columnName)
            
            if firstColumn :
                firstColumn = False
            else :
                query += ", "

            query += "{}".format(columnName)
        
        query += " FROM '{}'".format(tableName)

        if sqlCondition != "" :
            query += " WHERE {}".format(sqlCondition)

        query += ";"

        return query
    
    def delete(tableName : str, sqlCondition : str) -> str :
        if sqlCondition == "" :
            query = "DELETE FROM '{}';".format(tableName)
        else :
            query = "DELETE FROM '{}' WHERE {};".format(tableName, sqlCondition)
        
        return query
    
    def update(tableName : str, columnValuePairs : list, sqlCondition : str) -> str :
        query = "UPDATE '{}' SET ".format(tableName)

        firstPair = True
        for pair in columnValuePairs :
            if firstPair :
                firstPair = False
            else :
                query += ", "

            query += "'{}'='{}'".format(pair[0], pair[1])
        
        query += " WHERE {};".format(sqlCondition)

        return query