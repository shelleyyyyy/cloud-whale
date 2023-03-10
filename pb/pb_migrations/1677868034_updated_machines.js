migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  collection.createRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  collection.createRule = null

  return dao.saveCollection(collection)
})
