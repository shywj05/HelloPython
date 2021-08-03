import mybatis_mapper2sql

mapper, xml_raw_text = mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')

# statement = mybatis_mapper2sql.get_statement(mapper)

# print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "select")
print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "insert")
print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "update")
print(statement)

statement = mybatis_mapper2sql.get_child_statement(mapper, "delete")
print(statement)
