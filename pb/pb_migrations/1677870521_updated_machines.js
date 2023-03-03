migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hgnrkiht",
    "name": "os",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  // remove
  collection.schema.removeField("hgnrkiht")

  return dao.saveCollection(collection)
})
