migrate((db) => {
  const collection = new Collection({
    "id": "xwkyq3soeq5kyxn",
    "created": "2023-03-03 18:25:23.614Z",
    "updated": "2023-03-03 18:25:23.614Z",
    "name": "machines",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "iuxsz4ql",
        "name": "machineID",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "v5n5msws",
        "name": "name",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("xwkyq3soeq5kyxn");

  return dao.deleteCollection(collection);
})
