## From Install Scripts (Linux/Mac)
#  Installed successfully in /usr/local/bin.
curl https://get.dgraph.io -sSf | bash

# First run Dgraph zero
#   Run dgraph zero to start Dgraph zero.
#   This process controls Dgraph cluster, maintaining membership information,
#   shard assignment and shard movement, etc.
#
#   Note: the port numbers should be checked from console.
dgraph zero --port_offset -2000

# Secondf run Dgraph data server in another terminal
#  You need to set the estimated memory dgraph can take through memory_mb flag.
#  This is just a hint to the dgraph and actual usage would be higher than this.
#  It’s recommended to set memory_mb to half the available RAM.
#
#  IMPORTANT  TO  READ
#     https://discuss.dgraph.io/t/what-is-zero-what-is-server/1966
dgraph server --memory_mb 2048 --zero localhost:5080

# Dgraph up and running.

# Start web UI
dgraph-ratel  -port 11111

## Schema
#   There are two kinds of nodes in a graph, let’s call them nodes and values (or literals).
#   In the example, nodes representing people have a name edge to a string value and an age edge to an int value.
#   A value can’t have any edges coming out of it.

# Type
#   Dgraph Type	    Description
#   uid             for nodes, is picked by Dgraph and is unique
#   int	            signed 64 bit integer
#   float	          double precision floating point number
#   string	        string; support UTF-8
#   bool	          boolean
#   id	            ID’s stored as strings
#   dateTime	      RFC3339 time format with optional timezone eg: 
#                      2006-01-02T15:04:05.999999999+10:00 or 2006-01-02T15:04:05.999999999
#   geo	            geometries stored using go-geom (https://github.com/twpayne/go-geom)

schema(pred: [name, age, friend, owns_pet]) {
  type
  index
}
# or
schema(pred: []) {
  type
  index
}

## Adding schema - mutating schema
#   As we saw in an earlier lesson, Dgraph stores a schema describing the types of predicates.
#   When we want to add new data to an existing schema, we can just add it. But if we want to add new data in
#   a new schema we have two choices:
#     1. Add the data and let Dgraph work out the schema, or
#     2. Specify a schema and then add the data
#   
#   Dgraph can work out the schema just fine. But functions and filtering can only be applied to indexed
#   predicates and for that we need to specify the schema.
#
#   Making changes to the schema is called mutating the schema.
#   Run the schema mutation. The index allows applying filter functions, such as searching for all companies that
#   participate in a particular industry.

industry: string @index(term) .
boss_of: uid .

## Now that the schema has been updated we can add data as triples.
#   Dgraph creates its own internal id’s for nodes, but we need some way to refer to the same node many times in
#   our input data. That’s what _:company1 does. Technically, these are ‘blank nodes’. They tell Dgraph to create a
#   node, give it an internal id and make sure it’s used consistently.
#
#   After the upload, the label _:company1 doesn’t exist in Dgraph and we can’t query for it.
#   You’ll see in the result that Dgraph has replaced it with an internal id. You can query for this internal 
#   id — remember func: uid(<uid_number>).
#
#   Making changes to the graph stored in Dgraph is called mutating the data.

{
  set {
    _:company1 <name> "CompanyABC" .
    _:company2 <name> "The other company" .

    _:company1 <industry> "Manufacturing" .
    _:company1 <industry> "Fabricated Metal" .
    _:company1 <industry> "Machinery" .

    _:company2 <industry> "Manufacturing" .
    _:company2 <industry> "High Tech" .

    _:jack <works_for> _:company1 .
    _:ivy <works_for> _:company1 .
    _:zoe <works_for> _:company1 .

    _:jose <works_for> _:company2 .
    _:alexei <works_for> _:company2 .

    _:ivy <boss_of> _:jack .

    _:alexei <boss_of> _:jose .
  }
}

## External Identifiers
#   Dgraph doesn’t support directly setting the IDs of nodes. If an application requires unique identifiers for
#   nodes other than the UID assigned by Dgraph, then these are supplied as edges. It’s up to a user application to
#   ensure the uniqueness of such IDs/keys.

## Language Support
#   Language tags are used on the string on input
#
_:myID <an_edge> "something"@en .
_:myID <an_edge> "某物"@zh-Hans .

## Reverse edges
#   Edges are directional. A query can’t traverse an edge in reverse.
#
#   There are two choices to query in both directions:
#     1. Add the reverse edge to the schema and add all the reverse edge data.
#     2. Tell Dgraph to always store the reverse edge using the @reverse keyword in the schema.
#
#   Run the schema mutation and Dgraph will compute all the reverse edges. The reverse edge of an_edge is ~an_edge.
#
#   In terms of data modeling, some reverse edges always make sense, like boss_of, others like ,friend, are 
#   sometimes, but not always bidirectional.




## Dgraph query
#   Dgraph query results are graphs. In fact, the result structure matches the query structure.

#   Nodes are filtered based on functions applied to the node’s outgoing edges.

## Functions and filtering
#   There are many functions for filtering, some of them are
#     allOfTerms(edge_name, "term1 ... termN"): matches nodes with an outgoing string edge edge_name
#         where the string contains all listed terms.   
#     anyOfTerms(edge_name, "term1 ... termN"): As with allOfTerms, but matches at least one term.
#
#   The equalities and inequalities can be applied to edges of types: int, float, string and date
#     eq(edge_name, value): equal to
#     ge(edge_name, value): greater than or equal to
#     le(edge_name, value): less than or equal to
#     gt(edge_name, value): greater than
#     lt(edge_name, value): less than
#   
#   There’s also regular expressions, full text search and geo search.
#   Functions can only be applied to predicates that have been indexed

## AND, OR and NOT
#   The logical connectives AND, OR and NOT combine multiple functions in a filter.

## Sorting (orderasc or orderdesc)
#   Results can be ordered using orderasc and orderdesc.

## Pagination (first, offset and after)
#   It’s not uncommon to have thousands of results for a query.
#   But you might want to select only the top-k answers, paginate the results for display, or limit a large result.
#   In GraphQL+- this is done with first, offset and after in combination with ordering.
#
#   first: N Return only the first N results
#   offset: N Skip the first N results
#   after: uid Return the results after uid
#   
#   By default, query answers are ordered by uid. You can change this behavior by explicitly specifying an order.
#   After makes sense in pagination when we only know the last uid returned and don’t record how many results
#   have previously been retrieved.

## Count
#   The number of outgoing edges can be counted, using the count function.

## How Dgraph Search Works
#   Given what you’ve seen so far, you’ve probably already understood this, but it’s worth going over.
#   The graphs in Dgraph can be huge, so starting searching from all nodes isn’t efficient.
#   Dgraph needs a place to start searching, that’s the root node.
# 
#   At root, we use func: and a function to find an initial set of nodes. So far we’ve used eq and allofterms
#   for string search, but we can also search on other values like dates, numbers, and also filters on count.
#
#   Dgraph needs to build an index on values that are to be searched in this way because, without an index
#   to make the search efficient, Dgraph would have to trawl through the whole database to find matching values.
#
#   From the set of nodes matched in the root filter, Dgraph then follows edges to satisfy the remainder of the query.
#   The filters on blocks inside the root are only applied to the nodes reached by following listed edges to them.
#
#   The root func: only accepts a single function and doesn’t accept AND, OR and NOT connectives as in filters.
#   So the syntax (func: ...) @filter(... AND ...) is required when filtering on multiple properties at the root.

## Has
#   The function has(edge_name) returns nodes that have an outgoing edge of the given name.

## Alias
#   The output graph can set names for edges in the output with aliasing.

## Cascade
#   The @cascade directive removes any nodes that don’t have all matching edges in the query.
#   Another use is to remove nodes where a filter inside a block returns no results.

## Normalize
#   The @normalize directive
#       returns only edges listed with an alias, and
#       flattens the result to remove nesting
#   Tip Aliased names can be the same as the original edge.

## Comments
#   Queries can contain comments.
#   Anything after # on a line is a comment and ignored for query processing.
#   
#   This is helpful for debugging queries and for tutorials that need to explain parts of queries in-line,
#   which is what we’ll do for the more complex queries you’ll encounter later in the tutorial.























