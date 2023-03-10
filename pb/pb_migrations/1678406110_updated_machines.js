migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "les6f9ru",
    "name": "ip",
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
  collection.schema.removeField("les6f9ru")

  return dao.saveCollection(collection)
})
