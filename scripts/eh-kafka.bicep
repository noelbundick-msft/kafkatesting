param location string = resourceGroup().location

var suffix = take(toLower(uniqueString(resourceGroup().id)), 5)
var name = 'kafka${suffix}'

resource ehNamespace 'Microsoft.EventHub/namespaces@2021-11-01' = {
  name: name
  location: location
  sku: {
    name: 'Standard'
    capacity: 1
  }
  properties: {
    kafkaEnabled: true
  }
}

resource eventHub 'Microsoft.EventHub/namespaces/eventhubs@2021-11-01' = {
  parent: ehNamespace
  name: 'mytopic'
  properties: {
    partitionCount: 4
    messageRetentionInDays: 1
  }
}
