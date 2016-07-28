
//// use Gremlin.sh to connect to Titan database. 
// Note: Every graph operation in Titan occurs within the context of a transaction. According to the Blueprints' specification, each thread opens its own transaction against the graph database with the first operation (i.e. retrieval or mutation) on the graph

//  a remote Titan graph database is opened.
graph = TitanFactory.open('conf/my-titan.properites')
//==>standardtitangraph[cassandra:[192.168.122.101]]

// Adding the vertex "juno" is the first operation (in this thread) which automatically opens a new transaction
//  All subsequent operations occur in the context of that same transaction until the transaction is explicitly stopped or the graph database is shutdown()
juno = graph.addVertex() //Automatically opens a new transaction
juno.property("name", "juno")
graph.tx().commit() //Commits transaction
// When committing a transaction, Titan will attempt to persist all changes to the storage backend. 

g = graph.traversal()
