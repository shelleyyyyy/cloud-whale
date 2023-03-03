migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  collection.listRule = "\"\" != @request.auth.id"
  collection.createRule = "\"\" != @request.auth.id"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  collection.listRule = null
  collection.createRule = null

  return dao.saveCollection(collection)
})
